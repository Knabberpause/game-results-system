import termcolor
import os
from datetime import *
import datetime
import time
from tabulate import tabulate


commands = [
    ['-h', 'help'],
    ['cr score1-score2 player1-player2', 'create result'],
    ['fr date(dd-mm-yyyy', 'find result'],
    ['-q', 'quit application']
]



def WriteToFile(path:str, method:str, content:str, filename:str):
    wtfFile = open(path, method)
    if method == 'a':
        wtfReadForAppend = wtfFile.read()
        try:
            wtfTestFor3DArray = (eval(wtfReadForAppend))[0][0][0]
            wtfTestFor3DArrayVar = True
            wtf3DArrayTestResult = True
        except:
            wtf3DArrayTestResult = False
            wtfTestFor3DArrayVar = False
        if wtf3DArrayTestResult == False:
            wtf2dArrayWTFContent = [
                [eval(wtfReadForAppend)]
                [content]
            ]
        elif wtf3DArrayTestResult==True:
            wtf3DArrayWTFList = eval(wtfReadForAppend)
            (wtfReadForAppend).append(content)

        print('file appended')
    elif method == 'w':
        wtfFile.write(content)
        print('file created and written to')
        wtfFL = open('filelist.txt', 'a')
        wtfFL.write(f'\n {filename}')
    else:
        print('error')
    wtfFile.close()



def getFileList() -> list[str]:
    gflFile = open('filelist.txt', 'r')
    gflList = gflFile.read()
    gflFile.close()
    gflListReturn = gflList.split()

    return gflListReturn



def cr(syntax:str):
    crSplit = syntax.split()
    del crSplit[0]
    try:
        crScore = (crSplit[0]).split('-', -1)
        crPlayers = (crSplit[1]).split('-', -1)
    except:
        print('error')
    crAttribute = [crScore[0], crPlayers[0]], [crScore[1], crPlayers[1]]
    crDateTrueStatus = False
    while crDateTrueStatus == False:
        crDate:str = input('>param: date(dd-mm-yyyy)')
        crDateSplit = crDate.split('-', 3)
        try:
            crDateTest = datetime.datetime(int(crDateSplit[2]), int(crDateSplit[1]), int(crDateSplit[0]))
            crDateTrueStatus = True
            print('date accepted')
        except:
            print('error')
    
    crDataToWrite = [
        crAttribute[0],
        crAttribute[1],
        [crDate]
    ]
    print(crDataToWrite)
    crFilePath = f'database/{crDate}.txt'
    crFileNameValidationList = getFileList()
    if (f'{crDate}.txt') in crFileNameValidationList:
        WriteToFile(crFilePath, 'a', str(crDataToWrite), (f'{crDate}.txt'))
    else:
        WriteToFile(crFilePath, 'w', str(crDataToWrite), (f'{crDate}.txt'))



def fr(operation:str):
    frSyntax = operation.split()
    del frSyntax[0]
    frDate = frSyntax[0]
    frDateSplit = frDate.split('-')
    try:
        frDateTest = datetime.datetime(int(frDateSplit[2]), int(frDateSplit[1]), int(frDateSplit[0]))
        print('date accepted')
    except:
        print('date error')
    
    frGFL = getFileList()
    frDateFormatted = (f'{frDate}.txt')
    if frDateFormatted in frGFL:
        
        print('date correct')
        frFindFile = open((f'database/{frDate}.txt'), 'r')
        frFileFound = frFindFile.read()
        frFindFile.close()
        print(frFileFound)
        frFileManipulate = eval(frFileFound)
        frFileLength = frFileFound.split('\n', -1)
        if len(frFileLength) ==1:
            print(f'1 game found for {frDate}')
            print(frFileManipulate)
            del frFileManipulate[2]
            print(frFileManipulate)

            frDataToPrint = [
                [frFileManipulate[0][1], frFileManipulate[0][0]],
                [frFileManipulate[1][1], frFileManipulate[1][0]]
            ]
            frDataToPrintFormat = tabulate(frDataToPrint, headers=['Name', 'Score'])
            print(frDataToPrintFormat)
        elif len(frFileLength) != 1:
            print(f'{len(frFileLength)} games found for {frDate}')
            frTableHeadings = ['Name']
            frDataToPrint = [
                [frFileManipulate[0][0][1] ],
                [frFileManipulate[0][1][1] ]
            ]

            for i in range(0, (len(frFileLength))):
                print('length', (len(frFileLength)))
                print(i)
                frPlayer1 = frFileManipulate[0][0][1]
                frPlayer2 = frFileManipulate[0][1][1]
                frTableHeadings.append(f'Game {i+1}')
                frPlayer1Scores = []
                frPlayer2Scores = []
                
                for score in range(0, len(frFileLength)):
                    if frFileManipulate[i][score][1] == frPlayer1:
                        frPlayer1Scores.append(frFileManipulate[i][score][0])
                        print(frPlayer1)
                        print(frPlayer1Scores)
                    elif frFileManipulate[i][score][1] == frPlayer2:
                        frPlayer2Scores.append(frFileManipulate[i][score][0])
                        print(frPlayer2)
                        print(frPlayer2Scores)
                    else:
                        print('error')
                (frDataToPrint[0]).append(frPlayer1Scores[i])
                (frDataToPrint[1]).append(frPlayer2Scores[i])

            frData3DArrayToPrintFormat = tabulate(frDataToPrint, headers=frTableHeadings)
            print(frData3DArrayToPrintFormat)
        else:
            print('error')
    else:
        print('date incorrect')



keywords = ['-h', 'cr', 'fr', '-q']
runStatus=True
termcolor.cprint('Welcome to the Results CLI. Type command below or type -h for help', 'green')
while runStatus == True:
    command = input('>')
    if command == '-h':
        print(commands)
    else:
        keyword1 = (command.split())[0]

        if keyword1 == 'cr':
            cr(command)
        elif keyword1 == 'fr':
            fr(command)
        elif keyword1 == '-q':
            runStatus=False
            quit()
        else:
            print('Invalid Syntax')