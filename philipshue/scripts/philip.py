from phue import Bridge
import random


b = Bridge('192.168.115.110')
b.connect()
b.get_api()


def get_lights():
    return b.lights


def on_off(lights):
    b.set_light(lights, 'on', not b.get_light(lights[random.randint(0, len(lights) - 1)], 'on'))
