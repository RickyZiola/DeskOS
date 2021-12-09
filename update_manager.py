import filecmp
import os
import json
import tkinter as tk
import time
root=tk.Tk()
root.eval('tk::PlaceWindow . center')
second_win = tk.Toplevel(root)
root.eval(f'tk::PlaceWindow {str(second_win)} center')
updateData=tk.Label(root, text="Checking for updates...")
updateData.pack()
os.system("mkdir updatecmp; cd updatecmp; git clone https://github.com/RickyZiola/DeskOS.git")
time.sleep(1)
try:
  package = json.load(open("src/DeskOS/package.json"))
except:
  package = ""
if(filecmp.cmp("src/DeskOS/package.json", "updatecmp/DeskOS/package.json",shallow=False) != True):
  updateData.config(text="Update available! Do you want to update now?")
  updateData.update_idletasks()
  def update():
    confirmButton.pack_forget()
    cancelButton.pack_forget()
    os.system("cd src; rmdir /S /Q DeskOS; rm -r -rf DeskOS; git clone https://github.com/RickyZiola/DeskOS.git")
    try:
      package = json.load(open("src/DeskOS/package.json"))
    except:
      package = ""
    updateData.config(text="Updated to DeskOS v" + package["version"])
    updateData.update_idletasks()
    time.sleep(5)
    root.destroy()
  def cancel():
    confirmButton.pack_forget()
    cancelButton.pack_forget()
    updateData.config(text="Update cancelled.")
    updateData.update_idletasks()
    time.sleep(5)
    root.destroy()
  confirmButton=tk.Button(root, text="Yes", command=update)
  cancelButton=tk.Button(root, text="No", command=cancel)
  confirmButton.pack()
  cancelButton.pack()
else:
  updateData.config(text="Up to date, version: v" + package["version"])
  updateData.update_idletasks()
root.mainloop()
os.system("rm -r -rf updatecmp; python src/DeskOS/main.py")
