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

# Function to construct the URL for job search
def link(query):
    base = "https://www.naukri.com/"
    base2 = "-jobs?k="
    
    # Convert the job title to lowercase and replace spaces with hyphens
    formatted_query = query.lower().replace(" ", "-")
    
    # Construct the full URL using the base and formatted query
    full_url = f"{base}{formatted_query}{base2}{formatted_query}"
    
    return full_url

# Define the job title to search for
job_title = "Data Analyst"
Internship = False

# Set up Chrome options for the WebDriver
chrome_options = Options()

# Specify the path to the ChromeDriver executable
service = Service("D:\AI&DS Student\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# Initialize the Chrome WebDriver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the Naukri.com search page for the specified job title
url = link(job_title)
driver.get(url)
time.sleep(2)   

# Initialize dictionaries to store extracted skills and key skills
skillsarr = {}
keyskillsarr = {}

# Loop through the first 5 job postings on the search results page
for i in range(1, 6):
    try:
        # Construct the XPath for the job posting and click on it to view details
        jobsxpath = f'//*[@id="listContainer"]/div[2]/div/div[{i}]/div'
        jobs = driver.find_element(By.XPATH, jobsxpath)
        jobs.click()  
        
        # Wait for the job details to open in a new window and switch to it
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])
        
        # Extract skills listed in the job posting
        k = 1
        skillsloop = True
        while skillsloop:
            try:
                # Construct the XPath for each skill and extract the text
                xpathskills = f'//*[@id="root"]/div/main/div[1]/div[1]/section[2]/div[3]/div[4]/a[{k}]'
                skills = driver.find_element(By.XPATH, xpathskills) 
                if skills.text in skillsarr:
                    skillsarr[skills.text] += 1
                else:
                    skillsarr[skills.text] = 1   
                k += 1
            except NoSuchElementException:
                skillsloop = False  # Exit the loop if no more skills are found
        
        # Extract key skills listed in the job posting
        k = 1  # Reset k for the key skills loop
        keyskillsloop = True
        while keyskillsloop:
            try:
                # Construct the XPath for each key skill and extract the text
                xpathkeyskills = f'//*[@id="root"]/div/main/div[1]/div[1]/section[2]/div[3]/div[3]/a[{k}]'
                keyskills = driver.find_element(By.XPATH, xpathkeyskills)
                if keyskills.text in keyskillsarr:
                    keyskillsarr[keyskills.text] += 1
                else:
                    keyskillsarr[keyskills.text] = 1 
                k += 1
            except NoSuchElementException:
                keyskillsloop = False  # Exit the loop if no more key skills are found
    
    except Exception as e:
        print(f"An error occurred: {e}")
        break  # Exit the main loop if an exception occurs
    
    finally:
        try:
            # Close the current job details window and switch back to the main window
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            print(f"Error closing window or switching back: {e}")

# Print the extracted key skills and skills
print(keyskillsarr, skillsarr)
sleep3()
sleep()

# Close the browser and end the session
driver.quit()
