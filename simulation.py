
from random import sample

GENRES = ["pop", "rock", "techno"]
MOODS = ["happy", "party", "calming", "lounge"]

# create the simulation
def simulation():
    playlists = []
    for i in range(100):
        playlist = []
        for i in range(50):
            song = (sample(GENRES, 1)[0], sample(MOODS, 1)[0])
            playlist.append(song)
        playlists.append(playlist)
        print(playlist)

if __name__ == "__main__":
    simulation()