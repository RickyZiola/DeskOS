import filecmp
import os
import json
import tkinter as tk
root=tk.Tk()
root.eval('tk::PlaceWindow . center')
second_win = tk.Toplevel(root)
root.eval(f'tk::PlaceWindow {str(second_win)} center')
updateData=tk.Label(root, text="Checking for updates...")
updateData.pack()
os.system("mkdir updatecmp; cd updatecmp; git clone https://github.com/RickyZiola/DeskOS.git")
main=open("updatecmp/DeskOS/src/DeskOS/main.py")
package=open("updatecmp/DeskOS/src/DeskOS/package.json")
wmain=open("updatecmp/DeskOS/main.py", "w")
wpackage=open("updatecmp/DeskOS/package.json", "w")
wmain.write(main.read())
os.system('rm -r -rf updatecmp/DeskOS/src; rmdir /S /Q updatecmp/DeskOS/src')
try:
  package = json.load(open("src/DeskOS/package.json"))
except:
  package = ""
if(filecmp.cmp("src/DeskOS/package.json", "updatecmp/DeskOS/package.json",shallow=False) != True):
  updateData.config(text="Update available! Do you want to update now?")
  updateData.update_idletasks()
  def update():
    os.system("cd src; rmdir /S /Q DeskOS; rm -r -rf DeskOS; git clone https://github.com/RickyZiola/DeskOS.git")
    main=open("src/DeskOS/src/DeskOS/main.py")
    package=open("src/DeskOS/src/DeskOS/package.json")
    wmain=open("src/DeskOS/main.py", "w")
    wpackage=open("src/DeskOS/package.json", "w")
    wmain.write(main.read())
    wpackage.write(package.read())
    os.system("rm -r -rf src/DeskOS/src; rmdir /S /Q src/DeskOS/src; rm src/DeskOS/update_manager.py; del src/DeskOS/update_manager.py")

    try:
      package = json.load(open("src/DeskOS/package.json"))
    except:
      package = ""
    updateData.config(text="Updated to DeskOS v" + package["version"])
    updateData.update_idletasks()
  def cancel():
    updateData.config(text="Update cancelled.")
    updateData.update_idletasks()
  confirmButton=tk.Button(root, text="Yes", command=update)
  cancelButton=tk.Button(root, text="No", command=cancel)
  confirmButton.pack()
  cancelButton.pack()
else:
  updateData.config(text="Up to date, version: v" + package["version"])
  updateData.update_idletasks()
os.system("rm -r -rf updatecmp; python src/DeskOS/main.py")
