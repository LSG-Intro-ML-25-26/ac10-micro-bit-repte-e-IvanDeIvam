option = 0
x = 2
y = 2

def mostrar_temperatura():
    led.plot_bar_graph(input.temperature(), 50)

def gota():
    global x, y
    oldX = x
    oldY = y

    accX = input.acceleration(Dimension.X)
    accY = input.acceleration(Dimension.Y)

    if accX < -150 and x > 0:
        x = x - 1
    if accX > 150 and x < 4:
        x = x + 1

    if accY < -150 and y > 0:
        y = y - 1
    if accY > 150 and y < 4:
        y = y + 1

    if x != oldX or y != oldY:
        led.unplot(oldX, oldY)

    led.plot(x, y)
    basic.pause(50)

def on_button_pressed_a():
    global option
    option = 1
    basic.clear_screen()
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global option
    option = 2
    basic.clear_screen()
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    if option == 1:
        mostrar_temperatura()
    if option == 2:
        gota()
    basic.pause(100)
basic.forever(on_forever)