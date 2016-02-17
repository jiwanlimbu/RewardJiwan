#!/usr/bin/python

###############################################################
#
#				Jiwan Ninglekhu
#				02/07/2016
#				Rewardjiwan
#				Language: Python
#
################################################################

from bs4 import BeautifulSoup
import requests
import re
import time
import unittest
from urllib2 import HTTPError
import urllib as UR
import webbrowser
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import *
import webbrowser
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from random import randint
import random

emails = {"jiwan.ninglekhu@hotmail.com": "Sanantonio123", "jacklimbu@hotmail.com": "meromanju1", "rozy_limbu@hotmail.com":"limbu123", "rosielimbu@hotmail.com":"limbu123", "joaanmillion@outlook.com":"limbu123"}

for key, value in emails.iteritems():
	count = 0
	driver = webdriver.Firefox()
	print "Browser fired-up!"
	driver.implicitly_wait(5)

	driver.get("https://www.bing.com/")
	time.sleep(1)
	driver.refresh()
	print "Broswer Refreshed!"
	time.sleep(2)
	avatar = driver.find_element_by_id("id_a")
	avatar.click()
	singinlink = driver.find_element_by_class_name("id_name")
	singinlink.click()
	print key
	print value

	hUsername = key
	hPassword = value
	emailFieldID  = "loginfmt"
	passFieldID= "passwd"
	loginButtonid = "idSIButton9"
	inLogoID 	   = "in-logo"

	emailFieldElement = driver.find_element_by_name(emailFieldID)
	passFieldElement = driver.find_element_by_name(passFieldID)
	loginButtonElement = driver.find_element_by_id(loginButtonid)

	emailFieldElement.clear()
	emailFieldElement.send_keys(hUsername)
	passFieldElement.clear()
	passFieldElement.send_keys(hPassword)
	loginButtonElement.click()
	time.sleep(1)

	driver.refresh()
	print "Broswer Refreshed!"
	time.sleep(5)
	while True:
		randnum = randint(0, 110000)
		randstr = str(randnum)
		randnum1 = randnum + 237647536
		randstrplus = str(randnum1)
		sword = randstr + "Number  "+ randstr + " and " +  randstrplus

		elem = driver.find_element_by_name("q")
		#elem.send_keys("valeove yours")
		elem.send_keys(sword, Keys.RETURN)
		assert "No results found." not in driver.page_source
		count = count+1
		time.sleep(1)
		if (count == 20):
			time.sleep(5)
			print "20 searches completed"
			continue
			
		elif (count == 30):
			print "30 searches competed"
			break

	driver.get("https://www.bing.com/rewards/dashboard")
	print "Bing!!!!"
	time.sleep(5)
	driver.refresh()
	print "Broswer Refreshed!"
	time.sleep(3)
	
	try:
		playlink = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/a")
		playlink.click()
		time.sleep(3)
	except NoSuchElementException: 
		print "playlink Element not found "
	else:
   		print "playlink clicked"
   		backbutton = driver.find_element_by_id("back-to-bing-text")
		backbutton.click()

	driver.refresh()
	print "Broswer Refreshed!"
	time.sleep(3)
	try:
		quizlink = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[1]/a/span/span[1]")
		quizlink.click()
	except NoSuchElementException: 
		print "quiz1 Element not found "
	else:
   		print "quiz1 clicked"
	
	driver.refresh()
	print "Broswer Refreshed!"
	time.sleep(3)
	try:
		quizlink2 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[2]/a/span/span[1]")
		quizlink2.click()
	except NoSuchElementException: 
		print "quiz2 Element not found"
	else:
   		print "quiz2 clicked"

	driver.refresh()
	print "Broswer Refreshed!"
	time.sleep(3)

	try:
		quizlink3 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[3]/a/span/span[1]")
		quizlink3.click()
	except NoSuchElementException: 
		print "quiz3 Element not found "
	else:
   		print "quiz3 clicked"

	driver.refresh()
	print "Broswer Refreshed!"
	time.sleep(3)

	try:
		quizlink4 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[4]/a/span/span[1]")
		quizlink4.click()
	except NoSuchElementException: 
		print "quiz4 Element not found "
	else:
   		print "quiz4 clicked"

	driver.refresh()
	print "Broswer Refreshed!"
	time.sleep(3)

	try:
		quizlink5 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[5]/a/span/span[1]")
		quizlink5.click()

	except NoSuchElementException: 
		print "quiz5 Element not found "
	else:
   		print "quiz5 clicked"


	driver.refresh()
	print "Broswer Refreshed!"
	time.sleep(3)

	try:
		quizlink6 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[6]/a/span/span[1]")
		quizlink6.click()

	except NoSuchElementException: 
		print "quiz6 Element not found "
	else:
   		print "quiz6 clicked"

	driver.refresh()
	print "Broswer Refreshed!"
	time.sleep(3)

	try:
		quizlink7 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[7]/a/span/span[1]")
		quizlink7.click()

	except NoSuchElementException: 
		print "quiz7 Element not found "
	else:
   		print "quiz7 clicked"

	driver.refresh()
	print "Broswer Refreshed!"
	time.sleep(3)

	try:
		quizlink8 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[]/a/span/span[1]")
		quizlink8.click()

	except NoSuchElementException: 
		print "quiz8 Element not found "
		driver.close()
	else:
   		print "quiz8 clicked"
   		driver.close()
print "------------------ STARTING MOBILE SEARCH ------------"
for key, value in emails.iteritems():
	count = 0
	time.sleep(5)
	profile = FirefoxProfile("/Users/jiwanninglekhu/Documents/python/RewardJiwan/foxjiwan")
	driver = webdriver.Firefox(profile)
	print "Browser fired-up!"
	driver.implicitly_wait(5)
	driver.get("https://www.bing.com/rewards/dashboard")
	enterin = driver.find_element_by_class_name("avatar")
	enterin.click()
	time.sleep(3)
	print key
	print value

	hUsername = key
	hPassword = value
	emailFieldID  = "loginfmt"
	passFieldID= "passwd"
	loginButtonid = "idSIButton9"
	inLogoID 	   = "in-logo"

	emailFieldElement = driver.find_element_by_name(emailFieldID)
	passFieldElement = driver.find_element_by_name(passFieldID)
	loginButtonElement = driver.find_element_by_id(loginButtonid)

	emailFieldElement.clear()
	emailFieldElement.send_keys(hUsername)
	passFieldElement.clear()
	passFieldElement.send_keys(hPassword)
	loginButtonElement.click()
	# time.sleep(7)

	driver.get("https://www.bing.com/")
	print "Bing!!!!"
	time.sleep(2)
	word_file = "/usr/share/dict/words"
	while True:
		def random_line(afile):
    			line = next(afile)
    			for num, aline in enumerate(afile):
      				if random.randrange(num + 2): 
      					continue
      					line = aline
    			return line
		
		randnum = randint(0, 110000)
		randstr = str(randnum)
		randnum1 = randnum + 237647536
		randstrplus = str(randnum1)
		sword = randstr + "Number  "+ randstr + " and " +  randstrplus
		
		# WORDS = open(word_file).read().splitlines()
		# print WORDS
		elem = driver.find_element_by_id("sb_form_q")
		#elem.send_keys(sword)
		#elem.submit()
		elem.send_keys(sword, Keys.RETURN)

		#elem.send_keys(Keys.RETURN)
		#assert "No results found." not in driver.page_source
		count = count+1
		time.sleep(2)
		driver.find_element_by_id("sb_form_q").clear()
		if (count == 10):
			time.sleep(3)
			print "10 searches completed"
			continue
			
		elif (count == 20):
			print "20 searches competed"
			break
		
	driver.get("https://www.bing.com/rewards/settings/profileframed")
    	
	driver.close()	
