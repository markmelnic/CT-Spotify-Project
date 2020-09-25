from random import sample


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


def week2(playlists, users, user_number):
    pass
