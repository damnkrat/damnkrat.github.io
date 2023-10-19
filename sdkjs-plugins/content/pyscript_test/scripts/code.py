import html

import js

import pyscript


def init():
    pyscript.Console().print("I am in Init")
    document.write("Method 1")
    js.document.write("Method 2")
    messageIE = "This plugin is not supported by IE"
    messageIncognito = "This plugin does not work in the browser's incognito mode. Please switch to normal mode."
    if "Chrome" in pyscript.window.navigator.userAgent and "Google Inc" in pyscript.window.navigator.vendor and not pyscript.window.AscDesktopEditor:
        # check incognito mode only in chrome
        # unfortunately, we can't check for incognito mode in PyScript
        pyscript.Console().print("I want to run 1")
        showFrame()
    elif "MSIE" in pyscript.window.navigator.userAgent or "Trident" in pyscript.window.navigator.userAgent:
        pyscript.Console().print("I want to run 2")
        createMessage(messageIE)
    else:
        pyscript.Console().print("I want to run 3")
        showFrame()


def createMessage(message):
    pyscript.document.getElementById("iframe").style.display = "none"
    divMessage = pyscript.document.getElementById("div_message")
    divMessage.style.display = "flex"
    divMessage.innerHTML = f"<p id='message' style='text-align:center; font-size:12pt;'>{message}</p>"
    divMessage.style.display = "block"


def showFrame():
    frame = pyscript.document.getElementById("iframe")
    frame.src = "https://evgeny-nadymov.github.io/telegram-react/"
    frame.style.display = "block"


def button(id):
    pyscript.window.Asc.plugin.executeCommand("close", "")


def onTranslate():
    elem = pyscript.document.getElementById("message")
    if elem:
        elem.innerHTML = pyscript.window.Asc.plugin.tr(elem.innerHTML)
