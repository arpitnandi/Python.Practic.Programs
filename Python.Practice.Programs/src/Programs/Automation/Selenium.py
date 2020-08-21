from selenium import webdriver

Driver=webdriver.Firefox()

Driver.maximize_window()

Driver.minimize_window()

Driver.maximize_window()

Driver.get("https://www.google.co/")

print('Title : ',Driver.title)

Driver.close()