# -----------------------------------
# Problem 8-1
# -----------------------------------

# function for radio station
def tune_radio(station):
    print("Let me tune in", station)

# user input
favorite_station = input("What is your favorite radio station? ")

# call function
tune_radio(favorite_station)

print()


# -----------------------------------
# Problem 8-2
# -----------------------------------

# function for business cards
def print_business_cards(name, quantity, tagline):
    print("Printing", quantity, "business cards for", name)
    print("Tag line:", tagline)
    print()

# function calls
print_business_cards("Zahedur Rahman", 100, "The Genius")
print_business_cards("Satoru Gojo", 250, "The Strongest")
print_business_cards("Ryomen Sukuna", 50, "The Smartest")


# -----------------------------------
# Problem 8-3
# -----------------------------------

# function with default quantity
def print_business_cards(name, tagline, quantity=100):
    print("Printing", quantity, "business cards for", name)
    print("Tag line:", tagline)
    print()

# function calls
print_business_cards("Zahedur Rahman", "The Genius", 150)
print_business_cards("Satoru Gojo", "The Strongest")


# -----------------------------------
# Problem 8-4
# -----------------------------------

# function returns song info
def song_info(song, artist="Unknown"):
    return song + " by " + artist

# function calls
print(song_info("Lose Yourself", "Eminem"))
print(song_info("Starboy", "The Weeknd"))
print(song_info("Mystery Song"))

print()


# -----------------------------------
# Problem 8-5
# -----------------------------------

# function creates song dictionary
def create_song(song, artist="Unknown"):
    return {"song": song, "artist": artist}

# function to print playlist
def print_playlist(song_list):
    for item in song_list:
        print("Song:", item["song"])
        print("Artist:", item["artist"])
        print()

# empty list
playlist = []

# while loop for input
while True:
    song = input("Enter a song title (or type quit to stop): ")

    if song.lower() == "quit":
        break

    artist = input("Enter artist name: ")

    playlist.append(create_song(song, artist))

# print playlist
print()
print("Playlist:")
print_playlist(playlist)