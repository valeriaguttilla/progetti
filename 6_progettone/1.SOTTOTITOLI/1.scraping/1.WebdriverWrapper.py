from selenium import webdriver

class WebdriverWrapper:

# da inserire path locale chrome driver

    chromedriver = r"/Users/valeriaguttilla/Desktop/MASTER/_Tools/chromedriver"


    def __init__(self):  
        self.driver = webdriver.Chrome(WebdriverWrapper.chromedriver)

    def __del__(self):
        self.driver.close()

    def get_driver(self):
        return self.driver
