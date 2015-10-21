from os import path
from replay import Replay
import replay as replay_tools
from pprint import pprint
from database import DataBase
import file_manager
import time

#TODO Add stats to mulligans (winrate, percentages)

# Config:
database = DataBase(file_manager.databse_file)

def read_mulligans(deck_name):
        for f in file_manager.find_deck_games(deck_name):
            if file_manager.unzip_file(f):
                replay = Replay(file_manager.replay_file)
                l = []
                lz = []
                kept, mulliganed, drawn = replay.get_cards_kept_by_player()
                for i in kept:
                    l.append(database.get_card_name(i))
                print('Kept: ' + ', '.join(l))
                for i in mulliganed:
                    lz.append(database.get_card_name(i))
                print('Mulliganed: ' + ', '.join(lz))
# Run
if __name__ == '__main__':
    t = time.time()
    read_mulligans('Demon Handlock')
    print 'Time spent:', (str(time.time() - t)+ ' secs')