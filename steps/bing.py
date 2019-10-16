# coding=utf-8
from behave import *
import pageObject.BingHomepage as HomePage
import pageObject.SearchPage as searchPage

@Step (u'我在bing的首页')
def step_impl(context):
    HomePage.Open(context)
@Step (u'我搜索"{keyword}"')
def step_impl(context,keyword):
    HomePage.Search_TextBox(context).send_keys(keyword)
    HomePage.Submit_Button(context).click()
@Step (u'我应该看见包含"{keyword}"的搜索结果')
def step_impl(context,keyword):
    assert searchPage.__contains__(keyword)

