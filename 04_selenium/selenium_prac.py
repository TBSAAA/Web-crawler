import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

web = Chrome()
web.get('https://au.indeed.com/')

job = web.find_element(By.XPATH, '//*[@id="text-input-what"]')
job.send_keys('python')

city = web.find_element(By.XPATH, '//*[@id="text-input-where"]')
city.send_keys('Sydney', Keys.ENTER)

# get the data from the search
job_list = web.find_elements(By.XPATH, '//ul[@class="jobsearch-ResultsList css-0"]//div[@class="job_seen_beacon"]')
for job in job_list:
    job_title = job.find_element(By.XPATH, './/td[@class="resultContent"]//span').text
    job_company = job.find_element(By.XPATH, './/span[@class="companyName"]').text
    company_location = job.find_element(By.XPATH, './/div[@class="companyLocation"]').text
    try:
        salary = job.find_element(By.XPATH, './/div[@class="metadata salary-snippet-container"]/div').text
    except:
        salary = 'N/A'
    try:
        job_type = job.find_element(By.XPATH, './/div[@class="metadata"]/div').text
        job_type = job_type.split('\n')[0]
    except:
        job_type = 'N/A'

    print(job_title, job_company, company_location, salary, job_type)

    # a_tag = job.find_element(By.XPATH, './/td[@class="resultContent"]//a')
    # a_tag.click()
    # time.sleep(5)
    # iframe = web.find_element(By.XPATH, '//iframe[@id="vjs-container-iframe"]')
    # web.switch_to.frame(iframe)
    # job_description = web.find_elements(By.XPATH, '//*[@id="jobDescriptionText"]//p')
    # for p in job_description:
    #     print(p.text)
    # web.switch_to.parent_frame()
    # break
