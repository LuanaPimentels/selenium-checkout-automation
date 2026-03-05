from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--incognito")

navegador = webdriver.Chrome(options=options)

# abrir o site
navegador.get("https://www.saucedemo.com/")
navegador.maximize_window()

# login
WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")
navegador.find_element(By.ID, "password").send_keys("secret_sauce")
navegador.find_element(By.ID, "login-button").click()

# clicar no produto
produto = WebDriverWait(navegador, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "img.inventory_item_img"))
)
produto.click()

# adicionar ao carrinho
WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.ID, "add-to-cart"))
).click()

# abrir carrinho
WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
).click()

# checkout
WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.ID, "checkout"))
).click()

# preencher dados
WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.ID, "first-name"))
).send_keys("Jane")
navegador.find_element(By.ID, "last-name").send_keys("Smith")
navegador.find_element(By.ID, "postal-code").send_keys("00000")

# continuar e finalizar
navegador.find_element(By.ID, "continue").click()
WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.ID, "finish"))
).click()

print("Compra finalizada com sucesso!")
navegador.save_screenshot("resultado_checkout.png")
navegador.quit()