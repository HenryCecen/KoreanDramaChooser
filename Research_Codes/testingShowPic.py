import pandas as pd
import random
import os
from PIL import Image


class Main():
    def get_movie(self):
        dataframe = pd.read_excel("top100_kdrama.xlsx", usecols="B, C")

        movie_title = dataframe["Title"].tolist()

        image_folder_path = "/pictures"

        image_files = [f for f in os.listdir(image_folder_path) if f.endswith('.jpg')]

        random_movie = random.choice(movie_title)

        print("Random: ", random_movie)

        image_file = next((f for f in image_files if random_movie.lower() in f.lower()), None)

        if image_file:
            # Load and display the image
            print("Here is picture")
            image_path = os.path.join(image_folder_path, image_file)
            image = Image.open(image_path)
            image.show()
        else:
            print("No image found for the selected movie.")
            #tester.download_images()
            tester.download_images(image_folder_path, random_movie)
            self.get_movie()

        #value_to_send = random_movie
        #tester.receive_value(value_to_send)
        return random_movie

if __name__ == '__main__':
    main_instance = Main()
    main_instance.get_movie()