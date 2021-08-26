from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
from selenium.webdriver.firefox.options import Options

# options = Options()
# options.headless = True


for i in range (1, 100):
	browser = webdriver.Firefox(executable_path = '/Users/hunterkrasa/Downloads/geckodriver')
	browser.get('https://distrokid.com/spotlight/tpie/vote/')
	a = ActionChains(browser)

	sleep(4)

	# vote_button = browser.find_element_by_xpath('//div[@class="voting-card_actions"]/*[name()="a"][@data-songid="24124656"]')
	vote_button = browser.find_element_by_class_name("voteButton")

	a.move_to_element(vote_button).perform()

	vote_button.click()

	sleep_number = random.randint(1,6)
	sleep(sleep_number)

	browser.close()

	print("Voted {} times".format(i))

	sleep(2)