import os
import pygame
from pygame.locals import *
if not pygame.font: print('fonts disabled')
if not pygame.mixer: print('sound disabled')


# 加载资源
def load_image(name, colorkey = None):
    fullname = os.path.join('data', name)
    print(fullname)
    try:
        # 加载图片资源
        image = pygame.image.load(fullname)
    except pygame.error as message:
        # 失败就退出
        print('cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    #如果有RGB值，就使用传递过来的RGB值
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self): pass
    # 没有pygame 的音乐加载模块的话，就返回一个虚拟方法
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        # 读取音乐文件
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        # 失败就退出
        print('cannot load sound:', name)
        raise SystemExit(message)
    return sound

