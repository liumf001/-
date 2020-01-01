'''
亚马逊
亚马逊对来源作审查
模拟headers
'''
import requests
url = 'https://www.amazon.cn/gp/product/B0794LT13Q?pf_rd_p=c6d17c3b-92ef-4aa7-920b-19155bc9b830&pf_rd_s=merchandised-search-7&pf_rd_t=101&pf_rd_i=1403206071&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=D4PKSA30SAEMA01G05K8&ref=cn_ags_floor_hotasin_1403206071_mobile-2'
kv = {'user-agent' : 'Mozilla/5.0'}
try:
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print('爬取失败')
    print('headers:')
print(r.request.headers)