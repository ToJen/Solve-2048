from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, random

driver = webdriver.Chrome('assets/chromedriver')
driver.get('https://gabrielecirulli.github.io/2048/')

time.sleep(2)	# wait for page to load

gameElem = driver.find_element_by_class_name('grid-container')

directions = [Keys.UP, Keys.DOWN, Keys.RIGHT, Keys.LEFT]

ActionChains(driver).move_to_element_with_offset(gameElem, 0, 50).perform()
# print("moving...")
time.sleep(3)
# print("moved...")
# choice_last = None
# choice = None
while True:
	for direction in directions:
		choice = random.choice(direction)
		# if choice == choice_last:

		ActionChains(driver).send_keys(choice).perform()
		# time.sleep(2)
		# choice_last = choice

# restartElem = driver.find_element_by_link_text('New Game')
restartElem = driver.find_element_by_link_text('Try again')
# restartElem.click()
game_over = false

while not game_over:
	if restartElem:
		restartElem.click()

	for direction in directions:
		choice = random.choice(direction)
		ActionChains(driver).send_keys(choice).perform()