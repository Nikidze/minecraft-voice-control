import pyautogui
from math import radians, sin, sqrt


class AutoGui:
    def __init__(self):
        self.down_keys = []

    def runCommand(self, coomand):
        commands = coomand.split(" и ")
        for command in commands:
            words = command.split()
            self.parseAction(words)

    def parseAction(self, words):
        action = words[0]
        if action in ['идти', 'бежать', 'бежать вприпрыжку', 'идти в приседе']:
            self.goAction(words)
        if action in ['нажать', 'зажать', 'отпустить']:
            self.mouseAction(words)
        if action == 'выбрать':
            self.selectAction(words)
        if action == 'повернуть':
            self.rotateAction(words)
        if action == 'переключить':
            self.switchPerspective()
        if action == 'выкинуть':
            self.throwItem()
        if action == 'стоп':
            self.keyUp()

    def goAction(self, words):
        if words[0] == 'идти':
            if words[1] == 'в':
                key = self.getKeyByDir(words[3])
                self.keyDown('shiftleft', key)
            else:
                key = self.getKeyByDir(words[1])
                self.keyDown(key)
        if words[0] == 'бежать':
            if words[1] == 'вприпрыжку':
                key = self.getKeyByDir(words[2])
                self.keyDown('ctrlleft', 'space', key)
            else:
                key = self.getKeyByDir(words[1])
                self.keyDown('ctrlleft', key)
    
    def mouseAction(self, words):
        action = words[0]
        if action == 'нажать':
            button = 'left'
            if words[1] == 'правую':
                button = 'right'
            pyautogui.click(button=button)
        if action == 'зажать':
            button = 'left'
            if words[1] == 'правую':
                button = 'right'
            pyautogui.mouseDown(button=button)
        if action == 'отпустить':
            button = 'left'
            if words[1] == 'правую':
                button = 'right'
            pyautogui.mouseUp(button=button)

    def rotateAction(self, words):
        deg = 0
        if words[5] == 'минус':
            deg = int(words[6])
        else:
            deg = -int(words[5])
        rad = radians(deg)
        w, h = pyautogui.size()
        if words[3] == 'вертикали':
            y = sin(rad)*sqrt(h*h+h*h)/2
            pyautogui.move(0, int(y))
        if words[3] == 'горизонтали':
            x = sin(rad)*sqrt(w*w+w*w)/2
            pyautogui.move(-int(x), 0)
        
    def selectAction(self, words):
        pyautogui.press(words[2])

    def switchPerspective(self):
        pyautogui.press('f5')

    def throwItem(self):
        pyautogui.press('q')

    def getKeyByDir(self, dir):
        keys = {'вперёд': 'w', 'назад': 's', 'вправо': 'd', 'влево': 'a'}
        return keys[dir]

    def keyDown(self, *args):
        self.down_keys = args
        for key in args:
            pyautogui.keyDown(key)

    def keyUp(self):
        for key in self.down_keys:
            pyautogui.keyUp(key)
        self.down_keys = []