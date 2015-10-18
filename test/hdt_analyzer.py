from os import path
from replay import Replay
from pprint import pprint
from database import DataBase

# TODO Find about 2way import
# TODO Bind ids to card names
# TODO Check results with HDT

if __name__ == '__main__':
    # Config:
    files_folder = path.join(path.dirname(path.abspath(__file__)), '..', 'files')
    replay_file = path.join(files_folder, 'replay.json')
    databse_file = path.join(files_folder, 'database.json')
    replay = None

    # Run
    database = DataBase(databse_file)
    replay = Replay(replay_file)
    print('Your Hero: ' + database.get_card_name(replay.get_player_hero()))
    l = []
    lz = []
    kept, mulliganed = replay.get_cards_kept_by_player()
    for i in kept:
        l.append(database.get_card_name(i))
    print('Kept: ' + ', '.join(l))
    for i in mulliganed:
        lz.append(database.get_card_name(i))
    print('Mulliganed: ' + ', '.join(lz))
