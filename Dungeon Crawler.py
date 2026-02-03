from random import randint
from time import sleep
import os
clear = lambda: os.system('cls')

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
	if randint(0, 100) < 60:
		print("You found a health potion!")
		want_to_drink = input('❓  Drink the health potion? [Y/n]❓').lower()

		potionEffect = randint(-20, 20)
		if want_to_drink == '' or 'y' in want_to_drink:
			if potionEffect < 0:
				print("☠️ Oh no! It was a poison! Hero lost", abs(potionEffect), "health points.☠️")
				hero["health"] += potionEffect
			else:
				print("💖 Yay! It was a healing potion! Hero gained", potionEffect, "health points.💖")
				hero["health"] += potionEffect
	print("💙 Hero's current health:", hero["health"], "💙")

		
	if hero["health"] <= 0:
		gameOver()


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




if day == 5:
	print("📖Hero found a spellbook!📖")
	# your code here...
	want_to_learn = input('❓  Learn a new spell? [Y/n]❓').lower()
	if want_to_learn == '' or 'y' in want_to_learn and hero["experience"] >= 100:
		hero["strength"] += 5
		print("✨ Hero learned a new spell and increased strength to", hero["strength"], "✨")









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