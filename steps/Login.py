# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from behave import *
import pageObject.BingLoginpage as Loginpage
import pageObject.BingHomepage as Homepage
import defineFunction.MyFunction as Myfunction

@Step(u'我在bing登陆页面')
def step_impl(context):
    Homepage.Open(context)
    Myfunction.Web_Wait(context,'id_s')
    #WebDriverWait(context.driver,10).until(EC.element_to_be_clickable((By.ID,'id_s')))
    Loginpage.Signin_Link(context).click()


@Step(u'我登陆账号"{account}"密码:"{password}"')
def step_impl(context,account,password):
    #WebDriverWait(context.driver,10).until(EC.element_to_be_clickable((By.ID,'i0116')))
    Myfunction.Web_Wait(context,'i0116')
    Loginpage.Account_Textbox(context).clear()
    Loginpage.Account_Textbox(context).send_keys(account)

    Loginpage.Nextstep_Button(context).click()

    #WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'i0118')))
    Myfunction.Web_Wait(context,'i0118')
    Loginpage.Password_Textbox(context).clear()
    Loginpage.Password_Textbox(context).send_keys(password)

    Loginpage.Signin_Button(context).click()
@Step(u'我应该成功登陆bing账号')
def step_impl(context):
    WebDriverWait(context.driver,10).until(EC.new_window_is_opened)
    assert Loginpage.Account_menu(context)
