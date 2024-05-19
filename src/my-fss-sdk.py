import json
import requests
import copy


class FSS:

    def __init__(self,host,username,password): # code runs when the instance created
        self.host=host
        self.username=username
        self.password=password
        
    def getToken(self):
      
        headers={'Content-Type': 'application/json'}
        data='{"username":"admin","password":"NokiaFss1!"}'
        res = requests.post(host+'/rest/auth/login', headers=headers, data=data, verify=False)
        token=res.json()['access_token']
        return token  
      
    def get_regions(self,id):
      
      token=self.getToken()
      headers={'Authorization':'Bearer {}'.format(token)}
      result = requests.get(url+'/rest/intentmgr/api/v1/regions', headers=headers,verify=False).json()
      if self.id == "*":
        return result
      else:
        for region in result:
          if region.id == self.id:
            break
        return region
          