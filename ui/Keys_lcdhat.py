import RPi.GPIO as GPIO

KEY_UP_PIN = 6
KEY_DOWN_PIN = 19
KEY_LEFT_PIN = 5
KEY_RIGHT_PIN = 26
KEY_PRESS_PIN = 13
KEY1_PIN = 21
KEY2_PIN = 20
KEY3_PIN = 16


# init GPIO
def init_keys():
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setup(KEY_UP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
    GPIO.setup(KEY_DOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
    GPIO.setup(KEY_LEFT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
    GPIO.setup(KEY_RIGHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
    GPIO.setup(KEY_PRESS_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
    GPIO.setup(KEY1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
    GPIO.setup(KEY2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
    GPIO.setup(KEY3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up


def key_pressed_up():
    return GPIO.input(KEY_UP_PIN) == 1


def key_pressed_down():
    return GPIO.input(KEY_DOWN_PIN) == 1


def key_pressed_left():
    return GPIO.input(KEY_LEFT_PIN) == 1


def key_pressed_right():
    return GPIO.input(KEY_RIGHT_PIN) == 1


def key_pressed_center():
    return GPIO.input(KEY_PRESS_PIN) == 1


def key_pressed_1():
    return GPIO.input(KEY1_PIN) == 1


def key_pressed_2():
    return GPIO.input(KEY2_PIN) == 1


def key_pressed_3():
    return GPIO.input(KEY3_PIN) == 1
