from selenium import webdriver
url = 'https://www.irctc.co.in/nget/train-search'
path = '/home/bigbash/Downloads/chromedriver_latest' #  this varies according to ur latest chrome driver path
driver = webdriver.Chrome(path)  # initialize driver 

text1 = 'PUNE JN - PUNE'
text2 = 'MUMBAI CENTRAL - BCT'


def enter_text():
    driver.get(url)  # opens the URL in the chromedriver (a browser is popped up) 
    textbox1 = driver.find_element_by_xpath('//*[@id="origin"]/span/input')  # finds the element by xpath which is a textbox
    textbox1.send_keys(text1)
    textbox2 = driver.find_element_by_xpath('//*[@id="destination"]/span/input')
    textbox2.send_keys(text2)


enter_text()
