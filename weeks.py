from random import sample
from simulation import MOODS, GENRES

# week one recommendation function
def week1(playlists, users, user_number):
    recommendations = []
    for user in users:
        for playlist in playlists:
            # append playlist index if it has more than 3 listened songs
            if len(list(set(playlist) & set(user))) > 3:
                try:
                    # remove listened songs to avoid duplicates
                    for song in list(set(playlist) & set(user)):
                        playlist.remove(song)
                    recommendations.append(sample(playlist, 5))
                    break
                except ValueError:
                    pass

    # for i in range(100):
    #    print("User %i was recommended: " % (i + 1), recommendations[i])
    print("- In the first week, you have been recommended the following songs:")
    print(recommendations[user_number])

    return recommendations


# week two recommendation function based on genre
def week2(playlists, users, user_number):
    recommendations = []
    for user in users:
        genres_index = [0, 0, 0]
        for song in user:
            if song[1] == GENRES[0]:
                genres_index[0] += 1
            elif song[1] == GENRES[1]:
                genres_index[1] += 1
            elif song[1] == GENRES[2]:
                genres_index[2] += 1
        max_genre = genres_index.index(max(genres_index))

        recommended = []
        for playlist in playlists:
            for song in playlist:
                if song[1] == GENRES[max_genre]:
                    recommended.append(song)
                if len(recommended) > 4:
                    recommendations.append(recommended)
                    break
            if len(recommended) > 4:
                break

    print(
        "- In the second week, you have been recommended the following %s songs:"
        % GENRES[max_genre]
    )
    print(recommendations[user_number])
