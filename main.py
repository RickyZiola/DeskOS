import tkinter as tk
import random
import json
import time
import os
import requests
from datetime import datetime
now = datetime.now()
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
URL = BASE_URL + "q=" + "chesaning" + "&appid=" + "2a530c734a9fba21b6e3ffff2aa2c552"
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = round(((int(main['temp']) - 273.15) * 1.8) + 32)
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")
package = json.load(open("package.json"))
version = package["version"]
root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("DeskOS v" + version)
title = tk.Label(root, text="DeskOS v" + version, font=("Arial", 7))
title.pack()
close = tk.Button(root, text="SHUTDOWN", command=root.destroy)
close.pack(side=tk.BOTTOM)
if(int(now.strftime("%H")) > 12):
    currentTime = str(int(now.strftime("%H")) - 11) + ":" + str(now.strftime("%M")) + " PM"
else:
    currentTime = str(int(now.strftime("%H")) + 1) + ":" + str(now.strftime("%M")) + " AM"
current_time = tk.Label(root, text="It's "+currentTime, font=("arial", 30))
current_time.pack(expand=1, fill=tk.BOTH)
temp = tk.Label(root, text="", font=("arial", 30))
temp.pack(expand=1, fill=tk.BOTH)
def update():
    now = datetime.now()
    if(int(now.strftime("%H")) > 12):
        currentTime = str(int(now.strftime("%H")) - 11) + ":" + str(now.strftime("%M")) + " PM"
    else:
        currentTime = str(int(now.strftime("%H")) + 1) + ":" + str(now.strftime("%M")) + " AM"
    current_time.config(text="It's "+currentTime)
    current_time.update_idletasks()
    response = requests.get(URL)
    if response.status_code == 200:
       data = response.json()
       temperature = round(((int(main['temp']) - 273.15) * 1.8) + 32)
       temp.config(text=str(temperature) + "°F")
    else:
        temp.config(text="Failed HTTP read!")
    temp.update_idletasks()
    root.after(1000, update)

root.after(1000, update)
root.mainloop()
time.sleep(10) #sleep, giving the user time to end the script and return to linux OS
#os.system("sudo shutdown now") #Linux shutdown
#os.system("shutdown /s") #Windows shutdown


