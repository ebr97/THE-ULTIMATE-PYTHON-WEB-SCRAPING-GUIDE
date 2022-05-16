<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a>
# Browser Automation - Login function

In this project I will use Selenium to automate Login into a browser paired with webdriver_manager. In this way, whenever you use the function, you'll be running the latest webdriver.

## Use case
This functions can be used as a first step, whenever you need to scrape websites that require to be login in order to access the data. 

## How it works
The script will start a Chrome window, then will access the link using the webdriver. Using Selenium we'll imitate human behavour and automate the script part, parsing the username and password into the login form. We've added some delays (time.sleep()) to better imitate human interaction and to not be detected by anti-bot system. 
