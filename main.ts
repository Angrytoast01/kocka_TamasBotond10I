let szam = 0
input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 1; index++) {
        szam = randint(1, 6)
        basic.showNumber(szam)
    }
})
basic.forever(function () {
    basic.showIcon(IconNames.Happy)
})
