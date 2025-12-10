let option = 0
let x = 0
let y = 0
function mostrar_temperatura() {
    led.plotBarGraph(input.temperature(), 50)
}

function gota() {
    
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    option = 1
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    option = 2
    
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
