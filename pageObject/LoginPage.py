def Search_Account_Textbox(context):
    return context.driver.find_element_by_id('i0116')


def Search_Nextstep_Button(context):
    return context.driver.find_element_by_id('idSIButton9')


def Search_Password_Textbox(context):
    return context.driver.find_element_by_id('i0118')


def Search_Signin_Button(context):
    return context.driver.find_element_by_id('idSIButton9')


def Signin_page(context):
    return context.driver.current_url

def Signin_Go(context):
    return context.driver.find_element_by_id('id_s')
