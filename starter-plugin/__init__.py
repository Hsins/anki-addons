"""
Anki Add-on : Starter Plugin
Description :

Author      : H.-H. Peng (Hsins) <https://github.com/Hsins>
Contact     : hsinspeng@gmail.com
License     : MIT <https://opensource.org/licenses/MIT>
"""


# import the main window object (mw) from aqt
from aqt import mw

# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect

# import all of the Qt GUI library
from aqt.qt import *

config = mw.addonManager.getConfig(__name__)

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.
def testFunction() -> None:
    # get the number of cards in the current collection, which is stored in
    # the main window
    cardCount = mw.col.cardCount()

    # show a message box
    showInfo(f"Card count: {cardCount}")
    showInfo(f"var is {config['myvar']}")


# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
