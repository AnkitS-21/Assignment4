import os
import requests
from googleapiclient.discovery import build

# Setup the API key and search engine ID
API_KEY = "AIzaSyBqjCo7t-OssAHZ0XZ1D1ZrA3an7YELRMo"
CSE_ID = "YOUR_CUSTOM_SEARCH_ENGINE_ID"

# Setup directory for saving images
saved_folder = 'images'
if not os.path.exists(saved_folder):
    os.mkdir(saved_folder)

def google_search(query, num_results=10):
    service = build("customsearch", "v1", developerKey=API_KEY)
    res = service.cse().list(q=query, cx=CSE_ID, searchType="image", num=num_results).execute()
    return res['items']

def download_images():
    query = input('What are you looking for? ')
    num_images = int(input('How many images do you want? '))

    print('Searching for images...')
    search_results = google_search(query, num_results=num_images)

    for idx, item in enumerate(search_results):
        img_url = item['link']
        try:
            response = requests.get(img_url)
            image_name = f"{saved_folder}/{query}_{idx + 1}.jpg"
            with open(image_name, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {image_name}")
        except Exception as e:
            print(f"Error downloading {image_name}: {e}")

if __name__ == "__main__":
    download_images()
