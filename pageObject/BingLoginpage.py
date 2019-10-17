import defineFunction.MyFunction as Myfunction
def Account_Textbox(context):
    return context.driver.find_element_by_id('i0116')


def Nextstep_Button(context):
    return context.driver.find_element_by_id('idSIButton9')


def Password_Textbox(context):
    return context.driver.find_element_by_id('i0118')


def Signin_Button(context):
    return context.driver.find_element_by_id('idSIButton9')

def Signin_Link(context):
    return context.driver.find_element_by_id('id_s')

def Account_menu(context):
    return Myfunction.Is_Elemnt_Exist(context,'#id_sc')
