#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.2),
    on January 18, 2019, at 11:56
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
from matplotlib import colors
import os  # handy system and path functions
import sys  # to get file system encoding

class CorsiParameters:
    experimentName = "Corsi_Blocks"
    outputFolder = "data"
    scaleToFullscreen = False
    maxWidth = 2560
    maxHeight = 1440
    width = 255
    height = 205
    scaleWidth = 1.0
    blockSize = 30
    blockSizeFractionBool = False
    stayClicked = False
    colourBlock = (1.0,1.0,1.0)
    colourBlockMarked = (1.0,0,0)
    colourBlockClicked = (0.5,0.5,0.5)
    colourBackground = (0,0,0)

    durationFlash = 1.0
    durationFlashFinal = 1.0
    durationDelayBeforeStart = 2.0
    durationDelayAfterSequence = 1.0
    durationTimer = 10.0
    
    blocksNumber = 9
    blocksNumberMaxUsed = 9
    showSequenceBlocksOnly = False
    failureChance = 2
    firstSequenceLength = 2
    sequentialLengthIncrease = True

    blockLocationsX = []
    blockLocationsY = []
    sequencesData = []
    sequencesLength = []
    
    blockLocationsString = []
    sequencesDataString = []
    
    textSize = 30
    textColour = (1.0,1.0,1.0)
    textDirection = 'LTR'
    textImagesBool = False
    sessionString = "2) Session"
    participantString = "1) Participant Name"
    genderString = "3) Gender"
    ageString = "4) Age"
    nextString = "Next sequence"
    repetitionString = "+"
    introString = "On each trial, watch the sequence of squares flashing red. When the sequence finishes try to click the same sequence.\n\nWhen you've made the same number of clicks as the original sequence the next trial will start.\n\nTo make it easier squares will change color after you click them\n\nPress any key to get started"

    def __init__(self):
        self.experimentName = "Corsi_Blocks"
        self.outputFolder = "data"
        self.scaleToFullscreen = True
        self.maxWidth = 2560
        self.maxHeight = 1440
        self.width = 255
        self.height = 205
        self.scaleWidth = 1.0
        self.blockSize = 30
        self.blockSizeFractionBool = False
        self.stayClicked = False
        self.colourBlock = (1.0,1.0,1.0)
        self.colourBlockMarked = (1.0,0,0)
        self.colourBlockClicked = (0.5,0.5,0.5)
        self.colourBackground = (0,0,0)

        self.blocksNumber = 9
        self.showSequenceBlocksOnly = False
        self.failureChance = 2
        self.firstSequenceLength = 2
        self.sequentialLengthIncrease = True

        self.durationFlash = 1.0
        self.durationFlashFinal = 1.0
        self.durationDelayBeforeStart = 2.0
        self.durationDelayAfterSequence = 1.0
        self.durationTimer = 10.0

        self.blockLocationsX = []
        self.blockLocationsY = []
        self.sequencesData = []
        self.sequencesLength = []
        
        self.blockLocationsString = []
        self.sequencesDataString = []

        self.blockLocationsString.append("130,155")
        self.blockLocationsString.append("30,145")
        self.blockLocationsString.append("180,120")
        self.blockLocationsString.append("70,110")
        self.blockLocationsString.append("140,90")
        self.blockLocationsString.append("195,60")
        self.blockLocationsString.append("15,50")
        self.blockLocationsString.append("75,20")
        self.blockLocationsString.append("135,30")

        self.sequencesDataString.append("5,3")
        self.sequencesDataString.append("4,9")
        self.sequencesDataString.append("8,2,4")
        self.sequencesDataString.append("6,2,7")
        self.sequencesDataString.append("9,1,6,2")
        self.sequencesDataString.append("3,1,8,5")
        self.sequencesDataString.append("7,2,4,8,1")
        self.sequencesDataString.append("6,3,5,9,4")
        self.sequencesDataString.append("9,2,6,7,3,8")
        self.sequencesDataString.append("8,7,3,4,1,6")
        self.sequencesDataString.append("7,9,6,2,5,4,1")
        self.sequencesDataString.append("5,4,2,7,1,8,3")
        self.sequencesDataString.append("5,4,9,6,4,1,3,7")
        self.sequencesDataString.append("9,1,3,8,5,2,4,7")
        self.sequencesDataString.append("3,9,7,6,2,8,1,4,5")
        self.sequencesDataString.append("1,8,7,4,3,9,5,2,6")
        self.sequencesDataString.append("4,9,8,2,1,7,6,4,5,3")
        self.sequencesDataString.append("5,7,3,1,2,9,8,4,2,6")
        self.sequencesDataString.append("8,1,8,2,3,9,7,4,6,5,2")
        self.sequencesDataString.append("2,8,5,3,9,6,7,6,2,4,9")
        self.sequencesDataString.append("9,7,8,1,7,3,4,8,2,6,5,9")
        self.sequencesDataString.append("8,4,9,1,2,8,7,6,3,7,1,5")
        self.sequencesDataString.append("2,9,1,4,9,8,4,3,5,7,6,7,5")
        self.sequencesDataString.append("6,9,8,3,2,8,5,1,4,9,2,7,3")
        self.sequencesDataString.append("6,3,9,1,7,2,7,3,6,2,4,8,1,5")
        self.sequencesDataString.append("2,9,4,1,3,7,8,5,8,7,2,6,1,9")
        self.sequencesDataString.append("1,2,8,5,3,9,4,2,6,1,3,8,4,5,7")
        self.sequencesDataString.append("3,1,8,5,6,2,4,2,3,1,9,8,6,7,4")

        self.textSize = 30
        self.textColour = (1.0,1.0,1.0)
        self.textDirection = 'LTR'
        self.textImagesBool = False
        self.sessionString = "2) Session"
        self.participantString = "1) Participant Name"
        self.genderString = "3) Gender"
        self.ageString = "4) Age"
        self.nextString = "Next sequence"
        self.repetitionString = "+"
        self.introString = "On each trial, watch the sequence of squares flashing red. When the sequence finishes try to click the same sequence.\n\nWhen you've made the same number of clicks as the original sequence the next trial will start.\n\nTo make it easier squares will change color after you click them\n\nPress any key to get started"

        self.blocksStringToCoordinates()
        self.sequenceStringToSequence()


    def blocksStringToCoordinates(self):
        self.blocksNumber = 0
        self.blockLocationsX = []
        self.blockLocationsY = []
        xArr = []
        yArr = []
        for l in self.blockLocationsString:
            blocksStr = l.split(',')
            if len(blocksStr) > 1:
                xStr = blocksStr[0].strip()
                yStr = blocksStr[1].strip()
                if len(xStr) > 0 and len(yStr) > 0:
                    xStrCheck = 0
                    yStrCheck = 0
                    if xStr[0] == '+' or xStr[0] == '-':
                        xStrCheck = 1
                    if yStr[0] == '+' or yStr[0] == '-':
                        yStrCheck = 1
                    if (xStr[xStrCheck:]).replace('.','',1).isdigit() and (yStr[yStrCheck:]).replace('.','',1).isdigit():
                        xArr.append(float(xStr))
                        yArr.append(float(yStr))
                        self.blocksNumber = self.blocksNumber + 1
        if self.blocksNumber > 0:
            minX = min(xArr)
            maxX = max(xArr)
            minY = min(yArr)
            maxY = max(yArr)
            xOffset = (minX + maxX) / 2
            yOffset = (minY + maxY) / 2
            for i in range(self.blocksNumber):
                self.blockLocationsX.append(xArr[i] - xOffset)
                self.blockLocationsY.append(yArr[i] - yOffset)

    def sequenceStringToSequence(self):
        self.sequencesData = []
        self.sequencesLength = []
        self.sequencesOrder = []
        i = 0
        for l in self.sequencesDataString:
            sequenceStr = l.split(',')
            if len(sequenceStr) > 0:
                currentSequence = []
                for s in sequenceStr:
                    sStripped = s.strip()
                    if len(sStripped) > 0:
                        if sStripped.isdigit():
                            sInt = int(sStripped)
                            if sInt > 0 and sInt < self.blocksNumber + 1:
                                currentSequence.append(sInt - 1)
                if len(currentSequence) > 0:
                    self.sequencesLength.append(len(currentSequence))
                    self.sequencesData.append(currentSequence)
                    self.sequencesOrder.append(i)
                    i = i + 1
        if self.sequentialLengthIncrease:
            i = 0
            while i < len(self.sequencesOrder) - 1:
                if self.sequencesLength[self.sequencesOrder[i+1]] < self.sequencesLength[self.sequencesOrder[i]]:
                    iTemp = self.sequencesOrder[i+1]
                    self.sequencesOrder[i+1] = self.sequencesOrder[i]
                    self.sequencesOrder[i] = iTemp
                    if i > 0:
                        i = i - 1
                else:
                    i = i + 1
        
                
            

def ReadParametersFile(paramFile):
    paramsVar = CorsiParameters()
    paramLines = []

    if os.path.isfile(paramFile):
        with open(paramFile) as f:
            paramLines = f.read()
        paramLines = paramLines.split("\n")
        i = 0
        while i < len(paramLines) - 1:
            paramLineBool = False
            if len(paramLines[i]) > 0:
                paramLineBool = paramLines[i][0] == '='
            if paramLineBool:
                currentLine = (paramLines[i]).lower()
                contBool = True
                if contBool and  "= output data folder".lower() in currentLine:
                    paramsVar.outputFolder = paramLines[i+1]
                    i = i + 1
                    contBool = False
                if contBool and "= experiment name".lower() in currentLine:
                    paramsVar.experimentName = paramLines[i+1]
                    i = i + 1
                    contBool = False
                if contBool and "= scale to fullscreen size".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    currentB = True
                    if len(currentLine) > 0:
                        if currentLine[0] == 'f' or currentLine[0] == '0':
                            currentB = False
                    else:
                        currentB = False
                    paramsVar.scaleToFullscreen = currentB
                    i = i + 1
                    contBool = False
                if contBool and "= screen width".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    if(currentLine.isdigit()):
                        paramsVar.width = int(currentLine)
                    i = i + 1
                    contBool = False
                if contBool and "= screen height".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    if(currentLine.isdigit()):
                        paramsVar.height = int(currentLine)
                    i = i + 1
                    contBool = False
                if contBool and "= size of block".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    if(currentLine.replace('.','',1).isdigit()):
                        paramsVar.blockSize = float(currentLine)
                    i = i + 1
                    contBool = False
                if contBool and "= size is fraction of screen width".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    currentB = True
                    if len(currentLine) > 0:
                        if currentLine[0] == 'f' or currentLine[0] == '0':
                            currentB = False
                    else:
                        currentB = False
                    paramsVar.blockSizeFractionBool = currentB
                    i = i + 1
                    contBool = False
                if contBool and "= clicked blocks stay coloured".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    currentB = True
                    if len(currentLine) > 0:
                        if currentLine[0] == 'f' or currentLine[0] == '0':
                            currentB = False
                    else:
                        currentB = False
                    paramsVar.stayClicked = currentB
                    i = i + 1
                    contBool = False
                if contBool and "= block colour R,G,B".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    currentSplit = currentLine.split(',')
                    if len(currentSplit) > 2:
                        rText = currentSplit[0].strip()
                        gText = currentSplit[1].strip()
                        bText = currentSplit[2].strip()
                        if(rText.replace('.','',1).isdigit() and gText.replace('.','',1).isdigit() and bText.replace('.','',1).isdigit()):
                            currentRed = float(rText)
                            currentGre = float(gText)
                            currentBlu = float(bText)
                            if currentRed > 1 or currentGre > 1 or currentBlu > 1:
                                currentRed = ((1.0*currentRed) % 255) / 255.0
                                currentGre = ((1.0*currentGre) % 255) / 255.0
                                currentBlu = ((1.0*currentBlu) % 255) / 255.0
                            paramsVar.colourBlock = (currentRed , currentGre , currentBlu)
                        else:
                            if colors.is_color_like(currentLine):
                                rgbaArr = colors.to_rgba(currentLine)
                                paramsVar.colourBlock = (rgbaArr[0] , rgbaArr[1] , rgbaArr[2])
                    i = i + 1
                    contBool = False
                if contBool and "= marked block colour R,G,B".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    currentSplit = currentLine.split(',')
                    if len(currentSplit) > 2:
                        rText = currentSplit[0].strip()
                        gText = currentSplit[1].strip()
                        bText = currentSplit[2].strip()
                        if(rText.replace('.','',1).isdigit() and gText.replace('.','',1).isdigit() and bText.replace('.','',1).isdigit()):
                            currentRed = float(rText)
                            currentGre = float(gText)
                            currentBlu = float(bText)
                            if currentRed > 1 or currentGre > 1 or currentBlu > 1:
                                currentRed = ((1.0*currentRed) % 255) / 255.0
                                currentGre = ((1.0*currentGre) % 255) / 255.0
                                currentBlu = ((1.0*currentBlu) % 255) / 255.0
                                paramsVar.colourBlockMarked = (currentRed , currentGre , currentBlu)
                        else:
                            if colors.is_color_like(currentLine):
                                rgbaArr = colors.to_rgba(currentLine)
                                paramsVar.colourBlockMarked = (rgbaArr[0] , rgbaArr[1] , rgbaArr[2])
                    i = i + 1
                    contBool = False
                if contBool and "= clicked block colour R,G,B".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    currentSplit = currentLine.split(',')
                    if len(currentSplit) > 2:
                        rText = currentSplit[0].strip()
                        gText = currentSplit[1].strip()
                        bText = currentSplit[2].strip()
                        if(rText.replace('.','',1).isdigit() and gText.replace('.','',1).isdigit() and bText.replace('.','',1).isdigit()):
                            currentRed = float(rText)
                            currentGre = float(gText)
                            currentBlu = float(bText)
                            if currentRed > 1 or currentGre > 1 or currentBlu > 1:
                                currentRed = ((1.0*currentRed) % 255) / 255.0
                                currentGre = ((1.0*currentGre) % 255) / 255.0
                                currentBlu = ((1.0*currentBlu) % 255) / 255.0
                                paramsVar.colourBlockClicked = (currentRed , currentGre , currentBlu)
                        else:
                            if colors.is_color_like(currentLine):
                                rgbaArr = colors.to_rgba(currentLine)
                                paramsVar.colourBlockClicked = (rgbaArr[0] , rgbaArr[1] , rgbaArr[2])
                    i = i + 1
                    contBool = False
                if contBool and "= background colour R,G,B".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    currentSplit = currentLine.split(',')
                    if len(currentSplit) > 2:
                        rText = currentSplit[0].strip()
                        gText = currentSplit[1].strip()
                        bText = currentSplit[2].strip()
                        if(rText.replace('.','',1).isdigit() and gText.replace('.','',1).isdigit() and bText.replace('.','',1).isdigit()):
                            currentRed = float(rText)
                            currentGre = float(gText)
                            currentBlu = float(bText)
                            if currentRed > 1 or currentGre > 1 or currentBlu > 1:
                                currentRed = ((1.0*currentRed) % 255) / 255.0
                                currentGre = ((1.0*currentGre) % 255) / 255.0
                                currentBlu = ((1.0*currentBlu) % 255) / 255.0
                            paramsVar.colourBackground = (currentRed , currentGre , currentBlu)
                        else:
                            if colors.is_color_like(currentLine):
                                rgbaArr = colors.to_rgba(currentLine)
                                paramsVar.colourBackground = (rgbaArr[0] , rgbaArr[1] , rgbaArr[2])
                    i = i + 1
                    contBool = False
                    
                if contBool and "= duration block flashes".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    if(currentLine.replace('.','',1).isdigit()):
                        currentFloat = float(currentLine)
                        paramsVar.durationFlash = currentFloat
                    i = i + 1
                    contBool = False
                if contBool and "= duration final block flashes".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    if(currentLine.replace('.','',1).isdigit()):
                        currentFloat = float(currentLine)
                        paramsVar.durationFlashFinal = currentFloat
                    i = i + 1
                    contBool = False
                if contBool and "= delay before start".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    if(currentLine.replace('.','',1).isdigit()):
                        currentFloat = float(currentLine)
                        paramsVar.durationDelayBeforeStart = currentFloat
                    i = i + 1
                    contBool = False
                if contBool and "= delay after sequence ends".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    if(currentLine.replace('.','',1).isdigit()):
                        currentFloat = float(currentLine)
                        paramsVar.durationDelayAfterSequence = currentFloat
                    i = i + 1
                    contBool = False
                if contBool and "= sequence entry timer".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    if(currentLine.replace('.','',1).isdigit()):
                        currentFloat = float(currentLine)
                        paramsVar.durationTimer = currentFloat
                    i = i + 1
                    contBool = False
                if contBool and "= number of blocks".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    if(currentLine.isdigit()):
                        paramsVar.blocksNumber = int(currentLine)
                    i = i + 1
                    contBool = False
                if contBool and "= show only blocks used in sequence".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    currentB = True
                    if len(currentLine) > 0:
                        if currentLine[0] == 'f' or currentLine[0] == '0':
                            currentB = False
                    else:
                        currentB = False
                    paramsVar.showSequenceBlocksOnly = currentB
                    i = i + 1
                    contBool = False
                if contBool and "= chances at sequence before failure".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    if(currentLine.isdigit()):
                        paramsVar.failureChance = int(currentLine)
                    i = i + 1
                    contBool = False
                if contBool and "= start at sequence length".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    if(currentLine.isdigit()):
                        paramsVar.firstSequenceLength = int(currentLine)
                    i = i + 1
                    contBool = False
                if contBool and "= always increase sequence length".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    currentB = True
                    if len(currentLine) > 0:
                        if currentLine[0] == 'f' or currentLine[0] == '0':
                            currentB = False
                    else:
                        currentB = False
                    paramsVar.sequentialLengthIncrease = currentB
                    i = i + 1
                    contBool = False
                    
                if contBool and "= text colour".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    currentSplit = currentLine.split(',')
                    if len(currentSplit) > 2:
                        rText = currentSplit[0].strip()
                        gText = currentSplit[1].strip()
                        bText = currentSplit[2].strip()
                        if(rText.replace('.','',1).isdigit() and gText.replace('.','',1).isdigit() and bText.replace('.','',1).isdigit()):
                            currentRed = float(rText)
                            currentGre = float(gText)
                            currentBlu = float(bText)
                            if currentRed > 1 or currentGre > 1 or currentBlu > 1:
                                currentRed = ((1.0*currentRed) % 255) / 255.0
                                currentGre = ((1.0*currentGre) % 255) / 255.0
                                currentBlu = ((1.0*currentBlu) % 255) / 255.0
                            paramsVar.textColour = (currentRed , currentGre , currentBlu)
                        else:
                            if colors.is_color_like(currentLine):
                                rgbaArr = colors.to_rgba(currentLine)
                                paramsVar.textColour = (rgbaArr[0] , rgbaArr[1] , rgbaArr[2])
                    i = i + 1
                    contBool = False
                if contBool and "= text size".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    if(currentLine.isdigit()):
                        paramsVar.textSize = int(currentLine)
                    i = i + 1
                    contBool = False
                if contBool and "= text direction".lower() in currentLine:
                    paramsVar.textDirection = paramLines[i+1].strip()
                    i = i + 1
                    contBool = False
                if contBool and "= text images".lower() in currentLine:
                    currentLine = paramLines[i+1].lower().strip()
                    currentB = True
                    if len(currentLine) > 0:
                        if currentLine[0] == 'f' or currentLine[0] == '0':
                            currentB = False
                    else:
                        currentB = False
                    i = i + 1
                    paramsVar.textImagesBool = currentB
                    contBool = False
                if contBool and "= user text".lower() in currentLine:
                    paramsVar.participantString = paramLines[i+1]
                    i = i + 1
                    contBool = False
                if contBool and "= session text".lower() in currentLine:
                    paramsVar.sessionString = paramLines[i+1]
                    i = i + 1
                    contBool = False
                if contBool and "= gender text".lower() in currentLine:
                    paramsVar.genderString = paramLines[i+1]
                    i = i + 1
                    contBool = False
                if contBool and "= age text".lower() in currentLine:
                    paramsVar.ageString = paramLines[i+1]
                    i = i + 1
                    contBool = False
                if contBool and "= next task text".lower() in currentLine:
                    currentString = paramLines[i+1]
                    i = i + 2
                    while i < len(paramLines) and contBool:
                        if len(paramLines[i]) > 0:
                            if paramLines[i][0] == '=':
                                contBool = False
                                i = i - 1
                            else:
                                currentString = currentString + '\n' + paramLines[i]
                                i = i + 1
                        else:
                            i = i + 1
                    paramsVar.nextString = currentString
                    contBool = False
                if contBool and "= repetition text".lower() in currentLine:
                    currentString = paramLines[i+1]
                    i = i + 2
                    while i < len(paramLines) and contBool:
                        if len(paramLines[i]) > 0:
                            if paramLines[i][0] == '=':
                                contBool = False
                                i = i - 1
                            else:
                                currentString = currentString + '\n' + paramLines[i]
                                i = i + 1
                        else:
                            i = i + 1
                    paramsVar.repetitionString = currentString
                    contBool = False
                if contBool and "= intro text".lower() in currentLine:
                    currentString = paramLines[i+1]
                    i = i + 2
                    while i < len(paramLines) and contBool:
                        if len(paramLines[i]) > 0:
                            if paramLines[i][0] == '=':
                                contBool = False
                                i = i - 1
                            else:
                                currentString = currentString + '\n' + paramLines[i]
                                i = i + 1
                        else:
                            currentString = currentString + '\n'
                            i = i + 1
                    paramsVar.introString = currentString
                    contBool = False
                    
                if contBool and "= block locations".lower() in currentLine:
                    paramsVar.blockLocationsString = []
                    i = i + 1
                    while i < len(paramLines) and contBool:
                        if len(paramLines[i]) > 0:
                            if paramLines[i][0] == '=':
                                contBool = False
                                i = i - 1
                            else:
                                paramsVar.blockLocationsString.append(paramLines[i])
                                i = i + 1
                        else:
                            i = i + 1
                    contBool = False
                if contBool and "= sequences".lower() in currentLine:
                    paramsVar.sequencesDataString = []
                    i = i + 1
                    while i < len(paramLines) and contBool:
                        if len(paramLines[i]) > 0:
                            if paramLines[i][0] == '=':
                                contBool = False
                                i = i - 1
                            else:
                                paramsVar.sequencesDataString.append(paramLines[i])
                                i = i + 1
                        else:
                            i = i + 1
                    contBool = False
                i = i + 1
            else:
                i = i + 1
        paramsVar.blocksStringToCoordinates()
        paramsVar.sequenceStringToSequence()
    else:
        paramFileStr = ""
        paramFileStr = paramFileStr + "\n" + "= output data folder"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.outputFolder)
        paramFileStr = paramFileStr + "\n" + "= experiment name"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.experimentName)
        paramFileStr = paramFileStr + "\n" + "\n Graphics\n"
        paramFileStr = paramFileStr + "\n" + "= scale to fullscreen size"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.scaleToFullscreen)
        paramFileStr = paramFileStr + "\n" + "= screen width"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.width)
        paramFileStr = paramFileStr + "\n" + "= screen height"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.height)
        paramFileStr = paramFileStr + "\n" + "= size of block"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.blockSize)
        paramFileStr = paramFileStr + "\n" + "= size is fraction of screen width"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.blockSizeFractionBool)
        paramFileStr = paramFileStr + "\n" + "= clicked blocks stay coloured"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.stayClicked)
        paramFileStr = paramFileStr + "\n" + "= block colour R,G,B"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.colourBlock[0]) + ', ' + str(paramsVar.colourBlock[1]) + ', ' + str(paramsVar.colourBlock[2])
        paramFileStr = paramFileStr + "\n" + "= marked block colour R,G,B"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.colourBlockMarked[0]) + ', ' + str(paramsVar.colourBlockMarked[1]) + ', ' + str(paramsVar.colourBlockMarked[2])
        paramFileStr = paramFileStr + "\n" + "= clicked block colour R,G,B"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.colourBlockClicked[0]) + ', ' + str(paramsVar.colourBlockClicked[1]) + ', ' + str(paramsVar.colourBlockClicked[2])
        paramFileStr = paramFileStr + "\n" + "= background colour R,G,B"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.colourBackground[0]) + ', ' + str(paramsVar.colourBackground[1]) + ', ' + str(paramsVar.colourBackground[2])
        paramFileStr = paramFileStr + "\n" + "\n Time Parameters in seconds\n"
        paramFileStr = paramFileStr + "\n" + "= duration block flashes"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.durationFlash)
        paramFileStr = paramFileStr + "\n" + "= duration final block flashes"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.durationFlashFinal)
        paramFileStr = paramFileStr + "\n" + "= delay before start"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.durationDelayBeforeStart)
        paramFileStr = paramFileStr + "\n" + "= delay after sequence ends"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.durationDelayAfterSequence)
        paramFileStr = paramFileStr + "\n" + "= sequence entry timer"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.durationTimer)
        paramFileStr = paramFileStr + "\n" + "\n Blocks Parameters\n"
        paramFileStr = paramFileStr + "\n" + "= number of blocks"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.blocksNumber)
        paramFileStr = paramFileStr + "\n" + "= show only blocks used in sequence"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.showSequenceBlocksOnly)
        paramFileStr = paramFileStr + "\n" + "= chances at sequence before failure"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.failureChance)
        paramFileStr = paramFileStr + "\n" + "= start at sequence length"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.firstSequenceLength)
        paramFileStr = paramFileStr + "\n" + "= always increase sequence length"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.sequentialLengthIncrease)
        paramFileStr = paramFileStr + "\n"
        paramFileStr = paramFileStr + "\n" + "= block locations"
        for l in paramsVar.blockLocationsString:
            paramFileStr = paramFileStr + "\n" + str(l)
        paramFileStr = paramFileStr + "\n"
        paramFileStr = paramFileStr + "\n" + "= sequences"
        for l in paramsVar.sequencesDataString:
            paramFileStr = paramFileStr + "\n" + str(l)
        paramFileStr = paramFileStr + "\n" + "\n Text Parameters\n"
        paramFileStr = paramFileStr + "\n" + "= text colour"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.textColour[0]) + ', ' + str(paramsVar.textColour[1]) + ', ' + str(paramsVar.textColour[2])
        paramFileStr = paramFileStr + "\n" + "= text size"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.textSize)
        paramFileStr = paramFileStr + "\n" + "= text direction"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.textDirection)
        paramFileStr = paramFileStr + "\n" + "= text images"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.textImagesBool)
        paramFileStr = paramFileStr + "\n"
        paramFileStr = paramFileStr + "\n" + "= user text"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.participantString)
        paramFileStr = paramFileStr + "\n" + "= session text"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.sessionString)
        paramFileStr = paramFileStr + "\n" + "= gender text"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.genderString)
        paramFileStr = paramFileStr + "\n" + "= age text"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.ageString)
        paramFileStr = paramFileStr + "\n"
        paramFileStr = paramFileStr + "\n" + "= next task text"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.nextString)
        paramFileStr = paramFileStr + "\n"
        paramFileStr = paramFileStr + "\n" + "= repetition text"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.repetitionString)
        paramFileStr = paramFileStr + "\n"
        paramFileStr = paramFileStr + "\n" + "= intro text"
        paramFileStr = paramFileStr + "\n" + str(paramsVar.introString)
        paramFileStr = paramFileStr + "\n" + ""
        text_file = open(paramFile, "w")
        text_file.write(paramFileStr)
        text_file.close()

    return paramsVar

def translateColourToPsychopy(colourArr):
    r = 2.0*colourArr[0] - 1.0
    g = 2.0*colourArr[1] - 1.0
    b = 2.0*colourArr[2] - 1.0
    return [r,g,b]

def Main():

    # Ensure that relative paths start from the same directory as this script

    paramFile = "CorsiFixedParameters.txt"
    params = ReadParametersFile(paramFile)

    # Store info about the experiment session
    psychopyVersion = '3.0.2'
    codeFileName = params.experimentName
    expName = 'CorsiBlocksFixed'  # from the Builder filename that created this script
    expInfo = {params.sessionString: '001', params.participantString: '', params.genderString: '', params.ageString: ''}
    dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName
    expInfo['psychopyVersion'] = psychopyVersion

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = params.outputFolder + os.sep + u'%s_%s_%s' % (expInfo[params.participantString], expName, expInfo['date'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath=codeFileName,
        savePickle=True, saveWideText=True,
        dataFileName=filename)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    endExpNow = False  # flag for 'escape' or other condition => quit the exp

    # Start Code - component code to be run before the window creation

    # Setup the Window
    win = visual.Window(
        size=[params.maxWidth, params.maxHeight], fullscr=True, screen=0,
        allowGUI=False,units='height', allowStencil=False,
        monitor='testMonitor', color=translateColourToPsychopy(params.colourBackground), colorSpace='rgb',
        blendMode='avg', useFBO=True)
    winWidth = win.size[0]
    winHeight = win.size[1]
    # store frame rate of monitor if we can measure it
    expInfo['frameRate'] = win.getActualFrameRate()
    if expInfo['frameRate'] != None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess

    # Initialize components for Routine "instructions"
    instructionsClock = core.Clock()
    ISIClock = core.Clock()
    if params.textImagesBool:
        text = visual.ImageStim(win=win, name='text',
                image=params.introString,
                units="pix"
            )
        fixCross = visual.ImageStim(win=win, name='fixCross',
                image=params.nextString,
                units="pix"
            )
        repString = visual.ImageStim(win=win, name='repString',
                image=params.repetitionString,
                units="pix"
            )
    else:
        text = visual.TextStim(win=win, name='text',
            text=params.introString,
            font='Arial',
            pos=(1, 0), height=(1.0*params.textSize)/winHeight, wrapWidth=None, ori=0, 
            color=translateColourToPsychopy(params.textColour), colorSpace='rgb', opacity=1, 
            languageStyle=params.textDirection,
            depth=0.0);
        # Initialize components for Routine "ISI"
        fixCross = visual.TextStim(win=win, name='fixCross',
            text=params.nextString,
            font='Arial',
            pos=(1, 0), height=(1.0*params.textSize)/winHeight, wrapWidth=None, ori=0, 
            color=translateColourToPsychopy(params.textColour), colorSpace='rgb', opacity=1, 
            languageStyle=params.textDirection,
            depth=0.0);
        repString = visual.TextStim(win=win, name='repString',
            text=params.repetitionString,
            font='Arial',
            pos=(0, 0), height=(1.0*params.textSize)/winHeight, wrapWidth=None, ori=0, 
            color=translateColourToPsychopy(params.textColour), colorSpace='rgb', opacity=1, 
            languageStyle=params.textDirection,
            depth=0.0);
    text.anchorHoriz = 'center'
    fixCross.anchorHoriz = 'center'
    repString.anchorHoriz = 'center'

    blockColour = translateColourToPsychopy(params.colourBlock)
    blockMark = translateColourToPsychopy(params.colourBlockMarked)
    blockClick = translateColourToPsychopy(params.colourBlockClicked)

    # Initialize components for Routine "trial"
    trialClock = core.Clock()
    winScale = (1.0*winWidth) / winHeight
    blocksArrX = []
    blocksArrY = []
    heightScale = (1.0*params.width) / params.height
    scaleFactor = 1.0
    if heightScale*scaleFactor > winScale:
        scaleFactor = (1.0*winScale)/heightScale
    if not params.scaleToFullscreen and params.height < winHeight*scaleFactor:
        scaleFactor = (1.0*params.height)/winHeight
    scaleFactorFull = (1.0*scaleFactor) / params.height
    for i in range(params.blocksNumber):
        xTemp = params.blockLocationsX[i]
        yTemp = params.blockLocationsY[i]
        if xTemp > params.width / 2:
            xTemp = params.width/2
        if xTemp < -params.width/2:
            xTemp = -params.width/2
        if yTemp > params.height / 2:
            yTemp = params.height/2
        if yTemp < -params.height/2:
            yTemp = -params.height/2
        blocksArrX.append(xTemp * scaleFactorFull)
        blocksArrY.append(yTemp * scaleFactorFull)
    blockSize = params.blockSize * scaleFactorFull
    if params.blockSizeFractionBool:
        if params.blockSize <= 1 and params.blockSize > 0:
            blockSize = params.blockSize

    blocksArr = []
    for i in range(params.blocksNumber):
        newBlock = visual.Rect(
        win=win, name=int(i+1),units='height', 
        width=blockSize, height=blockSize,
        ori=0, pos=(blocksArrX[i],blocksArrY[i]),
        lineWidth=1, lineColor=blockColour, lineColorSpace='rgb',
        fillColor=blockColour, fillColorSpace='rgb',
        opacity=1, depth=-i, interpolate=True)
        blocksArr.append(newBlock)
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()

    fS = params.firstSequenceLength
    if params.firstSequenceLength < min(params.sequencesLength):
        fS = min(params.sequencesLength)
    blockDuration = params.durationFlash
    trialNum = 0
    contCheck = True
    while contCheck and trialNum < len(params.sequencesLength):
        if params.sequencesLength[trialNum] == fS:
            contCheck = False
        else:
            trialNum = trialNum + 1
            
    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    # ------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    instructionsComponents = [text, key_resp_2]
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "instructions"-------
    quitBool = False
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            quitBool = True
            continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    if quitBool:
        return 1
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
    thisExp.nextEntry()
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    trialsList = []
    iTemp = trialNum
    while iTemp < len(params.sequencesLength):
        sequenceOrderString = "["
        jTemp = 0
        if jTemp < params.sequencesLength[iTemp]:
            sequenceOrderString = sequenceOrderString + "'" + str(params.sequencesData[iTemp][jTemp]+1)
            jTemp = 1
            while jTemp < params.sequencesLength[iTemp]:
                sequenceOrderString = sequenceOrderString + "', '" + str(params.sequencesData[iTemp][jTemp]+1)
                jTemp = jTemp + 1
            sequenceOrderString = sequenceOrderString + "'"
        sequenceOrderString = sequenceOrderString + "]"
        newTrial = {}
        newTrial['blockDuration'] = params.durationFlash
        newTrial['sequence'] = sequenceOrderString
        trialsList.append(newTrial)
        iTemp = iTemp + 1
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=trialsList,
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    incorrectCount = 0
    completeSequence = False
    iTemp = 0
    while trialNum < len(params.sequencesLength):
        thisTrial = trialsList[iTemp]
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)

        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        blockDuration = thisTrial['blockDuration']
        sequence = []
        sequence = thisTrial['sequence']
        
        # ------Prepare to start Routine "ISI"-------
        t = 0
        ISIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.600000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [fixCross]
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixCross* updates
            if t >= 0.0 and fixCross.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixCross.tStart = t
                fixCross.frameNStart = frameN  # exact frame index
                fixCross.setAutoDraw(True)
            frameRemains = 0.0 + 0.6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixCross.status == STARTED and t >= frameRemains:
                fixCross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        endRoutine = False
        endRoutineTime = 0
        startClickTime = 0
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        validClickBoolArr = []
        gotValidClick = False  # until a click is received
        # initial state
        blkIndex = 0
        nextSwitch = blockDuration
        doingResponse = False
        responseStringBool = False
        responseStringTime = 0
        currBlock = None
        clickedBlock = None
        prevBlock = None
        
        # store blocks as a dictionary (to switch between name/object)
        blocksUsed = []
        if params.showSequenceBlocksOnly:
            for i in range(len(blocksArr)):
                showBlockBool = False
                for j in params.sequencesData[trialNum]:
                    if i == j:
                        showBlockBool = True
                if showBlockBool:
                    blocksUsed.append(blocksArr[i])
        else:
            for i in range(len(blocksArr)):
                blocksUsed.append(blocksArr[i])
        trialComponents = []
        for blockTemp in blocksUsed:
            blockTemp.color=blockColour
            trialComponents.append(blockTemp)
        trialComponents.append(mouse)
        # keep track of which components have finished
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        if hasattr(repString, 'status'):
            repString.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        quitBool = False
        while continueRoutine and not quitBool:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            for blockTemp in blocksUsed:
                # *blk1* updates
                if t >= 0.0 and blockTemp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    blockTemp.tStart = t
                    blockTemp.frameNStart = frameN  # exact frame index
                    blockTemp.setAutoDraw(True)
            
            # *mouse* updates
            if t >= doingResponse and mouse.status == NOT_STARTED:
                # keep track of start time/frame for later
                mouse.tStart = t
                mouse.frameNStart = frameN  # exact frame index
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        prevBlock = clickedBlock
                        clickedBlock = None
                        if doingResponse:
                            for obj in blocksUsed:
                                if obj.contains(mouse):
                                    gotValidClick = True
                                    mouse.clicked_name.append(obj.name)
                                    clickedBlock = obj
                        validClickBoolArr.append(gotValidClick)
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
            if (not doingResponse and not responseStringBool) and (not endRoutine and t > nextSwitch):
                if currBlock is not None:
                    #reset color of current block
                    currBlock.color = blockColour

                # then change current block and make that red
                if blkIndex >= params.sequencesLength[trialNum]:
                    if params.durationDelayAfterSequence > 0:
                        responseStringBool = True
                        responseStringTime = t
                        for blockTemp in blocksUsed:
                            blockTemp.setAutoDraw(False)
                        repString.setAutoDraw(True)
                    else:
                        doingResponse = True  # no more blocks to show
                        startClickTime = t
                    currBlock = None
                else:
                    currBlockInt = params.sequencesData[trialNum][blkIndex]
                    currBlockName = str(currBlockInt + 1)
                    currBlock = blocksArr[currBlockInt]
                    currBlock.color = blockMark
            
                    # track time of this change
                    nextSwitch += blockDuration
                blkIndex += 1
            if (responseStringBool and not endRoutine) and t - responseStringTime > params.durationDelayAfterSequence:
                doingResponse = True
                responseStringBool = False
                startClickTime = t
                repString.setAutoDraw(False)
                for blockTemp in blocksUsed:
                    blockTemp.setAutoDraw(True)
                
            
            # all clicked?
            if not endRoutine and len(mouse.clicked_name) >= params.sequencesLength[trialNum]:
                endRoutine = True
                endRoutineTime = t
                doingResponse = False

            if endRoutine and t - endRoutineTime > params.durationFlashFinal:
                continueRoutine = False
            
            # update color of clicked
            if params.stayClicked:
                for blockName in mouse.clicked_name:
                    blocksArr[int(blockName) - 1].color = blockClick
            else:
                if prevBlock is not None:
                    prevBlock.color = blockColour
                if clickedBlock is not None:
                    clickedBlock.color = blockClick
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                quitBool = True

            if not quitBool:
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
##                if hasattr(repString, "status") and repString.status != FINISHED:
##                    continueRoutine = True
##                    break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        if hasattr(repString, "setAutoDraw"):
            repString.setAutoDraw(False)

        newSequence = []
        correctSequence = True
        for jTemp in range(len(mouse.clicked_name)):
            if int(mouse.clicked_name[jTemp]) - 1 != params.sequencesData[trialNum][jTemp]:
                correctSequence = False
            newSequence.append(params.sequencesData[trialNum][jTemp] + 1)
        # store data for trials (TrialHandler)
        trials.addData('mouse.x', mouse.x)
        trials.addData('mouse.y', mouse.y)
        trials.addData('mouse.leftButton', mouse.leftButton)
        trials.addData('mouse.midButton', mouse.midButton)
        trials.addData('mouse.rightButton', mouse.rightButton)
        trials.addData('mouse.time', mouse.time)
        trials.addData('mouse.clicked_name', mouse.clicked_name)
        trials.addData('startClickTime', startClickTime)
        trials.addData('correctSequence', str(newSequence))
        trials.addData('correctBool', correctSequence)
        trials.addData('clickedOnBlock', validClickBoolArr)
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

        sLen = params.sequencesLength[trialNum]
        iTemp = iTemp + 1
        trialNum = trialNum + 1
        if correctSequence:
            incorrectCount = 0
            if params.sequentialLengthIncrease:
                findOldTrial = True
                while findOldTrial and trialNum < len(params.sequencesLength):
                    if params.sequencesLength[trialNum] > sLen:
                        findOldTrial = False
                    else:
                        iTemp = iTemp + 1
                        trialNum = trialNum + 1
        else:
            incorrectCount = incorrectCount + 1
            if incorrectCount < params.failureChance:
                if params.sequentialLengthIncrease:
                    findOldTrial = trialNum > len(params.sequencesLength) - 1
                    if not findOldTrial:
                        findOldTrial = sLen < params.sequencesLength[trialNum]
                    if findOldTrial:
                        trialNum = trialNum - iTemp
                        iTemp = 0
                        while findOldTrial and trialNum < len(params.sequencesLength):
                            if sLen == params.sequencesLength[trialNum]:
                                findOldTrial = False
                            else:
                                iTemp = iTemp + 1
                                trialNum = trialNum + 1
            else:
                trialNum = len(params.sequencesLength)
        if quitBool:
            trialNum = len(params.sequencesLength)
        
    # completed 1 repeats of 'trials'


    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename+'.csv')
    thisExp.saveAsPickle(filename)
    logging.flush()
    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    win.close()
    core.quit()
    return(1)

if __name__ == "__main__":
    Main()
