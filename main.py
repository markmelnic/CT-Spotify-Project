from weeks import *
from simulation import simulation

if __name__ == "__main__":
    playlists, users, user_number = simulation()
    week1(playlists, users, user_number)
