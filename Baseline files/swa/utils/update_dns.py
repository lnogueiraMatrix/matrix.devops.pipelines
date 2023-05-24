import http.client
from os import getenv
import yaml

#ci_file = f"{getenv.ENVIRONMENT_LOWER}-values.yaml"

with open('./config.yaml','r') as f:
    config = yaml.safe_load(f)

custom_host = config['customHost']
enable = custom_host['enabled']
url = custom_host['url']

def update_dns(url):
  conn = http.client.HTTPSConnection("api.cloudflare.com")
  payload = ('{\n  \"content\": \"20.122.44.27\", \n  \"name\":"' + str(url) +'",\n  \"proxied\": false,\n  \"type\": \"A\",\n  \"comment\": \"Domain verification record\",\n  \"tags\": [\n    \"owner:dns-team\"\n  ],\n  \"ttl\": 3600\n}" ' )
  uri =  f"/client/v4/zones/f4c524fd1af23394abf7a4a5a9e82376/dns_records" 
  
  headers = {
  'Content-Type': "application/json",
  'Authorization': "Bearer sRlsLT3fW1rIC9IMvDZULrGyrpzLWd2HmGAAQcD6"
  }

  conn.request("POST", uri , payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))
  
if enable == True:
   update_dns(url)
else:
   url = f"{getenv.ENVIRONMENT_LOWER}-{getenv.APP_NAME}.matrixenergia.com" 
   update_dns(url)    