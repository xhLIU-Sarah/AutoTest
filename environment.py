# coding=utf-8
import time
from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome('driver/chromedriver.exe')


def before_feature(context, feature):
    print 'before feature'


def after_all(context):
    context.driver.quit()
