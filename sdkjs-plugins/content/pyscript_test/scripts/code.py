from pyscript import window, document


def init():
    messageIE = "This plugin is not supported by IE"
    messageIncognito = "This plugin does not work in the browser's incognito mode. Please switch to normal mode."
    if "Chrome" in window.navigator.userAgent and "Google Inc" in window.navigator.vendor and not window.AscDesktopEditor:
        # check incognito mode only in chrome
        # unfortunately, we can't check for incognito mode in PyScript
        showFrame()
    elif "MSIE" in window.navigator.userAgent or "Trident" in window.navigator.userAgent:
        createMessage(messageIE)
    else:
        showFrame()


def createMessage(message):
    document.getElementById("iframe").style.display = "none"
    divMessage = document.getElementById("div_message")
    divMessage.style.display = "flex"
    divMessage.innerHTML = f"<p id='message' style='text-align:center; font-size:12pt;'>{message}</p>"
    divMessage.style.display = "block"


def showFrame():
    frame = document.getElementById("iframe")
    frame.src = "https://evgeny-nadymov.github.io/telegram-react/"
    frame.style.display = "block"


def button(id):
    window.Asc.plugin.executeCommand("close", "")


def onTranslate():
    elem = document.getElementById("message")
    if elem:
        elem.innerHTML = window.Asc.plugin.tr(elem.innerHTML)
