from tbselenium.tbdriver import TorBrowserDriver
import tbselenium.common as cm
from tbselenium.utils import launch_tbb_tor_with_stem
from selenium.common.exceptions import NoSuchElementException

from time import sleep
from atexit import register as atexit_register



class DarkWebSherlock():
    def __init__(self):
        self.tbb_dir = "/home/ian/Storage/Files/Programs/DarkWebSherlock/tor-browser_en-US/"
        torrc = {
            "SOCKSPort": "9250",
            "Log": ["NOTICE file /dev/null"]
        }
        self.tor_process = launch_tbb_tor_with_stem(tbb_path=self.tbb_dir, torrc=torrc)
        atexit_register(self.tor_process.kill)


    def stop_tor(self):
        self.tor_process.kill()


    def tor_browser_start(self):
        return TorBrowserDriver(self.tbb_dir, tor_cfg=cm.USE_STEM)


    def dread(self, url, username, screenshot=True):
        # Start the tor browser
        driver = self.tor_browser_start()
        # Get the URL using the driver
        driver.get(f"{url}/u/{username}")
        # This command waits for the element's below to be loaded
        driver.implicitly_wait(10000)
        # If the user couldn't be found, find the error message
        error = driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[1]')

        # Check if the error message contains the error text
        if error.text == "Error 404":
            print("\n\n\n\n USERNAME NOT FOUND \n\n\n\n")
            # If screenshot is true, screenshot and save as USERNAME-WEBSITE.png
            if screenshot:
                driver.screenshot(f"../../{username}-error-dread.png")

            # Return the function with an error
            return False

        # Find the user's information
        user_header = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]")
        # Sleep to wait for CSS to load
        sleep(10)

        # If screenshot is true, screenshot and save as USERNAME-WEBSITE.png
        if screenshot:
            print("\n\n\nSCREENSHOT\n\n\n\n")
            user_header.screenshot(f"../../{username}-dread.png")

        # Quit the driver
        driver.quit()

        return True


    def recon(self, url, username, screenshot=True):
        # Start the tor browser
        driver = self.tor_browser_start()
        # Get the URL using the driver
        driver.get(f"{url}/vendor/{vendor}")
        # This command waits for the element's below to be loaded
        driver.implicitly_wait(10000)
        # If the user couldn't be found, find the error message
        error = driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[1]')

        # Check if the error message contains the error text
        if error.text == "Error 404":
            print("\n\n\n\n VENDOR NOT FOUND \n\n\n\n")
            # If screenshot is true, screenshot and save as USERNAME-WEBSITE.png
            if screenshot:
                driver.screenshot(f"../../{vendor}-recon.png")

            # Return the function with an error
            return False

        # Find the user's information
        user_header = driver.find_element_by_xpath(
            "/html/body/div/div[2]/div[1]")
        # Sleep to wait for CSS to load
        sleep(5)

        # If screenshot is true, screenshot and save as USERNAME-WEBSITE.png
        if screenshot:
            print("\n\n\nSCREENSHOT\n\n\n\n")
            user_header.screenshot(f"../../{vendor}-recon.png")

        # Quit the driver
        driver.quit()

        return True

    def hydra(self, url, username, screenshot=True):
        # NOT WORKING
        driver = self.tor_browser_start()

        driver.get(url)
        driver.implicitly_wait(10000)

        driver.get(f"{url}/user/{username}")

        driver.implicitly_wait(10000)
        error = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div/div[2]/div[1]")

        if error.text == "404":
            print("\nUsername not found!")
            if screenshot:
                driver.screenshot(f"../../{username}-error-hydra.png")

            return False

        user_header = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div[1]")

        sleep(10)

        if screenshot:
            print("\n\n\nSCREENSHOT\n\n\n\n")
            user_header.screenshot(f"../../{username}-hydra.png")


        driver.quit()

        return True

    def raidforums(self, url, username, screenshot=True):
        # Start the tor browser
        driver = self.tor_browser_start()
        # Get the URL using the driver
        url = f"{url}/User-{username}"
        driver.get(url)
        # If the user couldn't be found, find the error message
        try:
            error = driver.find_element_by_xpath('/html/body/div[1]/main/table/tbody/tr[2]/td')

            # Check if the error message contains the error text
            if error.text == "The member you specified is either invalid or doesn't exist.":
                print("\n\n\n\n USERNAME NOT FOUND \n\n\n\n")
                # If screenshot is true, screenshot and save as USERNAME-WEBSITE.png
                if screenshot:
                    driver.screenshot(f"../../{username}-error-raidforums.png")

                # Return the function with an error
                return False
        except NoSuchElementException:
            # Find the user's information
            user_header = driver.find_element_by_xpath(
                '//*[@id="profile"]')
            # Sleep to wait for CSS to load
            sleep(3)

            # If screenshot is true, screenshot and save as USERNAME-WEBSITE.png
            if screenshot:
                print("\n\n\nSCREENSHOT\n\n\n\n")
                user_header.screenshot(f"../../{username}-raidforums.png")

            # Quit the driver
            driver.quit()

            return True, url


if __name__ == '__main__':
    program = DarkWebSherlock()
    url = "https://raidforums.com"
    username = "Mrbom"

    program.raidforums(url, username)

    program.stop_tor()
