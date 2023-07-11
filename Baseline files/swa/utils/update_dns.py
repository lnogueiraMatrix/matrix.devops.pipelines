from os import getenv
import yaml
import requests

DEFAULT_URL  = getenv.DEFAULT_URL
API_TOKEN    = getenv.CF_API_TOKEN
BEARER_AUTH  = getenv.BEARER_AUTH
DNS_ZONE     = getenv.DNS_ZONE
EMAIL        = getenv.EMAIL
IP           = getenv.CLUSTER_IP
ENVIRONMENT  = getenv.ENVIRONMENT_LOWER

with open(f'../.ci/{ENVIRONMENT}-values.yaml','r') as f:
    config = yaml.safe_load(f)

custom_host = config['customHost']
enable = custom_host['enabled']
if enable == True: 
  url = custom_host['url']
else:
  url = DEFAULT_URL


def create_dns(url):
  target = f"https://api.cloudflare.com/client/v4/zones/{DNS_ZONE}/dns_records"
  payload = {
    "content": IP,
    "name": str(url),
    "proxied": True,
    "type": "A",
    "ttl": 3600
    }
 
  headers = {
  'Content-Type': "application/json",
  'Authorization': BEARER_AUTH
  }

  response = requests.request("POST",target,headers=headers,json=payload)
  data     = response.json()
  print("dns criado")  

def check_dns(url):
   target  = "https://api.cloudflare.com/client/v4/zones/4a5a9e82376/dns_records"
   email   = "gabriel.sutto@matrixenergia.com"
   exist   = True
   headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": f"{email}",
    'Authorization': BEARER_AUTH
   }
   params     = {"name":str(url)}
   response   = requests.request("GET",target,headers=headers,params=params)
   data       = response.json()
   try:
     data["result"][0]["name"]
   except IndexError:
      exist = False
      pass
   return exist

if __name__ == '__main__':
  if check_dns(url) == False:
   create_dns(url)
  else:
   print("dns ja existente")      