from tbselenium.tbdriver import TorBrowserDriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait


def main():
    driver = TorBrowserDriver("./tor-browser_en-US/")
    username = "Shakybeats"
    url = f"http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/u/{username}"
    driver.get(url)
    driver.implicitly_wait(10000)
    error = driver.find_element_by_xpath(
        '/html/body/div/div[2]/div/div[1]')
    if error.text == "Error 404":
        print("\n\n\n\n USERNAME NOT FOUND \n\n\n\n")
        return False

    user_header = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]")
    sleep(10)
    print("\n\n\nSCREENSHOT\n\n\n\n")
    user_header.screenshot(
        f"/home/ian/Storage/Files/Programs/DarkWebSherlock/{username}-dread.png")


if __name__ == '__main__':
    main()
