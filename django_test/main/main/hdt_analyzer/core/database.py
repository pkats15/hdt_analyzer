import json

class DataBase(object):
    def __init__(self, json_location):
        f = open(json_location)
        self.database = json.load(f)
        f.close()

    def get_database(self):
        return self.database

    def get_card_name(self, card_id):
        l = []
        for v in self.database.values():
            l.extend(v)
        for item in l:
            if item['id'] == card_id:
                return item['name']
        return None
