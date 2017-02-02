from selenium import webdriver
import json
import time
from pprint import pprint

sites_list = []
sites = {}
errors = {}
start_time = time.time()

print("====== scrap_with_selenium.py =======")
print("preparing browser...")
driver = webdriver.Firefox()
driver.set_window_size(1024, 768)
driver.set_page_load_timeout(20) 

print("loading site list...")
with open('lista.json', 'r') as file:
    content = file.read()
    sites_list = json.loads(content)

with open('sites.json', 'r') as file:
    content = file.read()
    sites = json.loads(content)

print("scraping........")
for h in sites_list:
    print("%s - %d" % (h, time.time()-start_time))
    try:
        driver.get(h)
        driver.save_screenshot(
                sites[h]['filename'].replace(".txt",".png")
                )
        body = driver.find_element_by_tag_name('body')

        with open(sites[h]['filename'],'w') as output:
            print(body.text, file=output)

    except Exception as e:
        errors[h] = e

if any(errors):
    print("saving errors")
    with open("errors.log", "w") as output:
        pprint(errors, stream=output)

print("done!")
