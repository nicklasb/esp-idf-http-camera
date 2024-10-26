import requests
import time
import os
import base64
from bs4 import BeautifulSoup

def take_picture():
    url = "http://192.168.0.100:8080/take/picture"
    response = requests.get(url)
    if response.status_code == 200:
        print("Picture taken successfully.")
    else:
        print("Failed to take picture.")

def fetch_image():
    url = "http://192.168.0.100:8080"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tag = soup.find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_data = img_tag['src'].split(',')[1]  # Extract base64 part
            return base64.b64decode(img_data)
    print("Failed to fetch image or invalid content.")
    return None

def save_image(image_data, image_number):
    if not os.path.exists('images'):
        os.makedirs('images')
    file_path = f'images/image_{image_number}.jpg'
    with open(file_path, 'wb') as file:
        file.write(image_data)
    print(f"Image saved as {file_path}")

def main():
    image_number = 1
    while True:
        take_picture()
        time.sleep(1)
        image_data = fetch_image()
        if image_data:
            save_image(image_data, image_number)
            image_number += 1
        time.sleep(1)  # Adjust the sleep time as needed

if __name__ == "__main__":
    main()