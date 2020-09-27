from random import sample, randint

GENRES = ["pop", "rock", "techno"]
MOODS = ["happy", "party", "calming", "lounge"]

# create the simulation
def simulation():
    genres_index = [0, 0, 0]
    moods_index = [0, 0, 0, 0]

    # generate the playlists
    playlists = []
    for i in range(100):
        playlist = []
        for j in range(50):
            song = (str(i) + "-" + str(j), sample(GENRES, 1)[0], sample(MOODS, 1)[0])
            if song[1] == GENRES[0]:
                genres_index[0] += 1
            elif song[1] == GENRES[1]:
                genres_index[1] += 1
            elif song[1] == GENRES[2]:
                genres_index[2] += 1

            if song[2] == MOODS[0]:
                moods_index[0] += 1
            elif song[2] == MOODS[1]:
                moods_index[1] += 1
            elif song[2] == MOODS[2]:
                moods_index[2] += 1
            elif song[2] == MOODS[3]:
                moods_index[3] += 1
            playlist.append(song)
        playlists.append(playlist)

    print("\nThe dataset has been simulated successfully. Here are some statistics:")
    print(
        "- There are %i pop, %i rock and %i techno songs."
        % (genres_index[0], genres_index[1], genres_index[2])
    )
    print(
        "- %i happy, %i party, %i calming and %i lounge songs."
        % (moods_index[0], moods_index[1], moods_index[2], moods_index[2])
    )
    print(
        "- All of these across %i playlists with a total of %i songs."
        % (len(playlists), len(playlists) * len(playlists[0]))
    )

    total_listened = 0
    # generate the users
    users = []
    for i in range(100):
        user = []
        for i in range(randint(150, 1000)):
            user.append(playlists[randint(0, 99)][randint(0, 49)])
        users.append(user)
        total_listened += len(user)

    print(
        "- The %i users listened to a total of %i songs.\n"
        % (len(users), total_listened)
    )

    # assign random user number for the purpose of the experiment
    user_number = randint(0, 99)
    print(
        "For the purpose of this simulation, you have been randomly selected to be user number %i."
        % (user_number + 1)
    )

    return playlists, users, user_number


if __name__ == "__main__":
    simulation()
