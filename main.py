numero = 0

def on_every_interval():
    global numero
    numero += 1
loops.every_interval(1000, on_every_interval)

def on_forever():
    global numero
    basic.show_number(numero)
    if numero >= 10:
        numero = 0
basic.forever(on_forever)
