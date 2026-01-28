from random import randint
from time import sleep
import os
clear = lambda: os.system('clear')

hero = {
	# create keys and values here
    "name": "Hero",
	"health": 100,
	"strength": 10,
	"defense": 5,
	"gold": 0,
	"level": 1,
	"experience": 0
}

day = 1


def startGame():
	global day
	while day <= 10:
		print("📅 Day", day, "started...📅")
		day += 1

		want_to_fight = input('❓  Fight with a goblin? [Y/n]❓').lower()

		if want_to_fight == '' or 'y' in want_to_fight:
			fight()
		else:
			noFight()
		


input("🎮 Press ENTER to continue...🎮")


def noFight():
	print("🏃 Hero decided to avoid this fight...🏃") 


def fight():
	print("🗡️ Hero decided to fight with a goblin...🗡️")
	damage = randint(10, 30)
	hero["health"] -= damage
	if hero["health"] <= 0:
		gameOver()
	else:
		print("🏆 Hero defeated the goblin!🏆")

	experience = randint(10, 25)
	hero["experience"] += experience
	print(f"🔵 Hero gained {experience} experience points.🔵")
	if hero["experience"] >= 100:
		hero["level"] += 1
		hero["experience"] = 0
		print("🆙 Hero leveled up! Now at level", hero["level"], "🆙")

def gameOver():
	reset()
	print("🟥 Game Over! Your hero has died.🟥")
	input("🎮 Press ENTER to play again🎮")
	startGame()


def endGame():
	reset()
	print("🎉 Congratulations! Your hero has survived the dungeon for 10 days.🎉")
	input("🎮 Press ENTER to play again🎮")
	startGame()


def reset():
	global hero
	global day
	day = 1
	# set all values of the hero dictionary to the same values they were declared
	hero = {
		"name": "Hero",
		"health": 100,
		"strength": 10,
		"defense": 5,
		"gold": 0,
		"level": 1,
		"experience": 0
	}



startGame()