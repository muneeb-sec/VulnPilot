from zapv2 import ZAPv2
import time

API_KEY = '5m8sls44ceast5kunb9i6qn49'
TARGET = 'http://localhost:3000'  # Juice Shop

zap = ZAPv2(apikey=API_KEY, proxies={'http': 'http://127.0.0.1:8081', 'https': 'http://127.0.0.1:8081'})

print("ZAP version:", zap.core.version)
print(f"Starting spider on {TARGET}...")

scan_id = zap.spider.scan(TARGET)

# Wait until the spider scan reaches 100% completion
while int(zap.spider.status(scan_id)) < 100:
    print(f"Spider progress: {zap.spider.status(scan_id)}%")
    time.sleep(2)

print("Spider complete!")

# Print all discovered URLs/pages
urls = zap.spider.results(scan_id)
print(f"\nTotal pages found: {len(urls)}")
for url in urls:
    print(url)
