from zapv2 import ZAPv2

API_KEY = '5m8sls44ceast5kunb9i6qn49'
zap = ZAPv2(apikey=API_KEY, proxies={'http': 'http://127.0.0.1:8081', 'https': 'http://127.0.0.1:8081'})

print("ZAP version:", zap.core.version)
