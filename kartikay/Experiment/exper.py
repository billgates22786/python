from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service  # Import Service for Edge WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# IMDb login credentials
IMDB_EMAIL = 'jetrixjain123@gmail.com'
IMDB_PASSWORD = 'Bhavya123'

# List of movie titles to add to the watchlist
movie_titles = ["Inception", "The Dark Knight", "Interstellar"]

def login_to_imdb(driver):
    # Navigate to IMDb login page
    driver.get("https://www.imdb.com/registration/signin")
    
    # Wait for the page to load and click on the IMDb login option
    time.sleep(3)
    driver.find_element(By.XPATH, '//a[contains(@href, "signin?ref")]').click()
    
    # Enter email and password
    time.sleep(3)
    email_field = driver.find_element(By.ID, 'ap_email')
    email_field.send_keys(IMDB_EMAIL)
    
    password_field = driver.find_element(By.ID, 'ap_password')
    password_field.send_keys(IMDB_PASSWORD)
    password_field.send_keys(Keys.RETURN)
    
    time.sleep(5)  # Wait for login to complete

def add_movie_to_watchlist(driver, movie_title):
    # Search for the movie
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(movie_title)
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(3)
    
    # Click on the first search result
    first_result = driver.find_element(By.XPATH, "//td[@class='result_text']/a")
    first_result.click()
    
    time.sleep(3)
    
    # Add the movie to the watchlist by clicking the watchlist button
    watchlist_button = driver.find_element(By.XPATH, '//div[contains(@class, "wl-ribbon")]')
    watchlist_button.click()
    
    time.sleep(2)  # Wait for the watchlist update

def main():
    # Set up the WebDriver
    driver = webdriver.Edge(executable_path=r'C:\Python\Experiment\msedgedriver.exe')


    try:
        # Log in to IMDb
        login_to_imdb(driver)
        
        # Add each movie in the list to the watchlist
        for movie in movie_titles:
            add_movie_to_watchlist(driver, movie)
            print(f'Added {movie} to your watchlist.')
    
    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    main()
