option = 0
x = 0
y = 0

def mostrar_temperatura():
    led.plot_bar_graph(input.temperature(), 50)

def gota():
    pass
def on_button_pressed_a():
    global option
    option = 1
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global option
    option = 2
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    if option == 1:
        mostrar_temperatura()
    if option == 2:
        gota()
    basic.pause(100)
basic.forever(on_forever)