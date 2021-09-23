def on_button_pressed_a():
    global megnyom
    megnyom = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

szam = 0
megnyom = 0
basic.show_string("123456")
megnyom = 0
if megnyom == 1:
    szam = randint(1, 6)
    basic.show_number(szam)