from os import path
from replay import Replay

#TODO Find about 2way import
#TODO Bind ids to card names

if __name__ == '__main__':
    #Config:
    files_folder = path.join(path.dirname(path.abspath(__file__)),'..','files')
    replay_file = path.join(files_folder,'replay.json')
    replay = None

    #Run
    replay = Replay(replay_file)
    replay.print_hero()
