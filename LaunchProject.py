#!/usr/bin/env python3.7

from Laravel import Laravel
import iterm2
import sys
from PyQt6.QtWidgets import QWidget, QApplication, QInputDialog, QFileDialog

async def main(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window
    if window is not None:
        # Alert for testing
        #alert = iterm2.Alert("", "HI")
        #await alert.async_run(connection)

        # Open an OptionDialog to select the project type
        items = ("Laravel", "React (Comming soon)", "Python (Comming soon)")
        application = QApplication(sys.argv)
        widget = QWidget()
        el = QInputDialog.getItem(widget, "Select your Project Type", 
        "List of types:", items, 0, False)

        ok = el[1]
        item = el[0]
    
        if not ok or not item:
            return

        # Open a FileDialog to select the project directory
        dir = str(QFileDialog.getExistingDirectory(widget, "Select Directory"))

        # Exit if no directory is selected
        if (dir == ""):
            return

        if (item == "Laravel"):
            await Laravel(app, dir)

        #if (item == "Name"):
            #await Name(app, dir)

        # ...
    else:
        print("No current window")
iterm2.run_until_complete(main)