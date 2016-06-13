from os import path
from replay import Replay
import replay as replay_tools
from pprint import pprint
from database import DataBase
import file_manager
import time

# TODO Add stats to mulligans (winrate, percentages)

# Config:
database = DataBase(file_manager.database_file)


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
    kept_and_result = {}
    percentages = {}
    outof = {}
    for f in file_manager.find_deck_games(deck_name):
        if file_manager.unzip_file(f):
            replay = Replay(file_manager.replay_file)
            k, m, d = replay.get_cards_kept_by_player()
            if k != None and m != None and d != None:
                r = replay.game_won()
                cards_kept.extend(k)
                cards_drawn.extend(d)
                # print(str(len(k)+len(m)))
                if len(k) <= 2:
                # if True:
                    for card in k:
                        if not card in kept_and_result:
                            kept_and_result[card] = None
                        if kept_and_result[card] == None:
                            kept_and_result[card] = [0, 0]
                        if r == True:
                            kept_and_result[card][0] += 1
                        kept_and_result[card][1] += 1
    cards_drawn_set = list(set(cards_drawn))
    for c in cards_drawn_set:
        times_drawn = float(cards_drawn.count(c))
        times_kept = float(cards_kept.count(c))
        outof.update({c: [int(times_kept), int(times_drawn)]})
        percent = round(times_kept / times_drawn, 3)
        percentages.update({c: percent})
    for i in range(len(percentages.items())):
        card_id = percentages.keys()[i]
        # winrate = "Not defined"
        # if card_id in kept_and_result and kept_and_result[card_id][1] != 0:
        #     winrate = float(kept_and_result[card_id][0]/)
        extra_str = 'Not defined'
        if card_id in kept_and_result:
            kar_won = kept_and_result[card_id][0]
            kar_kept = kept_and_result[card_id][1]
            extra_str = str(kar_won) + "/" + str(kar_kept) + \
                " " + str(round((float(kar_won) / kar_kept) * 100)) + "%"
        print(str(database.get_card_name(card_id)) +
              ": " + str(percentages[card_id] * 100) + "% " + str(outof[card_id][0]) + "/" + str(outof[card_id][1]) + ", winrate: " + extra_str)


def print_results(deck_name):
    for f in file_manager.find_deck_games(deck_name):
        if file_manager.unzip_file(f):
            replay = Replay(file_manager.replay_file)
            print replay.game_won()

# Run
if __name__ == '__main__':
    t = time.time()
    # read_mulligans('Demon Handlock')
    get_mulligan_stats('Kaizoku senshi')
    # print_results('Kaizoku senshi')
    print 'Time spent:', (str(time.time() - t) + ' secs')
