from time import sleep
link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_button_is_present(browser):
    browser.get(link)

    add_to_basket = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert add_to_basket, 'could not find the add button'