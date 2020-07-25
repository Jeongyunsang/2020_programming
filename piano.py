import turtle as t
from winsound import Beep

freq = {"c5":524,"d5":587,"e5":659,"f5":698,"g5":784,"a5":880,"b5":988,"c6":1047,"d6":1175,
        "c5#":554,"d5#":622,"f5#":740,"g5#":831,"a5#":932}

def play_freq(n):
    Beep(freq[n],300)

def key_1():
    play_freq("c5")
def key_q():
    play_freq("c5#")
def key_w():
    play_freq("d5#")
def key_r():
    play_freq("f5#")
def key_t():
    play_freq("g5#")
def key_y():
    play_freq("a5#")
def key_2():
    play_freq("d5")
def key_3():
    play_freq("e5")
def key_4():
    play_freq("f5")
def key_5():
    play_freq("g5")
def key_6():
    play_freq("a5")
def key_7():
    play_freq("b5")
def key_8():
    play_freq("c6")
def key_9():
    play_freq("d6")

t.setup(600,600)
s = t.Screen()

s.onkey(key_1,"1")
s.onkey(key_2,"2")
s.onkey(key_3,"3")
s.onkey(key_4,"4")
s.onkey(key_5,"5")
s.onkey(key_6,"6")
s.onkey(key_7,"7")
s.onkey(key_8,"8")
s.onkey(key_9,"9")
s.onkey(key_q,"q")
s.onkey(key_w,"w")
s.onkey(key_r,"r")
s.onkey(key_t,"t")
s.onkey(key_y,"y")
s.listen()




















