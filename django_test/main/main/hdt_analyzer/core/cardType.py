cardType=[
  "INVALID",
  "GAME",
  "PLAYER",
  "HERO",
  "MINION",
  "ABILITY",
  "ENCHANTMENT",
  "WEAPON",
  "ITEM",
  "TOKEN",
  "HERO_POWER"
]

def card_type(text):
  if text in cardType:
    return cardType.index(text)
  else:
    return -1