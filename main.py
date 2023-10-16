import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from MainUI import Ui_MainWindow

import os

import telebot

app = QApplication(sys.argv)

window = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(window)

window.show()

def getLines(textEdit):
    text = textEdit.toPlainText()

    lines = []
    
    for line in text.split("\n"):
        word = line.strip()
        if word:
            lines.append(word)

    return lines

def sendMessage():
    bot = telebot.TeleBot(ui.lineEdit.text())

    for l in getLines(ui.plainTextEdit):
        bot.send_message(l, ui.lineEdit_2.text())

ui.pushButton.clicked.connect(sendMessage)

# Start the event loop.
app.exec_()
