from selenium.webdriver.common.by import By

class PicturesPageLocators():
    SECOND_IMAGE_LINK = (By.XPATH, "//*[@data-ri='1']/a[@role='button']")
    CURRENT_IMAGE = (By.XPATH, "//div[@id='Sva75c']/div/div/div[3]/div[not(contains(@aria-hidden,'true'))]//div[@role='region']/a/img[not(contains(@src,'data:image'))]")
    NEXT_BUTTON = (By.XPATH, "//div[@id='Sva75c']/div/div/div[3]/div[not(contains(@aria-hidden,'true'))]//a[@aria-label='Следующее изображение']")
    PREV_BUTTON = (By.XPATH, "//div[@id='Sva75c']/div/div/div[3]/div[not(contains(@aria-hidden,'true'))]//a[@aria-label='Предыдущее изображение']")

class SearchPageLocators():
    SEARCH_FORM = (By.NAME, "q")
    HINT_TABLE = (By.XPATH, "//ul[@role='listbox']/li[@role='presentation']")
    WORD_IN_HINTS = (By.XPATH, "//ul[@role='listbox']/li[@role='presentation']//span[text() = 'совкомбанк']")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "#rso > div")
    SEARCH_BUTTON = (By.NAME, "btnK")
    PICTURES_BUTTON = (By.XPATH, "//*[@id='hdtb-msb']//a[text() = 'Картинки']")
