from selenium.webdriver.common.by import By


class MyAccountLocators:

    ACCOUNT_NAME = (By.CLASS_NAME, 'account-name')

    SORT_BUTTON = (By.CSS_SELECTOR, 'div[data-cy="sort-desktop"]')

    ASSCENDING_SORT_BUTTON = (By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[3]')

    DESCENDEING_SORT_BUTTON = (By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[2]')

    PRODUCTS_PRICE = (By.XPATH, '//div[@class=" flex-1 gap-4 grid grid-cols-1 sm:grid-cols-2 min-[991px]:grid-cols-3 "] //div[5]//div//div//span[@data-cy="phone-price"]')

    RECOMMENDATION_BUTTON = (By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[1]')

    ACCOUNT_SIDE_MENU_BAR = (By.CSS_SELECTOR, 'ul[class="sidebar-menu list-unstyled"]>li')

