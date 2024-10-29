from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
#from tkinter import messagebox as mb
import tkinter.messagebox as mb
from src import image_downloader
import pandas as pd
import os
import random
import sys

class Ui_DramaChooser(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_DramaChooser, self).__init__()
        self.activateGui()
        self.watched_movie = []


    def activateGui(self):
        self.buildWidget()
        self.buildSignals()
        self.buildMenubarStatusBar()
        self.buildTexts()

    def buildTexts(self):
        self.setWindowTitle("Drama Chooser")
        self.btnSubmit.setText("Submit")
        self.label.setText("Your Age:")
        self.btnSubmitforGenre.setText("Submit")
        self.label_2.setText("Which genre you want to watch:")
        self.label_3.setText("Do you want to add:")
        self.label_4.setText("Do you want to add:")
        self.label_5.setText("You can watch it:")
        self.label_6.setText("Name of this watch:")
        self.btnReset.setText("Reset")
        self.btnReset.setEnabled(False)
        self.btnWatched.setEnabled(False)
        self.btnWatched.setText("Any Else")

    def buildMenubarStatusBar(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 18))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
    def buildSignals(self):
        self.btnSubmit.clicked.connect(self.ask_your_age)
        self.btnSubmitforGenre.clicked.connect(self.next_question)
        self.btnReset.clicked.connect(self.all_clear)
        self.btnWatched.clicked.connect(self.another_movie)

    def all_clear(self):
        self.cmbGenre.setEnabled(False)
        self.cmbGenre.setCurrentText("")
        self.cmbGenre_2.setEnabled(False)
        self.cmbGenre_2.setCurrentText("")
        self.btnSubmitforGenre.setEnabled(False)
        self.txtName.clear()
        self.txtYourAge.clear()
        self.graphicsView.setScene(None)
        self.txtYourAge.setEnabled(True)
        self.btnSubmit.setEnabled(True)

    def buildWidget(self):
        self.resize(472, 382)
        self.centralwidget = QtWidgets.QWidget(self)
        self.btnSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.btnSubmit.setGeometry(QtCore.QRect(160, 30, 56, 21))
        self.txtYourAge = QtWidgets.QLineEdit(self.centralwidget)
        self.txtYourAge.setGeometry(QtCore.QRect(20, 30, 131, 20))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 51, 16))
        self.cmbGenre = QtWidgets.QComboBox(self.centralwidget)
        self.cmbGenre.setGeometry(QtCore.QRect(20, 77, 131, 22))
        self.cmbGenre.addItem("")
        self.cmbGenre.setItemText(0, "")
        self.btnSubmitforGenre = QtWidgets.QPushButton(self.centralwidget)
        self.btnSubmitforGenre.setGeometry(QtCore.QRect(160, 77, 56, 21))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 200, 16))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(20, 103, 131, 16))
        self.cmbGenre_2 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbGenre_2.setEnabled(False)
        self.cmbGenre.setEnabled(False)
        self.btnSubmitforGenre.setEnabled(False)
        self.cmbGenre_2.setGeometry(QtCore.QRect(20, 120, 131, 22))
        self.cmbGenre_3 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbGenre_3.setEnabled(False)
        self.cmbGenre_3.setGeometry(QtCore.QRect(20, 160, 131, 22))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(20, 143, 131, 16))
        self.txtName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(240, 291, 201, 20))
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 10, 100, 16))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 290, 130, 20))

        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(240, 30, 201, 251))


        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setGeometry(QtCore.QRect(320, 320, 56, 21))
        self.btnWatched = QtWidgets.QPushButton(self.centralwidget)
        self.btnWatched.setGeometry(QtCore.QRect(380, 320, 56, 21))
        self.setCentralWidget(self.centralwidget)

    def show_image(self, image_path):
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(240, 30, 201, 251))
        self.graphicsView.setScene(self.scene)
        self.scene.addPixmap(QPixmap(image_path))
        self.graphicsView.show()

    def get_graphic_scene(self):
        return self.graphicsView

    def ask_your_age(self):
        AVG_AGE = 15 # Korean legal age

        your_age_str = self.txtYourAge.text()

        try:
            your_age = int(your_age_str)
        except ValueError:
            print("Invalid age entered. Please enter a valid number.")
            return

        if your_age > AVG_AGE:
            self.show_message_box("About your age", "Are you sure about your age?")
            self.select_genres_big_age()
        else:
            self.show_message_box("About your age", "Are you sure about your age?")
            self.select_genres_little_age()

    def select_genres_big_age(self):
        self.cmbGenre.addItem("")
        self.cmbGenre.addItem("")
        self.cmbGenre.addItem("")
        self.cmbGenre.addItem("")
        self.cmbGenre.addItem("")
        _translate = QtCore.QCoreApplication.translate
        self.cmbGenre.setItemText(1, _translate("DramaChooser", "Romance"))
        self.cmbGenre.setItemText(2, _translate("DramaChooser", "Crime"))
        self.cmbGenre.setItemText(3, _translate("DramaChooser", "Fantasy"))
        self.cmbGenre.setItemText(4, _translate("DramaChooser", "Life"))
        self.cmbGenre.setItemText(5, _translate("DramaChooser", "Melodrama"))

        self.cmbGenre_2.addItem("")
        self.cmbGenre_2.addItem("")
        self.cmbGenre_2.addItem("")
        self.cmbGenre_2.addItem("")
        self.cmbGenre_2.addItem("")  
        self.cmbGenre_2.addItem("")
        self.cmbGenre_2.setItemText(1, _translate("DramaChooser", "Romance"))
        self.cmbGenre_2.setItemText(2, _translate("DramaChooser", "Crime"))
        self.cmbGenre_2.setItemText(3, _translate("DramaChooser", "Fantasy"))
        self.cmbGenre_2.setItemText(4, _translate("DramaChooser", "Life"))
        self.cmbGenre_2.setItemText(5, _translate("DramaChooser", "Melodrama"))
    def select_genres_little_age(self):
        self.cmbGenre.addItem("")
        self.cmbGenre.addItem("")
        self.cmbGenre.addItem("")
        _translate = QtCore.QCoreApplication.translate
        self.cmbGenre.setItemText(1, _translate("DramaChooser", "Animation"))
        self.cmbGenre.setItemText(2, _translate("DramaChooser", "Family"))
        self.cmbGenre.setItemText(3, _translate("DramaChooser", "Comedy"))

    def another_movie(self):
        # Add the current movie to the watched list
        current_movie = self.txtName.text()
        if current_movie:
            self.watched_movie.append(current_movie)

        # Clear the displayed movie name
        #self.txtName.clear()

    def next_question(self, random_movie):
        # Enable buttons such as Reset
        self.btnReset.setEnabled(True)
        self.btnWatched.setEnabled(True)

        dataframe = pd.read_excel("C:/Users/ASUS/PycharmProjects/KoreanDramaChooser/Helper/top100_kdrama.xlsx", usecols="B, C")

        available_genres = dataframe["Genre"].unique()

        select_genre = self.cmbGenre.currentText()
        select_genre_2 = self.cmbGenre_2.currentText()
        folder_path = "C:/Users/ASUS/PycharmProjects/KoreanDramaChooser/pictures"

        if any(select_genre in genres for genres in available_genres):
            genre_movies = dataframe[dataframe["Genre"].str.contains(select_genre + ", " + select_genre_2)]
            if not genre_movies.empty:
                random_movie = random.choice(genre_movies["Title"].tolist())
                print(f"Here is a random {select_genre} movie: {random_movie}")
                self.txtName.setText(random_movie)
                files_in_folder = os.listdir(folder_path)
                matching_files = [file for file in files_in_folder if os.path.splitext(file)[0] == random_movie]

                if matching_files:
                    print(f"Matching images in the folder for {random_movie}: {matching_files}")
                    for image_file in matching_files:
                        image_path = os.path.join(folder_path, image_file)
                        self.show_image(image_path)

                else:
                    print(f"No matching images found for {random_movie} in the folder.")
                    image_downloader.download_images(folder_path, random_movie)
                    downloaded_files = [f"{random_movie}.jpg"]  # Adjust this based on your actual filename format

                    for image_file in downloaded_files:
                        image_path = os.path.join(folder_path, image_file)
                        self.show_image(image_path)
            else:
                print(f"No movies found for the genre: {select_genre} + {select_genre_2}")
        else:
            print("Invalid genre selection.")

    def show_message_box(self, title, message):
        res = mb.askquestion(title, message)

        if res == 'yes':
            self.cmbGenre.setEnabled(True)
            self.btnSubmitforGenre.setEnabled(True)
            self.btnSubmit.setEnabled(False)
            self.txtYourAge.setEnabled(False)

            self.cmbGenre_2.setEnabled(True)
        else:
            self.txtYourAge.clear()
            self.cmbGenre.setEnabled(False)
            self.btnSubmitforGenre.setEnabled(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_DramaChooser()
    ui.show()
    sys.exit(app.exec_())
