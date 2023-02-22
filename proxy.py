import requests
import csv
import concurrent.futures

proxylist = []
with open('Proxy_list.txt','r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])

def extract(proxy):
        try:
            r = requests.get('https://httpbin.org/ip',proxies={'http':proxy,'https':proxy},timeout=2)
            print(r.json()," - working")
        except:
            print('failed')
            pass
        return proxy

extract(proxylist)

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(extract,proxylist)


# proxy = '10.10.10.1'
# try:
#     r = requests.get('https://httpbin.org/ip', proxies={'http': proxy,'https':proxy},timeout=3)
#     print(r.json())
# except:
#     print('failed')
#     pass