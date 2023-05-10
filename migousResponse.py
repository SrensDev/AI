import random

def randomString():
    messageList = [
        "Sorry, I don't understand.",
        "Sorry, I can't answer it right now."
    ]

    listCount = len(messageList)
    randomItem = random.randrange(listCount)

    return messageList[randomItem]