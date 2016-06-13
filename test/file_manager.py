from os import path, listdir, remove
import zipfile
from pprint import pprint

import xmltodict

files_folder = path.join(path.dirname(path.abspath(__file__)), '..', 'files')
input_folder = path.join(files_folder, 'input')
temp_folder = path.join(files_folder, 'temp')
replay_file = path.join(files_folder, 'temp', 'replay.json')
deck_file = path.join(input_folder, 'DeckStats.xml')
database_file = path.join(files_folder, 'database.json')


def find_deck_games(deck_name):
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

def unzip_file(file_name):
    for fn in listdir(temp_folder):
        remove(path.join(temp_folder, fn))
    if path.exists(path.join(input_folder, file_name)):
        zip_file = zipfile.ZipFile(path.join(input_folder, file_name))
        zip_file.extract('replay.json', path=temp_folder)
        zip_file.close()
        return True
    else: return False
