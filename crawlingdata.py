from random import random

from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#tự động vào chrome driver
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")

#chỉnh max size cho browser
driver.maximize_window()

#vào trang fb
driver.get("https://www.facebook.com/permalink.php?story_fbid=1903351729816938&id=100004263875299")
time.sleep(5)

#click vao nut "luc khac"
driver.find_element_by_id("expanding_cta_close_button").click()

#click vao nut comment
driver.find_element_by_class_name("_4vn2").click()
time.sleep(3)

#click hien thi them comment
driver.find_element_by_class_name("_4sxd").click()
time.sleep(4)

def func_crawling():
    comment_list = driver.find_elements_by_xpath("//div[@aria-label='Bình luận']")

    # lap trong tat ca comment va crawling du lieu comment
    for comment in comment_list:
        poster = comment.find_element_by_class_name("_6qw4")
        content = comment.find_element_by_class_name("_3l3x")
        print("*", poster.text, ":", content.text)


func_crawling()
time.sleep(4)
driver.quit()
