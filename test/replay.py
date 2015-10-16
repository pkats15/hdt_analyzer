import json
from cardType import card_type
from os import path
#import hdt_analyzer as hdt
class Replay():
    @staticmethod
    def read_json(replay_file):
        data = open(replay_file)
        json_data = json.load(data)
        data.close()
        return json_data
    @staticmethod
    def get_player_id(keypoints):
        for kp in keypoints:
            for d in kp["Data"]:
                if d["IsPlayer"] and "PLAYER_ID" in d["Tags"].keys():
                    return d['Tags']['PLAYER_ID']

    def __init__(self,replay_file):
        self.keypoints = Replay.read_json(replay_file)
        self.player_id = Replay.get_player_id(self.keypoints)

    def print_hero(self):
        hero = None
        for kp in self.keypoints:
            for d in kp['Data']:
                if "CONTROLLER" in d['Tags'].keys() and "CARDTYPE" in d['Tags'].keys():
                    if d['Tags']['CONTROLLER'] == self.player_id and d['Tags']['CARDTYPE'] == card_type('HERO') and d['CardId']!= None:
                        hero = d['CardId']
                        break
        if hero != None:
            print hero

