from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time



def sleep():
    time.sleep(20)

def sleep3():
    time.sleep(3)


job_title = "Data Analyst"
Internship = False
# Set up Chrome options
chrome_options = Options() 

# Specify the path to chromedriver
service = Service("D:\AI&DS Student\chromedriver-win64\chromedriver-win64\chromedriver.exe")  # Update this path

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to Naukri.com
driver.get("https://www.naukri.com")
time.sleep(2)
search = driver.find_element(By.XPATH, '//*[@id="root"]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input')
search.send_keys(job_title)
search.send_keys(Keys.RETURN)
sleep3()
jobs = driver.find_element(By.XPATH, '//*[@id="listContainer"]/div[2]/div/div[1]/div')
jobs.click()
driver.switch_to.window(driver.window_handles[1])
sleep3()

# jab tak hai key skills //*[@id="root"]/div/main/div[1]/div[1]/section[2]/div[3]/div[3]/a[2]
# jab tak hai skills //*[@id="root"]/div/main/div[1]/div[1]/section[2]/div[3]/div[4]/a[1]
keyskills = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div[1]/div[1]/section[2]/div[3]/div[4]/a[1]')
keyskillsarr=[]
i=1
while keyskills:
    xpathkeyskills = f'//*[@id="root"]/div/main/div[1]/div[1]/section[2]/div[3]/div[4]/a[{i}]'
    print(xpathkeyskills)
    keyskills = driver.find_element(By.XPATH, xpathkeyskills)
    keyskillsarr.append(keyskills.text)
    i+=1
print(keyskillsarr)



#print(job_ids)
sleep()

# Your code to interact with the page goes here



# Close the browser
driver.quit()


