from random import sample, randint

# define genres and moods
GENRES = ["pop", "rock", "techno"]
MOODS = ["happy", "party", "calming", "lounge"]

# create the simulation
def simulation():
    # define counter genres and moods indexes
    genres_index = [0, 0, 0]
    moods_index = [0, 0, 0, 0]

    # generate the playlists
    playlists = []
    # loop to create 100 playlists
    for i in range(100):
        playlist = []
        # loop to create 50 songs per playlist
        for j in range(50):
            # define the song
            song = (str(i) + "-" + str(j), sample(GENRES, 1)[0], sample(MOODS, 1)[0])
            # increment the genre of the song
            if song[1] == GENRES[0]:
                genres_index[0] += 1
            elif song[1] == GENRES[1]:
                genres_index[1] += 1
            elif song[1] == GENRES[2]:
                genres_index[2] += 1

            # increment the mood of the song
            if song[2] == MOODS[0]:
                moods_index[0] += 1
            elif song[2] == MOODS[1]:
                moods_index[1] += 1
            elif song[2] == MOODS[2]:
                moods_index[2] += 1
            elif song[2] == MOODS[3]:
                moods_index[3] += 1
            # append the song to the playlist
            playlist.append(song)
        # append the playlist to the playlists list
        playlists.append(playlist)

    # print the results of the simulation
    print("\nThe dataset has been simulated successfully.")
    print(
        "- It contains %i pop, %i rock and %i techno songs."
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
    # loop to create 100 users
    for i in range(100):
        user = []
        # loop to add between 150 and 200 songs to the user
        for i in range(randint(150, 200)):
            # append a random song to the user
            user.append(playlists[randint(0, 99)][randint(0, 49)])
        # append the user to the users list
        users.append(user)
        # increment the total number of songs which have been listened to across all users
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

    # return the simulation results
    return playlists, users, user_number

''' main test method for simulation.py
will not run if main.py is executed '''
if __name__ == "__main__":
    simulation()
