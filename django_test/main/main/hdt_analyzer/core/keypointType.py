keypointType = [
    'Play',
    'Draw',
    'Mulligan',
    'Death',
    'HandDiscard',
    'DeckDiscard',
    'SecretPlayed',
    'SecretTriggered',
    'Turn',
    'Attack',
    'PlayToHand',
    'PlayToDeck',
    'Obtain',
    'Summon',
    'HandPos',
    'BoardPos',
    'PlaySpell',
    'Weapon',
    'WeaponDestroyed',
    'HeroPower',
    'Victory',
    'Defeat',
    'SecretStolen',
    'CreateToDeck'
]

def keypoint_type(text):
  if text in keypointType:
    return keypointType.index(text)
  else:
    return -1
