#! /usr/bin/env python3
#This code compiles information from various municipal websites that
#post information about coronavirus statistics it was created to
#help out my brother and send him an email daily to keep him up to date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime, re, ezgmail

browser = webdriver.Chrome(executable_path=r'/Users/nicholashockey/Code/chromedriver')
browser.get('https://www.google.com/search?sxsrf=ALeKk02ef9815ge4bXln2fhKSseBfNQehQ%3A1594250775572&ei=F1YGX-nFIuaJytMP_f-ZyAc&q=coronacirus+ontario&oq=coronacirus+ontario&gs_lcp=CgZwc3ktYWIQAzIHCCMQsQIQJzIHCCMQsQIQJzIHCCMQsQIQJzIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjoCCAA6BwgjEOoCECc6BAgjECc6BAgAEEM6BwgAELEDEEM6BQgAEJECOgoIABCxAxCDARBDOgcIABBDEIsDOggIABCRAhCLAzoKCAAQsQMQQxCLAzoFCAAQsQM6CAgAELEDEIMBOgoIABCxAxCDARAKOgcIABAKEIsDOggIABCxAxCLAzoFCAAQiwNQvGNYjnpgj3toAXAAeACAAZADiAGyEZIBBzkuOS40LTGYAQCgAQGqAQdnd3Mtd2l6sAEKuAEC&sclient=psy-ab&ved=0ahUKEwipraT55r7qAhXmhHIEHf1_BnkQ4dUDCAw&uact=5#scso=_h1YGX__iHOiyytMPyJaI8A412:0')

#Getting the info for ontario by searching headlines with keyword new cases
newsElem = browser.find_element_by_partial_link_text('new coronavirus cases')
newsElem.click()
casesElem = browser.find_element_by_class_name('l-article__title')
ontario_info = casesElem.text

#The info for halton areas (oakville milton burlington) To capture
#all the information on this page I take a screenshot of a table that is featured
#on the website
browser.get('https://www.halton.ca/For-Residents/New-Coronavirus')
time.sleep(3)
haltonElem = browser.find_element_by_partial_link_text('Halton cases by municipality')
haltonElem.click()
haltonElem.click()
pageElem = browser.find_element_by_tag_name('html')
time.sleep(3)
pageElem.send_keys(Keys.PAGE_DOWN)
browser.save_screenshot('zachpic.png')

#Info for waterloo. Waterloo has a very detailed graph so I take a screenshot
browser.get('https://public.tableau.com/views/WaterlooRegionCOVID-19Summary/COVID-19?:showVizHome=no&amp;:embed=true&amp;:linktarget= blank;:toolbar=no&amp;:display_count=yes&amp;:tabs=no&amp;wmode=transparent&amp;&amp;wmode=transparent:render=false&amp;&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent&amp;wmode=transparent')
time.sleep(5)
browser.save_screenshot('zachpic2.png')

#Info for hamilton. Hamilton has much less information therefore 
#i only search the website using a regular expression to find the number of probable
#active cases
browser.get('https://www.hamilton.ca/coronavirus/status-cases-in-hamilton')
hamElem = browser.find_element_by_css_selector('#wb-pri-in > div.region-alexander-first > div.panel-pane.pane-node-content > div > div > div > div > div.panel-pane.pane-entity-field.pane-node-body > div > div > div > div > div.coh-column.half.first > div > p:nth-child(1) > strong')
hamRegex = re.compile(r'Number of probable cases - +\d')
mo1 = hamRegex.search(hamElem.text)
hamInfo = mo1.group()

#GETTING DATE FOR TODAY
today_date = datetime.datetime.now()
date_string = today_date.strftime('%Y/%m/%d %H:%M:%S')

#Sending the email
ezgmail.send('zach101jc@gmail.com','Corona cases ' + str(date_string), 'In ontario: ' + str(ontario_info) + '\n' + 'In hamilton there are: ' + str(hamInfo), ['zachpic.png','zachpic2.png'])
