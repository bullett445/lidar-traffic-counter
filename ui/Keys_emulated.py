import keyboard

def init_keys():
    pass

def key_pressed_up():
    return keyboard.is_pressed('up')


def key_pressed_down():
    return keyboard.is_pressed('down')


def key_pressed_left():
    return keyboard.is_pressed('left')


def key_pressed_right():
    return keyboard.is_pressed('right')


def key_pressed_center():
    return keyboard.is_pressed('c')


def key_pressed_1():
    return keyboard.is_pressed('1')


def key_pressed_2():
    return keyboard.is_pressed('2')


def key_pressed_3():
    return keyboard.is_pressed('3')


if __name__ == '__main__':
    key_pressed()
