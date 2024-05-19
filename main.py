import os
import dotenv
import mlx_functions as mlx
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as Ac
import random

dotenv.load_dotenv()
profile_type = os.getenv("PROFILE_TYPE")
folder_id = os.getenv("FOLDER_ID")
profile_id = os.getenv("PROFILE_ID")

websites = ["https://wikipedia.org/",
            "https://multilogin.com/"
            "https://dell.com/",
            "https://reddit.com/",
            "https://youtube.com/"]

def automation(driver, profile_id, token): # Automation!

    try:
        for website in websites:
            cookie_counter = 0
            driver.get(website)
            while cookie_counter < 15:
                scroll_randomly(driver, random.randint(1, 5))
                links = driver.find_elements(By.TAG_NAME, "a")
                random_link = random.choice(links)
                try:
                    Ac(driver).move_to_element(random_link).pause(5).click().perform()
                    cookie_counter += 1
                except:
                    continue
                finally:
                    time.sleep(random.randint(3, 5))

    except Exception as e:
            print(f"Something happened: {e}")

    finally:
        driver.quit()
        mlx.stop_profile(profile_id, token) # Close browser profile

def scroll_randomly(driver, times):
    for _ in range(times):
        total_height = driver.execute_script("return document.body.scrollHeight")
        random_position = random.randint(0, total_height)
        driver.execute_script(f"window.scrollTo(0, {random_position});")
        time.sleep(random.randint(1, 5))

def start_profile(token, profile_type, profile_id, folder_id):

    if profile_type == "normal":
        try:
            profile_started = False
            while profile_started != True:
                profile_id, profile_port, profile_started, message = mlx.start_normal_profile(token, profile_id, folder_id)
                if profile_started == True:
                    return profile_id, profile_port
                print(f"Profile couldn't be started. Probably downloading core. Will wait for 60 seconds and try again. Here is the message: {message}")
                time.sleep(60)

        except Exception as e:
            print(f"Problem with starting profile: {e}")

    elif profile_type == "quick":
            try:
                profile_started = False
                while profile_started != True:
                    quick_profile_id, quick_profile_port, profile_started, message = mlx.start_quick_profile(token) # Start a quick profile
                    if profile_started == True:
                        return quick_profile_id, quick_profile_port
                    print(f"Profile couldn't be started. Probably downloading core. Will wait for 60 seconds and try again. Here is the message: {message}")
                    time.sleep(60)

            except Exception as e:
                print(f"Problem with starting profile: {e}")

def main(profile_id, folder_id):

    token = mlx.signin() # Get MLX token
    profile_id, profile_port = start_profile(token, profile_type, profile_id, folder_id) # Start a quick profile
    driver = mlx.instantiate_driver(profile_port) # Instantiate a webdriver, so we can run automation
    automation(driver, profile_id, token) # Start automation

if __name__ == "__main__":
    main(profile_id, folder_id)