#!usr/bin/env python3

import pprint
default_board = {
    '1a': ' ', '2a': ' ', '3a': ' ', '4a': ' ',
    '5a': ' ', '6a': ' ', '7a': ' ', '8a': ' ',
    '1b': ' ', '2b': ' ', '3b': ' ', '4b': ' ',
    '5b': ' ', '6b': ' ', '7b': ' ', '8b': ' ',
    '1c': ' ', '2c': ' ', '3c': ' ', '4c': ' ',
    '5c': ' ', '6c': ' ', '7c': ' ', '8c': ' ',
    '1d': ' ', '2d': ' ', '3d': ' ', '4d': ' ',
    '5d': ' ', '6d': ' ', '7d': ' ', '8d': ' ',
    '1e': ' ', '2e': ' ', '3e': ' ', '4e': ' ',
    '5e': ' ', '6e': ' ', '7e': ' ', '8e': ' ',
    '1f': ' ', '2f': ' ', '3f': ' ', '4f': ' ',
    '5f': ' ', '6f': ' ', '7f': ' ', '8f': ' ',
    '1g': ' ', '2g': ' ', '3g': ' ', '4g': ' ',
    '5g': ' ', '6g': ' ', '7g': ' ', '8g': ' ',
    '1h': ' ', '2h': ' ', '3h': ' ', '4h': ' ',
    '5h': ' ', '6h': ' ', '7h': ' ', '8h': ' ',
}

board = {
    '1a': ' ', '2a': ' ', '3a': ' ', '4a': ' ',
    '5a': ' ', '6a': ' ', '7a': ' ', '8a': ' ',
    '1b': ' ', '2b': ' ', '3b': 'bpawn', '4b': 'bpawn',
    '5b': 'bpawn', '6b': ' ', '7b': ' ', '8b': ' ',
    '1c': ' ', '2c': ' ', '3c': ' ', '4c': ' ',
    '5c': ' ', '6c': ' ', '7c': ' ', '8c': ' ',
    '1d': ' ', '2d': 'wbishop', '3d': ' ', '4d': ' ',
    '5d': ' ', '6d': ' ', '7d': ' ', '8d': ' ',
    '1e': 'wrook', '2e': ' ', '3e': ' ', '4e': 'wqueen',
    '5e': ' ', '6e': ' ', '7e': ' ', '8e': ' ',
    '1f': ' ', '2f': ' ', '3f': ' ', '4f': ' ',
    '5f': ' ', '6f': ' ', '7f': ' ', '8f': ' ',
    '1g': ' ', '2g': 'wking', '3g': ' ', '4g':
    'bking', '5g': ' ', '6g': ' ', '7g': ' ', '8g': ' ',
    '1h': ' ', '2h': ' ', '3h': ' ', '4h': ' ',
    '5h': ' ', '6h': ' ', '7h': ' ', '8h': ' ',
}


pawns = {'wking': 0, 'wqueen': 0, 'wknight': 0, 'wbishop': 0, 'wrook': 0,
         'wpawn': 0, 'bking': 0, 'bqueen': 0, 'bknight': 0, 'bbishop': 0,
         'brook': 0, 'bpawn': 0}

board_places = list(default_board.keys())


def isValid(b, p=pawns):
    valid = True
    message = 'Plansza jest prawidłowa.'
    for key, value in b.items():
        if value in p:
            p[value] += 1
        if key not in board_places:
            valid = False
            message = 'Figura umiejscowiona poza planszą.'

    whites = p['wking'] + p['wqueen'] + p['wknight'] \
        + p['wbishop'] + p['wrook'] + p['wpawn']
    blacks = p['bking'] + p['bqueen'] + p['bknight'] \
        + p['bbishop'] + p['brook'] + p['bpawn']

    if whites > 16 or blacks > 16:
        valid = False
        message = 'Za duża liczba figur na planszy.'

    if p['wking'] > 1 or p['bking'] > 1 or p['wpawn'] > 8 or p['bpawn'] > 8:
        valid = False
        message = 'Za duża liczba króli lub pionków na planszy.'

    return valid, message


print(isValid(board))

pprint.pprint(pawns)
