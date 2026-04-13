print("""Cześć!
LOL
CRINGE
ROFL
SHEESH
CREEPY
AGGRO""")
meme_dict = {
"LOL" : "odpowiedź na coś zabawnego",
"CRINGE" : "coś dziwnego lub wstydliwego",
"ROFL" : "odpowiedź na żart",
"SHEESH" : "lekka dezaprobata",
"CREEPY" : "straszny, złowieszczy",
"AGGRO" : "stać się agresywnym/zły"
}
world = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")
if world in meme_dict.keys():
    print(meme_dict[world])
else:
    print('Nie znaleziono słowa.')
