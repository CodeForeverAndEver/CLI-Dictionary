# https://github.com/CodeForeverAndEver/ColorIt
import os
import sys


class Colors:
    red = (245, 90, 66)
    orange = (245, 170, 66)
    yellow = (245, 252, 71)
    green = (92, 252, 71)
    blue = (71, 177, 252)
    purple = (189, 71, 252)
    white = (255, 255, 255)


def init_colorit():
    if sys.platform.startswith('win32'):
        os.system("cls")
    elif sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
        os.system("clear")


def color(text, rgb):
    return "\033[38;2;{};{};{}m{}\033[0m".format(str(rgb[0]), str(rgb[1]), str(rgb[2]), text)


def background(text, rgb):
    return "\033[48;2;{};{};{}m{}\033[0m".format(str(rgb[0]), str(rgb[1]), str(rgb[2]), text)