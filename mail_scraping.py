from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re



# configure the webdriver
binary = FirefoxBinary(r'C:\Program Files\Firefox Developer Edition\firefox.exe')       #This specifies the firefox.exe path. 
driver = webdriver.Firefox(firefox_binary=binary)

# navigate to Google search page
driver.get("https://www.google.com")

# find the search box element and enter the search query
cookie = driver.find_element(By.ID, 'L2AGLb')
cookie.click()
search_box = driver.find_element("name", "q")
search_box.send_keys('intext:"gmail.com" site:linkedin.com/in')     # You can change the website
search_box.submit()

# wait for the search results to load
results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.g"))
)

# extract the email addresses from the search results
email_tags = driver.find_elements("xpath", "//*[contains(text(), '@')]")

email_addresses = []
for tag in email_tags:
    email = tag.text
    email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(email_regex, email)
    if match:
        email_address = match.group()
        email_addresses.append(email_address)
    else:
        pass

email_addresses_no_duplicates = []

# loop through the original list
for email in email_addresses:
    # check if the current email is already in the new list
    if email not in email_addresses_no_duplicates:
        # if not, add it to the new list
        email_addresses_no_duplicates.append(email)

# print the email addresses
print(email_addresses_no_duplicates)

email_txt = open("emails.txt", "w")
for i in email_addresses_no_duplicates:
    email_txt.write("\n"+i)
email_txt.close()

# close the web driver
driver.quit()
