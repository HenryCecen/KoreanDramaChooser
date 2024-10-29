import os
import random
from PIL import Image


def select_random_image_from_folder(folder_path):
    try:
        image_files = [f for f in os.listdir(folder_path) if
                       f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

        if not image_files:
            print(f"No image files found in the folder: {folder_path}")
            return None

        random_image_filename = random.choice(image_files)
        random_image_path = os.path.join(folder_path, random_image_filename)

        image = Image.open(random_image_path)
        return random_image_filename, image
    except FileNotFoundError:
        print("Error: Folder not found.")
        return None
