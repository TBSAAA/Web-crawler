from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

opt = Options()
opt.add_argument("--headless")
opt.add_argument('--disable-gpu')
opt.add_argument("--window-size=4000,1600")

web = Chrome(options=opt)
web.get('https://au.indeed.com/')

job = web.find_element(By.XPATH, '//*[@id="text-input-what"]')
job.send_keys('python')

city = web.find_element(By.XPATH, '//*[@id="text-input-where"]')
city.send_keys('Sydney', Keys.ENTER)

# get the data from the search
job_list = web.find_elements(By.XPATH, '//ul[@class="jobsearch-ResultsList css-0"]//div[@class="job_seen_beacon"]')
for job in job_list:
    a_tag = job.find_element(By.XPATH, './/td[@class="resultContent"]//a')
    a_tag.click()
    time.sleep(2)
    iframe = web.find_element(By.XPATH, '//iframe[@id="vjs-container-iframe"]')
    web.switch_to.frame(iframe)
    job_description = web.find_elements(By.XPATH, '//*[@id="jobDescriptionText"]//p')
    for p in job_description:
        print(p.text)
    web.switch_to.parent_frame()
    break