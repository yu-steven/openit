import os
import json
import time
import copy
import hashlib
from ruamel import yaml

from git.repo import Repo
from git.repo.fun import is_git_dir


class YamlUtils:
    def __init__(self, local_path="./"):
        self.local_path = local_path
        self.not_support_ciphers = ["chacha20", "rc4", "none"]
        self.not_support_alterIds = ["undefined"]
        self.not_support_type = ["vless"]
        self.network = ["grpc", "h2"]

        self.proxies_md5_dict = dict()
        self.proxies_md5_name_dict = dict()
        self.filtered_rules = list()
        self.proxy_names_set = set()
        self.proxy_groups = dict()
        self.proxy_groups_test_set = set()
        with open("template.json", "r", encoding="utf8") as template_file:
            self.template = json.load(template_file)
        with open("adguard_dns.json", "r", encoding="utf8") as template_file:
            self.adguard_dns = json.load(template_file)

    def clone_repo(self, repo_url, branch=None):
        git_local_path = os.path.join(self.local_path, ".git")
        if not is_git_dir(git_local_path):
            Repo.clone_from(repo_url, to_path=self.local_path, branch=branch)
        else:
            self.pull()

    def pull(self):
        repo = Repo(self.local_path)
        repo.git.pull()

    def make_template_dict(self, keyword="yaml", dirname=None):
        if not os.path.exists(self.local_path):
            os.makedirs(self.local_path)
        repo = Repo(self.local_path)
        # 2 days ago
        # git log --since='date -d "yesterday" +%Y.%m.%d' --name-only --pretty=format:""
        commit_log = repo.git.log(
            "--since='date -d \"yesterday\" +%Y.%m.%d'",
            "--name-only",
            '--pretty=format:""',
        )
        log_list = commit_log.split("\n")
        self.make_template(log_list, keyword, dirname)

    def make_template(self, filelist, keyword="yaml", dirname=None):
        def check_proxy(proxy):
            return (
                "server" in proxy
                and proxy.get("cipher") not in self.not_support_ciphers
                and proxy.get("alterId") is not None
                and proxy.get("alterId") not in self.not_support_alterIds
                and proxy.get("type") not in self.not_support_type
                and type(proxy.get("port") == int)
                and proxy.get("port") > 0
            )

        for item in filelist:
            if (dirname is None or dirname in item) and keyword in item:
                try:
                    file_path = os.path.join(self.local_path, item)
                    if os.path.exists(file_path) and os.path.isfile(file_path):
                        with open(file_path, "r", encoding="utf8") as yaml_file:
                            yaml_obj = yaml.safe_load(yaml_file)
                            rules = yaml_obj.get("rules")
                            proxies = yaml_obj.get("proxies")
                            self.filtered_rules.extend(rules)
                            merged_proxy = dict()
                            deleted_proxy = list()
                            for proxy in proxies:
                                if check_proxy(proxy):
                                    if proxy.get(
                                        "network"
                                    ) in self.network and not proxy.get("tls"):
                                        deleted_proxy.append(proxy.get("name"))
                                        continue
                                    proxy["port"] = int(proxy.get("port"))
                                    proxy_copy = copy.deepcopy(proxy)
                                    proxy_copy.pop("name")
                                    data_md5 = hashlib.md5(
                                        json.dumps(proxy_copy, sort_keys=True).encode(
                                            "utf-8"
                                        )
                                    ).hexdigest()
                                    if data_md5 not in self.proxies_md5_dict:
                                        if proxy.get("name") in self.proxy_names_set:
                                            proxy["name"] = (
                                                proxy.get("name")
                                                + "_"
                                                + item
                                                + "_"
                                                + str(round(time.time() * 1000))
                                                + uuid.uuid4()
                                            )
                                        self.proxy_names_set.add(proxy.get("name"))
                                        self.proxies_md5_dict[data_md5] = proxy
                                        self.proxies_md5_name_dict[
                                            data_md5
                                        ] = proxy.get("name")
                                    merged_proxy[
                                        proxy.get("name")
                                    ] = self.proxies_md5_name_dict.get(data_md5)
                                else:
                                    deleted_proxy.append(proxy.get("name"))
                            proxy_groups = yaml_obj.get("proxy-groups")

                            for index, group in enumerate(proxy_groups):
                                group_name = group.get("name")
                                if group.get("type") == "url-test":
                                    self.proxy_groups_test_set.add(group_name)
                                    group["name"] = "♻️ 自动选择"
                                    proxy_groups[index] = group

                            for group in proxy_groups:
                                group_name = group.get("name")
                                saved_group = self.proxy_groups.get(group_name, dict())
                                saved_proxies = saved_group.get("proxies", list())
                                proxies = group.get("proxies")
                                for proxy in proxies:
                                    if (
                                        proxy not in deleted_proxy
                                        and proxy not in saved_proxies
                                        and proxy in self.proxy_names_set
                                    ):
                                        for one in self.proxy_groups_test_set:
                                            proxy = proxy.replace(one, "♻️ 自动选择")
                                        saved_proxies.append(
                                            merged_proxy.get(proxy, proxy)
                                        )
                                group["proxies"] = (
                                    saved_proxies
                                    if len(saved_proxies) > 0
                                    else ["DIRECT", "REJECT"]
                                )
                                self.proxy_groups[group_name] = group
                except Exception as e:
                    pass
        if len(self.proxy_groups) > 0:
            self.template["proxy-groups"] = list(self.proxy_groups.values())

        filtered_rules_set = set()
        for item in self.filtered_rules:
            for one in self.proxy_groups_test_set:
                filtered_rules_set.add(item.replace(one, "♻️ 自动选择"))

        self.template["proxies"] = list(self.proxies_md5_dict.values())
        self.template["rules"] = list(filtered_rules_set)

    def get_template_dict(self):
        return self.template

    def save_file(self, savepath="clash.yaml", with_adguard_dns=False):
        if savepath is not None:
            template = copy.deepcopy(self.template)
            template.pop("rule-providers")
            if with_adguard_dns:
                template["dns"] = self.adguard_dns
            yml = yaml.YAML()
            yml.indent(mapping=2, sequence=4, offset=2)
            with open(savepath, "w+", encoding="utf8") as outfile:
                yml.dump(template, outfile)

    def save_file_without_providers(
        self, savepath="clash_without_providers.yaml", with_adguard_dns=False
    ):
        if savepath is not None:
            template = copy.deepcopy(self.template)
            template.pop("rule-providers")
            if with_adguard_dns:
                template["dns"] = self.adguard_dns
            yml = yaml.YAML()
            yml.indent(mapping=2, sequence=4, offset=2)
            with open(savepath, "w+", encoding="utf8") as outfile:
                yml.dump(template, outfile)
