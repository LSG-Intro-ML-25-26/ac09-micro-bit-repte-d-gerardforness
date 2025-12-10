let temp = 0
let llum = 0
basic.forever(function () {
    temp = input.temperature()
    if (temp > 22) {
        basic.showString("calor")
    } else {
        basic.showString("fred")
    }
    basic.pause(100)
})
basic.forever(function () {
    llum = input.lightLevel()
    if (llum > 200) {
        music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.Once)
    } else if (llum < 50) {
        music.startMelody(music.builtInMelody(Melodies.Blues), MelodyOptions.Once)
    }
    basic.pause(1000)
})
