temp = 0
llum = 0

def on_forever():
    global temp
    temp = input.temperature()
    if temp > 22:
        basic.show_string("calor")
    else:
        basic.show_string("fred")
    basic.pause(100)
basic.forever(on_forever)

def on_forever2():
    global llum
    llum = input.light_level()
    if llum > 200:
        music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
            MelodyOptions.ONCE)
    elif llum < 50:
        music.start_melody(music.built_in_melody(Melodies.BLUES), MelodyOptions.ONCE)
    basic.pause(1000)
basic.forever(on_forever2)
