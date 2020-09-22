from random import sample

GENRES = ["pop", "rock", "techno"]
MOODS = ["happy", "party", "calming", "lounge"]

# create the simulation
def simulation():
    genres_index = [0, 0, 0]
    moods_index = [0, 0, 0, 0]
    playlists = []
    for i in range(100):
        playlist = []
        for i in range(50):
            song = (sample(GENRES, 1)[0], sample(MOODS, 1)[0])
            if song[0] == GENRES[0]:
                genres_index[0] += 1
            elif song[0] == GENRES[1]:
                genres_index[1] += 1
            elif song[0] == GENRES[2]:
                genres_index[2] += 1

            if song[1] == MOODS[0]:
                moods_index[0] += 1
            elif song[1] == MOODS[1]:
                moods_index[1] += 1
            elif song[1] == MOODS[2]:
                moods_index[2] += 1
            elif song[1] == MOODS[3]:
                moods_index[3] += 1
            playlist.append(song)
        playlists.append(playlist)

    print("The dataset has been simulated successfully. Here are some statistics:")
    print(
        "There are %i pop, %i rock and %i techno songs across %i playlists with a total of %i songs."
        % (genres_index[0], genres_index[1], genres_index[2], len(playlists), len(playlists)*len(playlists[0]))
    )


if __name__ == "__main__":
    simulation()
