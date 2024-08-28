from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Helper functions to introduce delays
def sleep():
    time.sleep(20)

def sleep3():
    time.sleep(3)

# Define the job title and whether it's an internship
job_title = "Data Analyst"
Internship = False

# Set up Chrome options
chrome_options = Options()

# Specify the path to the ChromeDriver executable
service = Service("D:\AI&DS Student\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to Naukri.com
driver.get("https://www.naukri.com")
time.sleep(2)

# Locate the search input field, enter the job title, and submit the search
search = driver.find_element(By.XPATH, '//*[@id="root"]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input')
search.send_keys(job_title)
search.send_keys(Keys.RETURN)
sleep3()

# Initialize lists to store extracted skills and key skills
skillsarr = []
keyskillsarr = []

# Loop through the first 5 job postings
for i in range(1, 6):
    try:
        # Construct the XPath for the job posting and click on it
        jobsxpath = f'//*[@id="listContainer"]/div[2]/div/div[{i}]/div'
        jobs = driver.find_element(By.XPATH, jobsxpath)
        jobs.click()  # Click the job to view its details
        
        # Wait for the new window to open and switch to it
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])
        
        # Extract skills listed in the job posting
        k = 1
        skillsloop = True
        while skillsloop:
            try:
                xpathskills = f'//*[@id="root"]/div/main/div[1]/div[1]/section[2]/div[3]/div[4]/a[{k}]'
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpathskills))
                )
                skills = driver.find_element(By.XPATH, xpathskills)   
                print(skills.text)
                skillsarr.append(skills.text)   
                k += 1
            except NoSuchElementException:
                skillsloop = False  # Exit the loop if no more skills are found
        
        # Extract key skills listed in the job posting
        k = 1  # Reset k for the key skills loop
        keyskillsloop = True
        while keyskillsloop:
            try:
                xpathkeyskills = f'//*[@id="root"]/div/main/div[1]/div[1]/section[2]/div[3]/div[3]/a[{k}]'
                keyskills = driver.find_element(By.XPATH, xpathkeyskills)
                keyskillsarr.append(keyskills.text)
                k += 1
            except NoSuchElementException:
                keyskillsloop = False  # Exit the loop if no more key skills are found
    
    except Exception as e:
        print(f"An error occurred: {e}")
        break  # Exit the main loop if an exception occurs
    
    finally:
        try:
            # Close the current window and switch back to the original window
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            print(f"Error closing window or switching back: {e}")

# Introduce a delay before closing the browser
sleep3()
sleep()

# Close the browser
driver.quit()
