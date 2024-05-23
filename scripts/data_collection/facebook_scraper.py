from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

FB_EMAIL = os.getenv('FB_EMAIL')
FB_PASSWORD = os.getenv('FB_PASSWORD')

# Function to login to Facebook
def login_to_facebook(driver, email, password):
    driver.get("https://www.facebook.com/")
    time.sleep(3)

    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(email)
    
    password_input = driver.find_element(By.ID, "pass")
    password_input.send_keys(password)
    
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()
    
    time.sleep(5)  # Wait for login to complete

# Function to scroll and load more posts
def scroll_and_load_posts(driver, num_scrolls):
    for _ in range(num_scrolls):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(3)

# Function to click all "See More" buttons
def click_see_more_buttons(driver):
    see_more_buttons = driver.find_elements(By.XPATH, "//div[@role='button' and contains(text(), 'See more')]")
    for button in see_more_buttons:
        try:
            driver.execute_script("arguments[0].click();", button)
            time.sleep(1)  # Wait a bit for the content to expand
        except Exception as e:
            print(f"Error clicking 'See more' button: {e}")

# Function to extract and print posts
def extract_posts(driver):
    posts = driver.find_elements(By.XPATH, "//div[@role='article']")
    for post in posts:
        try:
            content = post.find_element(By.XPATH, ".//div[@data-ad-preview='message']").text
            #date = 

            #create
            print(content)
            print("-" * 80)
        except Exception as e:
            continue


#def 

def scrape_facebook():
    driver = webdriver.Chrome()

    login_to_facebook(driver, FB_EMAIL, FB_PASSWORD)

    # Navigate to the specific Facebook page
    page_url = "https://www.facebook.com/bewketu.seyoum.3"  # Replace with the name of the page
    driver.get(page_url)
    time.sleep(5)

    # Scroll to load more posts
    scroll_and_load_posts(driver, num_scrolls=100)  # Adjust number of scrolls as needed

    # Click all "See More" buttons to expand posts
    click_see_more_buttons(driver)

    # Extract and print posts
    extract_posts(driver)

    # Close the driver
    driver.quit()

#if __name__ == "__main__":
 #   main()
