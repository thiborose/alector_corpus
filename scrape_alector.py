__author__ = "Psawa (github.com/psawa)"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


opts = Options()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts)

# Enter your credentials
name_value = input("User name?\n\t")
password_value = input("User password?\n\t")

driver.get("https://corpusalector.huma-num.fr/faces/register.xhtml")
login =  driver.find_element_by_id("input_connection:j_idt24")
password = driver.find_element_by_id("input_connection:j_idt27")
login_button = driver.find_element_by_id("connection:j_idt32")
login.clear()
login.send_keys(name_value)

password.clear()
password.send_keys(password_value)
login_button.click()

driver.implicitly_wait(10)


class element_has_css_class(object):
  """An expectation for checking that an element has a particular css class.
  locator - used to find the element
  returns the WebElement once it has the particular css class
  """
  def __init__(self, locator, css_class):
    self.locator = locator
    self.css_class = css_class

  def __call__(self, driver):
    element = self.locator   # Finding the referenced element
    if self.css_class in element.get_attribute("class"):
        return element
    else:
        return False


parallel_texts = []

# Number of pages in the default view
for i in range(8):
    print(f"Page {i}")
    # 10 articles per page execpt for the last one 
    num_articles = 10 if i<7 else 9
    for j in range(num_articles):
        print(f"Article {j}")
        # Clicking in the desired page number 
        # As going back to list after visiting an article redirects to page 1
        if i>=1 and i<8:
            # Identifying the desired page button
            pages = WebDriverWait(driver, 50).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ui-paginator-page"))
            )
            target_page = None
            for page in pages:
                if page.text == str(i+1):
                    target_page = page
                    break

            target_page.click()

            # Page buttons will be somewhat reloaded, so again 
            # Identifying the desired page button
            pages = WebDriverWait(driver, 50).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ui-paginator-page"))
            )
            target_page = None
            for page in pages:
                if page.text == str(i+1):
                    target_page = page
                    break

            # Wait until the page button is selected
            wait = WebDriverWait(driver, 10)
            wait.until(element_has_css_class(target_page, "ui-state-active"))

        # Selecting all the articles from the list on the page
        rows = WebDriverWait(driver, 50).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td:first-of-type .ui-commandlink"))
        )
        row = rows[j]
        print(row.text)

        # Going to the desired article's page
        row.click()
        
        # Getting the parallel texts 
        source_text = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.ID, "form:corpusOrig"))
        ).text

        target_text = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.ID, "form:corpusSimp"))
        ).text

        print(source_text[:15]+"...\n")

        parallel_texts.append((source_text, target_text))

        # Going back to the previous page (articles list)
        driver.back()


# writing corpus in files
for i in range(len(parallel_texts)):
    with open(f"./corpus/{i}_source.txt", 'w') as f:
        f.write(parallel_texts[i][0])
    with open(f"./corpus/{i}_target.txt", 'w') as f:
        f.write(parallel_texts[i][1])
    
driver.close()