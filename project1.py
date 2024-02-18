from pygame import * 
import pygame_menu


init()
window = display.set_mode((600,400))

def start():
    print('start')
def end():
    exit()
def help():
    help_menu = pygame_menu.Menu('M.M',600,400,theme=pygame_menu.themes.THEME_DARK.copy())
    help_menu.add.label('інформація')
    help_menu.add.label('Щоб зіграти гу натисніть: запуск')
    help_menu.add.label('Щоб зупинити гру натисніть: вихід')

    def back():
        menu.enable()
        help_menu.disable()
        menu.mainloop(window)


    help_menu.add.button('back',back)
    menu.disable()
    help_menu.mainloop(window)

    
menu = pygame_menu.Menu('M.M',600,400,theme=pygame_menu.themes.THEME_DARK.copy())
menu.add.button('start game',start)
menu.add.button('end game',end)
menu.add.button('help',help)

menu.mainloop(window)

game = True

