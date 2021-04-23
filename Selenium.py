from random import random

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#tự động vào chrome driver
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")

#chỉnh max size cho browser
driver.maximize_window()

#vào trang fb
driver.get("https://www.facebook.com/")
time.sleep(1)


def login(a,b):
    driver.find_element_by_name("email").send_keys(a)
    time.sleep(1)
    driver.find_element_by_name("pass").send_keys(b)
    time.sleep(1)
    # Nhấn nút login
    driver.find_element_by_name("login").click()
    time.sleep(3)


def func_like(like1):
    button_like = driver.find_element_by_xpath(like1)
    driver.execute_script("arguments[0].click();", button_like)
    time.sleep(6)


def func_comment(comment1):
    comment_link = driver.find_element_by_xpath(comment1)
    comment_link.send_keys("hello")
    time.sleep(6)
    comment_link.send_keys(Keys.ENTER)
    time.sleep(5)


def func_comment2(comment1):
    comment_link = driver.find_element_by_xpath(comment1)
    comment_link.send_keys("hi")
    time.sleep(6)
    comment_link.send_keys(Keys.ENTER)
    time.sleep(5)


def func_share(share1, share_on_profile):
    button_share = driver.find_element_by_xpath(share1)
    driver.execute_script("arguments[0].click();", button_share)
    time.sleep(6)
    button_share_now = driver.find_element_by_xpath(share_on_profile)
    driver.execute_script("arguments[0].click();", button_share_now)
    time.sleep(6)

def func_crawling():
    comment_list = driver.find_elements_by_xpath("//div[@aria-label='Bình luận']")


    # lap trong tat ca comment va crawling du lieu comment
    for comment in comment_list:
        poster = comment.find_element_by_class_name("_6qw4")
        content = comment.find_element_by_class_name("_3l3x")
        print("*", poster.text, ":", content.text)


# khai bao cac xpath
userlist = [("thienvippro306@yahoo.com", "ThienTuyen3007"), ("binhboohutech99@gmail.com", "12345678binh")]
like1 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]"
comment1 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[5]/div[2]/div/div/div/div/form/div/div/div[2]/div/div/div/div"
share1 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[3]/div"
share_on_profile = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[1]"
button_show_log = "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]"

#nhap email voi password
for a, b in userlist:

    if a == "thienvippro306@yahoo.com":
        #login
        login(a, b)
        # vào một trang bai viet muon tang tuong tac
        driver.get("https://www.facebook.com/permalink.php?story_fbid=1903351729816938&id=100004263875299")
        time.sleep(8)

        # thich theo path
        func_like(like1)

        # comment theo path
        func_comment(comment1)

        # share theo path
        func_share(share1, share_on_profile)

        # Dang xuat
        logout_link = driver.find_element_by_xpath(button_show_log)
        driver.execute_script("arguments[0].click();", logout_link)
        time.sleep(7)
        logout = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[5]/div")
        driver.execute_script("arguments[0].click();", logout)
        time.sleep(5)
    elif a == "binhboohutech99@gmail.com":
        login(a, b)
        # vào một trang facebook cá nhân bất kì
        driver.get("https://www.facebook.com/permalink.php?story_fbid=1903351729816938&id=100004263875299")
        time.sleep(7)

        # thich theo path
        func_like(like1)

        # comment theo path
        func_comment2(comment1)

        # share theo path
        func_share(share1, share_on_profile)

        # Dang xuat
        logout_link = driver.find_element_by_xpath(button_show_log)
        driver.execute_script("arguments[0].click();", logout_link)
        time.sleep(6)
        logout = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[1]/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[6]/div/div[1]")
        driver.execute_script("arguments[0].click();", logout)
        time.sleep(5)

        # vào trang fb comment
        driver.get("https://www.facebook.com/permalink.php?story_fbid=1903351729816938&id=100004263875299")
        time.sleep(5)

        # click vao nut "luc khac"
        driver.find_element_by_id("expanding_cta_close_button").click()

        # click vao nut comment
        driver.find_element_by_class_name("_4vn2").click()

        # click hien thi them comment
        driver.find_element_by_class_name(" _4ssp").click()
        time.sleep(4)

        # crawling du lieu
        func_crawling()
        time.sleep(6)
input()
driver.quit()  #KET THUC QUA TRINH