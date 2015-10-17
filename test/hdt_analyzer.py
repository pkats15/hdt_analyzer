from os import path
from replay import Replay
from pprint import pprint

#TODO Find about 2way import
#TODO Bind ids to card names
#TODO Check results with HDT

if __name__ == '__main__':
    #Config:
    files_folder = path.join(path.dirname(path.abspath(__file__)),'..','files')
    replay_file = path.join(files_folder,'replay.json')
    replay = None

    #Run
    replay = Replay(replay_file)
    replay.print_hero()
    pprint(replay.get_cards_kept_by_player())
