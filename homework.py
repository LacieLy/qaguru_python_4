# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass


def no_arguments_test():
    pass


def print_readable_names(names):
    function_name = names.__name__
    arguments_name = names.__code__.co_varnames
    print('Function: ', *function_name.capitalize().replace("_", " "), sep='')
    if len(arguments_name) > 0:
        print('Argument: ', *arguments_name, '\n')
    else:
        print("The function has no arguments")


list_func = [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page, no_arguments_test]
for names in list_func:
    print_readable_names(names)
