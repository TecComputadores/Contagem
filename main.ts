let numero = 0
loops.everyInterval(1000, function () {
    numero += 1
})
basic.forever(function () {
    basic.showNumber(numero)
    if (numero >= 10) {
        numero = 0
    }
})
