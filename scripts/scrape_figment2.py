from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import requests

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)


driver.get("https://store.epicgames.com/en-US/p/figment2-creed-valley")
img_elements = driver.find_elements(By.TAG_NAME, "img")
img_urls = [img.get_attribute('src') for img in img_elements if img.get_attribute('src') and img.get_attribute('src').endswith(('.jpg', '.png'))]

os.makedirs("images", exist_ok=True)

for url in img_urls:
    fname = os.path.join("images", url.split("/")[-1])
    try:
        r = requests.get(url)
        with open(fname, "wb") as f:
            f.write(r.content)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

driver.quit()
