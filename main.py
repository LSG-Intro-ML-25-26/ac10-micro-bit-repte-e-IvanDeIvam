def on_forever():
    led.plot_bar_graph(input.temperature(), 50)
    pass
basic.forever(on_forever)