import json
import re
import migousResponse
import random

def loadJson(file):
    with open(file) as migousResponses:
        print('Welcome to Migous AI!')
        return json.load(migousResponses)
    
responseData = loadJson('intents.json')

def getResponse(inputString):
    splitMessage = re.split(r'\s+|[,;?!.-]\s*', inputString.lower())
    scoreList = []

    for response in responseData:
        responseScore = 0
        requiredScore = 0
        requiredWords = response['required']

        if requiredWords:
            for word in splitMessage:
                if word in requiredWords:
                    requiredScore += 1

        if requiredScore == len(requiredWords):
            for word in splitMessage:
                if word in response['patterns']:
                    responseScore += 1

        scoreList.append(responseScore)

    bestResponse = max(scoreList)
    responseIndex = scoreList.index(bestResponse)

    if inputString == '':
        return 'Please type something!'
    
    if inputString == response['patterns'][1]:
        print('Goodbye!')
        exit()
    
    if bestResponse != 0:
        return random.choice(responseData[responseIndex]['response'])
    
    return migousResponse.randomString()

while True:
    response = input('You: ')
    print('Migous: ', getResponse(response))