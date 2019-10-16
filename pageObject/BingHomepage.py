import time
def Open(context):
    context.driver.get('http://www.bing.com')
    context.driver.maximize_window()


def Search_TextBox(context):
    return context.driver.find_element_by_id('sb_form_q')

def Input_text(context,keyword):
    context.driver.send_keys(keyword)


def Submit_Button(context):
    return context.driver.find_element_by_id('sb_go_par')
