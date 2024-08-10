from selenium.webdriver.common.by import By


class ProductListLocators:
    SEARCH_BAR = (By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[1]/div/div[2]/div/div/input')

    BRANDS_NAME_BUTTON = (By.CSS_SELECTOR, 'div[class="flex items-baseline"] > button')

    ASSCENDING_SORT_BUTTON = (
        By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[3]')

    DESCENDEING_SORT_BUTTON = (
        By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[2]')

    PRODUCTS_PRICE = (By.XPATH,
                      '//div[@class=" flex-1 gap-4 grid grid-cols-1 sm:grid-cols-2 min-[991px]:grid-cols-3 "] //div[5]//div//div//span[@data-cy="phone-price"]')

    RECOMMENDATION_BUTTON = (
        By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[1]')

    RESULT_MESSAGE_FOR_TERM = (By.CSS_SELECTOR, 'h1[class="text-[#231F20] text-sm tablet2:text-lg"]')

    SEARCH_SUGGESTIONS = (By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div')

    PRODUCTS_ITEM_TITLE = (By.XPATH, '//div[@data-cy="phone-title"]')

    FILTER_MESSAGE_TITLE = (By.XPATH, '//div[@class="d-flex justify-content-around container"] //h3')

    RESULT_MESSAGE_FOR_COUNT_TERM = (
        By.CSS_SELECTOR, 'div[class="inline-block tablet2:p-[6px] tablet2:bg-gray-background tablet2:rounded"]')

    SORT_BUTTON = (By.CSS_SELECTOR, 'div[data-cy="sort-desktop"]')

    CATEGORIES = (By.CSS_SELECTOR, 'div[id="headlessui-radiogroup-:R4osppb6:"] >div')
