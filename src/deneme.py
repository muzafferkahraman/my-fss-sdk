import my_fss_sdk  as fss

session=fss.FSS('https://10.85.17.253','admin','NokiaFss1!')

region=session.get_regions("ASM_GUW_ERIC")

# intents=session.get_intents("12Node-Fab_gatenet_fabric")
intents=session.get_intents()

print(intents[0].keys())
# print(session.get_regions()[0].keys())

