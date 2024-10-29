import pandas as pd
import random
import os
from PIL import Image

dataframe = pd.read_excel("top100_kdrama.xlsx", usecols="B, C")  # Assuming "Title" is in column A and "Genre" is in column C

# Display available genres
available_genres = dataframe["Genre"].unique()
#print("Available genres:", available_genres)

select_genre = input("What genre do you want to watch: ")

folder_path = "/pictures"

if any(select_genre in genres for genres in available_genres):
    #genre_movies = dataframe[dataframe["Genre"] == select_genre]
    genre_movies = dataframe[dataframe["Genre"].str.contains(select_genre)]
    #print("Selected genre movies:", genre_movies["Title"].tolist())
    if not genre_movies.empty:
        random_movie = random.choice(genre_movies["Title"].tolist())
        print(f"Here is a random {select_genre} movie: {random_movie}")
        files_in_folder = os.listdir(folder_path)
        matching_files = [file for file in files_in_folder if os.path.splitext(file)[0] == random_movie]

        if matching_files:
            print(f"Matching images in the folder for {random_movie}: {matching_files}")
            for image_file in matching_files:
                image_path = os.path.join(folder_path, image_file)
                img = Image.open(image_path)
                img.show()
        else:
            print(f"No matching images found for {random_movie} in the folder.")
    else:
        print(f"No movies found for the genre: {select_genre}")
else:
    print("Invalid genre selection.")
