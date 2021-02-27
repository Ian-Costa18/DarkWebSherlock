from tbselenium.tbdriver import TorBrowserDriver
import tbselenium.common as cm
from tbselenium.utils import launch_tbb_tor_with_stem

from time import sleep
from atexit import register as atexit_register



class DarkWebSherlock():
    def __init__(self):
        self.tbb_dir = "./tor-browser_en-US/"
        torrc = {
            "SOCKSPort": "9250",
            "Log": ["NOTICE file /dev/null"]
        }
        self.tor_process = launch_tbb_tor_with_stem(
            tbb_path=tbb_dir, torrc=torrc)
        atexit_register(tor_process.kill)


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
                driver.screenshot(f"../../{username}-dread.png")

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

    def NEWWEBSITE(self, url, username, screenshot=True):
        driver = self.tor_browser_start()

        driver.quit()

if __name__ == '__main__':
    program = DarkWebSherlock()
    dread_url = "http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion"
    username = "USERNAME"

    program.dread(dread_url, username)

    program.stop_tor()
