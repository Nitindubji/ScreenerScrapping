import pyautogui
from selenium import webdriver
import time 
import os
import pandas as pd

path1 = '/Users/Downloads/Long_Setup.html'

try:
    os.remove(path1)
except:
    pass

url1 = 'https://chartink.com/screener/bullish-rsi-stochastic'

driver = webdriver.Chrome('/Users/Documents/GitHub/SignalGenerators/Scrape & Trade/chromedriver')#path to chromedriver
driver.get(url1)
time.sleep(2) 

pyautogui.hotkey('command', 's')
time.sleep(2)

pyautogui.write('Intraday RSI Long.html', interval=0)
pyautogui.press('enter')
time.sleep(2)

pyautogui.press('left')
pyautogui.press('enter')
driver.close()

path2 = '/Users/yashrajjaiswal/Downloads/Intraday RSI Short.html'

try:
    os.remove(path2)
except:
    pass

url2 = 'https://chartink.com/screener/sell-15-min'

driver = webdriver.Chrome('/Users/Documents/GitHub/SignalGenerators/Scrape & Trade/chromedriver')#path to chromedriver
driver.get(url2)
time.sleep(2) 

pyautogui.hotkey('command', 's')
time.sleep(2)

pyautogui.write('Short Setup.html', interval=0)
pyautogui.press('enter')
time.sleep(2)

pyautogui.press('left')
pyautogui.press('enter')
driver.close()

#save 
data_1 = pd.read_html(path1)
data_1 = pd.DataFrame(data_1[1])
data_1['Trade'] = 'BUY'

#save 
data_2 = pd.read_html(path2)
data_2 = pd.DataFrame(data_2[1])
data_2['Trade'] = 'SELL'

data = pd.concat([data_1,data_2],axis=0).reset_index(drop=True)
data.drop('Sr.',axis=1,inplace=True)

data.to_csv('Chartink Screened.csv',index=False)

