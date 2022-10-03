print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0,board.GP1, board.GP2, board.GP3)    # try D5 on Feather, keeboar
keyboard.row_pins = (board.GP4, board.GP5, board.GP6, board.GP7, board.GP8)    # try D6 on Feather, keeboar
keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.keymap = [
    [KC.A,    KC.LSHIFT,  KC.TAB,     KC.KP_PLUS,
     KC.N7,     KC.N8,      KC.N9,      KC.KP_ASTERISK,
     KC.N4,     KC.N5,      KC.N6,      KC.KP_MINUS,
     KC.N1,     KC.N2,      KC.N3,      KC.KP_SLASH,
     KC.BSPC,	KC.N0,      KC.KP_DOT,  KC.KP_ENTER,
    ]
]

if __name__ == '__main__':
    keyboard.go()    