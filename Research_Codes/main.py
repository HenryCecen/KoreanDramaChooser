#from simpleimage import SimpleImage
from src import RandomPicture

#from forInterface import forInterface

AVG_AGE = 15

def main():
    enter_age()
    #ask_more()

def next_question():
    ask_to_user = ask_anymore("If you are sure about your age, shall we go to next question? :D")

def ask_anymore(prompt):
    response1 = input(prompt + "(y/n): ")
    if response1 == "n":
        enter_age()
    if response1 == "y":
        print("Then, let's go to next step!")
        #choose_kind_of_drama()

#def choose_kind_of_drama():


def enter_age():
    your_age = int(input("Enter your age, please: "))
    if your_age > AVG_AGE:
        more_than_avg()
    else:
        less_than_avg()

    #gui.Ui_DramaChooser.setupUi().btnSubmit.clicked(more_than_avg())

    '''
    app = QApplication([])
    main_window = gui.Ui_DramaChooser()  # forInterface sınıfından bir nesne oluşturun
    main_window.setupUi(main_window)  # Arayüzü başlatın
    main_window.show()  # Arayüzü gösterin

    # QPushButton nesnesine ulaşarak click işlemi
    main_window.btnSubmit.clicked.connect(lambda: handle_submit(main_window))

    app.exec_()

    '''



    '''
    def handle_submit(interface):
        your_age = int(interface.txtYourAge.text())
        if your_age > AVG_AGE:
            more_than_avg()
        else:
            less_than_avg()
    '''

def more_than_avg():
    print("You are older than the average age.")

def less_than_avg():
    print("You are younger than the average age.")


def more_than_avg():
    next_question()
    print("Which one do you want to watch?")
    print("Action, Romantic, horror, Sci-fi")

    response2 = str(input("I want to watch "))
    if response2 == "Action":
        folder_path = "C:/Users/ASUS/Desktop/Wallpaper"  # Change this to the path of your image folder
        random_image_info = RandomPicture.select_random_image_from_folder(folder_path)
        if random_image_info:
            random_image_filename, random_image = random_image_info
            print(f"Selected random image: {random_image_filename}")
            random_image.show()
        else:
            print("Failed to select a random image.")
        #image = Image.open("C:/Users/ASUS/Desktop/Wallpaper/____ __Freya's Road.png")
        #image.show()


def less_than_avg():
    print("küçüksün")

if __name__ == "__main__":
    main()