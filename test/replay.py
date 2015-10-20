import json
import time
from cardType import card_type
from keypointType import keypoint_type, keypointType
from pprint import pprint
from os import path
import xmltodict

# import hdt_analyzer as hdt
class Replay():
    the_coin = 'GAME_005'
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

    def __init__(self, replay_file):
        self.keypoints = Replay.read_json(replay_file)
        self.player_id = Replay.get_player_id(self.keypoints)

    def get_player_hero(self):
        hero = None
        for kp in self.keypoints:
            for d in kp['Data']:
                if "CONTROLLER" in d['Tags'].keys() and "CARDTYPE" in d['Tags'].keys():
                    if d['Tags']['CONTROLLER'] == self.player_id and d['Tags']['CARDTYPE'] == card_type('HERO') and d[
                        'CardId'] != None:
                        hero = d['CardId']
                        return hero
        return None

    def get_last_choosing_draw(self):
        kps = self.keypoints
        last_draw = -1
        for i in range(len(kps)):
            if kps[i]['Type'] == keypoint_type('Draw'):
                for d in kps[i]['Data']:
                    if d['IsPlayer'] and 'MULLIGAN_STATE'not in d['Tags']:
                        last_draw = i
        if last_draw != -1:
            return last_draw
        else:
            return None

    def get_last_intro_draw(self):
        kps = self.keypoints
        last_mull = -1
        for i in range(len(kps)):
            if kps[i]['Type'] == keypoint_type('Mulligan'):
                last_mull = i
        if last_mull != -1:
            return last_mull + 1
        else:
            return None

    def get_cards_kept_by_player(self):
        cards_drawn = []
        cards_mulliganed = []
        kps = self.keypoints
        for i in range(self.get_last_choosing_draw() + 1):
            if kps[i]['Type'] == keypoint_type('Draw'):
                card = None
                target_id = kps[i]['Id']
                for d in kps[i]['Data']:
                    if d['Id'] == target_id and 'CARDTYPE' in d['Tags'] and 'CONTROLLER' in d['Tags'] and (
                                        d['Tags']['CONTROLLER'] == self.player_id and (d['Tags'][
                                    'CARDTYPE'] == card_type('MINION') or d['Tags']['CARDTYPE'] == card_type(
                                "INVALID")) and d['CardId'] != Replay.the_coin):
                        card = d['CardId']
                        break
                if card != None:
                    cards_drawn.append(card)
        for i in range(self.get_last_intro_draw() + 1):
            if kps[i]['Type'] == keypoint_type('Mulligan'):
                card = None
                target_id = kps[i]['Id']
                for d in kps[i]['Data']:
                    if d['Id'] == target_id and 'CARDTYPE' in d['Tags'] and 'CONTROLLER' in d['Tags'] and (
                                        d['Tags']['CONTROLLER'] == self.player_id and (d['Tags'][
                                    'CARDTYPE'] == card_type('MINION') or d['Tags']['CARDTYPE'] == card_type(
                                "INVALID"))):
                        card = d['CardId']
                        break
                if card != None:
                    cards_mulliganed.append(card)
        cards_kept = [item for item in cards_drawn if item not in cards_mulliganed]
        return cards_kept,cards_mulliganed

        '''for kp in self.keypoints:
            if kp['Type']==keypointType['Draw']:
                for d in kp['Data']
            elif kp['Type'] == keypointType['Mulligan']:
                pass'''

