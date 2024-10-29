import pandas as pd
import random
from src.RandomPicture import select_random_image_from_folder

#import tester

dataframe = pd.read_excel("top100_kdrama.xlsx", usecols="B, C")

movie_title = dataframe["Title"].tolist()

#print(dataframe)

random_movie = random.choice(movie_title)

#print("Random: ", random_movie)

image_folder_path = "/pictures"
random_image_info = select_random_image_from_folder(image_folder_path) #sanırım random picture çıkarılmalı

if random_image_info:
    random_image_filename, random_image = random_image_info
    #print(f"Selected random image: {random_image_filename}")
    print(f"Selected random image: {random_image_filename}")
    random_image.show()
    '''
    if random_movie.lower() in random_image_filename.lower():
        print(f"Selected random image: {random_image_filename}")
        random_image.show()
    else:
        print("No suitable image found.")
    '''
else:
    print("Failed to select a random image.")
    #tester.download_images()

'''
if movie_picture.startswith(random_movie):
    movie_picture.show()
else:
    print("yok")
    #tester.download_images()
'''
#
#
# def select_random_image_from_folder(folder_path):
#     files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
#     if files:
#         file_name = random.choice(files)
#         return file_name
#     else:
#         return None

value_to_send = random_movie
#tester.receive_value(value_to_send)
