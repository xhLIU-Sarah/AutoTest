# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from behave import *
import pageObject.LoginPage as LogIn
import pageObject.BingHomepage as Homepage

@Step(u'我在bing页面进入登陆页面')
def step_impl(context):
    Homepage.Open(context)
    WebDriverWait(context.driver,10).until(EC.element_to_be_clickable((By.ID,'id_s')))
    LogIn.Signin_Go(context).click()


@Step(u'我登陆账号"{account}"密码:"{password}"')
def step_impl(context,account,password):
    WebDriverWait(context.driver,10).until(EC.element_to_be_clickable((By.ID,'i0116')))

    LogIn.Search_Account_Textbox(context).clear()
    LogIn.Search_Account_Textbox(context).send_keys(account)

    LogIn.Search_Nextstep_Button(context).click()

    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'i0118')))
    LogIn.Search_Password_Textbox(context).clear()
    LogIn.Search_Password_Textbox(context).send_keys(password)
    LogIn.Search_Signin_Button(context).click()
    #WebDriverWait(context.driver, 10).until(EC.new_window_is_opened)
@Step(u'我应该看到包含"{successflag}"的登陆成功页面')
def step_impl(context,successflag):
    WebDriverWait(context.driver,10).until(EC.new_window_is_opened)
    assert LogIn.Signin_page(context).__contains__(successflag)
