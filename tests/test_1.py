import src.my_fss_sdk  as fss
import json

def test_get_token():
    session=fss.FSS('https://10.85.17.253','admin','NokiaFss1!')
    
    result = session.get_token()
    
    assert len(json.dumps(result)) > 4000
  

    

    
    







