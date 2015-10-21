from os import path
from replay import Replay
import replay as replay_tools
from pprint import pprint
from database import DataBase
import file_manager
import time

# TODO Add stats to mulligans (winrate, percentages)

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


def get_mulligan_stats(deck_name):
    cards_kept = []
    cards_drawn = []
    percentages = {}
    outof = {}
    for f in file_manager.find_deck_games(deck_name):
        if file_manager.unzip_file(f):
            replay = Replay(file_manager.replay_file)
            k, m, d = replay.get_cards_kept_by_player()
            cards_kept.extend(k)
            cards_drawn.extend(d)
    cards_drawn_set = list(set(cards_drawn))
    for c in cards_drawn_set:
        times_drawn = float(cards_drawn.count(c))
        times_kept = float(cards_kept.count(c))
        outof.update({c: [int(times_kept), int(times_drawn)]})
        percent = round(times_kept / times_drawn, 3)
        percentages.update({c: percent})
    for i in range(len(percentages.items())):
        print(
        database.get_card_name(percentages.items()[i][0]) + ': ' + str(percentages.items()[i][1] * 100) + '%, ' +
        str(outof[percentages.items()[i][0]][0]) + '/' + str(outof[percentages.items()[i][0]][1]))

# Run
if __name__ == '__main__':
    t = time.time()
    # read_mulligans('Demon Handlock')
    get_mulligan_stats('Demon Handlock')
    print 'Time spent:', (str(time.time() - t) + ' secs')
