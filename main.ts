let option = 0
let x = 2
let y = 2
function mostrar_temperatura() {
    led.plotBarGraph(input.temperature(), 50)
}

function gota() {
    
    let oldX = x
    let oldY = y
    let accX = input.acceleration(Dimension.X)
    let accY = input.acceleration(Dimension.Y)
    if (accX < -150 && x > 0) {
        x = x - 1
    }
    
    if (accX > 150 && x < 4) {
        x = x + 1
    }
    
    if (accY < -150 && y > 0) {
        y = y - 1
    }
    
    if (accY > 150 && y < 4) {
        y = y + 1
    }
    
    if (x != oldX || y != oldY) {
        led.unplot(oldX, oldY)
    }
    
    led.plot(x, y)
    basic.pause(50)
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    option = 1
    basic.clearScreen()
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    option = 2
    basic.clearScreen()
    
})
basic.forever(function on_forever() {
    if (option == 1) {
        mostrar_temperatura()
    }
    
    if (option == 2) {
        gota()
    }
    
    basic.pause(100)
})
