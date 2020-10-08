from random import sample
from simulation import MOODS, GENRES

# week one recommendation function
def week1(playlists: list, users: list, user_number: int) -> list:
    recommendations = []
    # iterate through each user
    for user in users:
        for playlist in playlists:
            # append playlist index if it has more than 3 listened songs
            if len(list(set(playlist) & set(user))) > 3:
                try:
                    # remove listened songs to avoid duplicates
                    for song in list(set(playlist) & set(user)):
                        playlist.remove(song)
                    # add 5 random songs to the recommendations
                    recommendations.append(sample(playlist, 5))
                    break
                except ValueError:
                    ''' if more than 45 songs are removed from a playlist
                    sampling 5 songs from what's left will generate a ValueError
                    for that reason we just skip that playlist '''
                    pass

    # print all recommendations
    # for i in range(100):
    #    print("User %i was recommended: " % (i + 1), recommendations[i])

    # print user recommendations
    print("- In the first week, you have been recommended the following songs:")
    print(recommendations[user_number])

    # return the generated recommendations
    return recommendations


# week two recommendation function based on genre
def week2(playlists: list, users: list, user_number: int) -> list:
    recommendations = []
    # iterate through each user
    for user in users:
        # define counter genres indexes
        genres_index = [0, 0, 0]
        # count which genres of songs has the user most listened to
        for song in user:
            if song[1] == GENRES[0]:
                genres_index[0] += 1
            elif song[1] == GENRES[1]:
                genres_index[1] += 1
            elif song[1] == GENRES[2]:
                genres_index[2] += 1
        # find the most listened to genre
        max_genre = genres_index.index(max(genres_index))

        recommended = []
        # iterate through each playlist and each song
        for playlist in playlists:
            for song in playlist:
                # if the song is the genre the user prefers, add to recomendations
                if song[1] == GENRES[max_genre]:
                    recommended.append(song)
                # if 5 recommendations have been generated, break the loop
                if len(recommended) > 4:
                    recommendations.append(recommended)
                    break
            if len(recommended) > 4:
                break

    # print the recommendations for the simulation user
    print(
        "- In the second week, you have been recommended the following %s songs:"
        % recommendations[user_number][0][1]
    )
    print(recommendations[user_number])

    # return the generated recommendations
    return recommendations


# week three recommendation function based on mood
def week3(playlists: list, users: list, user_number: int) -> list:
    recommendations = []
    # iterate through each user
    for user in users:
        # define counter moods indexes
        moods_index = [0, 0, 0, 0]
        # count which moods of songs has the user most listened to
        for song in user:
            if song[2] == MOODS[0]:
                moods_index[0] += 1
            elif song[2] == MOODS[1]:
                moods_index[1] += 1
            elif song[2] == MOODS[2]:
                moods_index[2] += 1
            elif song[2] == MOODS[3]:
                moods_index[3] += 1
        # find the most listened to mood
        max_mood = moods_index.index(max(moods_index))

        recommended = []
        # iterate through each playlist and each song
        for playlist in playlists:
            for song in playlist:
                # if the song is the mood the user prefers, add to recomendations
                if song[2] == MOODS[max_mood]:
                    recommended.append(song)
                # if 5 recommendations have been generated, break the loop
                if len(recommended) > 4:
                    recommendations.append(recommended)
                    break
            if len(recommended) > 4:
                break

    # print the recommendations for the simulation user
    print(
        "- In the thrid week, you have been recommended the following %s songs:"
        % recommendations[user_number][0][2]
    )
    print(recommendations[user_number], "\n")

    # return the generated recommendations
    return recommendations
