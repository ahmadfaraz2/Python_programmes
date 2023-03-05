import pyautogui as pg
import time
import webbrowser


url = "https://web.whatsapp.com"
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get("chrome").open_new(url)


time.sleep(20)  


for i in range(10):  # Select how many times you want to send following message
    pg.write("Saad")  # Write your message 
    pg.press('Enter') 
