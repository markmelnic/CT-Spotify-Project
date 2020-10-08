
# import each week from weeks.py
from weeks import *
# import the simulation method
from simulation import simulation

# main method
if __name__ == "__main__":
    # assign the playlists, users and user_number from the simulation
    playlists, users, user_number = simulation()
    # run week 1
    week1(playlists, users, user_number)
    # run week 2
    week2(playlists, users, user_number)
    # run week 3
    week3(playlists, users, user_number)
