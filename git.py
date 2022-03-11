import os
import time
import shutil
from utils.yamlUtils import YamlUtils
from utils.jiang import get_content as jiang_content
from utils.mattkaydiary import get_content as mattkaydiary_content

changfengoss = os.path.join("changfengoss")
dirname = time.strftime("%Y_%m_%d", time.localtime(time.time()))
yamlUtils = YamlUtils(changfengoss)
yamlUtils.clone_repo("https://ghproxy.com/https://github.com/changfengoss/pub.git")
yamlUtils.make_template_dict("yaml", dirname)
yamlUtils.save_file("pub/changfengoss.yaml")
shutil.rmtree(changfengoss)

bhqz = os.path.join("bhqz")
yamlUtils = YamlUtils(bhqz)
yamlUtils.clone_repo("https://github.com/bhqz/bhqz.git")
yamlUtils.make_template_dict()
yamlUtils.save_file("pub/bhqz.yaml")
shutil.rmtree(bhqz)

freenode = os.path.join("freenode")
yamlUtils = YamlUtils(freenode)
yamlUtils.clone_repo("https://github.com/adiwzx/freenode.git", "main")
yamlUtils.make_template_dict("adidesign.c")
yamlUtils.save_file("pub/freenode.yaml")
shutil.rmtree(freenode)

ssr = os.path.join("ssr")
yamlUtils = YamlUtils(ssr)
yamlUtils.clone_repo("https://github.com/ssrsub/ssr.git", "master")
yamlUtils.make_template_dict("yml")
yamlUtils.save_file("pub/ssr.yaml")
shutil.rmtree(ssr)

jiang = jiang_content()
mattkaydiary = mattkaydiary_content()

pub = os.path.join("pub")
yamlUtils = YamlUtils(pub)
yamlUtils.make_template(
    ["jiang.yaml", "mattkaydiary.yaml", "freenode.yaml", "bhqz.yaml", "ssr.yaml"]
)
yamlUtils.save_file("pub/combine.yaml")
