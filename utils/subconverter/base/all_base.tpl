{% if request.target == "clash" or request.target == "clashr" %}

port: {{ default(global.clash.http_port, "7890") }}
socks-port: {{ default(global.clash.socks_port, "7891") }}
allow-lan: {{ default(global.clash.allow_lan, "true") }}
mode: Rule
log-level: {{ default(global.clash.log_level, "info") }}
external-controller: '127.0.0.1:9090'
{% if default(request.clash.dns, "") == "1" %}
dns:
  enable: true
  listen: :1053
{% endif %}
dns:
  enable: true #是否启用dns false
  ipv6: false
  # listen: 0.0.0.0:53
  enhanced-mode: fake-ip
  fake-ip-range: 198.18.0.1/16
  fake-ip-filter:
    - "*.lan"
    - "*.local"
    - "dns.msftncsi.com"
    - "www.msftncsi.com"
    - "www.msftconnecttest.com"
    - "stun.*.*.*"
    - "stun.*.*"
    - miwifi.com
    - music.163.com
    - "*.music.163.com"
    - "*.126.net"
    - api-jooxtt.sanook.com
    - api.joox.com
    - joox.com
    - y.qq.com
    - "*.y.qq.com"
    - streamoc.music.tc.qq.com
    - mobileoc.music.tc.qq.com
    - isure.stream.qqmusic.qq.com
    - dl.stream.qqmusic.qq.com
    - aqqmusic.tc.qq.com
    - amobile.music.tc.qq.com
    - "*.xiami.com"
    - "*.music.migu.cn"
    - music.migu.cn
    - netis.cc
    - router.asus.com
    - repeater.asus.com
    - routerlogin.com
    - routerlogin.net
    - tendawifi.com
    - tendawifi.net
    - tplinklogin.net
    - tplinkwifi.net
    - tplinkrepeater.net
    - "*.ntp.org.cn"
    - "*.openwrt.pool.ntp.org"
    - "*.msftconnecttest.com"
    - "*.msftncsi.com"
    - localhost.ptlogin2.qq.com
    - "*.*.*.srv.nintendo.net"
    - "*.*.stun.playstation.net"
    - "xbox.*.*.microsoft.com"
    - "*.ipv6.microsoft.com"
    - "*.*.xboxlive.com"
    - speedtest.cros.wr.pvp.net
  default-nameserver: #解析Dot/Doh域名的DNS
    - 114.114.114.114
    - 9.9.9.9
  nameserver: #clash首次解析
    - 1.2.4.8 #CNNIC sDNS
    - 210.2.4.8 #CNNIC sDNS
    - 223.5.5.5 #阿里DNS
    - 223.6.6.6 #阿里DNS
    - 52.80.52.52 #OneDNS
    - 117.50.10.10 #OneDNS
    - 180.76.76.76 #百度DNS
    - 119.28.28.28 #腾讯DNS
    - 119.29.29.29 #腾讯DNS
    - 114.114.114.114 #114DNS
    - 114.114.115.115 #114DNS
    - 101.226.4.6 #360 DNS 派
    - 218.30.118.6 #360 DNS 派
    - 123.125.81.6 #360 DNS 派
    - 140.207.198.6 #360 DNS 派
    - 202.38.64.1 #中科大DNS
    - 202.112.20.131 #中科大DNS
    - 202.141.160.95 #中科大DNS
    - 202.141.160.99 #中科大DNS
    - 202.141.176.95 #中科大DNS
    - 202.141.176.99 #中科大DNS
    - tls://dot.pub:853 #腾讯DNS over TLS
    - tls://1.12.12.12:853 #腾讯DNS over TLS(IP)
    - tls://120.53.53.53:853 #腾讯DNS over TLS(IP)
    - https://doh.pub/dns-query #腾讯DNS over HTTPS
    - https://sm2.doh.pub/dns-query #腾讯DNS over HTTPS(国密)
    - https://1.12.12.12/dns-query #腾讯DNS over HTTPS(IP)
    - https://120.53.53.53/dns-query #腾讯DNS over HTTPS(IP)
    - https://dns.alidns.com/dns-query #阿里DNS over HTTPS
    - https://doh.dns.sb/dns-query #DNS.SB DNS over HTTPS
    - https://dns.rubyfish.cn/dns-query #红鱼DNS over HTTPS
  fallback: #遇到CN以外的ip和fallback-filter中的条件用如下DNS解析
    - 9.9.9.9 #IBM DNS
    - 149.112.112.112 #IBM DNS
    - 8.8.4.4 #Google DNS
    - 8.8.8.8 #Google DNS
    - 1.0.0.1 #Cloudflare DNS
    - 1.1.1.1 #Cloudflare DNS
    - 208.67.220.220 #OpenDNS
    - 208.67.220.222 #OpenDNS
    - 208.67.222.220 #OpenDNS
    - 208.67.222.222 #OpenDNS
    - 195.46.39.39 #SafeDNS
    - 195.46.39.40 #SafeDNS
    - 168.95.1.1 #HiNet DNS
    - 203.80.96.10 #HKBN DNS
    - 168.95.192.1 #HiNet DNS
    - 164.124.101.2 #LG U+ DNS
    - 164.124.107.9 #LG U+ DNS
    - 203.248.252.2 #LG U+ DNS
    - 203.248.242.2 #LG U+ DNS
    - 80.80.80.80 #freenom DNS
    - 80.80.81.81 #freenom DNS
    - 199.85.126.10 #norton DNS
    - 199.85.127.10 #norton DNS
    - 168.126.63.1 #KT olleh DNS
    - 168.126.63.2 #KT olleh DNS
    - 139.175.252.16 #Seednet DNS
    - 139.175.55.244 #Seednet DNS
    - 202.45.84.58 #和记环球电讯 DNS
    - 202.45.84.59 #和记环球电讯 DNS
    - 8.26.56.26 #Comodo SecureDNS
    - 23.253.163.53 #Alternate DNS
    - 77.88.8.1 #Yandex Public DNS
    - 77.88.8.8 #Yandex Public DNS
    - 89.233.43.71   #UncensoredDNS
    - 91.239.100.100 #UncensoredDNS
    - 198.101.242.72 #Alternate DNS
    - 8.20.247.20 #Comodo SecureDNS
    - 64.6.64.6 #Verisign Public DNS
    - 64.6.65.6 #Verisign Public DNS
    - 209.244.0.3 #Level3 Public DNS
    - 209.244.0.4 #Level3 Public DNS
    - 210.220.163.82 #SK Broadband DNS
    - 219.250.36.130 #SK Broadband DNS
    - 202.14.67.4 #Pacific SuperNet DNS
    - 84.200.69.80 #DNS.WATCH Public DNS
    - 84.200.70.40 #DNS.WATCH Public DNS
    - 202.14.67.14 #Pacific SuperNet DNS
    - 156.154.70.1 #Neustar Recursive DNS
    - 156.154.71.1 #Neustar Recursive DNS
    - 216.146.35.35 #ORACLE Dyn Public DNS
    - 216.146.36.36 #ORACLE Dyn Public DNS
    - 77.109.148.136 #xiala.net Public DNS
    - 77.109.148.137 #xiala.net Public DNS
    - 101.101.101.101 #TWNIC Quad101 Public DNS
    - 101.102.103.104 #TWNIC Quad101 Public DNS
    - 74.82.42.42 #Hurricane Electric Public DNS
    - 66.220.18.42 #Hurricane Electric Public DNS
    - https://dns.quad9.net/dns-query #IBM Doh
    - https://dns9.quad9.net/dns-query #IBM Doh
    - tls://dns.google:853 #Google Dot
    - https://8.8.4.4/dns-query #Google Doh(IP)
    - https://8.8.8.8/dns-query #Google Doh(IP)
    - https://dns.google/dns-query #Google Doh
    - tls://1.0.0.1:853 #Cloudflare Dot(IP)
    - tls://1.1.1.1:853 #Cloudflare Dot(IP)
    - tls://one.one.one.one #Cloudflare Dot
    - tls://1dot1dot1dot1.cloudflare-dns.com #Cloudflare Dot
    - https://1.0.0.1/dns-query #Cloudflare Doh(IP)
    - https://1.1.1.1/dns-query #Cloudflare Doh(IP)
    - https://cloudflare-dns.com/dns-query #Cloudflare Doh
    - https://dns.daycat.space/dns-query #openit/daycat Doh
    - https://dns.adguard.com/dns-query #AdGuard Doh
    - https://dns-family.adguard.com/dns-query #AdGuard Doh
    - https://dns-unfiltered.adguard.com/dns-query #AdGuard Doh
    - tls://b.iqiq.io:853 #passcloud Dot 华北北京 BGP 节点
    - tls://h.iqiq.io:853 #passcloud Dot 海南岛海口/三亚 BGP 节点
    - tls://j.iqiq.io:853 #passcloud Dot 江西九江双线 BGP 节点
    - tls://c.passcloud.xyz:853 #passcloud Dot 南方广州 BGP 节点
    - tls://x.passcloud.xyz:853 #passcloud Dot 华东上海 BGP 节点
    - https://a.passcloud.xyz/hk #passcloud Doh HK
    - https://a.passcloud.xyz/am #passcloud Doh AM
    - https://a.passcloud.xyz/us #passcloud Doh US
    - https://a.passcloud.xyz/sz #passcloud Doh SZ
    - https://a.passcloud.xyz/cdn #passcloud Doh CDN
    - https://a.passcloud.xyz/dns-query #passcloud Doh Anycast
    - https://worldwide.passcloud.xyz/dns-query #passcloud Doh Worldwide CDN
  fallback-filter:
    geoip: true
    geoip-code: CN
    ipcidr: #nameserver中解析到这里的域名用fallback
      - 240.0.0.0/4
      - 127.0.0.1/8
      - 0.0.0.0/32
    domain: #这些域名直接fallback
      - +.google.com
      - +.github.com
      - +.facebook.com
      - +.twitter.com
      - +.youtube.com
      - +.google.cn
      - +.googleapis.cn
      - +.googleapis.com
      - +.gvt1.com
{% if local.clash.new_field_name == "true" %}
proxies: ~
proxy-groups: ~
rules: ~
{% else %}
Proxy: ~
Proxy Group: ~
Rule: ~
{% endif %}
cfw-bypass:
  - localhost
  - 127.*
  - 10.*
  - 172.16.*
  - 172.17.*
  - 172.18.*
  - 172.19.*
  - 172.20.*
  - 172.21.*
  - 172.22.*
  - 172.23.*
  - 172.24.*
  - 172.25.*
  - 172.26.*
  - 172.27.*
  - 172.28.*
  - 172.29.*
  - 172.30.*
  - 172.31.*
  - 192.168.*
  - <local>

{% endif %}
{% if request.target == "surge" %}

[General]
loglevel = notify
bypass-system = true
skip-proxy = 127.0.0.1,192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,100.64.0.0/10,localhost,*.local,e.crashlytics.com,captive.apple.com,::ffff:0:0:0:0/1,::ffff:128:0:0:0/1
#DNS设置或根据自己网络情况进行相应设置
bypass-tun = 192.168.0.0/16,10.0.0.0/8,172.16.0.0/12
dns-server = 119.29.29.29,223.5.5.5

[Script]
http-request https?:\/\/.*\.iqiyi\.com\/.*authcookie= script-path=https://raw.githubusercontent.com/NobyDa/Script/master/iQIYI-DailyBonus/iQIYI.js

{% endif %}
{% if request.target == "loon" %}

[General]
skip-proxy = 192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,localhost,*.local,e.crashlynatics.com
bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,224.0.0.0/4,255.255.255.255/32
dns-server = system,119.29.29.29,223.5.5.5
allow-udp-proxy = false
host = 127.0.0.1

[Proxy]

[Remote Proxy]

[Proxy Group]

[Rule]

[Remote Rule]

[URL Rewrite]
enable = true
^https?:\/\/(www.)?(g|google)\.cn https://www.google.com 302

[Remote Rewrite]
https://raw.githubusercontent.com/Loon0x00/LoonExampleConfig/master/Rewrite/AutoRewrite_Example.list,auto

[MITM]
hostname = *.example.com,*.sample.com
enable = true
skip-server-cert-verify = true
#ca-p12 =
#ca-passphrase =

{% endif %}
{% if request.target == "quan" %}

[SERVER]

[SOURCE]

[BACKUP-SERVER]

[SUSPEND-SSID]

[POLICY]

[DNS]
1.1.1.1

[REWRITE]

[URL-REJECTION]

[TCP]

[GLOBAL]

[HOST]

[STATE]
STATE,AUTO

[MITM]

{% endif %}
{% if request.target == "quanx" %}

[general]
excluded_routes=192.168.0.0/16, 172.16.0.0/12, 100.64.0.0/10, 10.0.0.0/8
geo_location_checker=http://ip-api.com/json/?lang=zh-CN, https://github.com/KOP-XIAO/QuantumultX/raw/master/Scripts/IP_API.js
network_check_url=http://www.baidu.com/
server_check_url=http://www.gstatic.com/generate_204

[dns]
server=119.29.29.29
server=223.5.5.5
server=1.0.0.1
server=8.8.8.8

[policy]
static=♻️ 自动选择, direct, img-url=https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/Auto.png
static=🔰 节点选择, direct, img-url=https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/Proxy.png
static=🌍 国外媒体, direct, img-url=https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/GlobalMedia.png
static=🌏 国内媒体, direct, img-url=https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/DomesticMedia.png
static=Ⓜ️ 微软服务, direct, img-url=https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/Microsoft.png
static=📲 电报信息, direct, img-url=https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/Telegram.png
static=🍎 苹果服务, direct, img-url=https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/Apple.png
static=🎯 全球直连, direct, img-url=https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/Direct.png
static=🛑 全球拦截, direct, img-url=https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/Advertising.png
static=🐟 漏网之鱼, direct, img-url=https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/Final.png

[server_remote]

[filter_remote]

[rewrite_remote]

[server_local]

[filter_local]

[rewrite_local]

[mitm]

{% endif %}
{% if request.target == "mellow" %}

[Endpoint]
DIRECT, builtin, freedom, domainStrategy=UseIP
REJECT, builtin, blackhole
Dns-Out, builtin, dns

[Routing]
domainStrategy = IPIfNonMatch

[Dns]
hijack = Dns-Out
clientIp = 114.114.114.114

[DnsServer]
localhost
223.5.5.5
8.8.8.8, 53, Remote
8.8.4.4

[DnsRule]
DOMAIN-KEYWORD, geosite:geolocation-!cn, Remote
DOMAIN-SUFFIX, google.com, Remote

[DnsHost]
doubleclick.net = 127.0.0.1

[Log]
loglevel = warning

{% endif %}
{% if request.target == "surfboard" %}

[General]
loglevel = notify
interface = 127.0.0.1
skip-proxy = 127.0.0.1, 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, 100.64.0.0/10, localhost, *.local
ipv6 = false
dns-server = system, 223.5.5.5
exclude-simple-hostnames = true
enhanced-mode-by-rule = true
{% endif %}
{% if request.target == "sssub" %}
{
  "route": "bypass-lan-china",
  "remote_dns": "dns.google",
  "ipv6": false,
  "metered": false,
  "proxy_apps": {
    "enabled": false,
    "bypass": true,
    "android_list": [
      "com.eg.android.AlipayGphone",
      "com.wudaokou.hippo",
      "com.zhihu.android"
    ]
  },
  "udpdns": false
}

{% endif %}
