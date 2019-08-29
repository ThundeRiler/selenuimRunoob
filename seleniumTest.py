from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Open the website and check if it is correct
driver = webdriver.Chrome('/Users/yc/Downloads/chromedriver')
driver.get("https://www.naati.com.au/MyNaati/")
assert "Home Page" in driver.title

# Input username and password to sign in 
userName = driver.find_element_by_name("UserName")
passWord = driver.find_element_by_name('Password')
userName.send_keys("649980006@qq.com")
passWord.send_keys("Qq1Ww2Ee3!")
passWord.send_keys(Keys.RETURN)

# Go to the 'manage my test' page by XPath method
# got a question here: cannot find the link test when using link_test to get the link
driver.find_element_by_xpath("//div[@class='content']\
                             /div[@class='container']\
                             /div[2]/div[@class='menu-link-container']\
                             /div[3]/div[@class='thumbnail']\
                             /div[@class='caption']\
                             /h3\
                             /a").click()


# Go to the Manage page
# same question, same error : no such element: Unable to locate element: {"method":"link text","selector":"Manage"}
driver.find_element_by_class_name('btn btn-primary').click()




#driver.close()
