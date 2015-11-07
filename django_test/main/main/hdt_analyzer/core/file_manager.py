from os import path, listdir, remove
import zipfile
import online_file_manager as ofm
from pprint import pprint

import xmltodict

files_folder = path.join(path.dirname(path.abspath(__file__)), '..', 'files')
#input_folder = path.join(files_folder, 'input')
temp_folder = path.join(files_folder, 'temp')
#replay_file = path.join(files_folder, 'temp', 'replay.json')
#deck_file = path.join(input_folder, 'DeckStats.xml')
database_file = path.join(files_folder, 'database.json')
temp_range = 100

def find_deck_games(deck_name, folder):
    deck_file = path.join(folder, 'DeckStats.xml')
    deck_xml = open(deck_file)
    deck_stats = xmltodict.parse(deck_xml)
    deck_xml.close()
    files = []
    for g in deck_stats['DeckStatsList']['DeckStats']['Deck']:
        if g['Games'] != None:
            for game in g['Games']['Game']:
                if 'DeckName' in game and 'ReplayFile' in game and game['DeckName'] == deck_name:
                    files.append(game['ReplayFile'])
    return files

def unzip_file(file_name, folder):
    unzip = path.join(folder, 'unzip')
    for fn in listdir(unzip):
        remove(path.join(unzip, fn))
    if path.exists(path.join(folder, file_name)):
        zip_file = zipfile.ZipFile(path.join(folder, file_name))
        zip_file.extract('replay.json', path=unzip)
        zip_file.close()
        return True
    else: return False