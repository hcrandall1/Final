import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import os

# Function to read genre information from text files
def read_genre_info(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip().split(',') for line in file.readlines()]
    except FileNotFoundError:
        return []

# Initialize genre arrays
music_genres = read_genre_info('media finder mus.txt')
movie_genres = read_genre_info('media finder M.txt')
tv_genres = read_genre_info('media finder Tv.txt')
game_genres = read_genre_info('media finder G.txt')

# Declares arrays for each media type
M_genres = []
M_titles = []
M_years = []
Tv_genres = []
Tv_titles = []
Tv_seasons = []
Tv_years = []
G_genres = []
G_titles = []
G_years = []
mus_genres = []
mus_titles = []
mus_bands = []
mus_years = []

# Function to read media information from text files
def read_media_info(filename, genre_list, title_list, year_list, extra_list=None):
    media_info = read_genre_info(filename)
    for info in media_info:
        genre_list.append(info[0])
        title_list.append(info[1])
        year_list.append(info[2])
        if extra_list is not None:
            extra_list.append(info[3])

# Read media information for each media type
# Get the directory of the current script
base_directory = os.path.dirname(os.path.abspath(__file__))


base_directory = os.path.join(base_directory)

# Define the relative paths based on the adjusted base directory
media_files = [
    "media finder M.txt",
    "media finder Tv.txt",
    "media finder G.txt",
    "media finder mus.txt"
]

# Read media information using relative paths
for media_file in media_files:
    absolute_path = os.path.join(base_directory, media_file)
    if os.path.exists(absolute_path):
        if "M.txt" in media_file:
            read_media_info(absolute_path, M_genres, M_titles, M_years)
        elif "Tv.txt" in media_file:
            read_media_info(absolute_path, Tv_genres, Tv_titles, Tv_years, Tv_seasons)
        elif "G.txt" in media_file:
            read_media_info(absolute_path, G_genres, G_titles, G_years)
        elif "mus.txt" in media_file:
            read_media_info(absolute_path, mus_genres, mus_titles, mus_years, mus_bands)
    else:
        print(f"File '{absolute_path}' not found.")

# Function to search and display media based on type and genre
def search_media(media_type, genre):
    global result_window

    found_genre = False
    result_text = f"Sorry, we don't have any {media_type} in the {genre} genre."

    result_window = tk.Toplevel(root)
    result_window.title(f"{media_type}, {genre}")
    result_window.geometry("1200x1200")

    media_type_label = tk.Label(result_window, text=f"Media Type: {media_type}", font=("Arial", 14, "bold"))
    media_type_label.grid(row=0, column=0, padx=10, pady=10)
    genre_label = tk.Label(result_window, text=f"Genre: {genre}", font=("Arial", 14, "bold"))
    genre_label.grid(row=1, column=0, padx=10, pady=10)

    index = 2

    # Display media information based on type and genre
    if media_type == "Movies":
        for i in range(len(M_titles)):
            if M_genres[i] == genre:
                image_name = M_titles[i]
                image_directory = os.path.join(base_directory, "..", "Final Photos", "Movies")
                image_path = os.path.join(image_directory, image_name + ".jpg")
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    image = image.resize((100, 115), Image.BICUBIC)
                    photo = ImageTk.PhotoImage(image)
                    image_label = tk.Label(result_window, image=photo)
                    image_label.image = photo
                    image_label.grid(row=index, column=0, padx=10, pady=10)
                    text_label = tk.Label(result_window, text=f"{M_titles[i]}\nRelease Year: {M_years[i]}", justify=tk.LEFT)
                    text_label.grid(row=index, column=1, padx=10, pady=10)
                    index += 1
                    found_genre = True
    elif media_type == "Tv":
        for i in range(len(Tv_titles)):
            if Tv_genres[i] == genre:
                image_name = Tv_titles[i]
                image_directory = os.path.join(base_directory, "..", "Final Photos", "Tv")
                image_path = os.path.join(image_directory, image_name + ".jpg")
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    image = image.resize((100, 115), Image.BICUBIC)
                    photo = ImageTk.PhotoImage(image)
                    image_label = tk.Label(result_window, image=photo)
                    image_label.image = photo
                    image_label.grid(row=index, column=0, padx=10, pady=10)
                    text_label = tk.Label(result_window, text=f"{Tv_titles[i]}\n#Of Seasons: {Tv_seasons[i]}\nRelease Year: {Tv_years[i]}", justify=tk.LEFT)
                    text_label.grid(row=index, column=1, padx=10, pady=10)
                    index += 1
                    found_genre = True
    elif media_type == "Games":
        for i in range(len(G_titles)):
            if G_genres[i] == genre:
                image_name = G_titles[i]
                image_directory = os.path.join(base_directory, "..", "Final Photos", "Games")
                image_path = os.path.join(image_directory, image_name + ".jpg")
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    image = image.resize((100, 115), Image.BICUBIC)
                    photo = ImageTk.PhotoImage(image)
                    image_label = tk.Label(result_window, image=photo)
                    image_label.image = photo
                    image_label.grid(row=index, column=0, padx=10, pady=10)
                    text_label = tk.Label(result_window, text=f"{G_titles[i]}\nRelease Year: {G_years[i]}", justify=tk.LEFT)
                    text_label.grid(row=index, column=1, padx=10, pady=10)
                    index += 1
                    found_genre = True
    elif media_type == "Music":
        for i in range(len(mus_titles)):
            if mus_genres[i] == genre:
                image_name = mus_titles[i]
                image_directory = os.path.join(base_directory, "..", "Final Photos", "Music")
                image_path = os.path.join(image_directory, image_name + ".jpg")
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    image = image.resize((100, 115), Image.BICUBIC)
                    photo = ImageTk.PhotoImage(image)
                    image_label = tk.Label(result_window, image=photo)
                    image_label.image = photo
                    image_label.grid(row=index, column=0, padx=10, pady=10)
                    text_label = tk.Label(result_window, text=f"{mus_titles[i]}\nThe Band: {mus_bands[i]}\nRelease Year: {mus_years[i]}", justify=tk.LEFT)
                    text_label.grid(row=index, column=1, padx=10, pady=10)
                    index += 1
                    found_genre = True

    if not found_genre:
        result_text += f"Sorry, we don't have any {media_type} in the {genre} genre."

    find_more_label = tk.Label(result_window, text="Do you want to find more media?", font=("Arial", 12))
    find_more_label.grid(row=0, column=3, columnspan=2, padx=10, pady=5, sticky=tk.E)

    def destroy_result_window():
        result_window.destroy()
        root.deiconify()

    close_button_yes = tk.Button(result_window, text="Yes", command=destroy_result_window)
    close_button_yes.grid(row=1, column=3, padx=10, pady=10, sticky=tk.E)

    close_button_no = tk.Button(result_window, text="No", command=root.destroy)
    close_button_no.grid(row=1, column=4, padx=10, pady=10, sticky=tk.E)

# Function for button click and to ask for genre input
def on_button_click(genre_type):
    genre = simpledialog.askstring("Input", f"What {genre_type} genre do you prefer?")
    genre = genre.capitalize()
    search_media(genre_type, genre)

# Create the main window
root = tk.Tk()
root.title("Media Genre Selector")
root.geometry("800x350")

title_label = tk.Label(root, text="Select Your Preferred Media Type:", font=("Arial",36))
title_label.pack(side=tk.TOP, pady=10)

button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, pady=20)

buttons = {
    "Movies": lambda: on_button_click("Movies"),
    "Tv": lambda: on_button_click("Tv"),
    "Games": lambda: on_button_click("Games"),
    "Music": lambda: on_button_click("Music"),
}

button_colors = {
    "Movies": "red",
    "Tv": "blue",
    "Games": "green",
    "Music": "purple",
}

button_width = 20
button_height = 5  # Adjust the height of the button here
button_font_size = 20

for text, command in buttons.items():
    button = tk.Button(button_frame, text=text, command=command, bg=button_colors[text], width=button_width, height=button_height, font=button_font_size)
    button.pack(side=tk.LEFT, padx=10)

root.configure(bg="grey")

root.mainloop()
