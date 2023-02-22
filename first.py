from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


website = 'https://www.healthecareers.com/acoem/search-jobs'
path = '/home/user/Scraping/Selenium/chromedriver'
# browser_option = ChromeOptions()
# browser_option.headless = True
driver = Chrome(executable_path=path)
driver.get(website)
all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-results-card")
Jobs_data = []
for job in all_jobs:
    title = job.find_element(By.XPATH, "//span[@itemprop='title']").text
    job_location = job.find_element(By.CSS_SELECTOR, "#job-results-location").text
    job.click()
    job_tags = job.find_elements(By.CSS_SELECTOR,".job-tag").text
    print(job_tags)
    job_desc = job.find_elements(By.CSS_SELECTOR,".description")
    print('Description',job_desc)
    employer = job.find_elements(By.CSS_SELECTOR,".job-tab")
    print('Employer',employer)
    employer.click()


    # Jobs_data.append(job_link.get_attribute("href"))


driver.quit()