from selenium.webdriver.common.by import By

# Кнопки "Заказать" для разных размеров
button_order_large = [By.XPATH, "//button[contains(@class, 'Order_Button__large') and text()='Заказать']"]
button_order_medium = [By.XPATH, "//button[contains(@class, 'Order_Button__medium') and text()='Заказать']"]
button_order_small = [By.XPATH, "//button[contains(@class, 'Order_Button__small') and text()='Заказать']"]

# Поля ввода
input_name = [By.XPATH, "//input[@placeholder='* Имя']"]
input_surname = [By.XPATH, "//input[@placeholder='* Фамилия']"]
input_address = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
input_metro_station = [By.XPATH, "//input[@placeholder='* Станция метро']"]
input_phone = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]

# Кнопка "Далее"
button_next_step = [By.XPATH, "//button[text()='Далее']"]

# Заголовок раздела "Про аренду"
header_about_rent = [By.XPATH, "//div[text()='Про аренду']"]

# Поле ввода даты аренды
input_rent_date = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]

# Выпадающий список с выбором срока аренды
dropdown_rent_duration = [By.XPATH, "//div[text()='* Срок аренды']"]
option_one_day = [By.XPATH, "//div[text()='сутки']"]

# Чекбокс "Черный самокат"
checkbox_black_scooter = [By.XPATH, "//input[@id='black']"]

# Поле для комментария
input_comment = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

# Кнопка подтверждения заказа "Да"
button_confirm_yes = [By.XPATH, "//button[text()='Да']"]

# Сообщение об успешном оформлении заказа
message_order_success = [By.XPATH, "//div[text()='Заказ оформлен']"]

# Логотипы на странице
logo_main_scooter = [By.XPATH, "//img[@alt='Scooter']"]
logo_yandex_main = [By.XPATH, "//img[@alt='Yandex']"]

# Заголовок на главной странице "Самокат"
header_scooter_main = [By.XPATH, "//div[text()='Самокат ']"]

# Кнопки для поиска и проверки статуса
button_search_dzen = [By.XPATH, "//button[text()='Найти']"]
button_check_status = [By.XPATH, "//button[text()='Посмотреть статус']"]

# Кнопка принятия cookies
button_accept_cookies = [By.CLASS_NAME, "App_CookieButton__3cvqF"]
