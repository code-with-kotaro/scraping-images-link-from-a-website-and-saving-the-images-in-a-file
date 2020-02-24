from bs4 import BeautifulSoup as bs
import requests
import urllib

url = requests.get("https://www.imdb.com/")
soup = bs(url.content, "html.parser")

images = soup.find_all("img")

n = 1
for image in images:
    image_url = image.get('src')
    if image_url and "https://" in image_url:
        f_name = "scraped_images/"+"image_"+str(n)+".jpg"
        urllib.request.urlretrieve(image_url, f_name)
        n += 1