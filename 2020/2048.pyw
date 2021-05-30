#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, time, sys

#getting the chrome driver
browser = webdriver.Chrome(executable_path=r'/Users/nicholashockey/Code/chromedriver')

#accessing the 2048 game online
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')

#Variabls to store scores, moves and averages
scores = []
Tot_scores = []
current_moves = ''
total_moves = []
#List of possible moves
moveset = [Keys.UP, Keys.DOWN, Keys.RIGHT, Keys.LEFT]

#Move assignment function
def assign_move(lim):
	global current_moves
	move = moveset[random.randint(0,lim)]
	del moveset[moveset.index(move)]
	if move == Keys.UP:
		current_moves += 'UP, '
	elif move == Keys.DOWN:
		current_moves += 'DOWN, '
	elif move == Keys.RIGHT:
		current_moves += 'RIGHT, '
	elif move == Keys.LEFT:
		current_moves += 'LEFT, '
	return move

#Assigning moves
move1 = assign_move(3)
move2 = assign_move(2)
move3 = assign_move(1)
move4 = assign_move(0)
moveset = [Keys.UP, Keys.DOWN, Keys.RIGHT, Keys.LEFT]

while True: #main loop
	#Keystrokes
	htmlElem.send_keys(move1)
	htmlElem.send_keys(move2)
	htmlElem.send_keys(move3)
	htmlElem.send_keys(move4)

	#Pressing retry if the button appears
	retry_button = browser.find_element_by_class_name('retry-button')
	if retry_button.is_displayed() == True:
		score = browser.find_element_by_class_name('score-container')
		scores.append(int(score.text))
		
		retry_button.click()

	#after 5 games have been played with 1 moveset
	if len(scores) == 5:
		#Saving results
		Tot_scores.append(scores)
		total_moves.append(current_moves[:-2])
		scores = []
		current_moves = ''
		#Resetting moveset
		move1 = assign_move(3)
		move2 = assign_move(2)
		move3 = assign_move(1)
		move4 = assign_move(0)
		moveset = [Keys.UP, Keys.DOWN, Keys.RIGHT, Keys.LEFT]
		continue
	if len(Tot_scores) == 2: #Ending after 2 iterations
		break

averages = []

#Finding averages
for games in Tot_scores:
	average = sum(games) / 5
	averages.append(average)

results = {}
#Creating dictionary of results with averages and moveset pairs
for key in total_moves:
	for value in averages:
		results[key] = value
		averages.remove(value)

for key, value in results.items():
	print(f'For the moveset of {key} you have obtianed an average of {value}, Congradulations!')