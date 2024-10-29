from pygoogle_image import image as pi
from PIL import Image
import os


def download_image(series_name, folder_path="C:/Users/ASUS/PycharmProjects/KoreanDramaChooser/pictures"):
    # Create the pictures folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Download image using pygoogle_image
    pi.download(series_name, limit=1, output_directory=folder_path)

    # Check if the image was downloaded
    image_path = os.path.join(folder_path, f"{series_name}.jpg")
    if os.path.exists(image_path):
        return image_path
    else:
        return None


if __name__ == "__main__":
    series_name = input("Enter the series name: ")

    # Check if the image exists in the pictures folder
    image_path = os.path.join("/pictures", f"{series_name}.jpg")
    if os.path.exists(image_path):
        # Image exists, show it
        img = Image.open(image_path)
        img.show()
    else:
        # Image doesn't exist, download from pygoogle_image
        downloaded_image_path = download_image(series_name)
        if downloaded_image_path:
            # Image downloaded successfully, show it
            img = Image.open(downloaded_image_path)
            img.show()
        else:
            print("No image found using pygoogle_image.")
