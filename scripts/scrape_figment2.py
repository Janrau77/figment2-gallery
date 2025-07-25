import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

STORE_URL = "https://store.epicgames.com/en-US/p/figment-2"

resp = requests.get(STORE_URL)
soup = BeautifulSoup(resp.text, "html.parser")

img_tags = soup.find_all("img")
img_urls = {urljoin(STORE_URL, img['src']) for img in img_tags if img.get('src', '').endswith(('.jpg', '.png'))}

os.makedirs("images", exist_ok=True)

for url in img_urls:
    fname = os.path.join("images", url.split("/")[-1])
    with open(fname, "wb") as f:
        f.write(requests.get(url).content)
