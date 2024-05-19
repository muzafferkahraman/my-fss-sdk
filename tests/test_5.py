import src.my_fss_sdk  as fss
import json

def test_get_regions():
    session=fss.FSS('https://10.85.17.253','admin','NokiaFss1!')
    
    result = session.get_regions()
    
    if (type(result) == list) and (set(result[0].keys()) == {'createdAt', 'description', 'dsState', 'latitude', 'location', 'longitude', 'name', 'profile', 'queueLock', 'uuid'}):
         test_result= True
    else:
        test_result= False
        
    assert test_result == True