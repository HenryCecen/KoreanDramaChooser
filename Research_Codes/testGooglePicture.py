from googlesearch import search
import requests
from PIL import Image
from io import BytesIO

def google_image_search(series_name, num_results=3):
    image_urls = []

    # Google'da resim araması yap
    search_query = f"{series_name} poster"
    for j in search(search_query, num_results=num_results):
        if j.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_urls.append(j)

    # Resimleri indir ve göster
    for image_url in image_urls:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.show()

#if __name__ == "__main__":
 #   series_name = input("Dizi ismini girin: ")
  #  google_image_search(series_name)
