#credentials:
user_email = 'pburleva+01@gmail.com'
user_password = 'Yandex123!'

#section below with variables for login page:
page_login_url = 'https://stellarburgers.nomoreparties.site/login'
field_email_xpath = ".//input[(@class = 'text input__textfield text_type_main-default' and @type='text')]"
field_password_xpath = ".//input[(@class = 'text input__textfield text_type_main-default' and @type='password')]"
page_login_button_xpath = ".//button[(@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa')]"

#main page:
page_main_url = "https://stellarburgers.nomoreparties.site/"
page_main_name_label_xpath = ".//h1[(@class = 'text text_type_main-large mb-5 mt-10')]"
page_main_personal_account_tab_xpath = ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']"
page_main_button_gradient_button_xpath = ".//button[(@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg')]" #кнопка - оформить заказ

#registration page:
page_registration_url="https://stellarburgers.nomoreparties.site/register"
page_registration_registration_link = ".//a[(@class = 'Auth_link__1fOlj')]"
page_registration_enter_button = ".//a[(@class = 'Auth_link__1fOlj' and text()='Войти')]" #кнопка - Войти


#forgot password page:
page_forgot_password_url = "https://stellarburgers.nomoreparties.site/forgot-password"
page_forgot_password_enter_button = ".//a[(@class = 'Auth_link__1fOlj' and text()='Войти')]" #кнопка - Войти

#personal account page:
page_personal_account_logout_button_xpath = ".//button[(@class = 'Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход' )]"

