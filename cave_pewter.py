import time
import threading
import pyautogui
import pyscreenshot as ImageGrab



def falas():
	fala = 'oii'

def capture_screen():
	screen=ImageGrab.grab()
	return screen


def enfermeira_joy_detect(screen):
	#color text joy 41 143 244
	color = screen.getpixel((239,110))
	if color == (41, 143, 244):
		return True
	else:
		return False
def says_joy():
	pyautogui.press("space")
	time.sleep(1)
	pyautogui.press("space")
	pyautogui.press("space")
	pyautogui.press("space")
	pyautogui.press("space")
	pyautogui.press("space")
	time.sleep(2)
	pyautogui.click(x=386,y=253)
	pyautogui.press("space")
	time.sleep(3)
	pyautogui.press("space")
	time.sleep(3)
	pyautogui.press("space")
	time.sleep(3)
	pyautogui.press("space")
	time.sleep(0.5)
	pyautogui.press("down")

def hab_1():
	time.sleep(0.5)
	pyautogui.press("1")
	#pyautogui.click(x=709,y=536)
	time.sleep(0.5)
	pyautogui.press("1")
	#pyautogui.click(x=749,y=269)

def hab_2():
	time.sleep(1)
	time.sleep(0.5)
	pyautogui.press("1")
	#pyautogui.click(x=709,y=536)
	time.sleep(0.5)
	pyautogui.press("2")
	#pyautogui.click(x=749,y=327)

def hab_3():
	time.sleep(1)
	pyautogui.press("1")
	time.sleep(0.5)
	pyautogui.press("3")
	#pyautogui.click(x=749,y=378)

def hab_4():
	time.sleep(1)
	pyautogui.press("1")
	time.sleep(0.5)
	pyautogui.press("4")
	#pyautogui.click(x=749,y=429



def bot_move_cave():
	term_txt=open('terminal.txt','a')
	term_txt.write('Star Bot.....')
	term_txt.close()
	time.sleep(0.3)
	for x in range(1,6):
		time.sleep(0.3)
		pyautogui.press("down")
	time.sleep(3)
	for x in range(1,9):
		time.sleep(0.3)
		pyautogui.press("down")
	for x in range(1,10):
		time.sleep(0.3)
		pyautogui.press("left")
	for x in range(1,14):
		time.sleep(0.3)
		pyautogui.press("down")
	time.sleep(3)
	#segunda parte do mapa cav
	for x in range(1,14):
		time.sleep(0.3)
		pyautogui.press("down")
	for x in range(1,7):
		time.sleep(0.3)
		pyautogui.press("left")


def bot_move():
	time.sleep(0.3)
	pyautogui.press("right")
	time.sleep(0.3)
	pyautogui.press("left")
	term_txt=open('terminal.txt','a')
	term_txt.write('move...')
	term_txt.close()

def detect_enimy(screen):
	color = screen.getpixel((121,211))
	if color == (254, 214, 84):
		return True
	else:
		return False
def detect_enimy_th():
	term_txt=open('terminal.txt','a')
	term_txt.write('Battle...')
	term_txt.close()

def detect_heal_poke_center(screen):
    color = screen.getpixel((80,94))
    if color == (61, 59, 59):
    	return True

def detect_dead_poke(screen):
    color = screen.getpixel((74,94))
    if color == (61, 59, 59):
    	return True

def detect_dead_poke_battle(screen):
    color = screen.getpixel((648,522))
    if color == (247, 6, 0):
    	return True
def potion_poke():
	pyautogui.press("1")

def back_pc():
	for x in range(1,18):
		time.sleep(0.3)
		pyautogui.press("right")
	for x in range(1,4):
		time.sleep(0.3)
		pyautogui.press("left")
	for x in range(1,16):
		time.sleep(0.3)
		pyautogui.press("up")
	time.sleep(3)
	#mudando de mapa
	for x in range(1,7):
		time.sleep(0.3)
		pyautogui.press("left")
	for x in range(1,12):
		time.sleep(0.3)
		pyautogui.press("up")
	for x in range(1,11):
		time.sleep(0.3)
		pyautogui.press("right")
	for x in range(1,12):
		time.sleep(0.3)
		pyautogui.press("up")
	time.sleep(3)
	#entrando no cp
	for x in range(1,8):
		time.sleep(0.3)
		pyautogui.press("up")
	says_joy()

def bot():
	bot_move_cave()
	while True:
		screen = capture_screen()
		if detect_dead_poke(screen) == True:
			back_pc()
		elif detect_dead_poke_battle(screen) == True:
			leave_batlle()
			back_pc()
		elif enfermeira_joy_detect(screen) == True:
			says_joy()
			time.sleep(0.5)
			bot_move_cave()
		elif detect_enimy(screen) == True:
			hab_1()
			detect_enimy_th()
			if detect_enimy(screen) == True:
				hab_1()
				detect_enimy_th()
				if detect_enimy(screen) == True:
					hab_1()
					detect_enimy_th()
					if detect_enimy(screen) == True:
						hab_1()
						detect_enimy_th()
		#elif detect_heal_poke_center(screen) == True:
		#	potion_poke()
			
		elif detect_enimy(screen) == False:
			bot_move()

	#for a in range(1,7):
	#	time.sleep(0.7)
	#	pyautogui.press("down")
	#	for b in range(1,10):
	#		time.sleep(0.7)
	#		pyautogui.press("down")
	#		for c in range(1,10):
	#			time.sleep(0.9)
	#			pyautogui.press("left")