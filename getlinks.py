from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import time
def getLinksByLocation(name):
    # driver =  webdriver.PhantomJS(executable_path='D:\\ZGFSft\\Environment\\Python\\Lib\\site-packages\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    driver = webdriver.Firefox(executable_path='D:\\ZGFSft\\Environment\\Python\\Lib\\site-packages\\geckodriver.exe')
    driver.get('http://www.nsii.org.cn/2017/query.php?kingdom=plant')
    # driver.find_element_by_id('q_geotag').clear()
    # driver.find_element_by_id('q_geotag').send_keys(name)
	
    driver.find_element_by_id('q_fname').clear()
    driver.find_element_by_id('q_fname').send_keys(name)	
	
    # driver.find_element_by_id('q_lname').clear()
    # driver.find_element_by_id('q_lname').send_keys(name)
    driver.find_element_by_id('radio_HasImage_1').click()
    driver.find_element_by_id('btnStartQueryPro').click()
    #time.sleep(4)
    #driver.implicitly_wait(10)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnTable")))
    driver.find_element_by_id('btnTable').click()
    #By.ID
    #注意EC如何与driver结合
    while EC.visibility_of_element_located((By.ID,'btnLoadMore')).__call__(driver):
        driver.find_element_by_id('btnLoadMore').click()
    pageSource = driver.page_source
    bsObj = BeautifulSoup(pageSource,'html.parser')
    speUrls = bsObj.findAll("a",{"href":re.compile("^(specimen\.php\?id=).*")})
    spelinks = [Url['href'] for Url in speUrls]
    spelinksSet = set(spelinks)
    print(name + '\t' + str(len(spelinksSet)))
    file  = open('D:\\ZGFSft\\Environment\\NSII\\links\\' + name,'w')
    for link in spelinksSet:
        # print(link)
        file.write('http://www.nsii.org.cn/2017/' + link + '\n')
    file.flush()
    file.close()
    driver.quit()

infile = open('D:\\ZGFSft\\Environment\\NSII\\speciesname\\species_name.txt','rU')
while True:
    line = infile.readline()
    if line:
        name = line.strip()
        try:
            getLinksByLocation(name)
        except TimeoutException:
            print(name + '\t' + '0')
    else:
        break
