link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    button = browser.find_element_by_class_name("btn-add-to-basket2")
    value = button.text
    print("\n" + value)