import src.my_fss_sdk  as fss
import json

def test_get_regions():
    session=fss.FSS('https://10.85.17.253','admin','NokiaFss1!')
    
    result = session.get_intents()
    
    print('addPod' in list(result[0].keys()))
    
    # if  (type(result) == list) and ('addPod' in list(result[0].keys())):
    if (type(result) == list) and (set(result[0].keys()) == {'addPod', 'createdAt', 'description', 'enableVlan', 'evpn', 'fabric', 'hasBgpAuthUpdated', 'hasEvpnProfileUpdated', 'hasVlanISLUpdated', 'intentApplicabilityNetworkType', 'intentType', 'invAvDplTriggerPct', 'ipFamily', 'isBBChange', 'isCandidateFlipInProgress', 'isCandidateMode', 'isCurrent', 'isDeltaConfigChange', 'isLagChange', 'isMaintenance', 'isTopoChange', 'isWatchChange', 'lastTopoChangeVersion', 'name', 'nodeDeployStatus', 'prefixNaming', 'prevState', 'prevVersion', 'profile', 'queueID', 'region', 'staleReason', 'staleState', 'state', 'statusReason', 'templateName', 'updatedAt', 'uuid', 'version', 'versionSourceType', 'vlanID', 'wlCount'}) :
                                  
        test_result= True
    else:
        test_result= False
        
    assert test_result == True