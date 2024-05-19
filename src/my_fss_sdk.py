import requests
import urllib3



class FSS():

    def __init__(self,host,username,password): # code runs when the instance created
        
        self.host=host
        self.username=username
        self.password=password
        
    def get_token(self):
        
        urllib3.disable_warnings()
        headers={'Content-Type': 'application/json'}
        data='{"username":"admin","password":"NokiaFss1!"}'
        res = requests.post(self.host+'/rest/auth/login', headers=headers, data=data, verify=False)
        token=res.json()['access_token']
        return token  
      
    def get_regions(self, name=None):
      
      token=self.get_token()
      headers={'Authorization':'Bearer {}'.format(token)}
      result = requests.get(self.host+'/rest/intentmgr/api/v1/regions', headers=headers,verify=False).json()
      if name:
        for region in result:
          if region['name'] == name:
            region_id=region['profile']['asn']['uuid']
            break
        return {"content":region,"id":region_id}
      else:
        return result
    
    def get_intents(self, name=None):
      
      token=self.get_token()
      
      headers={'Authorization':'Bearer {}'.format(token)}
      result = requests.get(self.host+'/rest/intentmgr/api/v1/intents', headers=headers,verify=False).json()
      
      
      if name:
        
        item = None
        item_id = None  # Initialize item_id to avoid UnboundLocalError
        for item in result:
          
          if item['fabric'][0]['name'] == name:
              
            
            item_id=item["uuid"]
            break
        if item and item_id:
            return {"content":item,"id":item_id}
      return result

          