from selenium.webdriver.common.by import By
class Locators:
    #section below with variables for login page:
    page_login_url = 'https://stellarburgers.nomoreparties.site/login' #url страницы логин
    field_email_xpath = ".//input[(@class = 'text input__textfield text_type_main-default' and @type='text')]" #email поле
    field_password_xpath = ".//input[(@class = 'text input__textfield text_type_main-default' and @type='password')]" #password поле
    page_login_button_xpath = ".//button[(@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa')]" #кнопка войти
    page_login_registration_link = ".//a[(@class = 'Auth_link__1fOlj')]" #ссылка Зарегестрироваться
    #main page:
    page_main_url = "https://stellarburgers.nomoreparties.site/" #url главной страницы Конструктор
    page_main_name_label_xpath = ".//h1[(@class = 'text text_type_main-large mb-5 mt-10')]" #заголовок страницы
    page_main_personal_account_tab_xpath = ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']" #вкладка Личный кабинет
    page_main_constructor_tab_xpath = ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']" #вкладка Конструктор
    page_main_constructor_logo_xpath = ".//div[@class='AppHeader_header__logo__2D0X2']" #лого
    page_main_button_gradient_button_xpath = ".//button[(@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg')]" #кнопка - оформить заказ
    page_main_sections_xpath = ".//span[(@class='text text_type_main-default')][2]" # секции - доработать
    #registration page:
    page_registration_url="https://stellarburgers.nomoreparties.site/register" #url регистрации
    page_registration_register_button = (".//button[(@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa')]") #кнопка Зарегистрироваться
    page_registration_enter_button = ".//a[(@class = 'Auth_link__1fOlj' and text()='Войти')]" #кнопка - войти
    page_registration_name_field = By.XPATH, './/fieldset[1]//input' #имя
    page_registration_email_field = By.XPATH, './/fieldset[2]//input' #email
    page_registration_password_field = By.XPATH, './/fieldset[3]//input' #password
    #forgot password page:
    page_forgot_password_url = "https://stellarburgers.nomoreparties.site/forgot-password" #url восстановление пароля
    page_forgot_password_enter_button = ".//a[(@class = 'Auth_link__1fOlj' and text()='Войти')]" #кнопка - войти
    #personal account page:
    page_personal_account = "https://stellarburgers.nomoreparties.site/account/profile" # url личный кабинет
    page_personal_account_logout_button_xpath = ".//button[(@class = 'Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход' )]" #кнопка Выход
    page_personal_account_label_here_you_can = (By.XPATH,".//p[@class='Account_text__fZAIn text text_type_main-default' and text()='В этом разделе вы можете изменить свои персональные данные']") # текст В этом разделе вы можете
