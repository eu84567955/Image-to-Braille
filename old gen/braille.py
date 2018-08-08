﻿# -*- coding: utf-8 -*-
def get_char(current):
    if   current == [0,0,0,0,0,0,0,0]: return u"⠄"
    elif current == [1, 0, 0, 0, 0, 0, 0, 0]: return u"⠁"
    elif current == [0, 1, 0, 0, 0, 0, 0, 0]: return u"⠂"
    elif current == [1, 1, 0, 0, 0, 0, 0, 0]: return u"⠃"
    elif current == [0, 0, 1, 0, 0, 0, 0, 0]: return u"⠄"
    elif current == [0, 0, 1, 0, 0, 0, 0, 0]: return u"⠅"
    elif current == [0, 1, 1, 0, 0, 0, 0, 0]: return u"⠆"
    elif current == [1, 1, 1, 0, 0, 0, 0, 0]: return u"⠇"
    elif current == [0, 0, 0, 0, 1, 0, 0, 0]: return u"⠈"
    elif current == [1, 0, 0, 0, 1, 0, 0, 0]: return u"⠉"
    elif current == [0, 1, 0, 0, 1, 0, 0, 0]: return u"⠊"
    elif current == [1, 1, 0, 0, 1, 0, 0, 0]: return u"⠋"
    elif current == [0, 0, 1, 0, 1, 0, 0, 0]: return u"⠌"
    elif current == [0, 0, 1, 0, 0, 0, 0, 0]: return u"⠍"
    elif current == [0, 1, 1, 0, 1, 0, 0, 0]: return u"⠎"
    elif current == [1, 1, 1, 0, 1, 0, 0, 0]: return u"⠏"
    elif current == [0, 0, 0, 0, 0, 1, 0, 0]: return u"⠐"
    elif current == [1, 0, 0, 0, 0, 1, 0, 0]: return u"⠑"
    elif current == [0, 1, 0, 0, 0, 1, 0, 0]: return u"⠒"
    elif current == [1, 1, 0, 0, 0, 1, 0, 0]: return u"⠓"
    elif current == [0, 0, 1, 0, 0, 1, 0, 0]: return u"⠔"
    elif current == [0, 0, 1, 0, 0, 1, 0, 0]: return u"⠕"
    elif current == [0, 1, 1, 0, 0, 1, 0, 0]: return u"⠖"
    elif current == [1, 1, 1, 0, 0, 1, 0, 0]: return u"⠗"
    elif current == [0, 0, 0, 0, 1, 1, 0, 0]: return u"⠘"
    elif current == [1, 0, 0, 0, 1, 1, 0, 0]: return u"⠙"
    elif current == [0, 1, 0, 0, 1, 1, 0, 0]: return u"⠚"
    elif current == [1, 1, 0, 0, 1, 1, 0, 0]: return u"⠛"
    elif current == [0, 0, 1, 0, 1, 1, 0, 0]: return u"⠜"
    elif current == [1, 0, 1, 0, 1, 1, 0, 0]: return u"⠝"
    elif current == [0, 1, 1, 0, 1, 1, 0, 0]: return u"⠞"
    elif current == [1, 1, 1, 0, 1, 1, 0, 0]: return u"⠟"
    elif current == [0, 0, 0, 0, 0, 0, 1, 0]: return u"⠠"
    elif current == [1, 0, 0, 0, 0, 0, 1, 0]: return u"⠡"
    elif current == [0, 1, 0, 0, 0, 0, 1, 0]: return u"⠢"
    elif current == [1, 1, 0, 0, 0, 0, 1, 0]: return u"⠣"
    elif current == [0, 0, 1, 0, 0, 0, 1, 0]: return u"⠤"
    elif current == [0, 0, 1, 0, 0, 0, 1, 0]: return u"⠥"
    elif current == [0, 1, 1, 0, 0, 0, 1, 0]: return u"⠦"
    elif current == [1, 1, 1, 0, 0, 0, 1, 0]: return u"⠧"
    elif current == [0, 0, 0, 0, 0, 0, 1, 0]: return u"⠨"
    elif current == [0, 0, 0, 0, 0, 0, 1, 0]: return u"⠩"
    elif current == [0, 1, 0, 0, 0, 0, 1, 0]: return u"⠪"
    elif current == [1, 1, 0, 0, 1, 0, 1, 0]: return u"⠫"
    elif current == [0, 0, 1, 0, 0, 0, 1, 0]: return u"⠬"
    elif current == [0, 0, 1, 0, 0, 0, 1, 0]: return u"⠭"
    elif current == [0, 1, 1, 0, 0, 0, 1, 0]: return u"⠮"
    elif current == [1, 1, 1, 0, 1, 0, 1, 0]: return u"⠯"
    elif current == [0, 0, 0, 0, 0, 1, 1, 0]: return u"⠰"
    elif current == [1, 0, 0, 0, 0, 1, 1, 0]: return u"⠱"
    elif current == [0, 1, 0, 0, 0, 1, 1, 0]: return u"⠲"
    elif current == [1, 1, 0, 0, 0, 1, 1, 0]: return u"⠳"
    elif current == [0, 0, 1, 0, 0, 1, 1, 0]: return u"⠴"
    elif current == [0, 0, 1, 0, 0, 1, 1, 0]: return u"⠵"
    elif current == [0, 1, 1, 0, 0, 1, 1, 0]: return u"⠶"
    elif current == [1, 1, 1, 0, 0, 1, 1, 0]: return u"⠷"
    elif current == [0, 0, 0, 0, 1, 1, 1, 0]: return u"⠸"
    elif current == [1, 0, 0, 0, 1, 1, 1, 0]: return u"⠹"
    elif current == [0, 1, 0, 0, 1, 1, 1, 0]: return u"⠺"
    elif current == [1, 1, 0, 0, 1, 1, 1, 0]: return u"⠻"
    elif current == [0, 0, 1, 0, 1, 1, 1, 0]: return u"⠼"
    elif current == [1, 0, 1, 0, 1, 1, 1, 0]: return u"⠽"
    elif current == [0, 1, 1, 0, 1, 1, 1, 0]: return u"⠾"
    elif current == [1, 1, 1, 0, 1, 1, 1, 0]: return u"⠿"
    elif current == [0, 0, 0, 1, 0, 0, 0, 0]: return u"⡀"
    elif current == [0, 0, 0, 1, 0, 0, 0, 0]: return u"⡁"
    elif current == [0, 0, 0, 1, 0, 0, 0, 0]: return u"⡂"
    elif current == [0, 0, 0, 1, 0, 0, 0, 0]: return u"⡃"
    elif current == [0, 0, 1, 1, 0, 0, 0, 0]: return u"⡄"
    elif current == [0, 0, 1, 1, 0, 0, 0, 0]: return u"⡅"
    elif current == [0, 1, 1, 1, 0, 0, 0, 0]: return u"⡆"
    elif current == [1, 1, 1, 1, 0, 0, 0, 0]: return u"⡇"
    elif current == [0, 0, 0, 1, 1, 0, 0, 0]: return u"⡈"
    elif current == [0, 0, 0, 1, 0, 0, 0, 0]: return u"⡉"
    elif current == [0, 0, 0, 1, 1, 0, 0, 0]: return u"⡊"
    elif current == [0, 0, 0, 1, 0, 0, 0, 0]: return u"⡋"
    elif current == [0, 0, 1, 1, 1, 0, 0, 0]: return u"⡌"
    elif current == [0, 0, 1, 1, 0, 0, 0, 0]: return u"⡍"
    elif current == [0, 1, 1, 1, 1, 0, 0, 0]: return u"⡎"
    elif current == [1, 1, 1, 1, 1, 0, 0, 0]: return u"⡏"
    elif current == [0, 0, 0, 1, 0, 1, 0, 0]: return u"⡐"
    elif current == [0, 0, 0, 1, 0, 1, 0, 0]: return u"⡑"
    elif current == [0, 0, 0, 1, 0, 0, 0, 0]: return u"⡒"
    elif current == [0, 0, 0, 1, 0, 0, 0, 0]: return u"⡓"
    elif current == [0, 0, 1, 1, 0, 1, 0, 0]: return u"⡔"
    elif current == [0, 0, 1, 1, 0, 1, 0, 0]: return u"⡕"
    elif current == [0, 1, 1, 1, 0, 1, 0, 0]: return u"⡖"
    elif current == [1, 1, 1, 1, 0, 1, 0, 0]: return u"⡗"
    elif current == [0, 0, 0, 1, 1, 1, 0, 0]: return u"⡘"
    elif current == [1, 0, 0, 1, 1, 1, 0, 0]: return u"⡙"
    elif current == [0, 0, 0, 1, 0, 0, 0, 0]: return u"⡚"
    elif current == [0, 0, 0, 1, 0, 0, 0, 0]: return u"⡛"
    elif current == [0, 0, 1, 1, 1, 1, 0, 0]: return u"⡜"
    elif current == [1, 0, 1, 1, 1, 1, 0, 0]: return u"⡝"
    elif current == [0, 1, 1, 1, 1, 1, 0, 0]: return u"⡞"
    elif current == [1, 1, 1, 1, 1, 1, 0, 0]: return u"⡟"
    elif current == [0, 0, 0, 0, 0, 0, 0, 0]: return u"⡠"
    elif current == [0, 0, 0, 1, 0, 0, 1, 0]: return u"⡡"
    elif current == [0, 0, 0, 1, 0, 0, 1, 0]: return u"⡢"
    elif current == [0, 0, 0, 1, 0, 0, 1, 0]: return u"⡣"
    elif current == [0, 0, 1, 1, 0, 0, 1, 0]: return u"⡤"
    elif current == [0, 0, 1, 1, 0, 0, 1, 0]: return u"⡥"
    elif current == [0, 1, 1, 1, 0, 0, 1, 0]: return u"⡦"
    elif current == [1, 1, 1, 1, 0, 0, 1, 0]: return u"⡧"
    elif current == [0, 0, 0, 1, 0, 0, 1, 0]: return u"⡨"
    elif current == [0, 0, 0, 1, 0, 0, 1, 0]: return u"⡩"
    elif current == [0, 0, 0, 1, 0, 0, 1, 0]: return u"⡪"
    elif current == [0, 0, 0, 1, 0, 0, 1, 0]: return u"⡫"
    elif current == [0, 0, 1, 1, 0, 0, 1, 0]: return u"⡬"
    elif current == [0, 0, 1, 1, 0, 0, 1, 0]: return u"⡭"
    elif current == [0, 1, 1, 1, 0, 0, 1, 0]: return u"⡮"
    elif current == [1, 1, 1, 1, 1, 0, 1, 0]: return u"⡯"
    elif current == [0, 0, 0, 1, 0, 1, 1, 0]: return u"⡰"
    elif current == [0, 0, 0, 1, 0, 1, 1, 0]: return u"⡱"
    elif current == [0, 1, 0, 1, 0, 1, 1, 0]: return u"⡲"
    elif current == [0, 0, 0, 1, 0, 0, 1, 0]: return u"⡳"
    elif current == [0, 0, 1, 1, 0, 1, 1, 0]: return u"⡴"
    elif current == [0, 0, 1, 1, 0, 1, 1, 0]: return u"⡵"
    elif current == [0, 1, 1, 1, 0, 1, 1, 0]: return u"⡶"
    elif current == [1, 1, 1, 1, 0, 1, 1, 0]: return u"⡷"
    elif current == [0, 0, 0, 1, 1, 1, 1, 0]: return u"⡸"
    elif current == [1, 0, 0, 1, 1, 1, 1, 0]: return u"⡹"
    elif current == [0, 1, 0, 1, 1, 1, 1, 0]: return u"⡺"
    elif current == [1, 1, 0, 1, 1, 1, 1, 0]: return u"⡻"
    elif current == [0, 0, 1, 1, 1, 1, 1, 0]: return u"⡼"
    elif current == [1, 0, 1, 1, 1, 1, 1, 0]: return u"⡽"
    elif current == [0, 1, 1, 1, 1, 1, 1, 0]: return u"⡾"
    elif current == [1, 1, 1, 1, 1, 1, 1, 0]: return u"⡿"
    elif current == [0, 0, 0, 0, 0, 0, 0, 1]: return u"⢀"
    elif current == [1, 0, 0, 0, 0, 0, 0, 1]: return u"⢁"
    elif current == [0, 1, 0, 0, 0, 0, 0, 1]: return u"⢂"
    elif current == [1, 1, 0, 0, 0, 0, 0, 1]: return u"⢃"
    elif current == [0, 0, 1, 0, 0, 0, 0, 1]: return u"⢄"
    elif current == [0, 0, 1, 0, 0, 0, 0, 1]: return u"⢅"
    elif current == [0, 1, 1, 0, 0, 0, 0, 1]: return u"⢆"
    elif current == [1, 1, 1, 0, 0, 0, 0, 1]: return u"⢇"
    elif current == [0, 0, 0, 0, 0, 0, 0, 1]: return u"⢈"
    elif current == [0, 0, 0, 0, 0, 0, 0, 1]: return u"⢉"
    elif current == [0, 1, 0, 0, 0, 0, 0, 1]: return u"⢊"
    elif current == [1, 1, 0, 0, 1, 0, 0, 1]: return u"⢋"
    elif current == [0, 0, 1, 0, 0, 0, 0, 1]: return u"⢌"
    elif current == [0, 0, 1, 0, 0, 0, 0, 1]: return u"⢍"
    elif current == [0, 1, 1, 0, 0, 0, 0, 1]: return u"⢎"
    elif current == [1, 1, 1, 0, 1, 0, 0, 1]: return u"⢏"
    elif current == [0, 0, 0, 0, 0, 0, 0, 1]: return u"⢐"
    elif current == [1, 0, 0, 0, 0, 0, 0, 1]: return u"⢑"
    elif current == [0, 0, 0, 0, 0, 0, 0, 1]: return u"⢒"
    elif current == [0, 0, 0, 0, 0, 0, 0, 1]: return u"⢓"
    elif current == [0, 0, 1, 0, 0, 0, 0, 1]: return u"⢔"
    elif current == [0, 0, 1, 0, 0, 0, 0, 1]: return u"⢕"
    elif current == [0, 1, 1, 0, 0, 1, 0, 1]: return u"⢖"
    elif current == [1, 1, 1, 0, 0, 1, 0, 1]: return u"⢗"
    elif current == [0, 0, 0, 0, 0, 0, 0, 1]: return u"⢘"
    elif current == [0, 0, 0, 0, 0, 0, 0, 1]: return u"⢙"
    elif current == [0, 0, 0, 0, 0, 0, 0, 1]: return u"⢚"
    elif current == [0, 0, 0, 0, 0, 0, 0, 1]: return u"⢛"
    elif current == [0, 0, 1, 0, 0, 0, 0, 1]: return u"⢜"
    elif current == [0, 0, 1, 0, 0, 0, 0, 1]: return u"⢝"
    elif current == [0, 1, 1, 0, 1, 1, 0, 1]: return u"⢞"
    elif current == [1, 1, 1, 0, 1, 1, 0, 1]: return u"⢟"
    elif current == [0, 0, 0, 0, 0, 0, 1, 1]: return u"⢠"
    elif current == [1, 0, 0, 0, 0, 0, 1, 1]: return u"⢡"
    elif current == [0, 1, 0, 0, 0, 0, 1, 1]: return u"⢢"
    elif current == [1, 1, 0, 0, 0, 0, 1, 1]: return u"⢣"
    elif current == [0, 0, 1, 0, 0, 0, 1, 1]: return u"⢤"
    elif current == [0, 0, 1, 0, 0, 0, 1, 1]: return u"⢥"
    elif current == [0, 1, 1, 0, 0, 0, 1, 1]: return u"⢦"
    elif current == [1, 1, 1, 0, 0, 0, 1, 1]: return u"⢧"
    elif current == [0, 0, 0, 0, 0, 0, 1, 1]: return u"⢨"
    elif current == [0, 0, 0, 0, 0, 0, 1, 1]: return u"⢩"
    elif current == [0, 1, 0, 0, 0, 0, 1, 1]: return u"⢪"
    elif current == [1, 1, 0, 0, 1, 0, 1, 1]: return u"⢫"
    elif current == [0, 0, 1, 0, 0, 0, 1, 1]: return u"⢬"
    elif current == [0, 0, 1, 0, 0, 0, 1, 1]: return u"⢭"
    elif current == [0, 1, 1, 0, 0, 0, 1, 1]: return u"⢮"
    elif current == [1, 1, 1, 0, 1, 0, 1, 1]: return u"⢯"
    elif current == [0, 0, 0, 0, 0, 1, 1, 1]: return u"⢰"
    elif current == [1, 0, 0, 0, 0, 1, 1, 1]: return u"⢱"
    elif current == [0, 1, 0, 0, 0, 1, 1, 1]: return u"⢲"
    elif current == [1, 1, 0, 0, 0, 1, 1, 1]: return u"⢳"
    elif current == [0, 0, 1, 0, 0, 1, 1, 1]: return u"⢴"
    elif current == [0, 0, 1, 0, 0, 1, 1, 1]: return u"⢵"
    elif current == [0, 1, 1, 0, 0, 1, 1, 1]: return u"⢶"
    elif current == [1, 1, 1, 0, 0, 1, 1, 1]: return u"⢷"
    elif current == [0, 0, 0, 0, 1, 1, 1, 1]: return u"⢸"
    elif current == [1, 0, 0, 0, 1, 1, 1, 1]: return u"⢹"
    elif current == [0, 1, 0, 0, 1, 1, 1, 1]: return u"⢺"
    elif current == [1, 1, 0, 0, 1, 1, 1, 1]: return u"⢻"
    elif current == [0, 0, 1, 0, 1, 1, 1, 1]: return u"⢼"
    elif current == [1, 0, 1, 0, 1, 1, 1, 1]: return u"⢽"
    elif current == [0, 1, 1, 0, 1, 1, 1, 1]: return u"⢾"
    elif current == [1, 1, 1, 0, 1, 1, 1, 1]: return u"⢿"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣀"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣁"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣂"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣃"
    elif current == [0, 0, 1, 1, 0, 0, 0, 1]: return u"⣄"
    elif current == [0, 0, 1, 1, 0, 0, 0, 1]: return u"⣅"
    elif current == [0, 1, 1, 1, 0, 0, 0, 1]: return u"⣆"
    elif current == [1, 1, 1, 1, 0, 0, 0, 1]: return u"⣇"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣈"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣉"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣊"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣋"
    elif current == [0, 1, 1, 1, 0, 0, 0, 1]: return u"⣌"
    elif current == [0, 0, 1, 1, 0, 0, 0, 1]: return u"⣍"
    elif current == [0, 1, 1, 1, 0, 0, 0, 1]: return u"⣎"
    elif current == [1, 1, 1, 1, 1, 0, 0, 1]: return u"⣏"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣐"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣑"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣒"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣓"
    elif current == [0, 0, 1, 1, 0, 0, 0, 1]: return u"⣔"
    elif current == [0, 0, 1, 1, 0, 0, 0, 1]: return u"⣕"
    elif current == [0, 1, 1, 1, 0, 1, 0, 1]: return u"⣖"
    elif current == [1, 1, 1, 1, 0, 1, 0, 1]: return u"⣗"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣘"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣙"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣚"
    elif current == [0, 0, 0, 1, 0, 0, 0, 1]: return u"⣛"
    elif current == [0, 0, 1, 1, 0, 0, 0, 1]: return u"⣜"
    elif current == [0, 0, 1, 1, 0, 0, 0, 1]: return u"⣝"
    elif current == [0, 1, 1, 1, 1, 1, 0, 1]: return u"⣞"
    elif current == [1, 1, 1, 1, 1, 1, 0, 1]: return u"⣟"
    elif current == [0, 0, 0, 1, 0, 0, 1, 1]: return u"⣠"
    elif current == [0, 0, 0, 1, 0, 0, 1, 1]: return u"⣡"
    elif current == [0, 0, 0, 1, 0, 0, 1, 1]: return u"⣢"
    elif current == [0, 0, 0, 1, 0, 0, 1, 1]: return u"⣣"
    elif current == [0, 0, 1, 1, 0, 0, 1, 1]: return u"⣤"
    elif current == [0, 0, 1, 1, 0, 0, 1, 1]: return u"⣥"
    elif current == [0, 1, 1, 1, 0, 0, 1, 1]: return u"⣦"
    elif current == [1, 1, 1, 1, 0, 0, 1, 1]: return u"⣧"
    elif current == [0, 0, 0, 1, 0, 0, 1, 1]: return u"⣨"
    elif current == [0, 0, 0, 1, 0, 0, 1, 1]: return u"⣩"
    elif current == [0, 0, 0, 1, 0, 0, 1, 1]: return u"⣪"
    elif current == [0, 0, 0, 1, 0, 0, 1, 1]: return u"⣫"
    elif current == [0, 0, 1, 1, 0, 0, 1, 1]: return u"⣬"
    elif current == [0, 0, 1, 1, 0, 0, 1, 1]: return u"⣭"
    elif current == [0, 1, 1, 1, 0, 0, 1, 1]: return u"⣮"
    elif current == [1, 1, 1, 1, 1, 0, 1, 1]: return u"⣯"
    elif current == [0, 0, 0, 1, 0, 1, 1, 1]: return u"⣰"
    elif current == [0, 0, 0, 1, 0, 1, 1, 1]: return u"⣱"
    elif current == [0, 1, 0, 1, 0, 1, 1, 1]: return u"⣲"
    elif current == [1, 1, 0, 1, 0, 1, 1, 1]: return u"⣳"
    elif current == [0, 0, 1, 1, 0, 1, 1, 1]: return u"⣴"
    elif current == [0, 0, 1, 1, 0, 1, 1, 1]: return u"⣵"
    elif current == [0, 1, 1, 1, 0, 1, 1, 1]: return u"⣶"
    elif current == [1, 1, 1, 1, 0, 1, 1, 1]: return u"⣷"
    elif current == [0, 0, 0, 1, 1, 1, 1, 1]: return u"⣸"
    elif current == [1, 0, 0, 1, 1, 1, 1, 1]: return u"⣹"
    elif current == [0, 1, 0, 1, 1, 1, 1, 1]: return u"⣺"
    elif current == [1, 1, 0, 1, 1, 1, 1, 1]: return u"⣻"
    elif current == [0, 0, 1, 1, 1, 1, 1, 1]: return u"⣼"
    elif current == [1, 0, 1, 1, 1, 1, 1, 1]: return u"⣽"
    elif current == [0, 1, 1, 1, 1, 1, 1, 1]: return u"⣾"
    return u"⠄"