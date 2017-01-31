from selenium import webdriver
import time

start_time = time.time()
driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768) # optional
driver.get('http://032.la')
driver.save_screenshot('032_la.png') # save a screenshot to disk
body = driver.find_element_by_tag_name('body')

with open('032_la.txt','w') as output:
    print(body.text, file=output)

print("--- %s seconds ---" % (time.time() - start_time))
