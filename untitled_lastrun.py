#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on 一月 12, 2022, at 20:58
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import xlwt
import time
from decimal import *
from xlwt import Workbook

MenuClock = core.Clock()
ExperienceClock = core.Clock()
Finalend=2

book = Workbook(encoding='utf-8')
sheet1 = book.add_sheet('Sheet 1')
sheet1.write(0,0,"Active/Reflective")
sheet1.write(0,1,"Sensing/Intuitive")
sheet1.write(0,2,"Visual/Verbal")
sheet1.write(0,3,"Sequential/Globe")

sheet1.write(2,0,"Active")
sheet1.write(2,1,"Reflective")
sheet1.write(2,2,"Sensing")
sheet1.write(2,3,"Intuitive")
sheet1.write(2,4,"Visual")
sheet1.write(2,5,"Verbal")
sheet1.write(2,6,"Sequential")
sheet1.write(2,7,"Globe")

sheet1.write(4,0,"sum學習")
sheet1.write(4,1,"sum操作")
sheet1.write(4,2,"sum菜單")
sheet1.write(4,3,"sum大於")
sheet1.write(4,4,"sum小於")
sheet1.write(4,5,"sum影片")
sheet1.write(4,6,"sum教科書")

sheet1.write(6,0,"all學習")
sheet1.write(6,1,"all操作")
sheet1.write(6,2,"all菜單")
sheet1.write(6,3,"all大於")
sheet1.write(6,4,"all小於")


sheet1.write(8,0,"影片1-1")
sheet1.write(8,1,"影片1-2")
sheet1.write(8,2,"影片1-3")
sheet1.write(8,3,"影片1-4")
sheet1.write(8,4,"影片1-5")
sheet1.write(8,5,"影片1-6")

sheet1.write(8,7,"影片2-1")
sheet1.write(8,8,"影片2-2")
sheet1.write(8,9,"影片2-3")
sheet1.write(8,10,"影片2-4")
sheet1.write(8,11,"影片2-5")
sheet1.write(8,12,"影片2-6")
sheet1.write(8,13,"影片3-1")
sheet1.write(8,14,"影片3-2")
sheet1.write(8,15,"影片3-3")
sheet1.write(8,16,"影片3-4")
sheet1.write(8,17,"影片3-5")
sheet1.write(8,18,"影片3-6")
sheet1.write(8,19,"影片3-7")
sheet1.write(8,20,"影片4-1")
sheet1.write(8,21,"影片4-2")
sheet1.write(8,22,"影片4-3")
sheet1.write(8,23,"影片4-4")
sheet1.write(8,24,"Cookbook1")
sheet1.write(8,25,"Cookbook2")
sheet1.write(8,26,"Cookbook3")

sheet1.write(10,0,"改變行為數")
sheet1.write(10,1,"循序行為數")
sheet1.write(10,2,"enter次數")

sheet1.write(12,0,"總時長")
sheet1.write(12,1,"ALL時長")

sheet1.write(14,1,"ALL時間順序")

sheet1.write(16,0,"總blender/學習切換次數")
sheet1.write(16,1,"大於5次blender/學習切換次數")
sheet1.write(16,2,"小於5次blender/學習切換次數")
countenter=0
Time1=0
allsteptime=[]
Experiencetime=[]
Menutime=[]
AllWatchtime=[]
AllCookbook=[]
BlenderTime=[]
Max20=[]
Min20=[]

Cookbook1=[]
Cookbook2=[]
Cookbook3=[]

#1會清空
Watchtime1=[]
#111是影片1-2(第一個影片)
Watchtime111=[]
Watchtime2=[]
Watchtime3=[]
Watchtime4=[]
Watchtime5=[]
Watchtime6=[]
Watchtime7=[]
Watchtime8=[]
Watchtime9=[]
Watchtime10=[]
Watchtime11=[]
Watchtime12=[]
Watchtime13=[]
Watchtime14=[]
Watchtime15=[]
Watchtime16=[]
Watchtime17=[]
Watchtime18=[]
Watchtime19=[]
Watchtime20=[]
Watchtime21=[]
Watchtime22=[]
Watchtime23=[]
Watchtime24=[]

from psychopy import core

respClock = core.Clock()
BlenderClock = core.Clock()

fstart=0
from psychopy.constants import FINISHED, NOT_STARTED, PAUSED, PLAYING, STOPPED
from psychopy.constants import FINISHED, NOT_STARTED, PAUSED, PLAYING, STOPPED


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\TEST\\untitled_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "first"
firstClock = core.Clock()
firstbackgrand = visual.ImageStim(
    win=win,
    name='firstbackgrand', 
    image='介面 PNG\\\\初始畫面.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_29 = event.Mouse(win=win)
x, y = [None, None]
mouse_29.mouseClock = core.Clock()
exstart = visual.ImageStim(
    win=win,
    name='exstart', 
    image='介面 PNG\\\\開始探索按鈕.png', mask=None,
    ori=0.0, pos=(0.035,-0.4), size=(0.25,0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "taskgoal"
taskgoalClock = core.Clock()
introduce2 = visual.ImageStim(
    win=win,
    name='introduce2', 
    image='介面 PNG\\\\任務介紹2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
bintroduce3 = visual.ImageStim(
    win=win,
    name='bintroduce3', 
    image='介面 PNG\\\\任務介紹3.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
quickkey4 = visual.ImageStim(
    win=win,
    name='quickkey4', 
    image='介面 PNG\\\\任務介紹4.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
tostart=0
key_resp_18 = keyboard.Keyboard()
mouse_30 = event.Mouse(win=win)
x, y = [None, None]
mouse_30.mouseClock = core.Clock()
start4 = visual.ImageStim(
    win=win,
    name='start4', 
    image='介面 PNG\\\\開始實驗按鈕.png', mask=None,
    ori=0.0, pos=(0.7,-0.43), size=(0.28,0.17),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
goal1 = visual.ImageStim(
    win=win,
    name='goal1', 
    image='介面 PNG\\\\任務介紹1.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)

# Initialize components for Routine "totalmenu"
totalmenuClock = core.Clock()
key_menupath2_4 = keyboard.Keyboard()
countchange=[]
morefivechange=[]
lessfivechange=[]
mouse_18 = event.Mouse(win=win)
x, y = [None, None]
mouse_18.mouseClock = core.Clock()
key_resp_29 = keyboard.Keyboard()
TOTALMENU = visual.ImageStim(
    win=win,
    name='TOTALMENU', 
    image='介面 PNG\\\\封面.png', mask=None,
    ori=0.0, pos=(0,0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
nonono = visual.ImageStim(
    win=win,
    name='nonono', 
    image='介面 PNG\\\\End.png', mask=None,
    ori=0.0, pos=(-0.73,0.39), size=(0.25,0.17),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blendertotalmenu = visual.ImageStim(
    win=win,
    name='blendertotalmenu', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(0.01, -0.3), size=(1.7, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkeytotalmenu = visual.ImageStim(
    win=win,
    name='quickkeytotalmenu', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey = visual.ImageStim(
    win=win,
    name='blenderquickkey', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "menu3"
menu3Clock = core.Clock()
key_menupath2_2 = keyboard.Keyboard()
mouse_31 = event.Mouse(win=win)
x, y = [None, None]
mouse_31.mouseClock = core.Clock()
backmenu3 = visual.ImageStim(
    win=win,
    name='backmenu3', 
    image='介面 PNG\\\\彎曲.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
close2 = visual.ImageStim(
    win=win,
    name='close2', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
key_resp_30 = keyboard.Keyboard()
blendermenu3 = visual.ImageStim(
    win=win,
    name='blendermenu3', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(0.01, -0.15), size=(1.7, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkeymenu3 = visual.ImageStim(
    win=win,
    name='quickkeymenu3', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey3 = visual.ImageStim(
    win=win,
    name='blenderquickkey3', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video3_1"
video3_1Clock = core.Clock()
key_resp_19 = keyboard.Keyboard()
remembertimestamp31=[] 
change=0
countcontinue=0
mouse_19 = event.Mouse(win=win)
x, y = [None, None]
mouse_19.mouseClock = core.Clock()
backvideo31 = visual.ImageStim(
    win=win,
    name='backvideo31', 
    image='介面 PNG\\\\3.彎曲\\\\2.20秒少量快捷鍵字幕-手彎曲教學.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_19 = visual.MovieStim3(
    win=win, name='movie_19',
    noAudio = False,
    filename='影片\\\\彎曲教學\\\\2.少量快捷鍵字幕-20秒快速彎曲手指.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_19 = visual.ImageStim(
    win=win,
    name='closevideo_19', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender31 = visual.ImageStim(
    win=win,
    name='blender31', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey31 = visual.ImageStim(
    win=win,
    name='quickkey31', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey31 = visual.ImageStim(
    win=win,
    name='blenderquickkey31', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video3_2"
video3_2Clock = core.Clock()
key_resp_20 = keyboard.Keyboard()
remembertimestamp32=[] 
mouse_20 = event.Mouse(win=win)
x, y = [None, None]
mouse_20.mouseClock = core.Clock()
backvideo32 = visual.ImageStim(
    win=win,
    name='backvideo32', 
    image='介面 PNG\\\\3.彎曲\\\\3-3.機器人手+詳細快捷鍵字幕-手彎曲教學.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_20 = visual.MovieStim3(
    win=win, name='movie_20',
    noAudio = False,
    filename='影片\\\\彎曲教學\\\\3-3.機器人手+詳細快捷鍵字幕-手彎曲教學.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_20 = visual.ImageStim(
    win=win,
    name='closevideo_20', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.8,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender32 = visual.ImageStim(
    win=win,
    name='blender32', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey32 = visual.ImageStim(
    win=win,
    name='quickkey32', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey32 = visual.ImageStim(
    win=win,
    name='blenderquickkey32', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video3_3"
video3_3Clock = core.Clock()
key_resp_21 = keyboard.Keyboard()
remembertimestamp33=[] 

mouse_21 = event.Mouse(win=win)
x, y = [None, None]
mouse_21.mouseClock = core.Clock()
backvideo33 = visual.ImageStim(
    win=win,
    name='backvideo33', 
    image='介面 PNG\\\\3.彎曲\\\\4.只有骨架詳細快捷鍵字幕-手彎曲教學.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_21 = visual.MovieStim3(
    win=win, name='movie_21',
    noAudio = False,
    filename='影片\\\\彎曲教學\\\\4.只有骨架詳細快捷鍵字幕-手彎曲教學.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_21 = visual.ImageStim(
    win=win,
    name='closevideo_21', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender33 = visual.ImageStim(
    win=win,
    name='blender33', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey33 = visual.ImageStim(
    win=win,
    name='quickkey33', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey33 = visual.ImageStim(
    win=win,
    name='blenderquickkey33', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video3_4"
video3_4Clock = core.Clock()
key_resp_22 = keyboard.Keyboard()
remembertimestamp34=[] 
mouse_22 = event.Mouse(win=win)
x, y = [None, None]
mouse_22.mouseClock = core.Clock()
backvideo34 = visual.ImageStim(
    win=win,
    name='backvideo34', 
    image='介面 PNG\\\\3.彎曲\\\\5-3.無聲+操作快捷鍵-手彎曲教學.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_22 = visual.MovieStim3(
    win=win, name='movie_22',
    noAudio = True,
    filename='影片\\\\彎曲教學\\\\5-3.無聲+操作快捷鍵-手彎曲教學.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_22 = visual.ImageStim(
    win=win,
    name='closevideo_22', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender34 = visual.ImageStim(
    win=win,
    name='blender34', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey34 = visual.ImageStim(
    win=win,
    name='quickkey34', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey34 = visual.ImageStim(
    win=win,
    name='blenderquickkey34', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video3_5"
video3_5Clock = core.Clock()
key_resp_23 = keyboard.Keyboard()
remembertimestamp35=[] 
mouse_23 = event.Mouse(win=win)
x, y = [None, None]
mouse_23.mouseClock = core.Clock()
backvideo35 = visual.ImageStim(
    win=win,
    name='backvideo35', 
    image='介面 PNG\\\\3.彎曲\\\\6-3.詳細快捷鍵字幕-手彎曲教學.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_23 = visual.MovieStim3(
    win=win, name='movie_23',
    noAudio = False,
    filename='影片\\\\彎曲教學\\\\6-3.詳細快捷鍵字幕-手彎曲教學.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_23 = visual.ImageStim(
    win=win,
    name='closevideo_23', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender35 = visual.ImageStim(
    win=win,
    name='blender35', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey35 = visual.ImageStim(
    win=win,
    name='quickkey35', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey35 = visual.ImageStim(
    win=win,
    name='blenderquickkey35', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video3_6"
video3_6Clock = core.Clock()
key_resp_24 = keyboard.Keyboard()
remembertimestamp36=[] 
mouse_24 = event.Mouse(win=win)
x, y = [None, None]
mouse_24.mouseClock = core.Clock()
backvideo36 = visual.ImageStim(
    win=win,
    name='backvideo36', 
    image='介面 PNG\\\\3.彎曲\\\\7-3.卡通手+詳細快捷鍵字幕-手彎曲教學.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_24 = visual.MovieStim3(
    win=win, name='movie_24',
    noAudio = False,
    filename='影片\\\\彎曲教學\\\\7-3.卡通手+詳細快捷鍵字幕-手彎曲教學.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_24 = visual.ImageStim(
    win=win,
    name='closevideo_24', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender36 = visual.ImageStim(
    win=win,
    name='blender36', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey36 = visual.ImageStim(
    win=win,
    name='quickkey36', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey36 = visual.ImageStim(
    win=win,
    name='blenderquickkey36', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video3_7"
video3_7Clock = core.Clock()
key_resp_25 = keyboard.Keyboard()
remembertimestamp37=[] 
mouse_25 = event.Mouse(win=win)
x, y = [None, None]
mouse_25.mouseClock = core.Clock()
backvideo37 = visual.ImageStim(
    win=win,
    name='backvideo37', 
    image='介面 PNG\\\\3.彎曲\\\\8-3.木頭手+無字幕-手彎曲教學.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_25 = visual.MovieStim3(
    win=win, name='movie_25',
    noAudio = False,
    filename='影片\\\\彎曲教學\\\\8-3.木頭手+無字幕-手彎曲教學.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_25 = visual.ImageStim(
    win=win,
    name='closevideo_25', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender37 = visual.ImageStim(
    win=win,
    name='blender37', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey37 = visual.ImageStim(
    win=win,
    name='quickkey37', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey37 = visual.ImageStim(
    win=win,
    name='blenderquickkey37', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "cookbook3"
cookbook3Clock = core.Clock()
background_3 = visual.ImageStim(
    win=win,
    name='background_3', 
    image='介面 PNG\\\\3.彎曲\\\\1-3cookbook-手彎曲教學.png', mask=None,
    ori=0.0, pos=(0,0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_28 = event.Mouse(win=win)
x, y = [None, None]
mouse_28.mouseClock = core.Clock()
key_resp_28 = keyboard.Keyboard()
BOOK34 = visual.ImageStim(
    win=win,
    name='BOOK34', 
    image='CookBookPNG\\\\手彎曲4.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
BOOK33 = visual.ImageStim(
    win=win,
    name='BOOK33', 
    image='CookBookPNG\\\\手彎曲3.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
BOOK32 = visual.ImageStim(
    win=win,
    name='BOOK32', 
    image='CookBookPNG\\\\手彎曲2.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
BOOK35 = visual.ImageStim(
    win=win,
    name='BOOK35', 
    image='CookBookPNG\\\\手彎曲5.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
BOOK36 = visual.ImageStim(
    win=win,
    name='BOOK36', 
    image='CookBookPNG\\\\手彎曲6.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
BOOK37 = visual.ImageStim(
    win=win,
    name='BOOK37', 
    image='CookBookPNG\\\\手彎曲7.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
BOOK38 = visual.ImageStim(
    win=win,
    name='BOOK38', 
    image='CookBookPNG\\\\手彎曲8.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
BOOK31 = visual.ImageStim(
    win=win,
    name='BOOK31', 
    image='CookBookPNG\\\\手彎曲1.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
close_3 = visual.ImageStim(
    win=win,
    name='close_3', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
blender38 = visual.ImageStim(
    win=win,
    name='blender38', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.38), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
quickkey38 = visual.ImageStim(
    win=win,
    name='quickkey38', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
blenderquickkey38 = visual.ImageStim(
    win=win,
    name='blenderquickkey38', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)

# Initialize components for Routine "menu2"
menu2Clock = core.Clock()
key_menupath2_1 = keyboard.Keyboard()
mouse_32 = event.Mouse(win=win)
x, y = [None, None]
mouse_32.mouseClock = core.Clock()
backmenu2 = visual.ImageStim(
    win=win,
    name='backmenu2', 
    image='介面 PNG\\\\連接手.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
close4 = visual.ImageStim(
    win=win,
    name='close4', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
key_resp_31 = keyboard.Keyboard()
blendermenu2 = visual.ImageStim(
    win=win,
    name='blendermenu2', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(0.01, -0.15), size=(1.7, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkeymenu2 = visual.ImageStim(
    win=win,
    name='quickkeymenu2', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey2 = visual.ImageStim(
    win=win,
    name='blenderquickkey2', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video2_1"
video2_1Clock = core.Clock()
key_resp_12 = keyboard.Keyboard()
remembertimestamp21=[] 
mouse_12 = event.Mouse(win=win)
x, y = [None, None]
mouse_12.mouseClock = core.Clock()
backvideo21 = visual.ImageStim(
    win=win,
    name='backvideo21', 
    image='介面 PNG\\\\2.連接骨架\\\\3-2.機器人手+詳細快捷鍵字幕-連接骨架和手.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_12 = visual.MovieStim3(
    win=win, name='movie_12',
    noAudio = False,
    filename='影片\\\\連結骨架和手\\\\3-2.機器人手+詳細快捷鍵字幕-連接骨架和手.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_12 = visual.ImageStim(
    win=win,
    name='closevideo_12', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender21 = visual.ImageStim(
    win=win,
    name='blender21', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey21 = visual.ImageStim(
    win=win,
    name='quickkey21', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey21 = visual.ImageStim(
    win=win,
    name='blenderquickkey21', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video2_2"
video2_2Clock = core.Clock()
key_resp_13 = keyboard.Keyboard()
remembertimestamp22=[] 
mouse_13 = event.Mouse(win=win)
x, y = [None, None]
mouse_13.mouseClock = core.Clock()
backvideo22 = visual.ImageStim(
    win=win,
    name='backvideo22', 
    image='介面 PNG\\\\2.連接骨架\\\\5-2.無聲+操作快捷鍵-連接骨架和手.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_13 = visual.MovieStim3(
    win=win, name='movie_13',
    noAudio = True,
    filename='影片\\\\連結骨架和手\\\\5-2.無聲+操作快捷鍵-連接骨架和手.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_13 = visual.ImageStim(
    win=win,
    name='closevideo_13', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender22 = visual.ImageStim(
    win=win,
    name='blender22', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey22 = visual.ImageStim(
    win=win,
    name='quickkey22', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey22 = visual.ImageStim(
    win=win,
    name='blenderquickkey22', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video2_3"
video2_3Clock = core.Clock()
key_resp_14 = keyboard.Keyboard()
remembertimestamp23=[] 
mouse_14 = event.Mouse(win=win)
x, y = [None, None]
mouse_14.mouseClock = core.Clock()
backvideo23 = visual.ImageStim(
    win=win,
    name='backvideo23', 
    image='介面 PNG\\\\2.連接骨架\\\\6-2.詳細快捷鍵字幕-連接骨架和手.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_14 = visual.MovieStim3(
    win=win, name='movie_14',
    noAudio = False,
    filename='影片\\\\連結骨架和手\\\\6-2.詳細快捷鍵字幕-連接骨架和手.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_14 = visual.ImageStim(
    win=win,
    name='closevideo_14', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender23 = visual.ImageStim(
    win=win,
    name='blender23', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey23 = visual.ImageStim(
    win=win,
    name='quickkey23', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey23 = visual.ImageStim(
    win=win,
    name='blenderquickkey23', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video2_4"
video2_4Clock = core.Clock()
key_resp_15 = keyboard.Keyboard()
remembertimestamp24=[] 
mouse_15 = event.Mouse(win=win)
x, y = [None, None]
mouse_15.mouseClock = core.Clock()
backvideo24 = visual.ImageStim(
    win=win,
    name='backvideo24', 
    image='介面 PNG\\\\2.連接骨架\\\\7-2.卡通手+詳細快捷鍵字幕-連接骨架和手.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_15 = visual.MovieStim3(
    win=win, name='movie_15',
    noAudio = False,
    filename='影片\\\\連結骨架和手\\\\7-2.卡通手+詳細快捷鍵字幕-連接骨架和手.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_15 = visual.ImageStim(
    win=win,
    name='closevideo_15', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender24 = visual.ImageStim(
    win=win,
    name='blender24', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey24 = visual.ImageStim(
    win=win,
    name='quickkey24', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey24 = visual.ImageStim(
    win=win,
    name='blenderquickkey24', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video2_5"
video2_5Clock = core.Clock()
key_resp_16 = keyboard.Keyboard()
remembertimestamp25=[] 
mouse_16 = event.Mouse(win=win)
x, y = [None, None]
mouse_16.mouseClock = core.Clock()
backvideo25 = visual.ImageStim(
    win=win,
    name='backvideo25', 
    image='介面 PNG\\\\2.連接骨架\\\\8-2.木頭手+無字幕-連接骨架和手.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_16 = visual.MovieStim3(
    win=win, name='movie_16',
    noAudio = False,
    filename='影片\\\\連結骨架和手\\\\8-2.木頭手+無字幕-連接骨架和手.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_16 = visual.ImageStim(
    win=win,
    name='closevideo_16', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender25 = visual.ImageStim(
    win=win,
    name='blender25', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey25 = visual.ImageStim(
    win=win,
    name='quickkey25', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey25 = visual.ImageStim(
    win=win,
    name='blenderquickkey25', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video2_6"
video2_6Clock = core.Clock()
key_resp_17 = keyboard.Keyboard()
remembertimestamp26=[] 
mouse_17 = event.Mouse(win=win)
x, y = [None, None]
mouse_17.mouseClock = core.Clock()
backvideo26 = visual.ImageStim(
    win=win,
    name='backvideo26', 
    image='介面 PNG\\\\2.連接骨架\\\\9.無字幕-連接骨架和手.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_17 = visual.MovieStim3(
    win=win, name='movie_17',
    noAudio = False,
    filename='影片\\\\連結骨架和手\\\\9.無字幕-連接骨架和手.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_17 = visual.ImageStim(
    win=win,
    name='closevideo_17', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender26 = visual.ImageStim(
    win=win,
    name='blender26', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey26 = visual.ImageStim(
    win=win,
    name='quickkey26', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey26 = visual.ImageStim(
    win=win,
    name='blenderquickkey26', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "cookbook2"
cookbook2Clock = core.Clock()
background_2 = visual.ImageStim(
    win=win,
    name='background_2', 
    image='介面 PNG\\\\2.連接骨架\\\\1-2cookbook-連接骨架和手.png', mask=None,
    ori=0.0, pos=(0,0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
close_2 = visual.ImageStim(
    win=win,
    name='close_2', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_27 = event.Mouse(win=win)
x, y = [None, None]
mouse_27.mouseClock = core.Clock()
key_resp_27 = keyboard.Keyboard()
BOOK21 = visual.ImageStim(
    win=win,
    name='BOOK21', 
    image='CookBookPNG\\\\連結骨架.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
blender27 = visual.ImageStim(
    win=win,
    name='blender27', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.38), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey27 = visual.ImageStim(
    win=win,
    name='quickkey27', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey27 = visual.ImageStim(
    win=win,
    name='blenderquickkey27', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "menu1"
menu1Clock = core.Clock()
key_menupath1 = keyboard.Keyboard()
mouse_33 = event.Mouse(win=win)
x, y = [None, None]
mouse_33.mouseClock = core.Clock()
backmenu = visual.ImageStim(
    win=win,
    name='backmenu', 
    image='介面 PNG\\\\骨架建立.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
close3 = visual.ImageStim(
    win=win,
    name='close3', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
key_resp_32 = keyboard.Keyboard()
blendermenu1 = visual.ImageStim(
    win=win,
    name='blendermenu1', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(0.01, -0.15), size=(1.7, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkeymenu1 = visual.ImageStim(
    win=win,
    name='quickkeymenu1', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey1 = visual.ImageStim(
    win=win,
    name='blenderquickkey1', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video1_1"
video1_1Clock = core.Clock()
key_resp_5 = keyboard.Keyboard()
remembertimestamp11=[] 

mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()
backvideo11 = visual.ImageStim(
    win=win,
    name='backvideo11', 
    image='介面 PNG\\\\1.建骨架\\\\3-1.機器人手+詳細快捷鍵字幕-手骨架建立教學.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_5 = visual.MovieStim3(
    win=win, name='movie_5',
    noAudio = False,
    filename='影片\\\\骨架建立教學\\\\3-1.機器人手+詳細快捷鍵字幕-手骨架建立教學.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_5 = visual.ImageStim(
    win=win,
    name='closevideo_5', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender11 = visual.ImageStim(
    win=win,
    name='blender11', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey11 = visual.ImageStim(
    win=win,
    name='quickkey11', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey11 = visual.ImageStim(
    win=win,
    name='blenderquickkey11', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video1_2"
video1_2Clock = core.Clock()
key_resp_6 = keyboard.Keyboard()
remembertimestamp12=[] 
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()
backvideo12 = visual.ImageStim(
    win=win,
    name='backvideo12', 
    image='介面 PNG\\\\1.建骨架\\\\5-1.無聲+操作快捷鍵-手骨架建立教學.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_6 = visual.MovieStim3(
    win=win, name='movie_6',
    noAudio = True,
    filename='影片\\\\骨架建立教學\\\\5-1.無聲+操作快捷鍵-手骨架建立教學.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_6 = visual.ImageStim(
    win=win,
    name='closevideo_6', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender12 = visual.ImageStim(
    win=win,
    name='blender12', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey12 = visual.ImageStim(
    win=win,
    name='quickkey12', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey12 = visual.ImageStim(
    win=win,
    name='blenderquickkey12', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video1_3"
video1_3Clock = core.Clock()
key_resp_7 = keyboard.Keyboard()
remembertimestamp13=[] 
mouse_7 = event.Mouse(win=win)
x, y = [None, None]
mouse_7.mouseClock = core.Clock()
backvideo13 = visual.ImageStim(
    win=win,
    name='backvideo13', 
    image='介面 PNG\\\\1.建骨架\\\\6-1.詳細快捷鍵字幕-手骨架建立教學.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_7 = visual.MovieStim3(
    win=win, name='movie_7',
    noAudio = False,
    filename='影片\\\\骨架建立教學\\\\6-1.詳細快捷鍵字幕-手骨架建立教學.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_7 = visual.ImageStim(
    win=win,
    name='closevideo_7', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender13 = visual.ImageStim(
    win=win,
    name='blender13', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey13 = visual.ImageStim(
    win=win,
    name='quickkey13', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey13 = visual.ImageStim(
    win=win,
    name='blenderquickkey13', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video1_4"
video1_4Clock = core.Clock()
key_resp_8 = keyboard.Keyboard()
remembertimestamp14=[] 
mouse_8 = event.Mouse(win=win)
x, y = [None, None]
mouse_8.mouseClock = core.Clock()
backvideo14 = visual.ImageStim(
    win=win,
    name='backvideo14', 
    image='介面 PNG\\\\1.建骨架\\\\7-1.卡通手+詳細快捷鍵字幕-手骨架建立教學.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_8 = visual.MovieStim3(
    win=win, name='movie_8',
    noAudio = False,
    filename='影片\\\\骨架建立教學\\\\7-1.卡通手+詳細快捷鍵字幕-手骨架建立教學.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_8 = visual.ImageStim(
    win=win,
    name='closevideo_8', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender14 = visual.ImageStim(
    win=win,
    name='blender14', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey14 = visual.ImageStim(
    win=win,
    name='quickkey14', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey14 = visual.ImageStim(
    win=win,
    name='blenderquickkey14', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video1_5"
video1_5Clock = core.Clock()
key_resp_9 = keyboard.Keyboard()
remembertimestamp15=[] 
mouse_9 = event.Mouse(win=win)
x, y = [None, None]
mouse_9.mouseClock = core.Clock()
backvideo15 = visual.ImageStim(
    win=win,
    name='backvideo15', 
    image='介面 PNG\\\\1.建骨架\\\\8-1.木頭手+無字幕-手骨架建立教學.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_9 = visual.MovieStim3(
    win=win, name='movie_9',
    noAudio = False,
    filename='影片\\\\骨架建立教學\\\\8-1.木頭手+無字幕-手骨架建立教學.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_9 = visual.ImageStim(
    win=win,
    name='closevideo_9', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender15 = visual.ImageStim(
    win=win,
    name='blender15', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey15 = visual.ImageStim(
    win=win,
    name='quickkey15', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey15 = visual.ImageStim(
    win=win,
    name='blenderquickkey15', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video1_6"
video1_6Clock = core.Clock()
key_resp_10 = keyboard.Keyboard()
remembertimestamp16=[] 
mouse_10 = event.Mouse(win=win)
x, y = [None, None]
mouse_10.mouseClock = core.Clock()
backvideo16 = visual.ImageStim(
    win=win,
    name='backvideo16', 
    image='介面 PNG\\\\1.建骨架\\\\11.無字幕-相似實作文字教科書骨架建立教學.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_10 = visual.MovieStim3(
    win=win, name='movie_10',
    noAudio = False,
    filename='影片\\\\骨架建立教學\\\\11.無字幕-相似實作文字教科書骨架建立教學.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_10 = visual.ImageStim(
    win=win,
    name='closevideo_10', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender16 = visual.ImageStim(
    win=win,
    name='blender16', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey16 = visual.ImageStim(
    win=win,
    name='quickkey16', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey16 = visual.ImageStim(
    win=win,
    name='blenderquickkey16', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "cookbook1"
cookbook1Clock = core.Clock()
background = visual.ImageStim(
    win=win,
    name='background', 
    image='介面 PNG\\\\1.建骨架\\\\1-1cookbook-手骨架建立教學.png', mask=None,
    ori=0.0, pos=(0,0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
close = visual.ImageStim(
    win=win,
    name='close', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_26 = event.Mouse(win=win)
x, y = [None, None]
mouse_26.mouseClock = core.Clock()
key_resp_26 = keyboard.Keyboard()
remembertimestamp18=[]
BOOK2 = visual.ImageStim(
    win=win,
    name='BOOK2', 
    image='CookBookPNG\\\\前言2.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
BOOK3 = visual.ImageStim(
    win=win,
    name='BOOK3', 
    image='CookBookPNG\\\\前言3.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
BOOK4 = visual.ImageStim(
    win=win,
    name='BOOK4', 
    image='CookBookPNG\\\\建骨架1.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
BOOK5 = visual.ImageStim(
    win=win,
    name='BOOK5', 
    image='CookBookPNG\\\\建骨架2.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
BOOK6 = visual.ImageStim(
    win=win,
    name='BOOK6', 
    image='CookBookPNG\\\\建骨架3.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
BOOK7 = visual.ImageStim(
    win=win,
    name='BOOK7', 
    image='CookBookPNG\\\\建骨架4.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
BOOK1 = visual.ImageStim(
    win=win,
    name='BOOK1', 
    image='CookBookPNG\\\\前言1.png', mask=None,
    ori=0.0, pos=(-0.25,-0.03), size=(1.2,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
blender18 = visual.ImageStim(
    win=win,
    name='blender18', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.38), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
quickkey18 = visual.ImageStim(
    win=win,
    name='quickkey18', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
blenderquickkey18 = visual.ImageStim(
    win=win,
    name='blenderquickkey18', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)

# Initialize components for Routine "menu5_1"
menu5_1Clock = core.Clock()
key_menupath2 = keyboard.Keyboard()
mouse_34 = event.Mouse(win=win)
x, y = [None, None]
mouse_34.mouseClock = core.Clock()
backmenu5 = visual.ImageStim(
    win=win,
    name='backmenu5', 
    image='介面 PNG\\\\完成品.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
close5 = visual.ImageStim(
    win=win,
    name='close5', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
key_resp_33 = keyboard.Keyboard()
blendermenu4 = visual.ImageStim(
    win=win,
    name='blendermenu4', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(0.01, -0.15), size=(1.7, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkeymenu4 = visual.ImageStim(
    win=win,
    name='quickkeymenu4', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey4 = visual.ImageStim(
    win=win,
    name='blenderquickkey4', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "VIDEO"
VIDEOClock = core.Clock()
key_resp = keyboard.Keyboard()
remembertimestamp=[] 
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
backvideo5 = visual.ImageStim(
    win=win,
    name='backvideo5', 
    image='介面 PNG\\\\4.成品\\\\12.成品-10秒靜止狀態骨架位置呈現.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie = visual.MovieStim3(
    win=win, name='movie',
    noAudio = False,
    filename='影片\\\\成品觀看\\\\12.成品-10秒靜止狀態骨架位置呈現.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo = visual.ImageStim(
    win=win,
    name='closevideo', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender41 = visual.ImageStim(
    win=win,
    name='blender41', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey41 = visual.ImageStim(
    win=win,
    name='quickkey41', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey41 = visual.ImageStim(
    win=win,
    name='blenderquickkey41', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video2"
video2Clock = core.Clock()
key_resp_2 = keyboard.Keyboard()
remembertimestamp2=[] 
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
backvideo52 = visual.ImageStim(
    win=win,
    name='backvideo52', 
    image='介面 PNG\\\\4.成品\\\\13.成品-15秒揮手彎曲動畫.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_2 = visual.MovieStim3(
    win=win, name='movie_2',
    noAudio = False,
    filename='影片\\\\成品觀看\\\\13.成品-15秒揮手彎曲動畫.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_2 = visual.ImageStim(
    win=win,
    name='closevideo_2', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender42 = visual.ImageStim(
    win=win,
    name='blender42', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey42 = visual.ImageStim(
    win=win,
    name='quickkey42', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey42 = visual.ImageStim(
    win=win,
    name='blenderquickkey42', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video3"
video3Clock = core.Clock()
key_resp_3 = keyboard.Keyboard()
remembertimestamp3=[] 
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
backvideo53 = visual.ImageStim(
    win=win,
    name='backvideo53', 
    image='介面 PNG\\\\4.成品\\\\14.成品-10秒握拳張開動畫.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_3 = visual.MovieStim3(
    win=win, name='movie_3',
    noAudio = False,
    filename='影片\\\\成品觀看\\\\14.成品-10秒握拳張開動畫.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_3 = visual.ImageStim(
    win=win,
    name='closevideo_3', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender43 = visual.ImageStim(
    win=win,
    name='blender43', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey43 = visual.ImageStim(
    win=win,
    name='quickkey43', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey43 = visual.ImageStim(
    win=win,
    name='blenderquickkey43', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "video4"
video4Clock = core.Clock()
key_resp_4 = keyboard.Keyboard()
remembertimestamp4=[] 
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()
backvideo = visual.ImageStim(
    win=win,
    name='backvideo', 
    image='介面 PNG\\\\4.成品\\\\15.成品-15秒手部彎曲操作展示.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
movie_4 = visual.MovieStim3(
    win=win, name='movie_4',
    noAudio = False,
    filename='影片\\\\成品觀看\\\\15.成品-15秒手部彎曲操作展示.mp4',
    ori=0.0, pos=(-250,-45), opacity=None,
    loop=True,
    size=(1280,768),
    depth=-4.0,
    )
closevideo_4 = visual.ImageStim(
    win=win,
    name='closevideo_4', 
    image='叉叉.png', mask=None,
    ori=0.0, pos=(0.75,0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
blender44 = visual.ImageStim(
    win=win,
    name='blender44', 
    image='介面 PNG\\\\操作中.png', mask=None,
    ori=0.0, pos=(-0.26,0.39), size=(1.2,0.285),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
quickkey44 = visual.ImageStim(
    win=win,
    name='quickkey44', 
    image='介面 PNG\\\\內頁快捷鍵.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
blenderquickkey44 = visual.ImageStim(
    win=win,
    name='blenderquickkey44', 
    image='介面 PNG\\\\內頁快捷鍵-操作中.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "showdata"
showdataClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "first"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_29
mouse_29.x = []
mouse_29.y = []
mouse_29.leftButton = []
mouse_29.midButton = []
mouse_29.rightButton = []
mouse_29.time = []
mouse_29.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
firstComponents = [firstbackgrand, mouse_29, exstart]
for thisComponent in firstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
firstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "first"-------
while continueRoutine:
    # get current time
    t = firstClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=firstClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *firstbackgrand* updates
    if firstbackgrand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        firstbackgrand.frameNStart = frameN  # exact frame index
        firstbackgrand.tStart = t  # local t and not account for scr refresh
        firstbackgrand.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(firstbackgrand, 'tStartRefresh')  # time at next scr refresh
        firstbackgrand.setAutoDraw(True)
    # *mouse_29* updates
    if mouse_29.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_29.frameNStart = frameN  # exact frame index
        mouse_29.tStart = t  # local t and not account for scr refresh
        mouse_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_29, 'tStartRefresh')  # time at next scr refresh
        mouse_29.status = STARTED
        mouse_29.mouseClock.reset()
        prevButtonState = mouse_29.getPressed()  # if button is down already this ISN'T a new click
    if mouse_29.status == STARTED:  # only update if started and not finished!
        buttons = mouse_29.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [exstart,]:
                    if obj.contains(mouse_29):
                        gotValidClick = True
                        mouse_29.clicked_name.append(obj.name)
                x, y = mouse_29.getPos()
                mouse_29.x.append(x)
                mouse_29.y.append(y)
                buttons = mouse_29.getPressed()
                mouse_29.leftButton.append(buttons[0])
                mouse_29.midButton.append(buttons[1])
                mouse_29.rightButton.append(buttons[2])
                mouse_29.time.append(mouse_29.mouseClock.getTime())
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *exstart* updates
    if exstart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exstart.frameNStart = frameN  # exact frame index
        exstart.tStart = t  # local t and not account for scr refresh
        exstart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exstart, 'tStartRefresh')  # time at next scr refresh
        exstart.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in firstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "first"-------
for thisComponent in firstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('firstbackgrand.started', firstbackgrand.tStartRefresh)
thisExp.addData('firstbackgrand.stopped', firstbackgrand.tStopRefresh)
if gotValidClick ==True:
    tostart=1
# store data for thisExp (ExperimentHandler)
if len(mouse_29.x): thisExp.addData('mouse_29.x', mouse_29.x[0])
if len(mouse_29.y): thisExp.addData('mouse_29.y', mouse_29.y[0])
if len(mouse_29.leftButton): thisExp.addData('mouse_29.leftButton', mouse_29.leftButton[0])
if len(mouse_29.midButton): thisExp.addData('mouse_29.midButton', mouse_29.midButton[0])
if len(mouse_29.rightButton): thisExp.addData('mouse_29.rightButton', mouse_29.rightButton[0])
if len(mouse_29.time): thisExp.addData('mouse_29.time', mouse_29.time[0])
if len(mouse_29.clicked_name): thisExp.addData('mouse_29.clicked_name', mouse_29.clicked_name[0])
thisExp.addData('mouse_29.started', mouse_29.tStart)
thisExp.addData('mouse_29.stopped', mouse_29.tStop)
thisExp.nextEntry()
thisExp.addData('exstart.started', exstart.tStartRefresh)
thisExp.addData('exstart.stopped', exstart.tStopRefresh)
# the Routine "first" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_29 = data.TrialHandler(nReps=tostart, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_29')
thisExp.addLoop(trials_29)  # add the loop to the experiment
thisTrial_29 = trials_29.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_29.rgb)
if thisTrial_29 != None:
    for paramName in thisTrial_29:
        exec('{} = thisTrial_29[paramName]'.format(paramName))

for thisTrial_29 in trials_29:
    currentLoop = trials_29
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_29.rgb)
    if thisTrial_29 != None:
        for paramName in thisTrial_29:
            exec('{} = thisTrial_29[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "taskgoal"-------
    continueRoutine = True
    # update component parameters for each repeat
    count1=1
    
    key_resp_18.keys = []
    key_resp_18.rt = []
    _key_resp_18_allKeys = []
    # setup some python lists for storing info about the mouse_30
    mouse_30.x = []
    mouse_30.y = []
    mouse_30.leftButton = []
    mouse_30.midButton = []
    mouse_30.rightButton = []
    mouse_30.time = []
    mouse_30.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    taskgoalComponents = [introduce2, bintroduce3, quickkey4, key_resp_18, mouse_30, start4, goal1]
    for thisComponent in taskgoalComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    taskgoalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "taskgoal"-------
    while continueRoutine:
        # get current time
        t = taskgoalClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=taskgoalClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *introduce2* updates
        if introduce2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            introduce2.frameNStart = frameN  # exact frame index
            introduce2.tStart = t  # local t and not account for scr refresh
            introduce2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(introduce2, 'tStartRefresh')  # time at next scr refresh
            introduce2.setAutoDraw(True)
        
        # *bintroduce3* updates
        if bintroduce3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bintroduce3.frameNStart = frameN  # exact frame index
            bintroduce3.tStart = t  # local t and not account for scr refresh
            bintroduce3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bintroduce3, 'tStartRefresh')  # time at next scr refresh
            bintroduce3.setAutoDraw(True)
        
        # *quickkey4* updates
        if quickkey4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            quickkey4.frameNStart = frameN  # exact frame index
            quickkey4.tStart = t  # local t and not account for scr refresh
            quickkey4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(quickkey4, 'tStartRefresh')  # time at next scr refresh
            quickkey4.setAutoDraw(True)
        for key in event.getKeys():
            if key=='right':
                count1=count1+1
                if count1>=4:
                    count1=4
                    goal1.setAutoDraw(False)
                    introduce2.setAutoDraw(False)
                    bintroduce3.setAutoDraw(False)
                    quickkey4.setAutoDraw(True)
                    start4.setAutoDraw(True)
                elif count1==1:
                    goal1.setAutoDraw(True)
                    introduce2.setAutoDraw(False)
                    bintroduce3.setAutoDraw(False)
                    quickkey4.setAutoDraw(False)
                    start4.setAutoDraw(False)
                elif count1==2:
                    goal1.setAutoDraw(False)
                    introduce2.setAutoDraw(True)
                    bintroduce3.setAutoDraw(False)
                    quickkey4.setAutoDraw(False)
                    start4.setAutoDraw(False)
                   
                elif count1==3:
                    goal1.setAutoDraw(False)
                    introduce2.setAutoDraw(False)
                    bintroduce3.setAutoDraw(True)
                    quickkey4.setAutoDraw(False)
                    start4.setAutoDraw(False)  
            elif key=='left':
                count1=count1-1
                if count1<=1:
                    count1=1
                    goal1.setAutoDraw(True)
                    introduce2.setAutoDraw(False)
                    bintroduce3.setAutoDraw(False)
                    quickkey4.setAutoDraw(False)
                    start4.setAutoDraw(False)
                elif count1==2:
                    goal1.setAutoDraw(False)
                    introduce2.setAutoDraw(True)
                    bintroduce3.setAutoDraw(False)
                    quickkey4.setAutoDraw(False)
                    start4.setAutoDraw(False)
                   
                elif count1==3:
                    goal1.setAutoDraw(False)
                    introduce2.setAutoDraw(False)
                    bintroduce3.setAutoDraw(True)
                    quickkey4.setAutoDraw(False)
                    start4.setAutoDraw(False)
        
        # *key_resp_18* updates
        waitOnFlip = False
        if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_18.frameNStart = frameN  # exact frame index
            key_resp_18.tStart = t  # local t and not account for scr refresh
            key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
            key_resp_18.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_18.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_18.getKeys(keyList=['right', 'left'], waitRelease=False)
            _key_resp_18_allKeys.extend(theseKeys)
            if len(_key_resp_18_allKeys):
                key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
                key_resp_18.rt = _key_resp_18_allKeys[-1].rt
        # *mouse_30* updates
        if mouse_30.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_30.frameNStart = frameN  # exact frame index
            mouse_30.tStart = t  # local t and not account for scr refresh
            mouse_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_30, 'tStartRefresh')  # time at next scr refresh
            mouse_30.status = STARTED
            mouse_30.mouseClock.reset()
            prevButtonState = mouse_30.getPressed()  # if button is down already this ISN'T a new click
        if mouse_30.status == STARTED:  # only update if started and not finished!
            buttons = mouse_30.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [start4,]:
                        if obj.contains(mouse_30):
                            gotValidClick = True
                            mouse_30.clicked_name.append(obj.name)
                    x, y = mouse_30.getPos()
                    mouse_30.x.append(x)
                    mouse_30.y.append(y)
                    buttons = mouse_30.getPressed()
                    mouse_30.leftButton.append(buttons[0])
                    mouse_30.midButton.append(buttons[1])
                    mouse_30.rightButton.append(buttons[2])
                    mouse_30.time.append(mouse_30.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *start4* updates
        if start4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start4.frameNStart = frameN  # exact frame index
            start4.tStart = t  # local t and not account for scr refresh
            start4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start4, 'tStartRefresh')  # time at next scr refresh
            start4.setAutoDraw(True)
        
        # *goal1* updates
        if goal1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goal1.frameNStart = frameN  # exact frame index
            goal1.tStart = t  # local t and not account for scr refresh
            goal1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goal1, 'tStartRefresh')  # time at next scr refresh
            goal1.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taskgoalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "taskgoal"-------
    for thisComponent in taskgoalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_29.addData('introduce2.started', introduce2.tStartRefresh)
    trials_29.addData('introduce2.stopped', introduce2.tStopRefresh)
    trials_29.addData('bintroduce3.started', bintroduce3.tStartRefresh)
    trials_29.addData('bintroduce3.stopped', bintroduce3.tStopRefresh)
    trials_29.addData('quickkey4.started', quickkey4.tStartRefresh)
    trials_29.addData('quickkey4.stopped', quickkey4.tStopRefresh)
    # check responses
    if key_resp_18.keys in ['', [], None]:  # No response was made
        key_resp_18.keys = None
    trials_29.addData('key_resp_18.keys',key_resp_18.keys)
    if key_resp_18.keys != None:  # we had a response
        trials_29.addData('key_resp_18.rt', key_resp_18.rt)
    trials_29.addData('key_resp_18.started', key_resp_18.tStartRefresh)
    trials_29.addData('key_resp_18.stopped', key_resp_18.tStopRefresh)
    # store data for trials_29 (TrialHandler)
    if len(mouse_30.x): trials_29.addData('mouse_30.x', mouse_30.x[0])
    if len(mouse_30.y): trials_29.addData('mouse_30.y', mouse_30.y[0])
    if len(mouse_30.leftButton): trials_29.addData('mouse_30.leftButton', mouse_30.leftButton[0])
    if len(mouse_30.midButton): trials_29.addData('mouse_30.midButton', mouse_30.midButton[0])
    if len(mouse_30.rightButton): trials_29.addData('mouse_30.rightButton', mouse_30.rightButton[0])
    if len(mouse_30.time): trials_29.addData('mouse_30.time', mouse_30.time[0])
    if len(mouse_30.clicked_name): trials_29.addData('mouse_30.clicked_name', mouse_30.clicked_name[0])
    trials_29.addData('mouse_30.started', mouse_30.tStart)
    trials_29.addData('mouse_30.stopped', mouse_30.tStop)
    trials_29.addData('start4.started', start4.tStartRefresh)
    trials_29.addData('start4.stopped', start4.tStopRefresh)
    trials_29.addData('goal1.started', goal1.tStartRefresh)
    trials_29.addData('goal1.stopped', goal1.tStopRefresh)
    # the Routine "taskgoal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed tostart repeats of 'trials_29'


# set up handler to look after randomisation of conditions etc
trials_27 = data.TrialHandler(nReps=200.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_27')
thisExp.addLoop(trials_27)  # add the loop to the experiment
thisTrial_27 = trials_27.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_27.rgb)
if thisTrial_27 != None:
    for paramName in thisTrial_27:
        exec('{} = thisTrial_27[paramName]'.format(paramName))

for thisTrial_27 in trials_27:
    currentLoop = trials_27
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_27.rgb)
    if thisTrial_27 != None:
        for paramName in thisTrial_27:
            exec('{} = thisTrial_27[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "totalmenu"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_menupath2_4.keys = []
    key_menupath2_4.rt = []
    _key_menupath2_4_allKeys = []
    MenuClock.reset(0)
    ExperienceClock.reset(0)
           
    totalpath1=0
    totalpath2=0
    totalpath3=0
    totalpath4=0
    Time1 = 0
    showf=0
    enter1=0
    blender=0
    newchange=0
    # setup some python lists for storing info about the mouse_18
    mouse_18.x = []
    mouse_18.y = []
    mouse_18.leftButton = []
    mouse_18.midButton = []
    mouse_18.rightButton = []
    mouse_18.time = []
    mouse_18.clicked_name = []
    gotValidClick = False  # until a click is received
    mouse_18.mouseClock.reset()
    key_resp_29.keys = []
    key_resp_29.rt = []
    _key_resp_29_allKeys = []
    # keep track of which components have finished
    totalmenuComponents = [key_menupath2_4, mouse_18, key_resp_29, TOTALMENU, nonono, blendertotalmenu, quickkeytotalmenu, blenderquickkey]
    for thisComponent in totalmenuComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    totalmenuClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "totalmenu"-------
    while continueRoutine:
        # get current time
        t = totalmenuClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=totalmenuClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_menupath2_4* updates
        waitOnFlip = False
        if key_menupath2_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_menupath2_4.frameNStart = frameN  # exact frame index
            key_menupath2_4.tStart = t  # local t and not account for scr refresh
            key_menupath2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_menupath2_4, 'tStartRefresh')  # time at next scr refresh
            key_menupath2_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_menupath2_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_menupath2_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_menupath2_4.status == STARTED and not waitOnFlip:
            theseKeys = key_menupath2_4.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _key_menupath2_4_allKeys.extend(theseKeys)
            if len(_key_menupath2_4_allKeys):
                key_menupath2_4.keys = _key_menupath2_4_allKeys[-1].name  # just the last key pressed
                key_menupath2_4.rt = _key_menupath2_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        if (showf%2)!=1:
            quickkeytotalmenu.setAutoDraw(False)
            blenderquickkey.setAutoDraw(False)
        if (blender%2)!=1:
            blendertotalmenu.setAutoDraw(False)
        for key in event.getKeys():
            if key =='1':
                countcontinue=countcontinue+1
                if (enter1%2)==1 :
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('totalmenu blender')
                    allsteptime.append(BlenderClock.getTime())
                    countchange.append(newchange)
                else:
                    Menutime.append(MenuClock.getTime())
                    AllWatchtime.append(MenuClock.getTime())
                    allsteptime.append('totalmenu learn')
                    allsteptime.append(MenuClock.getTime())
                    countchange.append(newchange)
                totalpath1=1
            elif key =='2':
                countcontinue=countcontinue+1
                if (enter1%2)==1 :
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('totalmenu blender')
                    allsteptime.append(BlenderClock.getTime())
                    countchange.append(newchange)
                else:
                    Menutime.append(MenuClock.getTime())
                    AllWatchtime.append(MenuClock.getTime())
                    allsteptime.append('totalmenu learn')
                    allsteptime.append(MenuClock.getTime())
                    countchange.append(newchange)
                totalpath2=1
            elif key =='3':
                countcontinue=countcontinue+1
                if (enter1%2)==1 :
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('totalmenu blender')
                    allsteptime.append(BlenderClock.getTime())
                    countchange.append(newchange)
                else:
                    Menutime.append(MenuClock.getTime())
                    AllWatchtime.append(MenuClock.getTime())
                    allsteptime.append('totalmenu learn')
                    allsteptime.append(MenuClock.getTime())
                    countchange.append(newchange)
                totalpath3=1
            elif key =='4':
                countcontinue=countcontinue+1
                if (enter1%2)==1 :
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('totalmenu blender')
                    allsteptime.append(BlenderClock.getTime())
                    countchange.append(newchange)
                else:
                    Menutime.append(MenuClock.getTime())
                    AllWatchtime.append(MenuClock.getTime())
                    allsteptime.append('totalmenu learn')
                    allsteptime.append(MenuClock.getTime())
                    countchange.append(newchange)
                totalpath4=1     
            elif key =='f':
                countcontinue=countcontinue+1
                showf=showf+1
                if(showf%2)==1 and (enter1%2)==0:
                    quickkeytotalmenu.setAutoDraw(True) 
                    blenderquickkey.setAutoDraw(False)
                elif (showf%2)==1 and (enter1%2)==1:
                    blenderquickkey.setAutoDraw(True) 
                    quickkeytotalmenu.setAutoDraw(False) 
                else:
                    quickkeytotalmenu.setAutoDraw(False)
                    blenderquickkey.setAutoDraw(False)
        # f/enter blender&learn time  
            if key =='return':  
                countcontinue=countcontinue+1
                enter1=enter1+1
                blender=blender+1
                countenter=countenter+1
                newchange=newchange+1
                if(showf%2)==1 and (enter1%2)==0:
                    quickkeytotalmenu.setAutoDraw(True) 
                    blenderquickkey.setAutoDraw(False)
                elif (showf%2)==1 and (enter1%2)==1:
                    blenderquickkey.setAutoDraw(True) 
                    quickkeytotalmenu.setAutoDraw(False) 
                else:
                    quickkeytotalmenu.setAutoDraw(False)
                    blenderquickkey.setAutoDraw(False)
                if(enter1%2)==1:
                    Menutime.append(MenuClock.getTime())
                    AllWatchtime.append(MenuClock.getTime())
                    allsteptime.append('totalmenu learn')
                    allsteptime.append(MenuClock.getTime())
                    BlenderClock.reset(0)
                    blendertotalmenu.setAutoDraw(True)
                else: 
                    BlenderTime.append(BlenderClock.getTime())  
                    allsteptime.append('totalmenu blender')
                    allsteptime.append(BlenderClock.getTime())
                    MenuClock.reset(0)
                    blendertotalmenu.setAutoDraw(False)
        
        # *mouse_18* updates
        if mouse_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_18.frameNStart = frameN  # exact frame index
            mouse_18.tStart = t  # local t and not account for scr refresh
            mouse_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_18, 'tStartRefresh')  # time at next scr refresh
            mouse_18.status = STARTED
            prevButtonState = mouse_18.getPressed()  # if button is down already this ISN'T a new click
        if mouse_18.status == STARTED:  # only update if started and not finished!
            buttons = mouse_18.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [nonono,]:
                        if obj.contains(mouse_18):
                            gotValidClick = True
                            mouse_18.clicked_name.append(obj.name)
                    x, y = mouse_18.getPos()
                    mouse_18.x.append(x)
                    mouse_18.y.append(y)
                    buttons = mouse_18.getPressed()
                    mouse_18.leftButton.append(buttons[0])
                    mouse_18.midButton.append(buttons[1])
                    mouse_18.rightButton.append(buttons[2])
                    mouse_18.time.append(mouse_18.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *key_resp_29* updates
        waitOnFlip = False
        if key_resp_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_29.frameNStart = frameN  # exact frame index
            key_resp_29.tStart = t  # local t and not account for scr refresh
            key_resp_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_29, 'tStartRefresh')  # time at next scr refresh
            key_resp_29.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_29.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_29.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_29.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_29.getKeys(keyList=['f', 'return'], waitRelease=False)
            _key_resp_29_allKeys.extend(theseKeys)
            if len(_key_resp_29_allKeys):
                key_resp_29.keys = _key_resp_29_allKeys[-1].name  # just the last key pressed
                key_resp_29.rt = _key_resp_29_allKeys[-1].rt
        
        # *TOTALMENU* updates
        if TOTALMENU.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TOTALMENU.frameNStart = frameN  # exact frame index
            TOTALMENU.tStart = t  # local t and not account for scr refresh
            TOTALMENU.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TOTALMENU, 'tStartRefresh')  # time at next scr refresh
            TOTALMENU.setAutoDraw(True)
        
        # *nonono* updates
        if nonono.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nonono.frameNStart = frameN  # exact frame index
            nonono.tStart = t  # local t and not account for scr refresh
            nonono.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nonono, 'tStartRefresh')  # time at next scr refresh
            nonono.setAutoDraw(True)
        
        # *blendertotalmenu* updates
        if blendertotalmenu.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blendertotalmenu.frameNStart = frameN  # exact frame index
            blendertotalmenu.tStart = t  # local t and not account for scr refresh
            blendertotalmenu.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blendertotalmenu, 'tStartRefresh')  # time at next scr refresh
            blendertotalmenu.setAutoDraw(True)
        
        # *quickkeytotalmenu* updates
        if quickkeytotalmenu.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            quickkeytotalmenu.frameNStart = frameN  # exact frame index
            quickkeytotalmenu.tStart = t  # local t and not account for scr refresh
            quickkeytotalmenu.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(quickkeytotalmenu, 'tStartRefresh')  # time at next scr refresh
            quickkeytotalmenu.setAutoDraw(True)
        
        # *blenderquickkey* updates
        if blenderquickkey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blenderquickkey.frameNStart = frameN  # exact frame index
            blenderquickkey.tStart = t  # local t and not account for scr refresh
            blenderquickkey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blenderquickkey, 'tStartRefresh')  # time at next scr refresh
            blenderquickkey.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in totalmenuComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "totalmenu"-------
    for thisComponent in totalmenuComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_menupath2_4.keys in ['', [], None]:  # No response was made
        key_menupath2_4.keys = None
    trials_27.addData('key_menupath2_4.keys',key_menupath2_4.keys)
    if key_menupath2_4.keys != None:  # we had a response
        trials_27.addData('key_menupath2_4.rt', key_menupath2_4.rt)
    trials_27.addData('key_menupath2_4.started', key_menupath2_4.tStartRefresh)
    trials_27.addData('key_menupath2_4.stopped', key_menupath2_4.tStopRefresh)
    Experiencetime.append(ExperienceClock.getTime())
    
    if gotValidClick ==True  :
        countchange.append(newchange)
        trials_27.finished = True
        if(enter1%2)==1:
            BlenderTime.append(BlenderClock.getTime())  
            allsteptime.append('totalmenu blender')
            allsteptime.append(BlenderClock.getTime())   
        else: 
            Menutime.append(MenuClock.getTime())
            AllWatchtime.append(MenuClock.getTime())
            allsteptime.append('totalmenu learn')
            allsteptime.append(MenuClock.getTime())
            
    
            
    
        
    # store data for trials_27 (TrialHandler)
    if len(mouse_18.x): trials_27.addData('mouse_18.x', mouse_18.x[0])
    if len(mouse_18.y): trials_27.addData('mouse_18.y', mouse_18.y[0])
    if len(mouse_18.leftButton): trials_27.addData('mouse_18.leftButton', mouse_18.leftButton[0])
    if len(mouse_18.midButton): trials_27.addData('mouse_18.midButton', mouse_18.midButton[0])
    if len(mouse_18.rightButton): trials_27.addData('mouse_18.rightButton', mouse_18.rightButton[0])
    if len(mouse_18.time): trials_27.addData('mouse_18.time', mouse_18.time[0])
    if len(mouse_18.clicked_name): trials_27.addData('mouse_18.clicked_name', mouse_18.clicked_name[0])
    trials_27.addData('mouse_18.started', mouse_18.tStartRefresh)
    trials_27.addData('mouse_18.stopped', mouse_18.tStopRefresh)
    # check responses
    if key_resp_29.keys in ['', [], None]:  # No response was made
        key_resp_29.keys = None
    trials_27.addData('key_resp_29.keys',key_resp_29.keys)
    if key_resp_29.keys != None:  # we had a response
        trials_27.addData('key_resp_29.rt', key_resp_29.rt)
    trials_27.addData('key_resp_29.started', key_resp_29.tStartRefresh)
    trials_27.addData('key_resp_29.stopped', key_resp_29.tStopRefresh)
    trials_27.addData('TOTALMENU.started', TOTALMENU.tStartRefresh)
    trials_27.addData('TOTALMENU.stopped', TOTALMENU.tStopRefresh)
    trials_27.addData('nonono.started', nonono.tStartRefresh)
    trials_27.addData('nonono.stopped', nonono.tStopRefresh)
    trials_27.addData('blendertotalmenu.started', blendertotalmenu.tStartRefresh)
    trials_27.addData('blendertotalmenu.stopped', blendertotalmenu.tStopRefresh)
    trials_27.addData('quickkeytotalmenu.started', quickkeytotalmenu.tStartRefresh)
    trials_27.addData('quickkeytotalmenu.stopped', quickkeytotalmenu.tStopRefresh)
    trials_27.addData('blenderquickkey.started', blenderquickkey.tStartRefresh)
    trials_27.addData('blenderquickkey.stopped', blenderquickkey.tStopRefresh)
    # the Routine "totalmenu" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_17 = data.TrialHandler(nReps=totalpath3, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_17')
    thisExp.addLoop(trials_17)  # add the loop to the experiment
    thisTrial_17 = trials_17.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_17.rgb)
    if thisTrial_17 != None:
        for paramName in thisTrial_17:
            exec('{} = thisTrial_17[paramName]'.format(paramName))
    
    for thisTrial_17 in trials_17:
        currentLoop = trials_17
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_17.rgb)
        if thisTrial_17 != None:
            for paramName in thisTrial_17:
                exec('{} = thisTrial_17[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "menu3"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_menupath2_2.keys = []
        key_menupath2_2.rt = []
        _key_menupath2_2_allKeys = []
        MenuClock.reset(0)
        ExperienceClock.reset(0)
        videopath31=0
        videopath32=0
        videopath33=0
        videopath34=0
        videopath35=0
        videopath36=0
        videopath37=0
        videopath38=0
        showf=0
        Time1 = 0
        enter1=0
        blender=0
        newchange=0
        # setup some python lists for storing info about the mouse_31
        mouse_31.clicked_name = []
        gotValidClick = False  # until a click is received
        key_resp_30.keys = []
        key_resp_30.rt = []
        _key_resp_30_allKeys = []
        # keep track of which components have finished
        menu3Components = [key_menupath2_2, mouse_31, backmenu3, close2, key_resp_30, blendermenu3, quickkeymenu3, blenderquickkey3]
        for thisComponent in menu3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        menu3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "menu3"-------
        while continueRoutine:
            # get current time
            t = menu3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=menu3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_menupath2_2* updates
            waitOnFlip = False
            if key_menupath2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_menupath2_2.frameNStart = frameN  # exact frame index
                key_menupath2_2.tStart = t  # local t and not account for scr refresh
                key_menupath2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_menupath2_2, 'tStartRefresh')  # time at next scr refresh
                key_menupath2_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_menupath2_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_menupath2_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_menupath2_2.status == STARTED and not waitOnFlip:
                theseKeys = key_menupath2_2.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8'], waitRelease=False)
                _key_menupath2_2_allKeys.extend(theseKeys)
                if len(_key_menupath2_2_allKeys):
                    key_menupath2_2.keys = _key_menupath2_2_allKeys[-1].name  # just the last key pressed
                    key_menupath2_2.rt = _key_menupath2_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            if (showf%2)!=1:
                quickkeymenu3.setAutoDraw(False)
                blenderquickkey3.setAutoDraw(False)
            if (blender%2)!=1:
                blendermenu3.setAutoDraw(False)
            for key in event.getKeys():
                if key =='1':
                    countcontinue=countcontinue+1
                    countchange.append(newchange)
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu3 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu3 learn')
                        allsteptime.append(MenuClock.getTime())
                    videopath31=1
                elif key =='2':
                    countcontinue=countcontinue+1
                    countchange.append(newchange)
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu3 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu3 learn')
                        allsteptime.append(MenuClock.getTime())
                    videopath32=1
                elif key =='3':
                    countcontinue=countcontinue+1
                    countchange.append(newchange)
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu3 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu3 learn')
                        allsteptime.append(MenuClock.getTime())
                    videopath33=1
                elif key =='4':
                    countcontinue=countcontinue+1
                    countchange.append(newchange)
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu3 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu3 learn')
                        allsteptime.append(MenuClock.getTime())
                    videopath34=1
                elif key =='5':
                    countcontinue=countcontinue+1
                    countchange.append(newchange)
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu3 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu3 learn')
                        allsteptime.append(MenuClock.getTime())
                    videopath35=1
                elif key =='6':
                    countcontinue=countcontinue+1
                    countchange.append(newchange)
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu3 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu3 learn')
                        allsteptime.append(MenuClock.getTime())
                    videopath36=1
                elif key =='7':
                    countcontinue=countcontinue+1
                    countchange.append(newchange)
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu3 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu3 learn')
                        allsteptime.append(MenuClock.getTime())
                    videopath37=1
                elif key =='8':
                    countcontinue=countcontinue+1
                    countchange.append(newchange)
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu3 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu3 learn')
                        allsteptime.append(MenuClock.getTime())
                    videopath38=1
                elif key =='f':
                    countcontinue=countcontinue+1
                    showf=showf+1
                    if(showf%2)==1 and (enter1%2)==0:
                        quickkeymenu3.setAutoDraw(True)
                        blenderquickkey3.setAutoDraw(False)
                    elif (showf%2)==1 and (enter1%2)==1:
                        blenderquickkey3.setAutoDraw(True)   
                        quickkeymenu3.setAutoDraw(False)  
                    else:
                        blenderquickkey3.setAutoDraw(False)
                        quickkeymenu3.setAutoDraw(False)
            # f/enter blender&learn time  
                if key =='return':  
                    countcontinue=countcontinue+1
                    enter1=enter1+1
                    blender=blender+1
                    countenter=countenter+1
                    newchange=newchange+1
                    if(showf%2)==1 and (enter1%2)==0:
                        quickkeymenu3.setAutoDraw(True)
                        blenderquickkey3.setAutoDraw(False)
                    elif (showf%2)==1 and (enter1%2)==1:
                        blenderquickkey3.setAutoDraw(True)   
                        quickkeymenu3.setAutoDraw(False)  
                    else:
                        blenderquickkey3.setAutoDraw(False)
                        quickkeymenu3.setAutoDraw(False)
                    if(enter1%2)==1:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu3 learn')
                        allsteptime.append(MenuClock.getTime())
                        BlenderClock.reset(0)
                        blendermenu3.setAutoDraw(True)
                    else: 
                        BlenderTime.append(BlenderClock.getTime())  
                        allsteptime.append('menu3 blender')
                        allsteptime.append(BlenderClock.getTime())
                        MenuClock.reset(0)
                        blendermenu3.setAutoDraw(False)
            # *mouse_31* updates
            if mouse_31.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_31.frameNStart = frameN  # exact frame index
                mouse_31.tStart = t  # local t and not account for scr refresh
                mouse_31.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_31, 'tStartRefresh')  # time at next scr refresh
                mouse_31.status = STARTED
                mouse_31.mouseClock.reset()
                prevButtonState = mouse_31.getPressed()  # if button is down already this ISN'T a new click
            if mouse_31.status == STARTED:  # only update if started and not finished!
                buttons = mouse_31.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [close2,]:
                            if obj.contains(mouse_31):
                                gotValidClick = True
                                mouse_31.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *backmenu3* updates
            if backmenu3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                backmenu3.frameNStart = frameN  # exact frame index
                backmenu3.tStart = t  # local t and not account for scr refresh
                backmenu3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(backmenu3, 'tStartRefresh')  # time at next scr refresh
                backmenu3.setAutoDraw(True)
            
            # *close2* updates
            if close2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                close2.frameNStart = frameN  # exact frame index
                close2.tStart = t  # local t and not account for scr refresh
                close2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(close2, 'tStartRefresh')  # time at next scr refresh
                close2.setAutoDraw(True)
            
            # *key_resp_30* updates
            waitOnFlip = False
            if key_resp_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_30.frameNStart = frameN  # exact frame index
                key_resp_30.tStart = t  # local t and not account for scr refresh
                key_resp_30.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_30, 'tStartRefresh')  # time at next scr refresh
                key_resp_30.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_30.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_30.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_30.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_30.getKeys(keyList=['f', 'return'], waitRelease=False)
                _key_resp_30_allKeys.extend(theseKeys)
                if len(_key_resp_30_allKeys):
                    key_resp_30.keys = _key_resp_30_allKeys[-1].name  # just the last key pressed
                    key_resp_30.rt = _key_resp_30_allKeys[-1].rt
            
            # *blendermenu3* updates
            if blendermenu3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blendermenu3.frameNStart = frameN  # exact frame index
                blendermenu3.tStart = t  # local t and not account for scr refresh
                blendermenu3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blendermenu3, 'tStartRefresh')  # time at next scr refresh
                blendermenu3.setAutoDraw(True)
            
            # *quickkeymenu3* updates
            if quickkeymenu3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                quickkeymenu3.frameNStart = frameN  # exact frame index
                quickkeymenu3.tStart = t  # local t and not account for scr refresh
                quickkeymenu3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(quickkeymenu3, 'tStartRefresh')  # time at next scr refresh
                quickkeymenu3.setAutoDraw(True)
            
            # *blenderquickkey3* updates
            if blenderquickkey3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blenderquickkey3.frameNStart = frameN  # exact frame index
                blenderquickkey3.tStart = t  # local t and not account for scr refresh
                blenderquickkey3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blenderquickkey3, 'tStartRefresh')  # time at next scr refresh
                blenderquickkey3.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in menu3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "menu3"-------
        for thisComponent in menu3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_menupath2_2.keys in ['', [], None]:  # No response was made
            key_menupath2_2.keys = None
        trials_17.addData('key_menupath2_2.keys',key_menupath2_2.keys)
        if key_menupath2_2.keys != None:  # we had a response
            trials_17.addData('key_menupath2_2.rt', key_menupath2_2.rt)
        trials_17.addData('key_menupath2_2.started', key_menupath2_2.tStartRefresh)
        trials_17.addData('key_menupath2_2.stopped', key_menupath2_2.tStopRefresh)
        Experiencetime.append(ExperienceClock.getTime())
        
        if gotValidClick ==True:
            countchange.append(newchange)
            if (enter1%2)==1 :
                BlenderTime.append(BlenderClock.getTime())
                allsteptime.append('menu3 blender')
                allsteptime.append(BlenderClock.getTime())
            else:
                Menutime.append(MenuClock.getTime())
                AllWatchtime.append(MenuClock.getTime())
                allsteptime.append('menu3 learn')
                allsteptime.append(MenuClock.getTime())
            change=change+1
        # store data for trials_17 (TrialHandler)
        x, y = mouse_31.getPos()
        buttons = mouse_31.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [close2,]:
                if obj.contains(mouse_31):
                    gotValidClick = True
                    mouse_31.clicked_name.append(obj.name)
        trials_17.addData('mouse_31.x', x)
        trials_17.addData('mouse_31.y', y)
        trials_17.addData('mouse_31.leftButton', buttons[0])
        trials_17.addData('mouse_31.midButton', buttons[1])
        trials_17.addData('mouse_31.rightButton', buttons[2])
        if len(mouse_31.clicked_name):
            trials_17.addData('mouse_31.clicked_name', mouse_31.clicked_name[0])
        trials_17.addData('mouse_31.started', mouse_31.tStart)
        trials_17.addData('mouse_31.stopped', mouse_31.tStop)
        trials_17.addData('backmenu3.started', backmenu3.tStartRefresh)
        trials_17.addData('backmenu3.stopped', backmenu3.tStopRefresh)
        trials_17.addData('close2.started', close2.tStartRefresh)
        trials_17.addData('close2.stopped', close2.tStopRefresh)
        # check responses
        if key_resp_30.keys in ['', [], None]:  # No response was made
            key_resp_30.keys = None
        trials_17.addData('key_resp_30.keys',key_resp_30.keys)
        if key_resp_30.keys != None:  # we had a response
            trials_17.addData('key_resp_30.rt', key_resp_30.rt)
        trials_17.addData('key_resp_30.started', key_resp_30.tStartRefresh)
        trials_17.addData('key_resp_30.stopped', key_resp_30.tStopRefresh)
        trials_17.addData('blendermenu3.started', blendermenu3.tStartRefresh)
        trials_17.addData('blendermenu3.stopped', blendermenu3.tStopRefresh)
        trials_17.addData('quickkeymenu3.started', quickkeymenu3.tStartRefresh)
        trials_17.addData('quickkeymenu3.stopped', quickkeymenu3.tStopRefresh)
        trials_17.addData('blenderquickkey3.started', blenderquickkey3.tStartRefresh)
        trials_17.addData('blenderquickkey3.stopped', blenderquickkey3.tStopRefresh)
        # the Routine "menu3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_18 = data.TrialHandler(nReps=videopath32, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_18')
        thisExp.addLoop(trials_18)  # add the loop to the experiment
        thisTrial_18 = trials_18.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_18.rgb)
        if thisTrial_18 != None:
            for paramName in thisTrial_18:
                exec('{} = thisTrial_18[paramName]'.format(paramName))
        
        for thisTrial_18 in trials_18:
            currentLoop = trials_18
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_18.rgb)
            if thisTrial_18 != None:
                for paramName in thisTrial_18:
                    exec('{} = thisTrial_18[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video3_1"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_19.keys = []
            key_resp_19.rt = []
            _key_resp_19_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp31)!=0:
                movie_19.pause()
                movie_19.seek(int(remembertimestamp31[-1]))
                movie_19.play()
                Time1 = 0
            showf=0
            enter1=0   
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_19
            mouse_19.x = []
            mouse_19.y = []
            mouse_19.leftButton = []
            mouse_19.midButton = []
            mouse_19.rightButton = []
            mouse_19.time = []
            mouse_19.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_19.mouseClock.reset()
            # keep track of which components have finished
            video3_1Components = [key_resp_19, mouse_19, backvideo31, movie_19, closevideo_19, blender31, quickkey31, blenderquickkey31]
            for thisComponent in video3_1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video3_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video3_1"-------
            while continueRoutine:
                # get current time
                t = video3_1Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video3_1Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_19* updates
                waitOnFlip = False
                if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_19.frameNStart = frameN  # exact frame index
                    key_resp_19.tStart = t  # local t and not account for scr refresh
                    key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
                    key_resp_19.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_19.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_19.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_19_allKeys.extend(theseKeys)
                    if len(_key_resp_19_allKeys):
                        key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
                        key_resp_19.rt = _key_resp_19_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey31.setAutoDraw(False)
                    blenderquickkey31.setAutoDraw(False)
                if (blender%2)!=1:
                    blender31.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_19.status == PLAYING:
                            movie_19.pause()
                        elif movie_19.status == PAUSED:
                            movie_19.play()
                    elif key=='s':
                        change=change+1
                        movie_19.pause()
                        ntime = max(0.0,movie_19.duration)
                        movie_19.seek(ntime)
                        movie_19.play()
                    if movie_19.status == PLAYING:
                        if key=='period':
                            movie_19.pause()
                            ntime = min(movie_19.getCurrentFrameTime( ) + 5.0, movie_19.duration)
                            movie_19.seek(ntime)
                            movie_19.play()
                            change=change+1  
                        elif key=='comma':
                            movie_19.pause()
                            ntime = max(movie_19.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_19.seek(ntime)
                            movie_19.play()
                            change=change+1
                        elif key =='f':
                            showf=showf+1
                            countcontinue=countcontinue+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey31.setAutoDraw(True)    
                                blenderquickkey31.setAutoDraw(False) 
                                movie_19.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey31.setAutoDraw(True) 
                                quickkey31.setAutoDraw(False)
                                movie_19.pause()
                            else:
                                blenderquickkey31.setAutoDraw(False) 
                                quickkey31.setAutoDraw(False)
                                movie_19.play()
                                
                    elif movie_19.status == PAUSED:
                        if key=='period':
                            movie_19.pause()
                            ntime = min(movie_19.getCurrentFrameTime( ) + 5.0, movie_19.duration)
                            movie_19.seek(ntime)
                            movie_19.play()
                            change=change+1
                       
                        elif key=='comma':
                            movie_19.pause()
                            ntime = max(movie_19.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_19.seek(ntime)
                            movie_19.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_19.pause()
                            showf=showf+1
                            countcontinue=countcontinue+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey31.setAutoDraw(True)    
                                blenderquickkey31.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey31.setAutoDraw(True) 
                                quickkey31.setAutoDraw(False)
                            else:
                                blenderquickkey31.setAutoDraw(False) 
                                quickkey31.setAutoDraw(False)     
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey31.setAutoDraw(True)    
                            blenderquickkey31.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey31.setAutoDraw(True) 
                            quickkey31.setAutoDraw(False)
                        else:
                            blenderquickkey31.setAutoDraw(False) 
                            quickkey31.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video3-1 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender31.setAutoDraw(True)
                            enterspace=enterspace+1
                            
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video3-1 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender31.setAutoDraw(False)
                # *mouse_19* updates
                if mouse_19.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_19.frameNStart = frameN  # exact frame index
                    mouse_19.tStart = t  # local t and not account for scr refresh
                    mouse_19.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_19, 'tStartRefresh')  # time at next scr refresh
                    mouse_19.status = STARTED
                    prevButtonState = mouse_19.getPressed()  # if button is down already this ISN'T a new click
                if mouse_19.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_19.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_19,]:
                                if obj.contains(mouse_19):
                                    gotValidClick = True
                                    mouse_19.clicked_name.append(obj.name)
                            x, y = mouse_19.getPos()
                            mouse_19.x.append(x)
                            mouse_19.y.append(y)
                            buttons = mouse_19.getPressed()
                            mouse_19.leftButton.append(buttons[0])
                            mouse_19.midButton.append(buttons[1])
                            mouse_19.rightButton.append(buttons[2])
                            mouse_19.time.append(mouse_19.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo31* updates
                if backvideo31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo31.frameNStart = frameN  # exact frame index
                    backvideo31.tStart = t  # local t and not account for scr refresh
                    backvideo31.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo31, 'tStartRefresh')  # time at next scr refresh
                    backvideo31.setAutoDraw(True)
                
                # *movie_19* updates
                if movie_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_19.frameNStart = frameN  # exact frame index
                    movie_19.tStart = t  # local t and not account for scr refresh
                    movie_19.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_19, 'tStartRefresh')  # time at next scr refresh
                    movie_19.setAutoDraw(True)
                
                # *closevideo_19* updates
                if closevideo_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_19.frameNStart = frameN  # exact frame index
                    closevideo_19.tStart = t  # local t and not account for scr refresh
                    closevideo_19.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_19, 'tStartRefresh')  # time at next scr refresh
                    closevideo_19.setAutoDraw(True)
                
                # *blender31* updates
                if blender31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender31.frameNStart = frameN  # exact frame index
                    blender31.tStart = t  # local t and not account for scr refresh
                    blender31.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender31, 'tStartRefresh')  # time at next scr refresh
                    blender31.setAutoDraw(True)
                
                # *quickkey31* updates
                if quickkey31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey31.frameNStart = frameN  # exact frame index
                    quickkey31.tStart = t  # local t and not account for scr refresh
                    quickkey31.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey31, 'tStartRefresh')  # time at next scr refresh
                    quickkey31.setAutoDraw(True)
                
                # *blenderquickkey31* updates
                if blenderquickkey31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey31.frameNStart = frameN  # exact frame index
                    blenderquickkey31.tStart = t  # local t and not account for scr refresh
                    blenderquickkey31.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey31, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey31.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video3_1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video3_1"-------
            for thisComponent in video3_1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_19.keys in ['', [], None]:  # No response was made
                key_resp_19.keys = None
            trials_18.addData('key_resp_19.keys',key_resp_19.keys)
            if key_resp_19.keys != None:  # we had a response
                trials_18.addData('key_resp_19.rt', key_resp_19.rt)
            trials_18.addData('key_resp_19.started', key_resp_19.tStartRefresh)
            trials_18.addData('key_resp_19.stopped', key_resp_19.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime())  
                    allsteptime.append('video3-1 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video3-1 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_19.getCurrentFrameTime( )
                remembertimestamp31.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime14.append(sum(Watchtime1))
            #    allsteptime.append('video3-1 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime14.append(sum(Watchtime1))
            #    allsteptime.append('video3-1 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            
            totalpath3=1
                
            # store data for trials_18 (TrialHandler)
            if len(mouse_19.x): trials_18.addData('mouse_19.x', mouse_19.x[0])
            if len(mouse_19.y): trials_18.addData('mouse_19.y', mouse_19.y[0])
            if len(mouse_19.leftButton): trials_18.addData('mouse_19.leftButton', mouse_19.leftButton[0])
            if len(mouse_19.midButton): trials_18.addData('mouse_19.midButton', mouse_19.midButton[0])
            if len(mouse_19.rightButton): trials_18.addData('mouse_19.rightButton', mouse_19.rightButton[0])
            if len(mouse_19.time): trials_18.addData('mouse_19.time', mouse_19.time[0])
            if len(mouse_19.clicked_name): trials_18.addData('mouse_19.clicked_name', mouse_19.clicked_name[0])
            trials_18.addData('mouse_19.started', mouse_19.tStart)
            trials_18.addData('mouse_19.stopped', mouse_19.tStop)
            trials_18.addData('backvideo31.started', backvideo31.tStartRefresh)
            trials_18.addData('backvideo31.stopped', backvideo31.tStopRefresh)
            movie_19.stop()
            trials_18.addData('closevideo_19.started', closevideo_19.tStartRefresh)
            trials_18.addData('closevideo_19.stopped', closevideo_19.tStopRefresh)
            trials_18.addData('blender31.started', blender31.tStartRefresh)
            trials_18.addData('blender31.stopped', blender31.tStopRefresh)
            trials_18.addData('quickkey31.started', quickkey31.tStartRefresh)
            trials_18.addData('quickkey31.stopped', quickkey31.tStopRefresh)
            trials_18.addData('blenderquickkey31.started', blenderquickkey31.tStartRefresh)
            trials_18.addData('blenderquickkey31.stopped', blenderquickkey31.tStopRefresh)
            # the Routine "video3_1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath32 repeats of 'trials_18'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_19 = data.TrialHandler(nReps=videopath33, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_19')
        thisExp.addLoop(trials_19)  # add the loop to the experiment
        thisTrial_19 = trials_19.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_19.rgb)
        if thisTrial_19 != None:
            for paramName in thisTrial_19:
                exec('{} = thisTrial_19[paramName]'.format(paramName))
        
        for thisTrial_19 in trials_19:
            currentLoop = trials_19
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_19.rgb)
            if thisTrial_19 != None:
                for paramName in thisTrial_19:
                    exec('{} = thisTrial_19[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video3_2"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_20.keys = []
            key_resp_20.rt = []
            _key_resp_20_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp32)!=0:
                movie_20.pause()
                movie_20.seek(int(remembertimestamp32[-1]))
                movie_20.play()
                Time1 = 0
            showf=0
            enter1=0  
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_20
            mouse_20.x = []
            mouse_20.y = []
            mouse_20.leftButton = []
            mouse_20.midButton = []
            mouse_20.rightButton = []
            mouse_20.time = []
            mouse_20.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_20.mouseClock.reset()
            # keep track of which components have finished
            video3_2Components = [key_resp_20, mouse_20, backvideo32, movie_20, closevideo_20, blender32, quickkey32, blenderquickkey32]
            for thisComponent in video3_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video3_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video3_2"-------
            while continueRoutine:
                # get current time
                t = video3_2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video3_2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_20* updates
                waitOnFlip = False
                if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_20.frameNStart = frameN  # exact frame index
                    key_resp_20.tStart = t  # local t and not account for scr refresh
                    key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
                    key_resp_20.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_20.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_20.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_20_allKeys.extend(theseKeys)
                    if len(_key_resp_20_allKeys):
                        key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
                        key_resp_20.rt = _key_resp_20_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey32.setAutoDraw(False)
                    blenderquickkey32.setAutoDraw(False)
                if (blender%2)!=1:
                    blender32.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_20.status == PLAYING:
                            movie_20.pause()
                            Time1 = 1
                        elif movie_20.status == PAUSED:
                            movie_20.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_20.pause()
                        ntime = max(0.0,movie_20.duration)
                        movie_20.seek(ntime)
                        movie_20.play()
                        Time1 = 0
                    if movie_20.status == PLAYING:
                        if key=='period':
                            movie_20.pause()
                            ntime = min(movie_20.getCurrentFrameTime( ) + 5.0,movie_20.duration)
                            movie_20.seek(ntime)
                            movie_20.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_20.pause()
                            ntime = max(movie_20.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_20.seek(ntime)
                            movie_20.play() 
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey32.setAutoDraw(True)    
                                blenderquickkey32.setAutoDraw(False) 
                                movie_20.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey32.setAutoDraw(True) 
                                quickkey32.setAutoDraw(False)
                                movie_20.pause()
                            else:
                                blenderquickkey32.setAutoDraw(False) 
                                quickkey32.setAutoDraw(False)
                                movie_20.play()
                
                    elif movie_20.status == PAUSED:
                        if key=='period':
                            movie_20.pause()
                            ntime = min(movie_20.getCurrentFrameTime( ) + 5.0,movie_20.duration)
                            movie_20.seek(ntime)
                            movie_20.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_20.pause()
                            ntime = max(movie_20.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_20.seek(ntime)
                            movie_20.play() 
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_20.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey32.setAutoDraw(True)    
                                blenderquickkey32.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey32.setAutoDraw(True) 
                                quickkey32.setAutoDraw(False)
                            else:
                                blenderquickkey32.setAutoDraw(False) 
                                quickkey32.setAutoDraw(False)
                   
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey32.setAutoDraw(True)    
                            blenderquickkey32.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey32.setAutoDraw(True) 
                            quickkey32.setAutoDraw(False)
                        else:
                            blenderquickkey32.setAutoDraw(False) 
                            quickkey32.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video3-2 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender32.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video3-2 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender32.setAutoDraw(False)
                # *mouse_20* updates
                if mouse_20.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_20.frameNStart = frameN  # exact frame index
                    mouse_20.tStart = t  # local t and not account for scr refresh
                    mouse_20.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_20, 'tStartRefresh')  # time at next scr refresh
                    mouse_20.status = STARTED
                    prevButtonState = mouse_20.getPressed()  # if button is down already this ISN'T a new click
                if mouse_20.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_20.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_20,]:
                                if obj.contains(mouse_20):
                                    gotValidClick = True
                                    mouse_20.clicked_name.append(obj.name)
                            x, y = mouse_20.getPos()
                            mouse_20.x.append(x)
                            mouse_20.y.append(y)
                            buttons = mouse_20.getPressed()
                            mouse_20.leftButton.append(buttons[0])
                            mouse_20.midButton.append(buttons[1])
                            mouse_20.rightButton.append(buttons[2])
                            mouse_20.time.append(mouse_20.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo32* updates
                if backvideo32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo32.frameNStart = frameN  # exact frame index
                    backvideo32.tStart = t  # local t and not account for scr refresh
                    backvideo32.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo32, 'tStartRefresh')  # time at next scr refresh
                    backvideo32.setAutoDraw(True)
                
                # *movie_20* updates
                if movie_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_20.frameNStart = frameN  # exact frame index
                    movie_20.tStart = t  # local t and not account for scr refresh
                    movie_20.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_20, 'tStartRefresh')  # time at next scr refresh
                    movie_20.setAutoDraw(True)
                
                # *closevideo_20* updates
                if closevideo_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_20.frameNStart = frameN  # exact frame index
                    closevideo_20.tStart = t  # local t and not account for scr refresh
                    closevideo_20.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_20, 'tStartRefresh')  # time at next scr refresh
                    closevideo_20.setAutoDraw(True)
                
                # *blender32* updates
                if blender32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender32.frameNStart = frameN  # exact frame index
                    blender32.tStart = t  # local t and not account for scr refresh
                    blender32.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender32, 'tStartRefresh')  # time at next scr refresh
                    blender32.setAutoDraw(True)
                
                # *quickkey32* updates
                if quickkey32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey32.frameNStart = frameN  # exact frame index
                    quickkey32.tStart = t  # local t and not account for scr refresh
                    quickkey32.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey32, 'tStartRefresh')  # time at next scr refresh
                    quickkey32.setAutoDraw(True)
                
                # *blenderquickkey32* updates
                if blenderquickkey32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey32.frameNStart = frameN  # exact frame index
                    blenderquickkey32.tStart = t  # local t and not account for scr refresh
                    blenderquickkey32.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey32, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey32.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video3_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video3_2"-------
            for thisComponent in video3_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_20.keys in ['', [], None]:  # No response was made
                key_resp_20.keys = None
            trials_19.addData('key_resp_20.keys',key_resp_20.keys)
            if key_resp_20.keys != None:  # we had a response
                trials_19.addData('key_resp_20.rt', key_resp_20.rt)
            trials_19.addData('key_resp_20.started', key_resp_20.tStartRefresh)
            trials_19.addData('key_resp_20.stopped', key_resp_20.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime()) 
                    allsteptime.append('video3-2 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video3-2 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_20.getCurrentFrameTime( )
                remembertimestamp32.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime15.append(sum(Watchtime1))
            #    allsteptime.append('video3-2 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime15.append(sum(Watchtime1))
            #    allsteptime.append('video3-2 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
                
            totalpath3=1
            # store data for trials_19 (TrialHandler)
            if len(mouse_20.x): trials_19.addData('mouse_20.x', mouse_20.x[0])
            if len(mouse_20.y): trials_19.addData('mouse_20.y', mouse_20.y[0])
            if len(mouse_20.leftButton): trials_19.addData('mouse_20.leftButton', mouse_20.leftButton[0])
            if len(mouse_20.midButton): trials_19.addData('mouse_20.midButton', mouse_20.midButton[0])
            if len(mouse_20.rightButton): trials_19.addData('mouse_20.rightButton', mouse_20.rightButton[0])
            if len(mouse_20.time): trials_19.addData('mouse_20.time', mouse_20.time[0])
            if len(mouse_20.clicked_name): trials_19.addData('mouse_20.clicked_name', mouse_20.clicked_name[0])
            trials_19.addData('mouse_20.started', mouse_20.tStart)
            trials_19.addData('mouse_20.stopped', mouse_20.tStop)
            trials_19.addData('backvideo32.started', backvideo32.tStartRefresh)
            trials_19.addData('backvideo32.stopped', backvideo32.tStopRefresh)
            movie_20.stop()
            trials_19.addData('closevideo_20.started', closevideo_20.tStartRefresh)
            trials_19.addData('closevideo_20.stopped', closevideo_20.tStopRefresh)
            trials_19.addData('blender32.started', blender32.tStartRefresh)
            trials_19.addData('blender32.stopped', blender32.tStopRefresh)
            trials_19.addData('quickkey32.started', quickkey32.tStartRefresh)
            trials_19.addData('quickkey32.stopped', quickkey32.tStopRefresh)
            trials_19.addData('blenderquickkey32.started', blenderquickkey32.tStartRefresh)
            trials_19.addData('blenderquickkey32.stopped', blenderquickkey32.tStopRefresh)
            # the Routine "video3_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath33 repeats of 'trials_19'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_20 = data.TrialHandler(nReps=videopath34, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_20')
        thisExp.addLoop(trials_20)  # add the loop to the experiment
        thisTrial_20 = trials_20.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_20.rgb)
        if thisTrial_20 != None:
            for paramName in thisTrial_20:
                exec('{} = thisTrial_20[paramName]'.format(paramName))
        
        for thisTrial_20 in trials_20:
            currentLoop = trials_20
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_20.rgb)
            if thisTrial_20 != None:
                for paramName in thisTrial_20:
                    exec('{} = thisTrial_20[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video3_3"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_21.keys = []
            key_resp_21.rt = []
            _key_resp_21_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp33)!=0:
                movie_21.pause()
                movie_21.seek(int(remembertimestamp33[-1]))
                movie_21.play()
                Time1 = 0
            showf=0
            enter1=0  
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_21
            mouse_21.x = []
            mouse_21.y = []
            mouse_21.leftButton = []
            mouse_21.midButton = []
            mouse_21.rightButton = []
            mouse_21.time = []
            mouse_21.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_21.mouseClock.reset()
            # keep track of which components have finished
            video3_3Components = [key_resp_21, mouse_21, backvideo33, movie_21, closevideo_21, blender33, quickkey33, blenderquickkey33]
            for thisComponent in video3_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video3_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video3_3"-------
            while continueRoutine:
                # get current time
                t = video3_3Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video3_3Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_21* updates
                waitOnFlip = False
                if key_resp_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_21.frameNStart = frameN  # exact frame index
                    key_resp_21.tStart = t  # local t and not account for scr refresh
                    key_resp_21.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_21, 'tStartRefresh')  # time at next scr refresh
                    key_resp_21.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_21.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_21.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_21.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_21.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_21_allKeys.extend(theseKeys)
                    if len(_key_resp_21_allKeys):
                        key_resp_21.keys = _key_resp_21_allKeys[-1].name  # just the last key pressed
                        key_resp_21.rt = _key_resp_21_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey33.setAutoDraw(False)
                    blenderquickkey33.setAutoDraw(False)
                if (blender%2)!=1:
                    blender33.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_21.status == PLAYING:
                            movie_21.pause()
                            Time1 = 1
                        elif movie_21.status == PAUSED:
                            movie_21.play()
                            Time1 = 0
                    elif key=='s':
                        change=change+1
                        movie_21.pause()
                        ntime = max(0.0,movie_21.duration)
                        movie_21.seek(ntime)
                        movie_21.play()
                        Time1 = 0
                    if movie_21.status == PLAYING:
                        if key=='period':
                            movie_21.pause()
                            ntime = min(movie_21.getCurrentFrameTime( ) + 5.0, movie_21.duration)
                            movie_21.seek(ntime)
                            movie_21.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_21.pause()
                            ntime = max(movie_21.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_21.seek(ntime)
                            movie_21.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey33.setAutoDraw(True)  
                                blenderquickkey33.setAutoDraw(False) 
                                movie_21.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey33.setAutoDraw(True) 
                                quickkey33.setAutoDraw(False)
                                movie_21.pause()
                            else:
                                blenderquickkey33.setAutoDraw(False) 
                                quickkey33.setAutoDraw(False)
                                movie_21.play()
                     
                    elif movie_21.status == PAUSED:
                        if key=='period':
                            movie_21.pause()
                            ntime = min(movie_21.getCurrentFrameTime( ) + 5.0, movie_21.duration)
                            movie_21.seek(ntime)
                            movie_21.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_21.pause()
                            ntime = max(movie_21.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_21.seek(ntime)
                            movie_21.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_21.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey33.setAutoDraw(True)  
                                blenderquickkey33.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey33.setAutoDraw(True) 
                                quickkey33.setAutoDraw(False)
                            else:
                                blenderquickkey33.setAutoDraw(False) 
                                quickkey33.setAutoDraw(False)
                              
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey33.setAutoDraw(True)  
                            blenderquickkey33.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey33.setAutoDraw(True) 
                            quickkey33.setAutoDraw(False)
                        else:
                            blenderquickkey33.setAutoDraw(False) 
                            quickkey33.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video3-3 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender33.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video3-3 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender33.setAutoDraw(False)
                # *mouse_21* updates
                if mouse_21.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_21.frameNStart = frameN  # exact frame index
                    mouse_21.tStart = t  # local t and not account for scr refresh
                    mouse_21.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_21, 'tStartRefresh')  # time at next scr refresh
                    mouse_21.status = STARTED
                    prevButtonState = mouse_21.getPressed()  # if button is down already this ISN'T a new click
                if mouse_21.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_21.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_21,]:
                                if obj.contains(mouse_21):
                                    gotValidClick = True
                                    mouse_21.clicked_name.append(obj.name)
                            x, y = mouse_21.getPos()
                            mouse_21.x.append(x)
                            mouse_21.y.append(y)
                            buttons = mouse_21.getPressed()
                            mouse_21.leftButton.append(buttons[0])
                            mouse_21.midButton.append(buttons[1])
                            mouse_21.rightButton.append(buttons[2])
                            mouse_21.time.append(mouse_21.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo33* updates
                if backvideo33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo33.frameNStart = frameN  # exact frame index
                    backvideo33.tStart = t  # local t and not account for scr refresh
                    backvideo33.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo33, 'tStartRefresh')  # time at next scr refresh
                    backvideo33.setAutoDraw(True)
                
                # *movie_21* updates
                if movie_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_21.frameNStart = frameN  # exact frame index
                    movie_21.tStart = t  # local t and not account for scr refresh
                    movie_21.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_21, 'tStartRefresh')  # time at next scr refresh
                    movie_21.setAutoDraw(True)
                
                # *closevideo_21* updates
                if closevideo_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_21.frameNStart = frameN  # exact frame index
                    closevideo_21.tStart = t  # local t and not account for scr refresh
                    closevideo_21.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_21, 'tStartRefresh')  # time at next scr refresh
                    closevideo_21.setAutoDraw(True)
                
                # *blender33* updates
                if blender33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender33.frameNStart = frameN  # exact frame index
                    blender33.tStart = t  # local t and not account for scr refresh
                    blender33.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender33, 'tStartRefresh')  # time at next scr refresh
                    blender33.setAutoDraw(True)
                
                # *quickkey33* updates
                if quickkey33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey33.frameNStart = frameN  # exact frame index
                    quickkey33.tStart = t  # local t and not account for scr refresh
                    quickkey33.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey33, 'tStartRefresh')  # time at next scr refresh
                    quickkey33.setAutoDraw(True)
                
                # *blenderquickkey33* updates
                if blenderquickkey33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey33.frameNStart = frameN  # exact frame index
                    blenderquickkey33.tStart = t  # local t and not account for scr refresh
                    blenderquickkey33.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey33, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey33.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video3_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video3_3"-------
            for thisComponent in video3_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_21.keys in ['', [], None]:  # No response was made
                key_resp_21.keys = None
            trials_20.addData('key_resp_21.keys',key_resp_21.keys)
            if key_resp_21.keys != None:  # we had a response
                trials_20.addData('key_resp_21.rt', key_resp_21.rt)
            trials_20.addData('key_resp_21.started', key_resp_21.tStartRefresh)
            trials_20.addData('key_resp_21.stopped', key_resp_21.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime())  
                    allsteptime.append('video3-3 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video3-3 blender')
                    allsteptime.append(BlenderClock.getTime())
                    
                change=change+1
                nowtime=movie_21.getCurrentFrameTime( )
                remembertimestamp33.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime16.append(sum(Watchtime1))
            #    allsteptime.append('video3-3 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime16.append(sum(Watchtime1))
            #    allsteptime.append('video3-3 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
                
            totalpath3=1
            # store data for trials_20 (TrialHandler)
            if len(mouse_21.x): trials_20.addData('mouse_21.x', mouse_21.x[0])
            if len(mouse_21.y): trials_20.addData('mouse_21.y', mouse_21.y[0])
            if len(mouse_21.leftButton): trials_20.addData('mouse_21.leftButton', mouse_21.leftButton[0])
            if len(mouse_21.midButton): trials_20.addData('mouse_21.midButton', mouse_21.midButton[0])
            if len(mouse_21.rightButton): trials_20.addData('mouse_21.rightButton', mouse_21.rightButton[0])
            if len(mouse_21.time): trials_20.addData('mouse_21.time', mouse_21.time[0])
            if len(mouse_21.clicked_name): trials_20.addData('mouse_21.clicked_name', mouse_21.clicked_name[0])
            trials_20.addData('mouse_21.started', mouse_21.tStart)
            trials_20.addData('mouse_21.stopped', mouse_21.tStop)
            trials_20.addData('backvideo33.started', backvideo33.tStartRefresh)
            trials_20.addData('backvideo33.stopped', backvideo33.tStopRefresh)
            movie_21.stop()
            trials_20.addData('closevideo_21.started', closevideo_21.tStartRefresh)
            trials_20.addData('closevideo_21.stopped', closevideo_21.tStopRefresh)
            trials_20.addData('blender33.started', blender33.tStartRefresh)
            trials_20.addData('blender33.stopped', blender33.tStopRefresh)
            trials_20.addData('quickkey33.started', quickkey33.tStartRefresh)
            trials_20.addData('quickkey33.stopped', quickkey33.tStopRefresh)
            trials_20.addData('blenderquickkey33.started', blenderquickkey33.tStartRefresh)
            trials_20.addData('blenderquickkey33.stopped', blenderquickkey33.tStopRefresh)
            # the Routine "video3_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath34 repeats of 'trials_20'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_21 = data.TrialHandler(nReps=videopath35, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_21')
        thisExp.addLoop(trials_21)  # add the loop to the experiment
        thisTrial_21 = trials_21.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_21.rgb)
        if thisTrial_21 != None:
            for paramName in thisTrial_21:
                exec('{} = thisTrial_21[paramName]'.format(paramName))
        
        for thisTrial_21 in trials_21:
            currentLoop = trials_21
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_21.rgb)
            if thisTrial_21 != None:
                for paramName in thisTrial_21:
                    exec('{} = thisTrial_21[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video3_4"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_22.keys = []
            key_resp_22.rt = []
            _key_resp_22_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp34)!=0:
                movie_22.pause()
                movie_22.seek(int(remembertimestamp34[-1]))
                movie_22.play()
                Time1 = 0
            showf=0
            enter1=0 
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_22
            mouse_22.x = []
            mouse_22.y = []
            mouse_22.leftButton = []
            mouse_22.midButton = []
            mouse_22.rightButton = []
            mouse_22.time = []
            mouse_22.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_22.mouseClock.reset()
            # keep track of which components have finished
            video3_4Components = [key_resp_22, mouse_22, backvideo34, movie_22, closevideo_22, blender34, quickkey34, blenderquickkey34]
            for thisComponent in video3_4Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video3_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video3_4"-------
            while continueRoutine:
                # get current time
                t = video3_4Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video3_4Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_22* updates
                waitOnFlip = False
                if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_22.frameNStart = frameN  # exact frame index
                    key_resp_22.tStart = t  # local t and not account for scr refresh
                    key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
                    key_resp_22.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_22.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_22.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_22_allKeys.extend(theseKeys)
                    if len(_key_resp_22_allKeys):
                        key_resp_22.keys = _key_resp_22_allKeys[-1].name  # just the last key pressed
                        key_resp_22.rt = _key_resp_22_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey34.setAutoDraw(False)
                    blenderquickkey34.setAutoDraw(False)
                if (blender%2)!=1:
                    blender34.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_22.status == PLAYING:
                            movie_22.pause()
                            Time1 = 1
                        elif movie_22.status == PAUSED:  
                            movie_22.play()
                            Time1 = 0
                    elif key=='s':
                        change=change+1
                        movie_22.pause()
                        ntime = max(0.0,movie_22.duration)
                        movie_22.seek(ntime)
                        movie_22.play()       
                        Time1 = 0    
                    if movie_22.status == PLAYING:
                        if key=='period':
                            movie_22.pause()
                            ntime = min(movie_22.getCurrentFrameTime( ) + 5.0, movie_22.duration)
                            movie_22.seek(ntime)
                            movie_22.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma':
                            movie_22.pause()
                            ntime = max(movie_22.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_22.seek(ntime)
                            movie_22.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey34.setAutoDraw(True)    
                                blenderquickkey34.setAutoDraw(False) 
                                movie_22.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey34.setAutoDraw(True) 
                                quickkey34.setAutoDraw(False)
                                movie_22.pause()
                            else:
                                blenderquickkey34.setAutoDraw(False) 
                                quickkey34.setAutoDraw(False)
                                movie_22.play()
                       
                    elif movie_22.status == PAUSED:
                        if key=='period':
                            movie_22.pause()
                            ntime = min(movie_22.getCurrentFrameTime( ) + 5.0, movie_22.duration)
                            movie_22.seek(ntime)
                            movie_22.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma':
                            movie_22.pause()
                            ntime = max(movie_22.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_22.seek(ntime)
                            movie_22.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_22.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey34.setAutoDraw(True)    
                                blenderquickkey34.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey34.setAutoDraw(True) 
                                quickkey34.setAutoDraw(False)
                            else:
                                blenderquickkey34.setAutoDraw(False) 
                                quickkey34.setAutoDraw(False)
                           
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey34.setAutoDraw(True)    
                            blenderquickkey34.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey34.setAutoDraw(True) 
                            quickkey34.setAutoDraw(False)
                        else:
                            blenderquickkey34.setAutoDraw(False) 
                            quickkey34.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video3-4 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender34.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video3-4 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender34.setAutoDraw(False)
                # *mouse_22* updates
                if mouse_22.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_22.frameNStart = frameN  # exact frame index
                    mouse_22.tStart = t  # local t and not account for scr refresh
                    mouse_22.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_22, 'tStartRefresh')  # time at next scr refresh
                    mouse_22.status = STARTED
                    prevButtonState = mouse_22.getPressed()  # if button is down already this ISN'T a new click
                if mouse_22.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_22.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_22,]:
                                if obj.contains(mouse_22):
                                    gotValidClick = True
                                    mouse_22.clicked_name.append(obj.name)
                            x, y = mouse_22.getPos()
                            mouse_22.x.append(x)
                            mouse_22.y.append(y)
                            buttons = mouse_22.getPressed()
                            mouse_22.leftButton.append(buttons[0])
                            mouse_22.midButton.append(buttons[1])
                            mouse_22.rightButton.append(buttons[2])
                            mouse_22.time.append(mouse_22.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo34* updates
                if backvideo34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo34.frameNStart = frameN  # exact frame index
                    backvideo34.tStart = t  # local t and not account for scr refresh
                    backvideo34.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo34, 'tStartRefresh')  # time at next scr refresh
                    backvideo34.setAutoDraw(True)
                
                # *movie_22* updates
                if movie_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_22.frameNStart = frameN  # exact frame index
                    movie_22.tStart = t  # local t and not account for scr refresh
                    movie_22.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_22, 'tStartRefresh')  # time at next scr refresh
                    movie_22.setAutoDraw(True)
                
                # *closevideo_22* updates
                if closevideo_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_22.frameNStart = frameN  # exact frame index
                    closevideo_22.tStart = t  # local t and not account for scr refresh
                    closevideo_22.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_22, 'tStartRefresh')  # time at next scr refresh
                    closevideo_22.setAutoDraw(True)
                
                # *blender34* updates
                if blender34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender34.frameNStart = frameN  # exact frame index
                    blender34.tStart = t  # local t and not account for scr refresh
                    blender34.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender34, 'tStartRefresh')  # time at next scr refresh
                    blender34.setAutoDraw(True)
                
                # *quickkey34* updates
                if quickkey34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey34.frameNStart = frameN  # exact frame index
                    quickkey34.tStart = t  # local t and not account for scr refresh
                    quickkey34.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey34, 'tStartRefresh')  # time at next scr refresh
                    quickkey34.setAutoDraw(True)
                
                # *blenderquickkey34* updates
                if blenderquickkey34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey34.frameNStart = frameN  # exact frame index
                    blenderquickkey34.tStart = t  # local t and not account for scr refresh
                    blenderquickkey34.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey34, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey34.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video3_4Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video3_4"-------
            for thisComponent in video3_4Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_22.keys in ['', [], None]:  # No response was made
                key_resp_22.keys = None
            trials_21.addData('key_resp_22.keys',key_resp_22.keys)
            if key_resp_22.keys != None:  # we had a response
                trials_21.addData('key_resp_22.rt', key_resp_22.rt)
            trials_21.addData('key_resp_22.started', key_resp_22.tStartRefresh)
            trials_21.addData('key_resp_22.stopped', key_resp_22.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime())  
                    allsteptime.append('video3-4 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video3-4 blender')
                    allsteptime.append(BlenderClock.getTime())
                    
                change=change+1
                nowtime=movie_22.getCurrentFrameTime( )
                remembertimestamp34.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime17.append(sum(Watchtime1))
            #    allsteptime.append('video3-4 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime17.append(sum(Watchtime1))
            #    allsteptime.append('video3-4 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
                
            totalpath3=1
                
            # store data for trials_21 (TrialHandler)
            if len(mouse_22.x): trials_21.addData('mouse_22.x', mouse_22.x[0])
            if len(mouse_22.y): trials_21.addData('mouse_22.y', mouse_22.y[0])
            if len(mouse_22.leftButton): trials_21.addData('mouse_22.leftButton', mouse_22.leftButton[0])
            if len(mouse_22.midButton): trials_21.addData('mouse_22.midButton', mouse_22.midButton[0])
            if len(mouse_22.rightButton): trials_21.addData('mouse_22.rightButton', mouse_22.rightButton[0])
            if len(mouse_22.time): trials_21.addData('mouse_22.time', mouse_22.time[0])
            if len(mouse_22.clicked_name): trials_21.addData('mouse_22.clicked_name', mouse_22.clicked_name[0])
            trials_21.addData('mouse_22.started', mouse_22.tStart)
            trials_21.addData('mouse_22.stopped', mouse_22.tStop)
            trials_21.addData('backvideo34.started', backvideo34.tStartRefresh)
            trials_21.addData('backvideo34.stopped', backvideo34.tStopRefresh)
            movie_22.stop()
            trials_21.addData('closevideo_22.started', closevideo_22.tStartRefresh)
            trials_21.addData('closevideo_22.stopped', closevideo_22.tStopRefresh)
            trials_21.addData('blender34.started', blender34.tStartRefresh)
            trials_21.addData('blender34.stopped', blender34.tStopRefresh)
            trials_21.addData('quickkey34.started', quickkey34.tStartRefresh)
            trials_21.addData('quickkey34.stopped', quickkey34.tStopRefresh)
            trials_21.addData('blenderquickkey34.started', blenderquickkey34.tStartRefresh)
            trials_21.addData('blenderquickkey34.stopped', blenderquickkey34.tStopRefresh)
            # the Routine "video3_4" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath35 repeats of 'trials_21'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_22 = data.TrialHandler(nReps=videopath36, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_22')
        thisExp.addLoop(trials_22)  # add the loop to the experiment
        thisTrial_22 = trials_22.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_22.rgb)
        if thisTrial_22 != None:
            for paramName in thisTrial_22:
                exec('{} = thisTrial_22[paramName]'.format(paramName))
        
        for thisTrial_22 in trials_22:
            currentLoop = trials_22
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_22.rgb)
            if thisTrial_22 != None:
                for paramName in thisTrial_22:
                    exec('{} = thisTrial_22[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video3_5"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_23.keys = []
            key_resp_23.rt = []
            _key_resp_23_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp35)!=0:
                movie_23.pause()
                movie_23.seek(int(remembertimestamp35[-1]))
                movie_23.play()
                Time1 = 0
            showf=0
            enter1=0    
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_23
            mouse_23.x = []
            mouse_23.y = []
            mouse_23.leftButton = []
            mouse_23.midButton = []
            mouse_23.rightButton = []
            mouse_23.time = []
            mouse_23.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_23.mouseClock.reset()
            # keep track of which components have finished
            video3_5Components = [key_resp_23, mouse_23, backvideo35, movie_23, closevideo_23, blender35, quickkey35, blenderquickkey35]
            for thisComponent in video3_5Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video3_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video3_5"-------
            while continueRoutine:
                # get current time
                t = video3_5Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video3_5Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_23* updates
                waitOnFlip = False
                if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_23.frameNStart = frameN  # exact frame index
                    key_resp_23.tStart = t  # local t and not account for scr refresh
                    key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
                    key_resp_23.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_23.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_23.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_23_allKeys.extend(theseKeys)
                    if len(_key_resp_23_allKeys):
                        key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
                        key_resp_23.rt = _key_resp_23_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey35.setAutoDraw(False)
                    blenderquickkey35.setAutoDraw(False)
                if (blender%2)!=1:
                    blender35.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_23.status == PLAYING:
                            movie_23.pause()
                            Time1 = 1
                        elif movie_23.status == PAUSED:
                            movie_23.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_23.pause()
                        ntime = max(0.0,movie_23.duration)
                        movie_23.seek(ntime)
                        movie_23.play()     
                        Time1 = 0   
                    if movie_23.status == PLAYING:
                        if key=='period':
                            movie_23.pause()
                            ntime = min(movie_23.getCurrentFrameTime( ) + 5.0, movie_23.duration)
                            movie_23.seek(ntime)
                            movie_23.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_23.pause()
                            ntime = max(movie_23.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_23.seek(ntime)
                            movie_23.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            showf=showf+1
                            countcontinue=countcontinue+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey35.setAutoDraw(True)    
                                blenderquickkey35.setAutoDraw(False) 
                                movie_23.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey35.setAutoDraw(True) 
                                quickkey35.setAutoDraw(False)
                                movie_23.pause()
                            else:
                                blenderquickkey35.setAutoDraw(False) 
                                quickkey35.setAutoDraw(False)
                                movie_23.play()
                                            
                    elif movie_23.status == PAUSED:       
                        if key=='period':
                            movie_23.pause()
                            ntime = min(movie_23.getCurrentFrameTime( ) + 5.0, movie_23.duration)
                            movie_23.seek(ntime)
                            movie_23.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_23.pause()
                            ntime = max(movie_23.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_23.seek(ntime)
                            movie_23.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_23.pause()
                            showf=showf+1
                            countcontinue=countcontinue+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey35.setAutoDraw(True)    
                                blenderquickkey35.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey35.setAutoDraw(True) 
                                quickkey35.setAutoDraw(False)
                            else:
                                blenderquickkey35.setAutoDraw(False) 
                                quickkey35.setAutoDraw(False)
                         
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey35.setAutoDraw(True)    
                            blenderquickkey35.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey35.setAutoDraw(True) 
                            quickkey35.setAutoDraw(False)
                        else:
                            blenderquickkey35.setAutoDraw(False) 
                            quickkey35.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video3-5 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender35.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video3-5 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender35.setAutoDraw(False)
                # *mouse_23* updates
                if mouse_23.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_23.frameNStart = frameN  # exact frame index
                    mouse_23.tStart = t  # local t and not account for scr refresh
                    mouse_23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_23, 'tStartRefresh')  # time at next scr refresh
                    mouse_23.status = STARTED
                    prevButtonState = mouse_23.getPressed()  # if button is down already this ISN'T a new click
                if mouse_23.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_23.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_23,]:
                                if obj.contains(mouse_23):
                                    gotValidClick = True
                                    mouse_23.clicked_name.append(obj.name)
                            x, y = mouse_23.getPos()
                            mouse_23.x.append(x)
                            mouse_23.y.append(y)
                            buttons = mouse_23.getPressed()
                            mouse_23.leftButton.append(buttons[0])
                            mouse_23.midButton.append(buttons[1])
                            mouse_23.rightButton.append(buttons[2])
                            mouse_23.time.append(mouse_23.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo35* updates
                if backvideo35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo35.frameNStart = frameN  # exact frame index
                    backvideo35.tStart = t  # local t and not account for scr refresh
                    backvideo35.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo35, 'tStartRefresh')  # time at next scr refresh
                    backvideo35.setAutoDraw(True)
                
                # *movie_23* updates
                if movie_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_23.frameNStart = frameN  # exact frame index
                    movie_23.tStart = t  # local t and not account for scr refresh
                    movie_23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_23, 'tStartRefresh')  # time at next scr refresh
                    movie_23.setAutoDraw(True)
                
                # *closevideo_23* updates
                if closevideo_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_23.frameNStart = frameN  # exact frame index
                    closevideo_23.tStart = t  # local t and not account for scr refresh
                    closevideo_23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_23, 'tStartRefresh')  # time at next scr refresh
                    closevideo_23.setAutoDraw(True)
                
                # *blender35* updates
                if blender35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender35.frameNStart = frameN  # exact frame index
                    blender35.tStart = t  # local t and not account for scr refresh
                    blender35.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender35, 'tStartRefresh')  # time at next scr refresh
                    blender35.setAutoDraw(True)
                
                # *quickkey35* updates
                if quickkey35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey35.frameNStart = frameN  # exact frame index
                    quickkey35.tStart = t  # local t and not account for scr refresh
                    quickkey35.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey35, 'tStartRefresh')  # time at next scr refresh
                    quickkey35.setAutoDraw(True)
                
                # *blenderquickkey35* updates
                if blenderquickkey35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey35.frameNStart = frameN  # exact frame index
                    blenderquickkey35.tStart = t  # local t and not account for scr refresh
                    blenderquickkey35.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey35, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey35.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video3_5Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video3_5"-------
            for thisComponent in video3_5Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_23.keys in ['', [], None]:  # No response was made
                key_resp_23.keys = None
            trials_22.addData('key_resp_23.keys',key_resp_23.keys)
            if key_resp_23.keys != None:  # we had a response
                trials_22.addData('key_resp_23.rt', key_resp_23.rt)
            trials_22.addData('key_resp_23.started', key_resp_23.tStartRefresh)
            trials_22.addData('key_resp_23.stopped', key_resp_23.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime()) 
                    allsteptime.append('video3-5 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video3-5 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_23.getCurrentFrameTime( )
                remembertimestamp35.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime18.append(sum(Watchtime1))
            #    allsteptime.append('video3-5 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime18.append(sum(Watchtime1))
            #    allsteptime.append('video3-5 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            
            totalpath3=1
            # store data for trials_22 (TrialHandler)
            if len(mouse_23.x): trials_22.addData('mouse_23.x', mouse_23.x[0])
            if len(mouse_23.y): trials_22.addData('mouse_23.y', mouse_23.y[0])
            if len(mouse_23.leftButton): trials_22.addData('mouse_23.leftButton', mouse_23.leftButton[0])
            if len(mouse_23.midButton): trials_22.addData('mouse_23.midButton', mouse_23.midButton[0])
            if len(mouse_23.rightButton): trials_22.addData('mouse_23.rightButton', mouse_23.rightButton[0])
            if len(mouse_23.time): trials_22.addData('mouse_23.time', mouse_23.time[0])
            if len(mouse_23.clicked_name): trials_22.addData('mouse_23.clicked_name', mouse_23.clicked_name[0])
            trials_22.addData('mouse_23.started', mouse_23.tStart)
            trials_22.addData('mouse_23.stopped', mouse_23.tStop)
            trials_22.addData('backvideo35.started', backvideo35.tStartRefresh)
            trials_22.addData('backvideo35.stopped', backvideo35.tStopRefresh)
            movie_23.stop()
            trials_22.addData('closevideo_23.started', closevideo_23.tStartRefresh)
            trials_22.addData('closevideo_23.stopped', closevideo_23.tStopRefresh)
            trials_22.addData('blender35.started', blender35.tStartRefresh)
            trials_22.addData('blender35.stopped', blender35.tStopRefresh)
            trials_22.addData('quickkey35.started', quickkey35.tStartRefresh)
            trials_22.addData('quickkey35.stopped', quickkey35.tStopRefresh)
            trials_22.addData('blenderquickkey35.started', blenderquickkey35.tStartRefresh)
            trials_22.addData('blenderquickkey35.stopped', blenderquickkey35.tStopRefresh)
            # the Routine "video3_5" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath36 repeats of 'trials_22'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_23 = data.TrialHandler(nReps=videopath37, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_23')
        thisExp.addLoop(trials_23)  # add the loop to the experiment
        thisTrial_23 = trials_23.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_23.rgb)
        if thisTrial_23 != None:
            for paramName in thisTrial_23:
                exec('{} = thisTrial_23[paramName]'.format(paramName))
        
        for thisTrial_23 in trials_23:
            currentLoop = trials_23
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_23.rgb)
            if thisTrial_23 != None:
                for paramName in thisTrial_23:
                    exec('{} = thisTrial_23[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video3_6"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_24.keys = []
            key_resp_24.rt = []
            _key_resp_24_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp36)!=0:
                movie_24.pause()
                movie_24.seek(int(remembertimestamp36[-1]))
                movie_24.play()
                Time1 = 0
            showf=0
            enter1=0   
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
                
            # setup some python lists for storing info about the mouse_24
            mouse_24.x = []
            mouse_24.y = []
            mouse_24.leftButton = []
            mouse_24.midButton = []
            mouse_24.rightButton = []
            mouse_24.time = []
            mouse_24.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_24.mouseClock.reset()
            # keep track of which components have finished
            video3_6Components = [key_resp_24, mouse_24, backvideo36, movie_24, closevideo_24, blender36, quickkey36, blenderquickkey36]
            for thisComponent in video3_6Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video3_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video3_6"-------
            while continueRoutine:
                # get current time
                t = video3_6Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video3_6Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_24* updates
                waitOnFlip = False
                if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_24.frameNStart = frameN  # exact frame index
                    key_resp_24.tStart = t  # local t and not account for scr refresh
                    key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
                    key_resp_24.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_24.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_24.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_24_allKeys.extend(theseKeys)
                    if len(_key_resp_24_allKeys):
                        key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
                        key_resp_24.rt = _key_resp_24_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey36.setAutoDraw(False)
                    blenderquickkey36.setAutoDraw(False)
                if (blender%2)!=1:
                    blender36.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_24.status == PLAYING:
                            movie_24.pause()
                            Time1 = 1
                        elif movie_24.status == PAUSED:
                            movie_24.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_24.pause()
                        ntime = max(0.0,movie_24.duration)
                        movie_24.seek(ntime)
                        movie_24.play()    
                        Time1 = 0      
                    if movie_24.status == PLAYING:
                        if key=='period':
                            movie_24.pause()
                            ntime = min(movie_24.getCurrentFrameTime( ) + 5.0, movie_24.duration)
                            movie_24.seek(ntime)
                            movie_24.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_24.pause()
                            ntime = max(movie_24.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_24.seek(ntime)
                            movie_24.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            showf=showf+1
                            countcontinue=countcontinue+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey36.setAutoDraw(True)    
                                blenderquickkey36.setAutoDraw(False) 
                                movie_24.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey36.setAutoDraw(True) 
                                quickkey36.setAutoDraw(False)
                                movie_24.pause()
                            else:
                                blenderquickkey36.setAutoDraw(False) 
                                quickkey36.setAutoDraw(False)
                                movie_24.play()
                                           
                    elif movie_24.status == PAUSED:
                        if key=='period':
                            movie_24.pause()
                            ntime = min(movie_24.getCurrentFrameTime( ) + 5.0, movie_24.duration)
                            movie_24.seek(ntime)
                            movie_24.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_24.pause()
                            ntime = max(movie_24.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_24.seek(ntime)
                            movie_24.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_24.pause()
                            showf=showf+1
                            countcontinue=countcontinue+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey36.setAutoDraw(True)    
                                blenderquickkey36.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey36.setAutoDraw(True) 
                                quickkey36.setAutoDraw(False)
                            else:
                                blenderquickkey36.setAutoDraw(False) 
                                quickkey36.setAutoDraw(False)
                              
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey36.setAutoDraw(True)    
                            blenderquickkey36.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey36.setAutoDraw(True) 
                            quickkey36.setAutoDraw(False)
                        else:
                            blenderquickkey36.setAutoDraw(False) 
                            quickkey36.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video3-6 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender36.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video3-6 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender36.setAutoDraw(False)
                # *mouse_24* updates
                if mouse_24.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_24.frameNStart = frameN  # exact frame index
                    mouse_24.tStart = t  # local t and not account for scr refresh
                    mouse_24.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_24, 'tStartRefresh')  # time at next scr refresh
                    mouse_24.status = STARTED
                    prevButtonState = mouse_24.getPressed()  # if button is down already this ISN'T a new click
                if mouse_24.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_24.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_24,]:
                                if obj.contains(mouse_24):
                                    gotValidClick = True
                                    mouse_24.clicked_name.append(obj.name)
                            x, y = mouse_24.getPos()
                            mouse_24.x.append(x)
                            mouse_24.y.append(y)
                            buttons = mouse_24.getPressed()
                            mouse_24.leftButton.append(buttons[0])
                            mouse_24.midButton.append(buttons[1])
                            mouse_24.rightButton.append(buttons[2])
                            mouse_24.time.append(mouse_24.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo36* updates
                if backvideo36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo36.frameNStart = frameN  # exact frame index
                    backvideo36.tStart = t  # local t and not account for scr refresh
                    backvideo36.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo36, 'tStartRefresh')  # time at next scr refresh
                    backvideo36.setAutoDraw(True)
                
                # *movie_24* updates
                if movie_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_24.frameNStart = frameN  # exact frame index
                    movie_24.tStart = t  # local t and not account for scr refresh
                    movie_24.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_24, 'tStartRefresh')  # time at next scr refresh
                    movie_24.setAutoDraw(True)
                
                # *closevideo_24* updates
                if closevideo_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_24.frameNStart = frameN  # exact frame index
                    closevideo_24.tStart = t  # local t and not account for scr refresh
                    closevideo_24.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_24, 'tStartRefresh')  # time at next scr refresh
                    closevideo_24.setAutoDraw(True)
                
                # *blender36* updates
                if blender36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender36.frameNStart = frameN  # exact frame index
                    blender36.tStart = t  # local t and not account for scr refresh
                    blender36.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender36, 'tStartRefresh')  # time at next scr refresh
                    blender36.setAutoDraw(True)
                
                # *quickkey36* updates
                if quickkey36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey36.frameNStart = frameN  # exact frame index
                    quickkey36.tStart = t  # local t and not account for scr refresh
                    quickkey36.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey36, 'tStartRefresh')  # time at next scr refresh
                    quickkey36.setAutoDraw(True)
                
                # *blenderquickkey36* updates
                if blenderquickkey36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey36.frameNStart = frameN  # exact frame index
                    blenderquickkey36.tStart = t  # local t and not account for scr refresh
                    blenderquickkey36.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey36, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey36.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video3_6Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video3_6"-------
            for thisComponent in video3_6Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_24.keys in ['', [], None]:  # No response was made
                key_resp_24.keys = None
            trials_23.addData('key_resp_24.keys',key_resp_24.keys)
            if key_resp_24.keys != None:  # we had a response
                trials_23.addData('key_resp_24.rt', key_resp_24.rt)
            trials_23.addData('key_resp_24.started', key_resp_24.tStartRefresh)
            trials_23.addData('key_resp_24.stopped', key_resp_24.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime())  
                    allsteptime.append('video3-6 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video3-6 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_24.getCurrentFrameTime( )
                remembertimestamp36.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime19.append(sum(Watchtime1))
            #    allsteptime.append('video3-6 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime19.append(sum(Watchtime1))
            #    allsteptime.append('video3-6 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
             
            totalpath3=1
            # store data for trials_23 (TrialHandler)
            if len(mouse_24.x): trials_23.addData('mouse_24.x', mouse_24.x[0])
            if len(mouse_24.y): trials_23.addData('mouse_24.y', mouse_24.y[0])
            if len(mouse_24.leftButton): trials_23.addData('mouse_24.leftButton', mouse_24.leftButton[0])
            if len(mouse_24.midButton): trials_23.addData('mouse_24.midButton', mouse_24.midButton[0])
            if len(mouse_24.rightButton): trials_23.addData('mouse_24.rightButton', mouse_24.rightButton[0])
            if len(mouse_24.time): trials_23.addData('mouse_24.time', mouse_24.time[0])
            if len(mouse_24.clicked_name): trials_23.addData('mouse_24.clicked_name', mouse_24.clicked_name[0])
            trials_23.addData('mouse_24.started', mouse_24.tStart)
            trials_23.addData('mouse_24.stopped', mouse_24.tStop)
            trials_23.addData('backvideo36.started', backvideo36.tStartRefresh)
            trials_23.addData('backvideo36.stopped', backvideo36.tStopRefresh)
            movie_24.stop()
            trials_23.addData('closevideo_24.started', closevideo_24.tStartRefresh)
            trials_23.addData('closevideo_24.stopped', closevideo_24.tStopRefresh)
            trials_23.addData('blender36.started', blender36.tStartRefresh)
            trials_23.addData('blender36.stopped', blender36.tStopRefresh)
            trials_23.addData('quickkey36.started', quickkey36.tStartRefresh)
            trials_23.addData('quickkey36.stopped', quickkey36.tStopRefresh)
            trials_23.addData('blenderquickkey36.started', blenderquickkey36.tStartRefresh)
            trials_23.addData('blenderquickkey36.stopped', blenderquickkey36.tStopRefresh)
            # the Routine "video3_6" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath37 repeats of 'trials_23'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_24 = data.TrialHandler(nReps=videopath38, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_24')
        thisExp.addLoop(trials_24)  # add the loop to the experiment
        thisTrial_24 = trials_24.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_24.rgb)
        if thisTrial_24 != None:
            for paramName in thisTrial_24:
                exec('{} = thisTrial_24[paramName]'.format(paramName))
        
        for thisTrial_24 in trials_24:
            currentLoop = trials_24
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_24.rgb)
            if thisTrial_24 != None:
                for paramName in thisTrial_24:
                    exec('{} = thisTrial_24[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video3_7"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_25.keys = []
            key_resp_25.rt = []
            _key_resp_25_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp37)!=0:
                movie_25.pause()
                movie_25.seek(int(remembertimestamp37[-1]))
                movie_25.play()
                Time1 = 0
            showf=0
            enter1=0    
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_25
            mouse_25.x = []
            mouse_25.y = []
            mouse_25.leftButton = []
            mouse_25.midButton = []
            mouse_25.rightButton = []
            mouse_25.time = []
            mouse_25.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_25.mouseClock.reset()
            # keep track of which components have finished
            video3_7Components = [key_resp_25, mouse_25, backvideo37, movie_25, closevideo_25, blender37, quickkey37, blenderquickkey37]
            for thisComponent in video3_7Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video3_7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video3_7"-------
            while continueRoutine:
                # get current time
                t = video3_7Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video3_7Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_25* updates
                waitOnFlip = False
                if key_resp_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_25.frameNStart = frameN  # exact frame index
                    key_resp_25.tStart = t  # local t and not account for scr refresh
                    key_resp_25.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
                    key_resp_25.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_25.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_25.getKeys(keyList=['space', '<', '>', 'return', 'f', 's'], waitRelease=False)
                    _key_resp_25_allKeys.extend(theseKeys)
                    if len(_key_resp_25_allKeys):
                        key_resp_25.keys = _key_resp_25_allKeys[-1].name  # just the last key pressed
                        key_resp_25.rt = _key_resp_25_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey37.setAutoDraw(False)
                    blenderquickkey37.setAutoDraw(False)
                if (blender%2)!=1:
                    blender37.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_25.status == PLAYING:
                            movie_25.pause()
                            Time1 = 1
                        elif movie_25.status == PAUSED:
                            movie_25.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_25.pause()
                        ntime = max(0.0,movie_25.duration)
                        movie_25.seek(ntime)
                        movie_25.play()
                        Time1 = 0
                
                    if movie_25.status == PLAYING:
                        if key=='period':
                            movie_25.pause()
                            ntime = min(movie_25.getCurrentFrameTime( ) + 5.0, movie_25.duration)
                            movie_25.seek(ntime)
                            movie_25.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma':
                            movie_25.pause()
                            ntime = max(movie_25.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_25.seek(ntime)
                            movie_25.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            showf=showf+1
                            countcontinue=countcontinue+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey37.setAutoDraw(True)   
                                blenderquickkey37.setAutoDraw(False)  
                                movie_25.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey37.setAutoDraw(True) 
                                quickkey37.setAutoDraw(False)
                                movie_25.pause()
                            else:
                                blenderquickkey37.setAutoDraw(False)  
                                quickkey37.setAutoDraw(False)
                                movie_25.play()
                                           
                    elif movie_25.status == PAUSED:
                        if key=='period':
                            movie_25.pause()
                            ntime = min(movie_25.getCurrentFrameTime( ) + 5.0, movie_25.duration)
                            movie_25.seek(ntime)
                            movie_25.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma':
                            movie_25.pause()
                            ntime = max(movie_25.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_25.seek(ntime)
                            movie_25.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_25.pause()
                            showf=showf+1
                            countcontinue=countcontinue+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey37.setAutoDraw(True)   
                                blenderquickkey37.setAutoDraw(False)  
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey37.setAutoDraw(True) 
                                quickkey37.setAutoDraw(False)
                            else:
                                blenderquickkey37.setAutoDraw(False)  
                                quickkey37.setAutoDraw(False)
                          
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey37.setAutoDraw(True)   
                            blenderquickkey37.setAutoDraw(False)  
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey37.setAutoDraw(True) 
                            quickkey37.setAutoDraw(False)
                        else:
                            blenderquickkey37.setAutoDraw(False)  
                            quickkey37.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video3-7 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender37.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video3-7 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender37.setAutoDraw(False)
                # *mouse_25* updates
                if mouse_25.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_25.frameNStart = frameN  # exact frame index
                    mouse_25.tStart = t  # local t and not account for scr refresh
                    mouse_25.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_25, 'tStartRefresh')  # time at next scr refresh
                    mouse_25.status = STARTED
                    prevButtonState = mouse_25.getPressed()  # if button is down already this ISN'T a new click
                if mouse_25.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_25.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_25,]:
                                if obj.contains(mouse_25):
                                    gotValidClick = True
                                    mouse_25.clicked_name.append(obj.name)
                            x, y = mouse_25.getPos()
                            mouse_25.x.append(x)
                            mouse_25.y.append(y)
                            buttons = mouse_25.getPressed()
                            mouse_25.leftButton.append(buttons[0])
                            mouse_25.midButton.append(buttons[1])
                            mouse_25.rightButton.append(buttons[2])
                            mouse_25.time.append(mouse_25.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo37* updates
                if backvideo37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo37.frameNStart = frameN  # exact frame index
                    backvideo37.tStart = t  # local t and not account for scr refresh
                    backvideo37.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo37, 'tStartRefresh')  # time at next scr refresh
                    backvideo37.setAutoDraw(True)
                
                # *movie_25* updates
                if movie_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_25.frameNStart = frameN  # exact frame index
                    movie_25.tStart = t  # local t and not account for scr refresh
                    movie_25.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_25, 'tStartRefresh')  # time at next scr refresh
                    movie_25.setAutoDraw(True)
                
                # *closevideo_25* updates
                if closevideo_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_25.frameNStart = frameN  # exact frame index
                    closevideo_25.tStart = t  # local t and not account for scr refresh
                    closevideo_25.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_25, 'tStartRefresh')  # time at next scr refresh
                    closevideo_25.setAutoDraw(True)
                
                # *blender37* updates
                if blender37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender37.frameNStart = frameN  # exact frame index
                    blender37.tStart = t  # local t and not account for scr refresh
                    blender37.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender37, 'tStartRefresh')  # time at next scr refresh
                    blender37.setAutoDraw(True)
                
                # *quickkey37* updates
                if quickkey37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey37.frameNStart = frameN  # exact frame index
                    quickkey37.tStart = t  # local t and not account for scr refresh
                    quickkey37.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey37, 'tStartRefresh')  # time at next scr refresh
                    quickkey37.setAutoDraw(True)
                
                # *blenderquickkey37* updates
                if blenderquickkey37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey37.frameNStart = frameN  # exact frame index
                    blenderquickkey37.tStart = t  # local t and not account for scr refresh
                    blenderquickkey37.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey37, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey37.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video3_7Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video3_7"-------
            for thisComponent in video3_7Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_25.keys in ['', [], None]:  # No response was made
                key_resp_25.keys = None
            trials_24.addData('key_resp_25.keys',key_resp_25.keys)
            if key_resp_25.keys != None:  # we had a response
                trials_24.addData('key_resp_25.rt', key_resp_25.rt)
            trials_24.addData('key_resp_25.started', key_resp_25.tStartRefresh)
            trials_24.addData('key_resp_25.stopped', key_resp_25.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime()) 
                    allsteptime.append('video3-7 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video3-7 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_25.getCurrentFrameTime( )
                remembertimestamp37.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime20.append(sum(Watchtime1))
            #    allsteptime.append('video3-7 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime20.append(sum(Watchtime1))
            #    allsteptime.append('video3-7 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            
            totalpath3=1
            # store data for trials_24 (TrialHandler)
            if len(mouse_25.x): trials_24.addData('mouse_25.x', mouse_25.x[0])
            if len(mouse_25.y): trials_24.addData('mouse_25.y', mouse_25.y[0])
            if len(mouse_25.leftButton): trials_24.addData('mouse_25.leftButton', mouse_25.leftButton[0])
            if len(mouse_25.midButton): trials_24.addData('mouse_25.midButton', mouse_25.midButton[0])
            if len(mouse_25.rightButton): trials_24.addData('mouse_25.rightButton', mouse_25.rightButton[0])
            if len(mouse_25.time): trials_24.addData('mouse_25.time', mouse_25.time[0])
            if len(mouse_25.clicked_name): trials_24.addData('mouse_25.clicked_name', mouse_25.clicked_name[0])
            trials_24.addData('mouse_25.started', mouse_25.tStart)
            trials_24.addData('mouse_25.stopped', mouse_25.tStop)
            trials_24.addData('backvideo37.started', backvideo37.tStartRefresh)
            trials_24.addData('backvideo37.stopped', backvideo37.tStopRefresh)
            movie_25.stop()
            trials_24.addData('closevideo_25.started', closevideo_25.tStartRefresh)
            trials_24.addData('closevideo_25.stopped', closevideo_25.tStopRefresh)
            trials_24.addData('blender37.started', blender37.tStartRefresh)
            trials_24.addData('blender37.stopped', blender37.tStopRefresh)
            trials_24.addData('quickkey37.started', quickkey37.tStartRefresh)
            trials_24.addData('quickkey37.stopped', quickkey37.tStopRefresh)
            trials_24.addData('blenderquickkey37.started', blenderquickkey37.tStartRefresh)
            trials_24.addData('blenderquickkey37.stopped', blenderquickkey37.tStopRefresh)
            # the Routine "video3_7" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath38 repeats of 'trials_24'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_28 = data.TrialHandler(nReps=videopath31, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_28')
        thisExp.addLoop(trials_28)  # add the loop to the experiment
        thisTrial_28 = trials_28.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_28.rgb)
        if thisTrial_28 != None:
            for paramName in thisTrial_28:
                exec('{} = thisTrial_28[paramName]'.format(paramName))
        
        for thisTrial_28 in trials_28:
            currentLoop = trials_28
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_28.rgb)
            if thisTrial_28 != None:
                for paramName in thisTrial_28:
                    exec('{} = thisTrial_28[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "cookbook3"-------
            continueRoutine = True
            # update component parameters for each repeat
            # setup some python lists for storing info about the mouse_28
            mouse_28.clicked_name = []
            gotValidClick = False  # until a click is received
            key_resp_28.keys = []
            key_resp_28.rt = []
            _key_resp_28_allKeys = []
            count=1
            respClock.reset(0)
            ExperienceClock.reset(0)
            Time1=0
            showf=0
            blender=0
            enter1=0 
            newchange=0
            # keep track of which components have finished
            cookbook3Components = [background_3, mouse_28, key_resp_28, BOOK34, BOOK33, BOOK32, BOOK35, BOOK36, BOOK37, BOOK38, BOOK31, close_3, blender38, quickkey38, blenderquickkey38]
            for thisComponent in cookbook3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            cookbook3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "cookbook3"-------
            while continueRoutine:
                # get current time
                t = cookbook3Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=cookbook3Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *background_3* updates
                if background_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    background_3.frameNStart = frameN  # exact frame index
                    background_3.tStart = t  # local t and not account for scr refresh
                    background_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(background_3, 'tStartRefresh')  # time at next scr refresh
                    background_3.setAutoDraw(True)
                # *mouse_28* updates
                if mouse_28.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_28.frameNStart = frameN  # exact frame index
                    mouse_28.tStart = t  # local t and not account for scr refresh
                    mouse_28.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_28, 'tStartRefresh')  # time at next scr refresh
                    mouse_28.status = STARTED
                    mouse_28.mouseClock.reset()
                    prevButtonState = mouse_28.getPressed()  # if button is down already this ISN'T a new click
                if mouse_28.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_28.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [close_3,]:
                                if obj.contains(mouse_28):
                                    gotValidClick = True
                                    mouse_28.clicked_name.append(obj.name)
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *key_resp_28* updates
                waitOnFlip = False
                if key_resp_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_28.frameNStart = frameN  # exact frame index
                    key_resp_28.tStart = t  # local t and not account for scr refresh
                    key_resp_28.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_28, 'tStartRefresh')  # time at next scr refresh
                    key_resp_28.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_28.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_28.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_28.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_28.getKeys(keyList=['left', 'right', '1', '2', '3', '4', '5', '6', '7', '8', 'f', 'return'], waitRelease=False)
                    _key_resp_28_allKeys.extend(theseKeys)
                    if len(_key_resp_28_allKeys):
                        key_resp_28.keys = _key_resp_28_allKeys[-1].name  # just the last key pressed
                        key_resp_28.rt = _key_resp_28_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey38.setAutoDraw(False)
                    blenderquickkey38.setAutoDraw(False)
                if (blender%2)!=1:
                    blender38.setAutoDraw(False)
                for key in event.getKeys():
                    if key=='right':
                        countcontinue=countcontinue+1
                        count=count+1
                        if count>=8:
                            count=8
                            BOOK31.setAutoDraw(False)
                            BOOK32.setAutoDraw(False)
                            BOOK33.setAutoDraw(False)
                            BOOK34.setAutoDraw(False)
                            BOOK35.setAutoDraw(False)
                            BOOK36.setAutoDraw(False)
                            BOOK37.setAutoDraw(False)
                            BOOK38.setAutoDraw(True)
                        elif count==2:
                            BOOK31.setAutoDraw(False)
                            BOOK32.setAutoDraw(True)
                            BOOK33.setAutoDraw(False)
                            BOOK34.setAutoDraw(False)
                            BOOK35.setAutoDraw(False)
                            BOOK36.setAutoDraw(False)
                            BOOK37.setAutoDraw(False)
                            BOOK38.setAutoDraw(False)
                        elif count==3:
                            BOOK31.setAutoDraw(False)
                            BOOK32.setAutoDraw(False)
                            BOOK33.setAutoDraw(True)
                            BOOK34.setAutoDraw(False)
                            BOOK35.setAutoDraw(False)
                            BOOK36.setAutoDraw(False)
                            BOOK37.setAutoDraw(False)
                            BOOK38.setAutoDraw(False) 
                        elif count==4:
                            BOOK31.setAutoDraw(False)
                            BOOK32.setAutoDraw(False)
                            BOOK33.setAutoDraw(False)
                            BOOK34.setAutoDraw(True)
                            BOOK35.setAutoDraw(False)
                            BOOK36.setAutoDraw(False)
                            BOOK37.setAutoDraw(False)
                            BOOK38.setAutoDraw(False)   
                        elif count==5:
                            BOOK31.setAutoDraw(False)
                            BOOK32.setAutoDraw(False)
                            BOOK33.setAutoDraw(False)
                            BOOK34.setAutoDraw(False)
                            BOOK35.setAutoDraw(True)
                            BOOK36.setAutoDraw(False)
                            BOOK37.setAutoDraw(False)
                            BOOK38.setAutoDraw(False) 
                        elif count==6:
                            BOOK31.setAutoDraw(False)
                            BOOK32.setAutoDraw(False)
                            BOOK33.setAutoDraw(False)
                            BOOK34.setAutoDraw(False)
                            BOOK35.setAutoDraw(False)
                            BOOK36.setAutoDraw(True)
                            BOOK37.setAutoDraw(False)
                            BOOK38.setAutoDraw(False)   
                        elif count==7:
                            BOOK31.setAutoDraw(False)
                            BOOK32.setAutoDraw(False)
                            BOOK33.setAutoDraw(False)
                            BOOK34.setAutoDraw(False)
                            BOOK35.setAutoDraw(False)
                            BOOK36.setAutoDraw(False)
                            BOOK37.setAutoDraw(True)
                            BOOK38.setAutoDraw(False)             
                    elif key=='left':
                        countcontinue=countcontinue+1
                        count=count-1
                        if count<=1:
                            count=1
                            BOOK31.setAutoDraw(True)
                            BOOK32.setAutoDraw(False)
                            BOOK33.setAutoDraw(False)
                            BOOK34.setAutoDraw(False)
                            BOOK35.setAutoDraw(False)
                            BOOK36.setAutoDraw(False)
                            BOOK37.setAutoDraw(False)
                            BOOK38.setAutoDraw(False)
                        elif count==2:
                            BOOK31.setAutoDraw(False)
                            BOOK32.setAutoDraw(True)
                            BOOK33.setAutoDraw(False)
                            BOOK34.setAutoDraw(False)
                            BOOK35.setAutoDraw(False)
                            BOOK36.setAutoDraw(False)
                            BOOK37.setAutoDraw(False)
                            BOOK38.setAutoDraw(False)
                        elif count==3:
                            BOOK31.setAutoDraw(False)
                            BOOK32.setAutoDraw(False)
                            BOOK33.setAutoDraw(True)
                            BOOK34.setAutoDraw(False)
                            BOOK35.setAutoDraw(False)
                            BOOK36.setAutoDraw(False)
                            BOOK37.setAutoDraw(False)
                            BOOK38.setAutoDraw(False)
                        elif count==4:
                            BOOK31.setAutoDraw(False)
                            BOOK32.setAutoDraw(False)
                            BOOK33.setAutoDraw(False)
                            BOOK34.setAutoDraw(True)
                            BOOK35.setAutoDraw(False)
                            BOOK36.setAutoDraw(False)
                            BOOK37.setAutoDraw(False)
                            BOOK38.setAutoDraw(False)
                        elif count==5:
                            BOOK31.setAutoDraw(False)
                            BOOK32.setAutoDraw(False)
                            BOOK33.setAutoDraw(False)
                            BOOK34.setAutoDraw(False)
                            BOOK35.setAutoDraw(True)
                            BOOK36.setAutoDraw(False)
                            BOOK37.setAutoDraw(False)
                            BOOK38.setAutoDraw(False)
                        elif count==6:
                            BOOK31.setAutoDraw(False)
                            BOOK32.setAutoDraw(False)
                            BOOK33.setAutoDraw(False)
                            BOOK34.setAutoDraw(False)
                            BOOK35.setAutoDraw(False)
                            BOOK36.setAutoDraw(True)
                            BOOK37.setAutoDraw(False)
                            BOOK38.setAutoDraw(False)
                        elif count==7:
                            BOOK31.setAutoDraw(False)
                            BOOK32.setAutoDraw(False)
                            BOOK33.setAutoDraw(False)
                            BOOK34.setAutoDraw(False)
                            BOOK35.setAutoDraw(False)
                            BOOK36.setAutoDraw(False)
                            BOOK37.setAutoDraw(True)
                            BOOK38.setAutoDraw(False)
                    elif key=='1':
                        count=1
                        change=change+1
                        BOOK31.setAutoDraw(True)
                        BOOK32.setAutoDraw(False)
                        BOOK33.setAutoDraw(False)
                        BOOK34.setAutoDraw(False)
                        BOOK35.setAutoDraw(False)
                        BOOK36.setAutoDraw(False)
                        BOOK37.setAutoDraw(False)
                        BOOK38.setAutoDraw(False)
                    elif key=='2':
                        count=2
                        change=change+1
                        BOOK31.setAutoDraw(False)
                        BOOK32.setAutoDraw(True)
                        BOOK33.setAutoDraw(False)
                        BOOK34.setAutoDraw(False)
                        BOOK35.setAutoDraw(False)
                        BOOK36.setAutoDraw(False)
                        BOOK37.setAutoDraw(False)
                        BOOK38.setAutoDraw(False)
                    elif key=='3':
                        count=3
                        change=change+1
                        BOOK31.setAutoDraw(False)
                        BOOK32.setAutoDraw(False)
                        BOOK33.setAutoDraw(True)
                        BOOK34.setAutoDraw(False)
                        BOOK35.setAutoDraw(False)
                        BOOK36.setAutoDraw(False)
                        BOOK37.setAutoDraw(False)
                        BOOK38.setAutoDraw(False)
                    elif key=='4':
                        count=4
                        change=change+1
                        BOOK31.setAutoDraw(False)
                        BOOK32.setAutoDraw(False)
                        BOOK33.setAutoDraw(False)
                        BOOK34.setAutoDraw(True)
                        BOOK35.setAutoDraw(False)
                        BOOK36.setAutoDraw(False)
                        BOOK37.setAutoDraw(False)
                        BOOK38.setAutoDraw(False)
                    elif key=='5':
                        count=5
                        change=change+1
                        BOOK31.setAutoDraw(False)
                        BOOK32.setAutoDraw(False)
                        BOOK33.setAutoDraw(False)
                        BOOK34.setAutoDraw(False)
                        BOOK35.setAutoDraw(True)
                        BOOK36.setAutoDraw(False)
                        BOOK37.setAutoDraw(False)
                        BOOK38.setAutoDraw(False)
                    elif key=='6':
                        count=6
                        change=change+1
                        BOOK31.setAutoDraw(False)
                        BOOK32.setAutoDraw(False)
                        BOOK33.setAutoDraw(False)
                        BOOK34.setAutoDraw(False)
                        BOOK35.setAutoDraw(False)
                        BOOK36.setAutoDraw(True)
                        BOOK37.setAutoDraw(False)
                        BOOK38.setAutoDraw(False)
                    elif key=='7':
                        count=7
                        change=change+1
                        BOOK31.setAutoDraw(False)
                        BOOK32.setAutoDraw(False)
                        BOOK33.setAutoDraw(False)
                        BOOK34.setAutoDraw(False)
                        BOOK35.setAutoDraw(False)
                        BOOK36.setAutoDraw(False)
                        BOOK37.setAutoDraw(True)
                        BOOK38.setAutoDraw(False)
                    elif key=='8':
                        count=8
                        change=change+1
                        BOOK31.setAutoDraw(False)
                        BOOK32.setAutoDraw(False)
                        BOOK33.setAutoDraw(False)
                        BOOK34.setAutoDraw(False)
                        BOOK35.setAutoDraw(False)
                        BOOK36.setAutoDraw(False)
                        BOOK37.setAutoDraw(False)
                        BOOK38.setAutoDraw(True)
                
                    elif key =='f':
                        countcontinue=countcontinue+1
                        showf=showf+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey38.setAutoDraw(True)  
                            blenderquickkey38.setAutoDraw(False)
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey38.setAutoDraw(True)  
                            quickkey38.setAutoDraw(False) 
                        else:
                            blenderquickkey38.setAutoDraw(False)
                            quickkey38.setAutoDraw(False)
                # f/enter blender&learn time                
                    if key =='return':  
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey38.setAutoDraw(True)  
                            blenderquickkey38.setAutoDraw(False)
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey38.setAutoDraw(True)  
                            quickkey38.setAutoDraw(False) 
                        else:
                            blenderquickkey38.setAutoDraw(False)
                            quickkey38.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('cookbook3 learn')
                            allsteptime.append(MenuClock.getTime())
                            BlenderClock.reset(0)
                            blender38.setAutoDraw(True)
                        else: 
                            BlenderTime.append(BlenderClock.getTime())  
                            allsteptime.append('cookbook3 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            blender38.setAutoDraw(False)
                
                # *BOOK34* updates
                if BOOK34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK34.frameNStart = frameN  # exact frame index
                    BOOK34.tStart = t  # local t and not account for scr refresh
                    BOOK34.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK34, 'tStartRefresh')  # time at next scr refresh
                    BOOK34.setAutoDraw(True)
                
                # *BOOK33* updates
                if BOOK33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK33.frameNStart = frameN  # exact frame index
                    BOOK33.tStart = t  # local t and not account for scr refresh
                    BOOK33.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK33, 'tStartRefresh')  # time at next scr refresh
                    BOOK33.setAutoDraw(True)
                
                # *BOOK32* updates
                if BOOK32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK32.frameNStart = frameN  # exact frame index
                    BOOK32.tStart = t  # local t and not account for scr refresh
                    BOOK32.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK32, 'tStartRefresh')  # time at next scr refresh
                    BOOK32.setAutoDraw(True)
                
                # *BOOK35* updates
                if BOOK35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK35.frameNStart = frameN  # exact frame index
                    BOOK35.tStart = t  # local t and not account for scr refresh
                    BOOK35.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK35, 'tStartRefresh')  # time at next scr refresh
                    BOOK35.setAutoDraw(True)
                
                # *BOOK36* updates
                if BOOK36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK36.frameNStart = frameN  # exact frame index
                    BOOK36.tStart = t  # local t and not account for scr refresh
                    BOOK36.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK36, 'tStartRefresh')  # time at next scr refresh
                    BOOK36.setAutoDraw(True)
                
                # *BOOK37* updates
                if BOOK37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK37.frameNStart = frameN  # exact frame index
                    BOOK37.tStart = t  # local t and not account for scr refresh
                    BOOK37.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK37, 'tStartRefresh')  # time at next scr refresh
                    BOOK37.setAutoDraw(True)
                
                # *BOOK38* updates
                if BOOK38.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK38.frameNStart = frameN  # exact frame index
                    BOOK38.tStart = t  # local t and not account for scr refresh
                    BOOK38.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK38, 'tStartRefresh')  # time at next scr refresh
                    BOOK38.setAutoDraw(True)
                
                # *BOOK31* updates
                if BOOK31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK31.frameNStart = frameN  # exact frame index
                    BOOK31.tStart = t  # local t and not account for scr refresh
                    BOOK31.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK31, 'tStartRefresh')  # time at next scr refresh
                    BOOK31.setAutoDraw(True)
                
                # *close_3* updates
                if close_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    close_3.frameNStart = frameN  # exact frame index
                    close_3.tStart = t  # local t and not account for scr refresh
                    close_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(close_3, 'tStartRefresh')  # time at next scr refresh
                    close_3.setAutoDraw(True)
                
                # *blender38* updates
                if blender38.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender38.frameNStart = frameN  # exact frame index
                    blender38.tStart = t  # local t and not account for scr refresh
                    blender38.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender38, 'tStartRefresh')  # time at next scr refresh
                    blender38.setAutoDraw(True)
                
                # *quickkey38* updates
                if quickkey38.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey38.frameNStart = frameN  # exact frame index
                    quickkey38.tStart = t  # local t and not account for scr refresh
                    quickkey38.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey38, 'tStartRefresh')  # time at next scr refresh
                    quickkey38.setAutoDraw(True)
                
                # *blenderquickkey38* updates
                if blenderquickkey38.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey38.frameNStart = frameN  # exact frame index
                    blenderquickkey38.tStart = t  # local t and not account for scr refresh
                    blenderquickkey38.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey38, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey38.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cookbook3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "cookbook3"-------
            for thisComponent in cookbook3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_28.addData('background_3.started', background_3.tStartRefresh)
            trials_28.addData('background_3.stopped', background_3.tStopRefresh)
            # store data for trials_28 (TrialHandler)
            x, y = mouse_28.getPos()
            buttons = mouse_28.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [close_3,]:
                    if obj.contains(mouse_28):
                        gotValidClick = True
                        mouse_28.clicked_name.append(obj.name)
            trials_28.addData('mouse_28.x', x)
            trials_28.addData('mouse_28.y', y)
            trials_28.addData('mouse_28.leftButton', buttons[0])
            trials_28.addData('mouse_28.midButton', buttons[1])
            trials_28.addData('mouse_28.rightButton', buttons[2])
            if len(mouse_28.clicked_name):
                trials_28.addData('mouse_28.clicked_name', mouse_28.clicked_name[0])
            trials_28.addData('mouse_28.started', mouse_28.tStart)
            trials_28.addData('mouse_28.stopped', mouse_28.tStop)
            # check responses
            if key_resp_28.keys in ['', [], None]:  # No response was made
                key_resp_28.keys = None
            trials_28.addData('key_resp_28.keys',key_resp_28.keys)
            if key_resp_28.keys != None:  # we had a response
                trials_28.addData('key_resp_28.rt', key_resp_28.rt)
            trials_28.addData('key_resp_28.started', key_resp_28.tStartRefresh)
            trials_28.addData('key_resp_28.stopped', key_resp_28.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==1 :
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('cookbook3 blender')
                    allsteptime.append(BlenderClock.getTime())
                else:
                    Watchtime1.append(respClock.getTime()) 
                    allsteptime.append('cookbook3 learn')
                    allsteptime.append(MenuClock.getTime())
                change=change+1
            
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Cookbook3.append(sum(Watchtime1))
                AllCookbook.append(sum(Watchtime1))
            #    allsteptime.append('cookbook3 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Cookbook3.append(sum(Watchtime1))
                AllCookbook.append(sum(Watchtime1))
            #    allsteptime.append('cookbook3 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            
            trials_28.addData('BOOK34.started', BOOK34.tStartRefresh)
            trials_28.addData('BOOK34.stopped', BOOK34.tStopRefresh)
            trials_28.addData('BOOK33.started', BOOK33.tStartRefresh)
            trials_28.addData('BOOK33.stopped', BOOK33.tStopRefresh)
            trials_28.addData('BOOK32.started', BOOK32.tStartRefresh)
            trials_28.addData('BOOK32.stopped', BOOK32.tStopRefresh)
            trials_28.addData('BOOK35.started', BOOK35.tStartRefresh)
            trials_28.addData('BOOK35.stopped', BOOK35.tStopRefresh)
            trials_28.addData('BOOK36.started', BOOK36.tStartRefresh)
            trials_28.addData('BOOK36.stopped', BOOK36.tStopRefresh)
            trials_28.addData('BOOK37.started', BOOK37.tStartRefresh)
            trials_28.addData('BOOK37.stopped', BOOK37.tStopRefresh)
            trials_28.addData('BOOK38.started', BOOK38.tStartRefresh)
            trials_28.addData('BOOK38.stopped', BOOK38.tStopRefresh)
            trials_28.addData('BOOK31.started', BOOK31.tStartRefresh)
            trials_28.addData('BOOK31.stopped', BOOK31.tStopRefresh)
            trials_28.addData('close_3.started', close_3.tStartRefresh)
            trials_28.addData('close_3.stopped', close_3.tStopRefresh)
            trials_28.addData('blender38.started', blender38.tStartRefresh)
            trials_28.addData('blender38.stopped', blender38.tStopRefresh)
            trials_28.addData('quickkey38.started', quickkey38.tStartRefresh)
            trials_28.addData('quickkey38.stopped', quickkey38.tStopRefresh)
            trials_28.addData('blenderquickkey38.started', blenderquickkey38.tStartRefresh)
            trials_28.addData('blenderquickkey38.stopped', blenderquickkey38.tStopRefresh)
            # the Routine "cookbook3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath31 repeats of 'trials_28'
        
        thisExp.nextEntry()
        
    # completed totalpath3 repeats of 'trials_17'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_9 = data.TrialHandler(nReps=totalpath2, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_9')
    thisExp.addLoop(trials_9)  # add the loop to the experiment
    thisTrial_9 = trials_9.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
    if thisTrial_9 != None:
        for paramName in thisTrial_9:
            exec('{} = thisTrial_9[paramName]'.format(paramName))
    
    for thisTrial_9 in trials_9:
        currentLoop = trials_9
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
        if thisTrial_9 != None:
            for paramName in thisTrial_9:
                exec('{} = thisTrial_9[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "menu2"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_menupath2_1.keys = []
        key_menupath2_1.rt = []
        _key_menupath2_1_allKeys = []
        MenuClock.reset(0)
        ExperienceClock.reset(0)
        videopath21=0
        videopath22=0
        videopath23=0
        videopath24=0
        videopath25=0
        videopath26=0
        videopath27=0
        showf=0
        Time1 = 0
        enter1=0
        blender=0
        newchange=0
        # setup some python lists for storing info about the mouse_32
        mouse_32.clicked_name = []
        gotValidClick = False  # until a click is received
        key_resp_31.keys = []
        key_resp_31.rt = []
        _key_resp_31_allKeys = []
        # keep track of which components have finished
        menu2Components = [key_menupath2_1, mouse_32, backmenu2, close4, key_resp_31, blendermenu2, quickkeymenu2, blenderquickkey2]
        for thisComponent in menu2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        menu2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "menu2"-------
        while continueRoutine:
            # get current time
            t = menu2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=menu2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_menupath2_1* updates
            waitOnFlip = False
            if key_menupath2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_menupath2_1.frameNStart = frameN  # exact frame index
                key_menupath2_1.tStart = t  # local t and not account for scr refresh
                key_menupath2_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_menupath2_1, 'tStartRefresh')  # time at next scr refresh
                key_menupath2_1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_menupath2_1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_menupath2_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_menupath2_1.status == STARTED and not waitOnFlip:
                theseKeys = key_menupath2_1.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7'], waitRelease=False)
                _key_menupath2_1_allKeys.extend(theseKeys)
                if len(_key_menupath2_1_allKeys):
                    key_menupath2_1.keys = _key_menupath2_1_allKeys[-1].name  # just the last key pressed
                    key_menupath2_1.rt = _key_menupath2_1_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            if (showf%2)!=1:
                quickkeymenu2.setAutoDraw(False)
                blenderquickkey2.setAutoDraw(False)
            if (blender%2)!=1:
                blendermenu2.setAutoDraw(False)
            for key in event.getKeys():
                if key =='1':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())    
                    videopath21=1
                elif key =='2':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    videopath22=1     
                elif key =='3':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    videopath23=1
                elif key =='4':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    videopath24=1
                elif key =='5':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    videopath25=1
                elif key =='6':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    videopath26=1
                elif key =='7':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    videopath27=1
                elif key =='f':
                    countcontinue=countcontinue+1
                    showf=showf+1
                    if(showf%2)==1 and (enter1%2)==0:
                        quickkeymenu2.setAutoDraw(True)   
                        blenderquickkey2.setAutoDraw(False)
                    elif (showf%2)==1 and (enter1%2)==1:
                        blenderquickkey2.setAutoDraw(True) 
                        quickkeymenu2.setAutoDraw(False)
                    else:
                        blenderquickkey2.setAutoDraw(False)
                        quickkeymenu2.setAutoDraw(False)
            # f/enter blender&learn time  
                if key =='return':  
                    countcontinue=countcontinue+1
                    enter1=enter1+1
                    blender=blender+1
                    countenter=countenter+1
                    newchange=newchange+1
                    if(showf%2)==1 and (enter1%2)==0:
                        quickkeymenu2.setAutoDraw(True)   
                        blenderquickkey2.setAutoDraw(False)
                    elif (showf%2)==1 and (enter1%2)==1:
                        blenderquickkey2.setAutoDraw(True) 
                        quickkeymenu2.setAutoDraw(False)
                    else:
                        blenderquickkey2.setAutoDraw(False)
                        quickkeymenu2.setAutoDraw(False)
                    if(enter1%2)==1:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                        BlenderClock.reset(0)
                        blendermenu2.setAutoDraw(True)
                    else: 
                        BlenderTime.append(BlenderClock.getTime())  
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                        MenuClock.reset(0)
                        blendermenu2.setAutoDraw(False)
            # *mouse_32* updates
            if mouse_32.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_32.frameNStart = frameN  # exact frame index
                mouse_32.tStart = t  # local t and not account for scr refresh
                mouse_32.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_32, 'tStartRefresh')  # time at next scr refresh
                mouse_32.status = STARTED
                mouse_32.mouseClock.reset()
                prevButtonState = mouse_32.getPressed()  # if button is down already this ISN'T a new click
            if mouse_32.status == STARTED:  # only update if started and not finished!
                buttons = mouse_32.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [close4,]:
                            if obj.contains(mouse_32):
                                gotValidClick = True
                                mouse_32.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *backmenu2* updates
            if backmenu2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                backmenu2.frameNStart = frameN  # exact frame index
                backmenu2.tStart = t  # local t and not account for scr refresh
                backmenu2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(backmenu2, 'tStartRefresh')  # time at next scr refresh
                backmenu2.setAutoDraw(True)
            
            # *close4* updates
            if close4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                close4.frameNStart = frameN  # exact frame index
                close4.tStart = t  # local t and not account for scr refresh
                close4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(close4, 'tStartRefresh')  # time at next scr refresh
                close4.setAutoDraw(True)
            
            # *key_resp_31* updates
            waitOnFlip = False
            if key_resp_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_31.frameNStart = frameN  # exact frame index
                key_resp_31.tStart = t  # local t and not account for scr refresh
                key_resp_31.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_31, 'tStartRefresh')  # time at next scr refresh
                key_resp_31.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_31.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_31.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_31.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_31.getKeys(keyList=['f', 'return'], waitRelease=False)
                _key_resp_31_allKeys.extend(theseKeys)
                if len(_key_resp_31_allKeys):
                    key_resp_31.keys = _key_resp_31_allKeys[-1].name  # just the last key pressed
                    key_resp_31.rt = _key_resp_31_allKeys[-1].rt
            
            # *blendermenu2* updates
            if blendermenu2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blendermenu2.frameNStart = frameN  # exact frame index
                blendermenu2.tStart = t  # local t and not account for scr refresh
                blendermenu2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blendermenu2, 'tStartRefresh')  # time at next scr refresh
                blendermenu2.setAutoDraw(True)
            
            # *quickkeymenu2* updates
            if quickkeymenu2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                quickkeymenu2.frameNStart = frameN  # exact frame index
                quickkeymenu2.tStart = t  # local t and not account for scr refresh
                quickkeymenu2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(quickkeymenu2, 'tStartRefresh')  # time at next scr refresh
                quickkeymenu2.setAutoDraw(True)
            
            # *blenderquickkey2* updates
            if blenderquickkey2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blenderquickkey2.frameNStart = frameN  # exact frame index
                blenderquickkey2.tStart = t  # local t and not account for scr refresh
                blenderquickkey2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blenderquickkey2, 'tStartRefresh')  # time at next scr refresh
                blenderquickkey2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in menu2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "menu2"-------
        for thisComponent in menu2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_menupath2_1.keys in ['', [], None]:  # No response was made
            key_menupath2_1.keys = None
        trials_9.addData('key_menupath2_1.keys',key_menupath2_1.keys)
        if key_menupath2_1.keys != None:  # we had a response
            trials_9.addData('key_menupath2_1.rt', key_menupath2_1.rt)
        trials_9.addData('key_menupath2_1.started', key_menupath2_1.tStartRefresh)
        trials_9.addData('key_menupath2_1.stopped', key_menupath2_1.tStopRefresh)
        Experiencetime.append(ExperienceClock.getTime())
        
        if gotValidClick ==True:
            countchange.append(newchange)
            if (enter1%2)==1 :
                BlenderTime.append(BlenderClock.getTime())
                allsteptime.append('menu2 blender')
                allsteptime.append(BlenderClock.getTime())
            else:
                Menutime.append(MenuClock.getTime())
                AllWatchtime.append(MenuClock.getTime())
                allsteptime.append('menu2 learn')
                allsteptime.append(MenuClock.getTime())
            change=change+1
        # store data for trials_9 (TrialHandler)
        x, y = mouse_32.getPos()
        buttons = mouse_32.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [close4,]:
                if obj.contains(mouse_32):
                    gotValidClick = True
                    mouse_32.clicked_name.append(obj.name)
        trials_9.addData('mouse_32.x', x)
        trials_9.addData('mouse_32.y', y)
        trials_9.addData('mouse_32.leftButton', buttons[0])
        trials_9.addData('mouse_32.midButton', buttons[1])
        trials_9.addData('mouse_32.rightButton', buttons[2])
        if len(mouse_32.clicked_name):
            trials_9.addData('mouse_32.clicked_name', mouse_32.clicked_name[0])
        trials_9.addData('mouse_32.started', mouse_32.tStart)
        trials_9.addData('mouse_32.stopped', mouse_32.tStop)
        trials_9.addData('backmenu2.started', backmenu2.tStartRefresh)
        trials_9.addData('backmenu2.stopped', backmenu2.tStopRefresh)
        trials_9.addData('close4.started', close4.tStartRefresh)
        trials_9.addData('close4.stopped', close4.tStopRefresh)
        # check responses
        if key_resp_31.keys in ['', [], None]:  # No response was made
            key_resp_31.keys = None
        trials_9.addData('key_resp_31.keys',key_resp_31.keys)
        if key_resp_31.keys != None:  # we had a response
            trials_9.addData('key_resp_31.rt', key_resp_31.rt)
        trials_9.addData('key_resp_31.started', key_resp_31.tStartRefresh)
        trials_9.addData('key_resp_31.stopped', key_resp_31.tStopRefresh)
        trials_9.addData('blendermenu2.started', blendermenu2.tStartRefresh)
        trials_9.addData('blendermenu2.stopped', blendermenu2.tStopRefresh)
        trials_9.addData('quickkeymenu2.started', quickkeymenu2.tStartRefresh)
        trials_9.addData('quickkeymenu2.stopped', quickkeymenu2.tStopRefresh)
        trials_9.addData('blenderquickkey2.started', blenderquickkey2.tStartRefresh)
        trials_9.addData('blenderquickkey2.stopped', blenderquickkey2.tStopRefresh)
        # the Routine "menu2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_11 = data.TrialHandler(nReps=videopath22, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_11')
        thisExp.addLoop(trials_11)  # add the loop to the experiment
        thisTrial_11 = trials_11.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
        if thisTrial_11 != None:
            for paramName in thisTrial_11:
                exec('{} = thisTrial_11[paramName]'.format(paramName))
        
        for thisTrial_11 in trials_11:
            currentLoop = trials_11
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
            if thisTrial_11 != None:
                for paramName in thisTrial_11:
                    exec('{} = thisTrial_11[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video2_1"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_12.keys = []
            key_resp_12.rt = []
            _key_resp_12_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp21)!=0:
                movie_12.pause()
                movie_12.seek(int(remembertimestamp21[-1]))
                movie_12.play()
                Time1 = 0
            showf=0
            enter1=0    
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_12
            mouse_12.x = []
            mouse_12.y = []
            mouse_12.leftButton = []
            mouse_12.midButton = []
            mouse_12.rightButton = []
            mouse_12.time = []
            mouse_12.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_12.mouseClock.reset()
            # keep track of which components have finished
            video2_1Components = [key_resp_12, mouse_12, backvideo21, movie_12, closevideo_12, blender21, quickkey21, blenderquickkey21]
            for thisComponent in video2_1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video2_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video2_1"-------
            while continueRoutine:
                # get current time
                t = video2_1Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video2_1Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_12* updates
                waitOnFlip = False
                if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_12.frameNStart = frameN  # exact frame index
                    key_resp_12.tStart = t  # local t and not account for scr refresh
                    key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
                    key_resp_12.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_12.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_12.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_12_allKeys.extend(theseKeys)
                    if len(_key_resp_12_allKeys):
                        key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                        key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey21.setAutoDraw(False)
                    blenderquickkey21.setAutoDraw(False)
                if (blender%2)!=1:
                    blender21.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_12.status == PLAYING:
                            movie_12.pause()
                            Time1 = 1
                        elif movie_12.status == PAUSED:
                            movie_12.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_12.pause()
                        ntime = max(0.0,movie_12.duration)
                        movie_12.seek(ntime)
                        movie_12.play()
                        Time1 = 0
                
                    if movie_12.status == PLAYING:
                        if key=='period':
                            movie_12.pause()
                            ntime = min(movie_12.getCurrentFrameTime( ) + 5.0, movie_12.duration)
                            movie_12.seek(ntime)
                            movie_12.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_12.pause()
                            ntime = max(movie_12.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_12.seek(ntime)
                            movie_12.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey21.setAutoDraw(True)  
                                blenderquickkey21.setAutoDraw(False) 
                                movie_12.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey21.setAutoDraw(True) 
                                quickkey21.setAutoDraw(False)
                                movie_12.pause()
                            else:
                                blenderquickkey21.setAutoDraw(False) 
                                quickkey21.setAutoDraw(False)
                                movie_12.play()
                
                    elif movie_12.status == PAUSED:
                        if key=='period':
                            movie_12.pause()
                            ntime = min(movie_12.getCurrentFrameTime( ) + 5.0, movie_12.duration)
                            movie_12.seek(ntime)
                            movie_12.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_12.pause()
                            ntime = max(movie_12.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_12.seek(ntime)
                            movie_12.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_12.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey21.setAutoDraw(True)  
                                blenderquickkey21.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey21.setAutoDraw(True) 
                                quickkey21.setAutoDraw(False)
                            else:
                                blenderquickkey21.setAutoDraw(False) 
                                quickkey21.setAutoDraw(False)
                              
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1 
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey21.setAutoDraw(True)  
                            blenderquickkey21.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey21.setAutoDraw(True) 
                            quickkey21.setAutoDraw(False)
                        else:
                            blenderquickkey21.setAutoDraw(False) 
                            quickkey21.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video2-1 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender21.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video2-1 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender21.setAutoDraw(False)
                # *mouse_12* updates
                if mouse_12.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_12.frameNStart = frameN  # exact frame index
                    mouse_12.tStart = t  # local t and not account for scr refresh
                    mouse_12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_12, 'tStartRefresh')  # time at next scr refresh
                    mouse_12.status = STARTED
                    prevButtonState = mouse_12.getPressed()  # if button is down already this ISN'T a new click
                if mouse_12.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_12.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_12,]:
                                if obj.contains(mouse_12):
                                    gotValidClick = True
                                    mouse_12.clicked_name.append(obj.name)
                            x, y = mouse_12.getPos()
                            mouse_12.x.append(x)
                            mouse_12.y.append(y)
                            buttons = mouse_12.getPressed()
                            mouse_12.leftButton.append(buttons[0])
                            mouse_12.midButton.append(buttons[1])
                            mouse_12.rightButton.append(buttons[2])
                            mouse_12.time.append(mouse_12.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo21* updates
                if backvideo21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo21.frameNStart = frameN  # exact frame index
                    backvideo21.tStart = t  # local t and not account for scr refresh
                    backvideo21.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo21, 'tStartRefresh')  # time at next scr refresh
                    backvideo21.setAutoDraw(True)
                
                # *movie_12* updates
                if movie_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_12.frameNStart = frameN  # exact frame index
                    movie_12.tStart = t  # local t and not account for scr refresh
                    movie_12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_12, 'tStartRefresh')  # time at next scr refresh
                    movie_12.setAutoDraw(True)
                
                # *closevideo_12* updates
                if closevideo_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_12.frameNStart = frameN  # exact frame index
                    closevideo_12.tStart = t  # local t and not account for scr refresh
                    closevideo_12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_12, 'tStartRefresh')  # time at next scr refresh
                    closevideo_12.setAutoDraw(True)
                
                # *blender21* updates
                if blender21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender21.frameNStart = frameN  # exact frame index
                    blender21.tStart = t  # local t and not account for scr refresh
                    blender21.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender21, 'tStartRefresh')  # time at next scr refresh
                    blender21.setAutoDraw(True)
                
                # *quickkey21* updates
                if quickkey21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey21.frameNStart = frameN  # exact frame index
                    quickkey21.tStart = t  # local t and not account for scr refresh
                    quickkey21.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey21, 'tStartRefresh')  # time at next scr refresh
                    quickkey21.setAutoDraw(True)
                
                # *blenderquickkey21* updates
                if blenderquickkey21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey21.frameNStart = frameN  # exact frame index
                    blenderquickkey21.tStart = t  # local t and not account for scr refresh
                    blenderquickkey21.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey21, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey21.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video2_1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video2_1"-------
            for thisComponent in video2_1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_12.keys in ['', [], None]:  # No response was made
                key_resp_12.keys = None
            trials_11.addData('key_resp_12.keys',key_resp_12.keys)
            if key_resp_12.keys != None:  # we had a response
                trials_11.addData('key_resp_12.rt', key_resp_12.rt)
            trials_11.addData('key_resp_12.started', key_resp_12.tStartRefresh)
            trials_11.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime())  
                    allsteptime.append('video2-1 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video2-1 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_12.getCurrentFrameTime( )
                remembertimestamp21.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime8.append(sum(Watchtime1))
            #    allsteptime.append('video2-1 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime8.append(sum(Watchtime1))
            #    allsteptime.append('video2-1 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            
            totalpath2=1
            # store data for trials_11 (TrialHandler)
            if len(mouse_12.x): trials_11.addData('mouse_12.x', mouse_12.x[0])
            if len(mouse_12.y): trials_11.addData('mouse_12.y', mouse_12.y[0])
            if len(mouse_12.leftButton): trials_11.addData('mouse_12.leftButton', mouse_12.leftButton[0])
            if len(mouse_12.midButton): trials_11.addData('mouse_12.midButton', mouse_12.midButton[0])
            if len(mouse_12.rightButton): trials_11.addData('mouse_12.rightButton', mouse_12.rightButton[0])
            if len(mouse_12.time): trials_11.addData('mouse_12.time', mouse_12.time[0])
            if len(mouse_12.clicked_name): trials_11.addData('mouse_12.clicked_name', mouse_12.clicked_name[0])
            trials_11.addData('mouse_12.started', mouse_12.tStart)
            trials_11.addData('mouse_12.stopped', mouse_12.tStop)
            trials_11.addData('backvideo21.started', backvideo21.tStartRefresh)
            trials_11.addData('backvideo21.stopped', backvideo21.tStopRefresh)
            movie_12.stop()
            trials_11.addData('closevideo_12.started', closevideo_12.tStartRefresh)
            trials_11.addData('closevideo_12.stopped', closevideo_12.tStopRefresh)
            trials_11.addData('blender21.started', blender21.tStartRefresh)
            trials_11.addData('blender21.stopped', blender21.tStopRefresh)
            trials_11.addData('quickkey21.started', quickkey21.tStartRefresh)
            trials_11.addData('quickkey21.stopped', quickkey21.tStopRefresh)
            trials_11.addData('blenderquickkey21.started', blenderquickkey21.tStartRefresh)
            trials_11.addData('blenderquickkey21.stopped', blenderquickkey21.tStopRefresh)
            # the Routine "video2_1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath22 repeats of 'trials_11'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_12 = data.TrialHandler(nReps=videopath23, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_12')
        thisExp.addLoop(trials_12)  # add the loop to the experiment
        thisTrial_12 = trials_12.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
        if thisTrial_12 != None:
            for paramName in thisTrial_12:
                exec('{} = thisTrial_12[paramName]'.format(paramName))
        
        for thisTrial_12 in trials_12:
            currentLoop = trials_12
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
            if thisTrial_12 != None:
                for paramName in thisTrial_12:
                    exec('{} = thisTrial_12[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video2_2"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_13.keys = []
            key_resp_13.rt = []
            _key_resp_13_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp22)!=0:
                movie_13.pause()
                movie_13.seek(int(remembertimestamp22[-1]))
                movie_13.play()
                Time1 = 0
            showf=0
            enter1=0
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_13
            mouse_13.x = []
            mouse_13.y = []
            mouse_13.leftButton = []
            mouse_13.midButton = []
            mouse_13.rightButton = []
            mouse_13.time = []
            mouse_13.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_13.mouseClock.reset()
            # keep track of which components have finished
            video2_2Components = [key_resp_13, mouse_13, backvideo22, movie_13, closevideo_13, blender22, quickkey22, blenderquickkey22]
            for thisComponent in video2_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video2_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video2_2"-------
            while continueRoutine:
                # get current time
                t = video2_2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video2_2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_13* updates
                waitOnFlip = False
                if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_13.frameNStart = frameN  # exact frame index
                    key_resp_13.tStart = t  # local t and not account for scr refresh
                    key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
                    key_resp_13.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_13.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_13.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_13_allKeys.extend(theseKeys)
                    if len(_key_resp_13_allKeys):
                        key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
                        key_resp_13.rt = _key_resp_13_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey22.setAutoDraw(False)
                    blenderquickkey22.setAutoDraw(False)
                if (blender%2)!=1:
                    blender22.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_13.status == PLAYING:
                            movie_13.pause()
                            Time1 = 1
                        elif movie_13.status == PAUSED:
                            movie_13.play()
                            Time1 = 0
                    elif key=='s':
                        change=change+1
                        movie_13.pause()
                        ntime = max(0.0,movie_13.duration)
                        movie_13.seek(ntime)
                        movie_13.play()
                        Time1 = 0
                    if movie_13.status == PLAYING:
                        if key=='period':
                            movie_13.pause()
                            ntime = min(movie_13.getCurrentFrameTime( ) + 5.0, movie_13.duration)
                            movie_13.seek(ntime)
                            movie_13.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_13.pause()
                            ntime = max(movie_13.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_13.seek(ntime)
                            movie_13.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey22.setAutoDraw(True)    
                                blenderquickkey22.setAutoDraw(False) 
                                movie_13.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey22.setAutoDraw(True) 
                                quickkey22.setAutoDraw(False)
                                movie_13.pause()
                            else:
                                blenderquickkey22.setAutoDraw(False) 
                                quickkey22.setAutoDraw(False)
                                movie_13.play()
                                
                    elif movie_13.status == PAUSED:
                        if key=='period':
                            movie_13.pause()
                            ntime = min(movie_13.getCurrentFrameTime( ) + 5.0, movie_13.duration)
                            movie_13.seek(ntime)
                            movie_13.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_13.pause()
                            ntime = max(movie_13.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_13.seek(ntime)
                            movie_13.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_13.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey22.setAutoDraw(True)    
                                blenderquickkey22.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey22.setAutoDraw(True) 
                                quickkey22.setAutoDraw(False)
                            else:
                                blenderquickkey22.setAutoDraw(False) 
                                quickkey22.setAutoDraw(False)
                      
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey22.setAutoDraw(True)    
                            blenderquickkey22.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey22.setAutoDraw(True) 
                            quickkey22.setAutoDraw(False)
                        else:
                            blenderquickkey22.setAutoDraw(False) 
                            quickkey22.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video2-2 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender22.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video2-2 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender22.setAutoDraw(False)
                # *mouse_13* updates
                if mouse_13.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_13.frameNStart = frameN  # exact frame index
                    mouse_13.tStart = t  # local t and not account for scr refresh
                    mouse_13.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_13, 'tStartRefresh')  # time at next scr refresh
                    mouse_13.status = STARTED
                    prevButtonState = mouse_13.getPressed()  # if button is down already this ISN'T a new click
                if mouse_13.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_13.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_13,]:
                                if obj.contains(mouse_13):
                                    gotValidClick = True
                                    mouse_13.clicked_name.append(obj.name)
                            x, y = mouse_13.getPos()
                            mouse_13.x.append(x)
                            mouse_13.y.append(y)
                            buttons = mouse_13.getPressed()
                            mouse_13.leftButton.append(buttons[0])
                            mouse_13.midButton.append(buttons[1])
                            mouse_13.rightButton.append(buttons[2])
                            mouse_13.time.append(mouse_13.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo22* updates
                if backvideo22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo22.frameNStart = frameN  # exact frame index
                    backvideo22.tStart = t  # local t and not account for scr refresh
                    backvideo22.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo22, 'tStartRefresh')  # time at next scr refresh
                    backvideo22.setAutoDraw(True)
                
                # *movie_13* updates
                if movie_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_13.frameNStart = frameN  # exact frame index
                    movie_13.tStart = t  # local t and not account for scr refresh
                    movie_13.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_13, 'tStartRefresh')  # time at next scr refresh
                    movie_13.setAutoDraw(True)
                
                # *closevideo_13* updates
                if closevideo_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_13.frameNStart = frameN  # exact frame index
                    closevideo_13.tStart = t  # local t and not account for scr refresh
                    closevideo_13.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_13, 'tStartRefresh')  # time at next scr refresh
                    closevideo_13.setAutoDraw(True)
                
                # *blender22* updates
                if blender22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender22.frameNStart = frameN  # exact frame index
                    blender22.tStart = t  # local t and not account for scr refresh
                    blender22.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender22, 'tStartRefresh')  # time at next scr refresh
                    blender22.setAutoDraw(True)
                
                # *quickkey22* updates
                if quickkey22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey22.frameNStart = frameN  # exact frame index
                    quickkey22.tStart = t  # local t and not account for scr refresh
                    quickkey22.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey22, 'tStartRefresh')  # time at next scr refresh
                    quickkey22.setAutoDraw(True)
                
                # *blenderquickkey22* updates
                if blenderquickkey22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey22.frameNStart = frameN  # exact frame index
                    blenderquickkey22.tStart = t  # local t and not account for scr refresh
                    blenderquickkey22.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey22, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey22.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video2_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video2_2"-------
            for thisComponent in video2_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_13.keys in ['', [], None]:  # No response was made
                key_resp_13.keys = None
            trials_12.addData('key_resp_13.keys',key_resp_13.keys)
            if key_resp_13.keys != None:  # we had a response
                trials_12.addData('key_resp_13.rt', key_resp_13.rt)
            trials_12.addData('key_resp_13.started', key_resp_13.tStartRefresh)
            trials_12.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime())
                    allsteptime.append('video2-2 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video2-2 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_13.getCurrentFrameTime( )
                remembertimestamp22.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime9.append(sum(Watchtime1))
            #    allsteptime.append('video2-2 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime9.append(sum(Watchtime1))
            #    allsteptime.append('video2-2 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            
            totalpath2=1
            # store data for trials_12 (TrialHandler)
            if len(mouse_13.x): trials_12.addData('mouse_13.x', mouse_13.x[0])
            if len(mouse_13.y): trials_12.addData('mouse_13.y', mouse_13.y[0])
            if len(mouse_13.leftButton): trials_12.addData('mouse_13.leftButton', mouse_13.leftButton[0])
            if len(mouse_13.midButton): trials_12.addData('mouse_13.midButton', mouse_13.midButton[0])
            if len(mouse_13.rightButton): trials_12.addData('mouse_13.rightButton', mouse_13.rightButton[0])
            if len(mouse_13.time): trials_12.addData('mouse_13.time', mouse_13.time[0])
            if len(mouse_13.clicked_name): trials_12.addData('mouse_13.clicked_name', mouse_13.clicked_name[0])
            trials_12.addData('mouse_13.started', mouse_13.tStart)
            trials_12.addData('mouse_13.stopped', mouse_13.tStop)
            trials_12.addData('backvideo22.started', backvideo22.tStartRefresh)
            trials_12.addData('backvideo22.stopped', backvideo22.tStopRefresh)
            movie_13.stop()
            trials_12.addData('closevideo_13.started', closevideo_13.tStartRefresh)
            trials_12.addData('closevideo_13.stopped', closevideo_13.tStopRefresh)
            trials_12.addData('blender22.started', blender22.tStartRefresh)
            trials_12.addData('blender22.stopped', blender22.tStopRefresh)
            trials_12.addData('quickkey22.started', quickkey22.tStartRefresh)
            trials_12.addData('quickkey22.stopped', quickkey22.tStopRefresh)
            trials_12.addData('blenderquickkey22.started', blenderquickkey22.tStartRefresh)
            trials_12.addData('blenderquickkey22.stopped', blenderquickkey22.tStopRefresh)
            # the Routine "video2_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath23 repeats of 'trials_12'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_13 = data.TrialHandler(nReps=videopath24, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_13')
        thisExp.addLoop(trials_13)  # add the loop to the experiment
        thisTrial_13 = trials_13.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
        if thisTrial_13 != None:
            for paramName in thisTrial_13:
                exec('{} = thisTrial_13[paramName]'.format(paramName))
        
        for thisTrial_13 in trials_13:
            currentLoop = trials_13
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
            if thisTrial_13 != None:
                for paramName in thisTrial_13:
                    exec('{} = thisTrial_13[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video2_3"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_14.keys = []
            key_resp_14.rt = []
            _key_resp_14_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp23)!=0:
                movie_14.pause()
                movie_14.seek(int(remembertimestamp23[-1]))
                movie_14.play()
                Time1 = 0
            showf=0
            enter1=0    
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_14
            mouse_14.x = []
            mouse_14.y = []
            mouse_14.leftButton = []
            mouse_14.midButton = []
            mouse_14.rightButton = []
            mouse_14.time = []
            mouse_14.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_14.mouseClock.reset()
            # keep track of which components have finished
            video2_3Components = [key_resp_14, mouse_14, backvideo23, movie_14, closevideo_14, blender23, quickkey23, blenderquickkey23]
            for thisComponent in video2_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video2_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video2_3"-------
            while continueRoutine:
                # get current time
                t = video2_3Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video2_3Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_14* updates
                waitOnFlip = False
                if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_14.frameNStart = frameN  # exact frame index
                    key_resp_14.tStart = t  # local t and not account for scr refresh
                    key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
                    key_resp_14.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_14.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_14.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_14_allKeys.extend(theseKeys)
                    if len(_key_resp_14_allKeys):
                        key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
                        key_resp_14.rt = _key_resp_14_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey23.setAutoDraw(False)
                    blenderquickkey23.setAutoDraw(False)
                if (blender%2)!=1:
                    blender23.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_14.status == PLAYING:
                            movie_14.pause()
                            Time1 = 1
                        elif movie_14.status == PAUSED:
                            movie_14.play()
                            Time1 = 0
                    elif key=='s':
                        change=change+1
                        movie_14.pause()
                        ntime = max(0.0,movie_14.duration)
                        movie_14.seek(ntime)
                        movie_14.play()
                        Time1 = 0
                            
                    if movie_14.status == PLAYING:
                        if key=='period':
                            movie_14.pause()
                            ntime = min(movie_14.getCurrentFrameTime( ) + 5.0, movie_14.duration)
                            movie_14.seek(ntime)
                            movie_14.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma':
                            movie_14.pause()
                            ntime = max(movie_14.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_14.seek(ntime)
                            movie_14.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey23.setAutoDraw(True)   
                                blenderquickkey23.setAutoDraw(False) 
                                movie_14.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey23.setAutoDraw(True) 
                                quickkey23.setAutoDraw(False)
                                movie_14.pause()
                            else:
                                blenderquickkey23.setAutoDraw(False) 
                                quickkey23.setAutoDraw(False)
                                movie_14.play()
                
                    elif movie_14.status == PAUSED:
                        if key=='period':
                            movie_14.pause()
                            ntime = min(movie_14.getCurrentFrameTime( ) + 5.0, movie_14.duration)
                            movie_14.seek(ntime)
                            movie_14.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma':
                            movie_14.pause()
                            ntime = max(movie_14.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_14.seek(ntime)
                            movie_14.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_14.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey23.setAutoDraw(True)   
                                blenderquickkey23.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey23.setAutoDraw(True) 
                                quickkey23.setAutoDraw(False)
                            else:
                                blenderquickkey23.setAutoDraw(False) 
                                quickkey23.setAutoDraw(False)
                        
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey23.setAutoDraw(True)   
                            blenderquickkey23.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey23.setAutoDraw(True) 
                            quickkey23.setAutoDraw(False)
                        else:
                            blenderquickkey23.setAutoDraw(False) 
                            quickkey23.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video2-3 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender23.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video2-3 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender23.setAutoDraw(False)
                # *mouse_14* updates
                if mouse_14.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_14.frameNStart = frameN  # exact frame index
                    mouse_14.tStart = t  # local t and not account for scr refresh
                    mouse_14.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_14, 'tStartRefresh')  # time at next scr refresh
                    mouse_14.status = STARTED
                    prevButtonState = mouse_14.getPressed()  # if button is down already this ISN'T a new click
                if mouse_14.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_14.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_14,]:
                                if obj.contains(mouse_14):
                                    gotValidClick = True
                                    mouse_14.clicked_name.append(obj.name)
                            x, y = mouse_14.getPos()
                            mouse_14.x.append(x)
                            mouse_14.y.append(y)
                            buttons = mouse_14.getPressed()
                            mouse_14.leftButton.append(buttons[0])
                            mouse_14.midButton.append(buttons[1])
                            mouse_14.rightButton.append(buttons[2])
                            mouse_14.time.append(mouse_14.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo23* updates
                if backvideo23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo23.frameNStart = frameN  # exact frame index
                    backvideo23.tStart = t  # local t and not account for scr refresh
                    backvideo23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo23, 'tStartRefresh')  # time at next scr refresh
                    backvideo23.setAutoDraw(True)
                
                # *movie_14* updates
                if movie_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_14.frameNStart = frameN  # exact frame index
                    movie_14.tStart = t  # local t and not account for scr refresh
                    movie_14.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_14, 'tStartRefresh')  # time at next scr refresh
                    movie_14.setAutoDraw(True)
                
                # *closevideo_14* updates
                if closevideo_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_14.frameNStart = frameN  # exact frame index
                    closevideo_14.tStart = t  # local t and not account for scr refresh
                    closevideo_14.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_14, 'tStartRefresh')  # time at next scr refresh
                    closevideo_14.setAutoDraw(True)
                
                # *blender23* updates
                if blender23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender23.frameNStart = frameN  # exact frame index
                    blender23.tStart = t  # local t and not account for scr refresh
                    blender23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender23, 'tStartRefresh')  # time at next scr refresh
                    blender23.setAutoDraw(True)
                
                # *quickkey23* updates
                if quickkey23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey23.frameNStart = frameN  # exact frame index
                    quickkey23.tStart = t  # local t and not account for scr refresh
                    quickkey23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey23, 'tStartRefresh')  # time at next scr refresh
                    quickkey23.setAutoDraw(True)
                
                # *blenderquickkey23* updates
                if blenderquickkey23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey23.frameNStart = frameN  # exact frame index
                    blenderquickkey23.tStart = t  # local t and not account for scr refresh
                    blenderquickkey23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey23, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey23.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video2_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video2_3"-------
            for thisComponent in video2_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_14.keys in ['', [], None]:  # No response was made
                key_resp_14.keys = None
            trials_13.addData('key_resp_14.keys',key_resp_14.keys)
            if key_resp_14.keys != None:  # we had a response
                trials_13.addData('key_resp_14.rt', key_resp_14.rt)
            trials_13.addData('key_resp_14.started', key_resp_14.tStartRefresh)
            trials_13.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime()) 
                    allsteptime.append('video2-3 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video2-3 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_14.getCurrentFrameTime( )
                remembertimestamp23.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime10.append(sum(Watchtime1))
            #    allsteptime.append('video2-3 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime10.append(sum(Watchtime1))
            #    allsteptime.append('video2-3 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            
            totalpath2=1
            # store data for trials_13 (TrialHandler)
            if len(mouse_14.x): trials_13.addData('mouse_14.x', mouse_14.x[0])
            if len(mouse_14.y): trials_13.addData('mouse_14.y', mouse_14.y[0])
            if len(mouse_14.leftButton): trials_13.addData('mouse_14.leftButton', mouse_14.leftButton[0])
            if len(mouse_14.midButton): trials_13.addData('mouse_14.midButton', mouse_14.midButton[0])
            if len(mouse_14.rightButton): trials_13.addData('mouse_14.rightButton', mouse_14.rightButton[0])
            if len(mouse_14.time): trials_13.addData('mouse_14.time', mouse_14.time[0])
            if len(mouse_14.clicked_name): trials_13.addData('mouse_14.clicked_name', mouse_14.clicked_name[0])
            trials_13.addData('mouse_14.started', mouse_14.tStart)
            trials_13.addData('mouse_14.stopped', mouse_14.tStop)
            trials_13.addData('backvideo23.started', backvideo23.tStartRefresh)
            trials_13.addData('backvideo23.stopped', backvideo23.tStopRefresh)
            movie_14.stop()
            trials_13.addData('closevideo_14.started', closevideo_14.tStartRefresh)
            trials_13.addData('closevideo_14.stopped', closevideo_14.tStopRefresh)
            trials_13.addData('blender23.started', blender23.tStartRefresh)
            trials_13.addData('blender23.stopped', blender23.tStopRefresh)
            trials_13.addData('quickkey23.started', quickkey23.tStartRefresh)
            trials_13.addData('quickkey23.stopped', quickkey23.tStopRefresh)
            trials_13.addData('blenderquickkey23.started', blenderquickkey23.tStartRefresh)
            trials_13.addData('blenderquickkey23.stopped', blenderquickkey23.tStopRefresh)
            # the Routine "video2_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath24 repeats of 'trials_13'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_14 = data.TrialHandler(nReps=videopath25, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_14')
        thisExp.addLoop(trials_14)  # add the loop to the experiment
        thisTrial_14 = trials_14.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_14.rgb)
        if thisTrial_14 != None:
            for paramName in thisTrial_14:
                exec('{} = thisTrial_14[paramName]'.format(paramName))
        
        for thisTrial_14 in trials_14:
            currentLoop = trials_14
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_14.rgb)
            if thisTrial_14 != None:
                for paramName in thisTrial_14:
                    exec('{} = thisTrial_14[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video2_4"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_15.keys = []
            key_resp_15.rt = []
            _key_resp_15_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp24)!=0:
                movie_15.pause()
                movie_15.seek(int(remembertimestamp24[-1]))
                movie_15.play()
                Time1 = 0
            showf=0
            enter1=0  
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_15
            mouse_15.x = []
            mouse_15.y = []
            mouse_15.leftButton = []
            mouse_15.midButton = []
            mouse_15.rightButton = []
            mouse_15.time = []
            mouse_15.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_15.mouseClock.reset()
            # keep track of which components have finished
            video2_4Components = [key_resp_15, mouse_15, backvideo24, movie_15, closevideo_15, blender24, quickkey24, blenderquickkey24]
            for thisComponent in video2_4Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video2_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video2_4"-------
            while continueRoutine:
                # get current time
                t = video2_4Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video2_4Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_15* updates
                waitOnFlip = False
                if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_15.frameNStart = frameN  # exact frame index
                    key_resp_15.tStart = t  # local t and not account for scr refresh
                    key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
                    key_resp_15.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_15.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_15.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_15_allKeys.extend(theseKeys)
                    if len(_key_resp_15_allKeys):
                        key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
                        key_resp_15.rt = _key_resp_15_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey24.setAutoDraw(False)
                    blenderquickkey24.setAutoDraw(False)
                if (blender%2)!=1:
                    blender24.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_15.status == PLAYING:
                            movie_15.pause()
                            Time1 = 1
                        elif movie_15.status == PAUSED:
                            movie_15.play()
                            Time1 = 0
                    elif key=='s':
                        change=change+1
                        movie_15.pause()
                        ntime = max(0.0,movie_15.duration)
                        movie_15.seek(ntime)
                        movie_15.play()
                        Time1 = 0
                            
                    if movie_15.status == PLAYING:
                        if key=='period':
                            movie_15.pause()
                            ntime = min(movie_15.getCurrentFrameTime( ) + 5.0, movie_15.duration)
                            movie_15.seek(ntime)
                            movie_15.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma':
                            movie_15.pause()
                            ntime = max(movie_15.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_15.seek(ntime)
                            movie_15.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey24.setAutoDraw(True)    
                                blenderquickkey24.setAutoDraw(False) 
                                movie_15.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey24.setAutoDraw(True) 
                                quickkey24.setAutoDraw(False)
                                movie_15.pause()
                            else:
                                blenderquickkey24.setAutoDraw(False) 
                                quickkey24.setAutoDraw(False)
                                movie_15.play()
                
                    elif movie_15.status == PAUSED:
                        if key=='period':
                            movie_15.pause()
                            ntime = min(movie_15.getCurrentFrameTime( ) + 5.0, movie_15.duration)
                            movie_15.seek(ntime)
                            movie_15.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma':
                            movie_15.pause()
                            ntime = max(movie_15.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_15.seek(ntime)
                            movie_15.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_15.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey24.setAutoDraw(True)    
                                blenderquickkey24.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey24.setAutoDraw(True) 
                                quickkey24.setAutoDraw(False)
                            else:
                                blenderquickkey24.setAutoDraw(False) 
                                quickkey24.setAutoDraw(False)
                            
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey24.setAutoDraw(True)    
                            blenderquickkey24.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey24.setAutoDraw(True) 
                            quickkey24.setAutoDraw(False)
                        else:
                            blenderquickkey24.setAutoDraw(False) 
                            quickkey24.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video2-4 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender24.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video2-4 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender24.setAutoDraw(False)
                # *mouse_15* updates
                if mouse_15.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_15.frameNStart = frameN  # exact frame index
                    mouse_15.tStart = t  # local t and not account for scr refresh
                    mouse_15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_15, 'tStartRefresh')  # time at next scr refresh
                    mouse_15.status = STARTED
                    prevButtonState = mouse_15.getPressed()  # if button is down already this ISN'T a new click
                if mouse_15.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_15.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_15,]:
                                if obj.contains(mouse_15):
                                    gotValidClick = True
                                    mouse_15.clicked_name.append(obj.name)
                            x, y = mouse_15.getPos()
                            mouse_15.x.append(x)
                            mouse_15.y.append(y)
                            buttons = mouse_15.getPressed()
                            mouse_15.leftButton.append(buttons[0])
                            mouse_15.midButton.append(buttons[1])
                            mouse_15.rightButton.append(buttons[2])
                            mouse_15.time.append(mouse_15.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo24* updates
                if backvideo24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo24.frameNStart = frameN  # exact frame index
                    backvideo24.tStart = t  # local t and not account for scr refresh
                    backvideo24.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo24, 'tStartRefresh')  # time at next scr refresh
                    backvideo24.setAutoDraw(True)
                
                # *movie_15* updates
                if movie_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_15.frameNStart = frameN  # exact frame index
                    movie_15.tStart = t  # local t and not account for scr refresh
                    movie_15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_15, 'tStartRefresh')  # time at next scr refresh
                    movie_15.setAutoDraw(True)
                
                # *closevideo_15* updates
                if closevideo_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_15.frameNStart = frameN  # exact frame index
                    closevideo_15.tStart = t  # local t and not account for scr refresh
                    closevideo_15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_15, 'tStartRefresh')  # time at next scr refresh
                    closevideo_15.setAutoDraw(True)
                
                # *blender24* updates
                if blender24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender24.frameNStart = frameN  # exact frame index
                    blender24.tStart = t  # local t and not account for scr refresh
                    blender24.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender24, 'tStartRefresh')  # time at next scr refresh
                    blender24.setAutoDraw(True)
                
                # *quickkey24* updates
                if quickkey24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey24.frameNStart = frameN  # exact frame index
                    quickkey24.tStart = t  # local t and not account for scr refresh
                    quickkey24.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey24, 'tStartRefresh')  # time at next scr refresh
                    quickkey24.setAutoDraw(True)
                
                # *blenderquickkey24* updates
                if blenderquickkey24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey24.frameNStart = frameN  # exact frame index
                    blenderquickkey24.tStart = t  # local t and not account for scr refresh
                    blenderquickkey24.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey24, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey24.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video2_4Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video2_4"-------
            for thisComponent in video2_4Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_15.keys in ['', [], None]:  # No response was made
                key_resp_15.keys = None
            trials_14.addData('key_resp_15.keys',key_resp_15.keys)
            if key_resp_15.keys != None:  # we had a response
                trials_14.addData('key_resp_15.rt', key_resp_15.rt)
            trials_14.addData('key_resp_15.started', key_resp_15.tStartRefresh)
            trials_14.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime()) 
                    allsteptime.append('video2-4 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video2-4 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_15.getCurrentFrameTime( )
                remembertimestamp24.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime11.append(sum(Watchtime1))
            #    allsteptime.append('video2-4 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime11.append(sum(Watchtime1))
            #    allsteptime.append('video2-4 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
             
            totalpath2=1
            # store data for trials_14 (TrialHandler)
            if len(mouse_15.x): trials_14.addData('mouse_15.x', mouse_15.x[0])
            if len(mouse_15.y): trials_14.addData('mouse_15.y', mouse_15.y[0])
            if len(mouse_15.leftButton): trials_14.addData('mouse_15.leftButton', mouse_15.leftButton[0])
            if len(mouse_15.midButton): trials_14.addData('mouse_15.midButton', mouse_15.midButton[0])
            if len(mouse_15.rightButton): trials_14.addData('mouse_15.rightButton', mouse_15.rightButton[0])
            if len(mouse_15.time): trials_14.addData('mouse_15.time', mouse_15.time[0])
            if len(mouse_15.clicked_name): trials_14.addData('mouse_15.clicked_name', mouse_15.clicked_name[0])
            trials_14.addData('mouse_15.started', mouse_15.tStart)
            trials_14.addData('mouse_15.stopped', mouse_15.tStop)
            trials_14.addData('backvideo24.started', backvideo24.tStartRefresh)
            trials_14.addData('backvideo24.stopped', backvideo24.tStopRefresh)
            movie_15.stop()
            trials_14.addData('closevideo_15.started', closevideo_15.tStartRefresh)
            trials_14.addData('closevideo_15.stopped', closevideo_15.tStopRefresh)
            trials_14.addData('blender24.started', blender24.tStartRefresh)
            trials_14.addData('blender24.stopped', blender24.tStopRefresh)
            trials_14.addData('quickkey24.started', quickkey24.tStartRefresh)
            trials_14.addData('quickkey24.stopped', quickkey24.tStopRefresh)
            trials_14.addData('blenderquickkey24.started', blenderquickkey24.tStartRefresh)
            trials_14.addData('blenderquickkey24.stopped', blenderquickkey24.tStopRefresh)
            # the Routine "video2_4" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath25 repeats of 'trials_14'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_15 = data.TrialHandler(nReps=videopath26, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_15')
        thisExp.addLoop(trials_15)  # add the loop to the experiment
        thisTrial_15 = trials_15.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_15.rgb)
        if thisTrial_15 != None:
            for paramName in thisTrial_15:
                exec('{} = thisTrial_15[paramName]'.format(paramName))
        
        for thisTrial_15 in trials_15:
            currentLoop = trials_15
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_15.rgb)
            if thisTrial_15 != None:
                for paramName in thisTrial_15:
                    exec('{} = thisTrial_15[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video2_5"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_16.keys = []
            key_resp_16.rt = []
            _key_resp_16_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp25)!=0:
                movie_16.pause()
                movie_16.seek(int(remembertimestamp25[-1]))
                movie_16.play()
                Time1 = 0
            showf=0
            enter1=0 
            blender=0
            enterspace=0
            stopblender=0
            newchange=0    
            # setup some python lists for storing info about the mouse_16
            mouse_16.x = []
            mouse_16.y = []
            mouse_16.leftButton = []
            mouse_16.midButton = []
            mouse_16.rightButton = []
            mouse_16.time = []
            mouse_16.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_16.mouseClock.reset()
            # keep track of which components have finished
            video2_5Components = [key_resp_16, mouse_16, backvideo25, movie_16, closevideo_16, blender25, quickkey25, blenderquickkey25]
            for thisComponent in video2_5Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video2_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video2_5"-------
            while continueRoutine:
                # get current time
                t = video2_5Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video2_5Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_16* updates
                waitOnFlip = False
                if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_16.frameNStart = frameN  # exact frame index
                    key_resp_16.tStart = t  # local t and not account for scr refresh
                    key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
                    key_resp_16.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_16.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_16.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_16_allKeys.extend(theseKeys)
                    if len(_key_resp_16_allKeys):
                        key_resp_16.keys = _key_resp_16_allKeys[-1].name  # just the last key pressed
                        key_resp_16.rt = _key_resp_16_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey25.setAutoDraw(False)
                    blenderquickkey25.setAutoDraw(False)
                if (blender%2)!=1:
                    blender25.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_16.status == PLAYING:
                            movie_16.pause()
                            Time1 = 1
                        elif movie_16.status == PAUSED:
                            movie_16.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_16.pause()
                        ntime = max(0.0,movie_16.duration)
                        movie_16.seek(ntime)
                        movie_16.play()
                        Time1 = 0
                
                    if movie_16.status == PLAYING:
                        if key=='period':
                            movie_16.pause()
                            ntime = min(movie_16.getCurrentFrameTime( ) + 5.0, movie_16.duration)
                            movie_16.seek(ntime)
                            movie_16.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_16.pause()
                            ntime = max(movie_16.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_16.seek(ntime)
                            movie_16.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey25.setAutoDraw(True)    
                                blenderquickkey25.setAutoDraw(False) 
                                movie_16.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey25.setAutoDraw(True) 
                                quickkey25.setAutoDraw(False)
                                movie_16.pause()
                            else:
                                blenderquickkey25.setAutoDraw(False) 
                                quickkey25.setAutoDraw(False)
                
                    elif movie_16.status == PAUSED:    
                        if key=='period':
                            movie_16.pause()
                            ntime = min(movie_16.getCurrentFrameTime( ) + 5.0, movie_16.duration)
                            movie_16.seek(ntime)
                            movie_16.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_16.pause()
                            ntime = max(movie_16.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_16.seek(ntime)
                            movie_16.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_16.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey25.setAutoDraw(True)    
                                blenderquickkey25.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey25.setAutoDraw(True) 
                                quickkey25.setAutoDraw(False)
                            else:
                                blenderquickkey25.setAutoDraw(False) 
                                quickkey25.setAutoDraw(False)
                       
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey25.setAutoDraw(True)    
                            blenderquickkey25.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey25.setAutoDraw(True) 
                            quickkey25.setAutoDraw(False)
                        else:
                            blenderquickkey25.setAutoDraw(False) 
                            quickkey25.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video2-5 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender25.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video2-5 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender25.setAutoDraw(False)
                # *mouse_16* updates
                if mouse_16.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_16.frameNStart = frameN  # exact frame index
                    mouse_16.tStart = t  # local t and not account for scr refresh
                    mouse_16.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_16, 'tStartRefresh')  # time at next scr refresh
                    mouse_16.status = STARTED
                    prevButtonState = mouse_16.getPressed()  # if button is down already this ISN'T a new click
                if mouse_16.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_16.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_16,]:
                                if obj.contains(mouse_16):
                                    gotValidClick = True
                                    mouse_16.clicked_name.append(obj.name)
                            x, y = mouse_16.getPos()
                            mouse_16.x.append(x)
                            mouse_16.y.append(y)
                            buttons = mouse_16.getPressed()
                            mouse_16.leftButton.append(buttons[0])
                            mouse_16.midButton.append(buttons[1])
                            mouse_16.rightButton.append(buttons[2])
                            mouse_16.time.append(mouse_16.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo25* updates
                if backvideo25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo25.frameNStart = frameN  # exact frame index
                    backvideo25.tStart = t  # local t and not account for scr refresh
                    backvideo25.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo25, 'tStartRefresh')  # time at next scr refresh
                    backvideo25.setAutoDraw(True)
                
                # *movie_16* updates
                if movie_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_16.frameNStart = frameN  # exact frame index
                    movie_16.tStart = t  # local t and not account for scr refresh
                    movie_16.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_16, 'tStartRefresh')  # time at next scr refresh
                    movie_16.setAutoDraw(True)
                
                # *closevideo_16* updates
                if closevideo_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_16.frameNStart = frameN  # exact frame index
                    closevideo_16.tStart = t  # local t and not account for scr refresh
                    closevideo_16.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_16, 'tStartRefresh')  # time at next scr refresh
                    closevideo_16.setAutoDraw(True)
                
                # *blender25* updates
                if blender25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender25.frameNStart = frameN  # exact frame index
                    blender25.tStart = t  # local t and not account for scr refresh
                    blender25.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender25, 'tStartRefresh')  # time at next scr refresh
                    blender25.setAutoDraw(True)
                
                # *quickkey25* updates
                if quickkey25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey25.frameNStart = frameN  # exact frame index
                    quickkey25.tStart = t  # local t and not account for scr refresh
                    quickkey25.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey25, 'tStartRefresh')  # time at next scr refresh
                    quickkey25.setAutoDraw(True)
                
                # *blenderquickkey25* updates
                if blenderquickkey25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey25.frameNStart = frameN  # exact frame index
                    blenderquickkey25.tStart = t  # local t and not account for scr refresh
                    blenderquickkey25.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey25, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey25.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video2_5Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video2_5"-------
            for thisComponent in video2_5Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_16.keys in ['', [], None]:  # No response was made
                key_resp_16.keys = None
            trials_15.addData('key_resp_16.keys',key_resp_16.keys)
            if key_resp_16.keys != None:  # we had a response
                trials_15.addData('key_resp_16.rt', key_resp_16.rt)
            trials_15.addData('key_resp_16.started', key_resp_16.tStartRefresh)
            trials_15.addData('key_resp_16.stopped', key_resp_16.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime()) 
                    allsteptime.append('video2-5 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video2-5 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_16.getCurrentFrameTime( )
                remembertimestamp25.append(nowtime)
            
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime12.append(sum(Watchtime1))
            #    allsteptime.append('video2-5 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime12.append(sum(Watchtime1))
            #    allsteptime.append('video2-5 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            totalpath2=1
            # store data for trials_15 (TrialHandler)
            if len(mouse_16.x): trials_15.addData('mouse_16.x', mouse_16.x[0])
            if len(mouse_16.y): trials_15.addData('mouse_16.y', mouse_16.y[0])
            if len(mouse_16.leftButton): trials_15.addData('mouse_16.leftButton', mouse_16.leftButton[0])
            if len(mouse_16.midButton): trials_15.addData('mouse_16.midButton', mouse_16.midButton[0])
            if len(mouse_16.rightButton): trials_15.addData('mouse_16.rightButton', mouse_16.rightButton[0])
            if len(mouse_16.time): trials_15.addData('mouse_16.time', mouse_16.time[0])
            if len(mouse_16.clicked_name): trials_15.addData('mouse_16.clicked_name', mouse_16.clicked_name[0])
            trials_15.addData('mouse_16.started', mouse_16.tStart)
            trials_15.addData('mouse_16.stopped', mouse_16.tStop)
            trials_15.addData('backvideo25.started', backvideo25.tStartRefresh)
            trials_15.addData('backvideo25.stopped', backvideo25.tStopRefresh)
            movie_16.stop()
            trials_15.addData('closevideo_16.started', closevideo_16.tStartRefresh)
            trials_15.addData('closevideo_16.stopped', closevideo_16.tStopRefresh)
            trials_15.addData('blender25.started', blender25.tStartRefresh)
            trials_15.addData('blender25.stopped', blender25.tStopRefresh)
            trials_15.addData('quickkey25.started', quickkey25.tStartRefresh)
            trials_15.addData('quickkey25.stopped', quickkey25.tStopRefresh)
            trials_15.addData('blenderquickkey25.started', blenderquickkey25.tStartRefresh)
            trials_15.addData('blenderquickkey25.stopped', blenderquickkey25.tStopRefresh)
            # the Routine "video2_5" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath26 repeats of 'trials_15'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_16 = data.TrialHandler(nReps=videopath27, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_16')
        thisExp.addLoop(trials_16)  # add the loop to the experiment
        thisTrial_16 = trials_16.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_16.rgb)
        if thisTrial_16 != None:
            for paramName in thisTrial_16:
                exec('{} = thisTrial_16[paramName]'.format(paramName))
        
        for thisTrial_16 in trials_16:
            currentLoop = trials_16
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_16.rgb)
            if thisTrial_16 != None:
                for paramName in thisTrial_16:
                    exec('{} = thisTrial_16[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video2_6"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_17.keys = []
            key_resp_17.rt = []
            _key_resp_17_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp26)!=0:
                movie_17.pause()
                movie_17.seek(int(remembertimestamp26[-1]))
                movie_17.play()
                Time1 = 0
            showf=0
            enter1=0    
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_17
            mouse_17.x = []
            mouse_17.y = []
            mouse_17.leftButton = []
            mouse_17.midButton = []
            mouse_17.rightButton = []
            mouse_17.time = []
            mouse_17.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_17.mouseClock.reset()
            # keep track of which components have finished
            video2_6Components = [key_resp_17, mouse_17, backvideo26, movie_17, closevideo_17, blender26, quickkey26, blenderquickkey26]
            for thisComponent in video2_6Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video2_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video2_6"-------
            while continueRoutine:
                # get current time
                t = video2_6Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video2_6Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_17* updates
                waitOnFlip = False
                if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_17.frameNStart = frameN  # exact frame index
                    key_resp_17.tStart = t  # local t and not account for scr refresh
                    key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
                    key_resp_17.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_17.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_17.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_17_allKeys.extend(theseKeys)
                    if len(_key_resp_17_allKeys):
                        key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
                        key_resp_17.rt = _key_resp_17_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey26.setAutoDraw(False)
                    blenderquickkey26.setAutoDraw(False)
                if (blender%2)!=1:
                    blender26.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_17.status == PLAYING:
                            movie_17.pause()
                            Time1 = 1
                        elif movie_17.status == PAUSED:
                            movie_17.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_17.pause()
                        ntime = max(0.0,movie_17.duration)
                        movie_17.seek(ntime)
                        movie_17.play()
                        Time1 = 0
                            
                    if movie_17.status == PLAYING:
                        if key=='period':
                            movie_17.pause()
                            ntime = min(movie_17.getCurrentFrameTime( ) + 5.0, movie_17.duration)
                            movie_17.seek(ntime)
                            movie_17.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_17.pause()
                            ntime = max(movie_17.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_17.seek(ntime)
                            movie_17.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey26.setAutoDraw(True)    
                                blenderquickkey26.setAutoDraw(False)
                                movie_17.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey26.setAutoDraw(True) 
                                quickkey26.setAutoDraw(False)
                                movie_17.pause()
                            else:
                                blenderquickkey26.setAutoDraw(False)
                                quickkey26.setAutoDraw(False)
                
                    elif movie_17.status == PAUSED:      
                        if key=='period':
                            movie_17.pause()
                            ntime = min(movie_17.getCurrentFrameTime( ) + 5.0, movie_17.duration)
                            movie_17.seek(ntime)
                            movie_17.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_17.pause()
                            ntime = max(movie_17.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_17.seek(ntime)
                            movie_17.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_17.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey26.setAutoDraw(True)    
                                blenderquickkey26.setAutoDraw(False)
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey26.setAutoDraw(True) 
                                quickkey26.setAutoDraw(False)
                            else:
                                blenderquickkey26.setAutoDraw(False)
                                quickkey26.setAutoDraw(False)
                          
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1 
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey26.setAutoDraw(True)    
                            blenderquickkey26.setAutoDraw(False)
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey26.setAutoDraw(True) 
                            quickkey26.setAutoDraw(False)
                        else:
                            blenderquickkey26.setAutoDraw(False)
                            quickkey26.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video2-6 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender26.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video2-6 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender26.setAutoDraw(False)
                # *mouse_17* updates
                if mouse_17.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_17.frameNStart = frameN  # exact frame index
                    mouse_17.tStart = t  # local t and not account for scr refresh
                    mouse_17.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_17, 'tStartRefresh')  # time at next scr refresh
                    mouse_17.status = STARTED
                    prevButtonState = mouse_17.getPressed()  # if button is down already this ISN'T a new click
                if mouse_17.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_17.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_17,]:
                                if obj.contains(mouse_17):
                                    gotValidClick = True
                                    mouse_17.clicked_name.append(obj.name)
                            x, y = mouse_17.getPos()
                            mouse_17.x.append(x)
                            mouse_17.y.append(y)
                            buttons = mouse_17.getPressed()
                            mouse_17.leftButton.append(buttons[0])
                            mouse_17.midButton.append(buttons[1])
                            mouse_17.rightButton.append(buttons[2])
                            mouse_17.time.append(mouse_17.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo26* updates
                if backvideo26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo26.frameNStart = frameN  # exact frame index
                    backvideo26.tStart = t  # local t and not account for scr refresh
                    backvideo26.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo26, 'tStartRefresh')  # time at next scr refresh
                    backvideo26.setAutoDraw(True)
                
                # *movie_17* updates
                if movie_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_17.frameNStart = frameN  # exact frame index
                    movie_17.tStart = t  # local t and not account for scr refresh
                    movie_17.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_17, 'tStartRefresh')  # time at next scr refresh
                    movie_17.setAutoDraw(True)
                
                # *closevideo_17* updates
                if closevideo_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_17.frameNStart = frameN  # exact frame index
                    closevideo_17.tStart = t  # local t and not account for scr refresh
                    closevideo_17.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_17, 'tStartRefresh')  # time at next scr refresh
                    closevideo_17.setAutoDraw(True)
                
                # *blender26* updates
                if blender26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender26.frameNStart = frameN  # exact frame index
                    blender26.tStart = t  # local t and not account for scr refresh
                    blender26.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender26, 'tStartRefresh')  # time at next scr refresh
                    blender26.setAutoDraw(True)
                
                # *quickkey26* updates
                if quickkey26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey26.frameNStart = frameN  # exact frame index
                    quickkey26.tStart = t  # local t and not account for scr refresh
                    quickkey26.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey26, 'tStartRefresh')  # time at next scr refresh
                    quickkey26.setAutoDraw(True)
                
                # *blenderquickkey26* updates
                if blenderquickkey26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey26.frameNStart = frameN  # exact frame index
                    blenderquickkey26.tStart = t  # local t and not account for scr refresh
                    blenderquickkey26.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey26, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey26.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video2_6Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video2_6"-------
            for thisComponent in video2_6Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_17.keys in ['', [], None]:  # No response was made
                key_resp_17.keys = None
            trials_16.addData('key_resp_17.keys',key_resp_17.keys)
            if key_resp_17.keys != None:  # we had a response
                trials_16.addData('key_resp_17.rt', key_resp_17.rt)
            trials_16.addData('key_resp_17.started', key_resp_17.tStartRefresh)
            trials_16.addData('key_resp_17.stopped', key_resp_17.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime()) 
                    allsteptime.append('video2-6 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video2-6 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_17.getCurrentFrameTime( )
                remembertimestamp26.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime13.append(sum(Watchtime1))
            #    allsteptime.append('video2-6 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime13.append(sum(Watchtime1))
            #    allsteptime.append('video2-6 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            
            totalpath2=1
            # store data for trials_16 (TrialHandler)
            if len(mouse_17.x): trials_16.addData('mouse_17.x', mouse_17.x[0])
            if len(mouse_17.y): trials_16.addData('mouse_17.y', mouse_17.y[0])
            if len(mouse_17.leftButton): trials_16.addData('mouse_17.leftButton', mouse_17.leftButton[0])
            if len(mouse_17.midButton): trials_16.addData('mouse_17.midButton', mouse_17.midButton[0])
            if len(mouse_17.rightButton): trials_16.addData('mouse_17.rightButton', mouse_17.rightButton[0])
            if len(mouse_17.time): trials_16.addData('mouse_17.time', mouse_17.time[0])
            if len(mouse_17.clicked_name): trials_16.addData('mouse_17.clicked_name', mouse_17.clicked_name[0])
            trials_16.addData('mouse_17.started', mouse_17.tStart)
            trials_16.addData('mouse_17.stopped', mouse_17.tStop)
            trials_16.addData('backvideo26.started', backvideo26.tStartRefresh)
            trials_16.addData('backvideo26.stopped', backvideo26.tStopRefresh)
            movie_17.stop()
            trials_16.addData('closevideo_17.started', closevideo_17.tStartRefresh)
            trials_16.addData('closevideo_17.stopped', closevideo_17.tStopRefresh)
            trials_16.addData('blender26.started', blender26.tStartRefresh)
            trials_16.addData('blender26.stopped', blender26.tStopRefresh)
            trials_16.addData('quickkey26.started', quickkey26.tStartRefresh)
            trials_16.addData('quickkey26.stopped', quickkey26.tStopRefresh)
            trials_16.addData('blenderquickkey26.started', blenderquickkey26.tStartRefresh)
            trials_16.addData('blenderquickkey26.stopped', blenderquickkey26.tStopRefresh)
            # the Routine "video2_6" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath27 repeats of 'trials_16'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_26 = data.TrialHandler(nReps=videopath21, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_26')
        thisExp.addLoop(trials_26)  # add the loop to the experiment
        thisTrial_26 = trials_26.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_26.rgb)
        if thisTrial_26 != None:
            for paramName in thisTrial_26:
                exec('{} = thisTrial_26[paramName]'.format(paramName))
        
        for thisTrial_26 in trials_26:
            currentLoop = trials_26
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_26.rgb)
            if thisTrial_26 != None:
                for paramName in thisTrial_26:
                    exec('{} = thisTrial_26[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "cookbook2"-------
            continueRoutine = True
            # update component parameters for each repeat
            # setup some python lists for storing info about the mouse_27
            mouse_27.clicked_name = []
            gotValidClick = False  # until a click is received
            key_resp_27.keys = []
            key_resp_27.rt = []
            _key_resp_27_allKeys = []
            respClock.reset(0)
            Time1=0
            ExperienceClock.reset(0)
            showf=0
            blender=0
            enter1=0 
            newchange=0
            # keep track of which components have finished
            cookbook2Components = [background_2, close_2, mouse_27, key_resp_27, BOOK21, blender27, quickkey27, blenderquickkey27]
            for thisComponent in cookbook2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            cookbook2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "cookbook2"-------
            while continueRoutine:
                # get current time
                t = cookbook2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=cookbook2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *background_2* updates
                if background_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    background_2.frameNStart = frameN  # exact frame index
                    background_2.tStart = t  # local t and not account for scr refresh
                    background_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(background_2, 'tStartRefresh')  # time at next scr refresh
                    background_2.setAutoDraw(True)
                
                # *close_2* updates
                if close_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    close_2.frameNStart = frameN  # exact frame index
                    close_2.tStart = t  # local t and not account for scr refresh
                    close_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(close_2, 'tStartRefresh')  # time at next scr refresh
                    close_2.setAutoDraw(True)
                # *mouse_27* updates
                if mouse_27.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_27.frameNStart = frameN  # exact frame index
                    mouse_27.tStart = t  # local t and not account for scr refresh
                    mouse_27.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_27, 'tStartRefresh')  # time at next scr refresh
                    mouse_27.status = STARTED
                    mouse_27.mouseClock.reset()
                    prevButtonState = mouse_27.getPressed()  # if button is down already this ISN'T a new click
                if mouse_27.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_27.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [close_2,]:
                                if obj.contains(mouse_27):
                                    gotValidClick = True
                                    mouse_27.clicked_name.append(obj.name)
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *key_resp_27* updates
                waitOnFlip = False
                if key_resp_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_27.frameNStart = frameN  # exact frame index
                    key_resp_27.tStart = t  # local t and not account for scr refresh
                    key_resp_27.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_27, 'tStartRefresh')  # time at next scr refresh
                    key_resp_27.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_27.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_27.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_27.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_27.getKeys(keyList=['left', 'right', 'f', 'return'], waitRelease=False)
                    _key_resp_27_allKeys.extend(theseKeys)
                    if len(_key_resp_27_allKeys):
                        key_resp_27.keys = _key_resp_27_allKeys[-1].name  # just the last key pressed
                        key_resp_27.rt = _key_resp_27_allKeys[-1].rt
                
                # *BOOK21* updates
                if BOOK21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK21.frameNStart = frameN  # exact frame index
                    BOOK21.tStart = t  # local t and not account for scr refresh
                    BOOK21.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK21, 'tStartRefresh')  # time at next scr refresh
                    BOOK21.setAutoDraw(True)
                if (showf%2)!=1:
                    quickkey27.setAutoDraw(False)
                    blenderquickkey27.setAutoDraw(False)
                if (blender%2)!=1:
                    blender27.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='return':  
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey27.setAutoDraw(True) 
                            blenderquickkey27.setAutoDraw(False)
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey27.setAutoDraw(True) 
                            quickkey27.setAutoDraw(False)
                        else:
                            blenderquickkey27.setAutoDraw(False)
                            quickkey27.setAutoDraw(False)
                
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('cookbook2 learn')
                            allsteptime.append(MenuClock.getTime())
                            BlenderClock.reset(0)
                            blender27.setAutoDraw(True)
                        else: 
                            BlenderTime.append(BlenderClock.getTime())  
                            allsteptime.append('cookbook2 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            blender27.setAutoDraw(False)
                 # f blender&learn time                           
                    elif key =='f':
                        countcontinue=countcontinue+1
                        showf=showf+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey27.setAutoDraw(True) 
                            blenderquickkey27.setAutoDraw(False)
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey27.setAutoDraw(True) 
                            quickkey27.setAutoDraw(False)
                        else:
                            blenderquickkey27.setAutoDraw(False)
                            quickkey27.setAutoDraw(False)
                
                
                
                # *blender27* updates
                if blender27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender27.frameNStart = frameN  # exact frame index
                    blender27.tStart = t  # local t and not account for scr refresh
                    blender27.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender27, 'tStartRefresh')  # time at next scr refresh
                    blender27.setAutoDraw(True)
                
                # *quickkey27* updates
                if quickkey27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey27.frameNStart = frameN  # exact frame index
                    quickkey27.tStart = t  # local t and not account for scr refresh
                    quickkey27.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey27, 'tStartRefresh')  # time at next scr refresh
                    quickkey27.setAutoDraw(True)
                
                # *blenderquickkey27* updates
                if blenderquickkey27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey27.frameNStart = frameN  # exact frame index
                    blenderquickkey27.tStart = t  # local t and not account for scr refresh
                    blenderquickkey27.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey27, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey27.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cookbook2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "cookbook2"-------
            for thisComponent in cookbook2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_26.addData('background_2.started', background_2.tStartRefresh)
            trials_26.addData('background_2.stopped', background_2.tStopRefresh)
            trials_26.addData('close_2.started', close_2.tStartRefresh)
            trials_26.addData('close_2.stopped', close_2.tStopRefresh)
            # store data for trials_26 (TrialHandler)
            x, y = mouse_27.getPos()
            buttons = mouse_27.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [close_2,]:
                    if obj.contains(mouse_27):
                        gotValidClick = True
                        mouse_27.clicked_name.append(obj.name)
            trials_26.addData('mouse_27.x', x)
            trials_26.addData('mouse_27.y', y)
            trials_26.addData('mouse_27.leftButton', buttons[0])
            trials_26.addData('mouse_27.midButton', buttons[1])
            trials_26.addData('mouse_27.rightButton', buttons[2])
            if len(mouse_27.clicked_name):
                trials_26.addData('mouse_27.clicked_name', mouse_27.clicked_name[0])
            trials_26.addData('mouse_27.started', mouse_27.tStart)
            trials_26.addData('mouse_27.stopped', mouse_27.tStop)
            # check responses
            if key_resp_27.keys in ['', [], None]:  # No response was made
                key_resp_27.keys = None
            trials_26.addData('key_resp_27.keys',key_resp_27.keys)
            if key_resp_27.keys != None:  # we had a response
                trials_26.addData('key_resp_27.rt', key_resp_27.rt)
            trials_26.addData('key_resp_27.started', key_resp_27.tStartRefresh)
            trials_26.addData('key_resp_27.stopped', key_resp_27.tStopRefresh)
            trials_26.addData('BOOK21.started', BOOK21.tStartRefresh)
            trials_26.addData('BOOK21.stopped', BOOK21.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==1 :
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('cookbook2 blender')
                    allsteptime.append(BlenderClock.getTime())
                else:
                    Watchtime1.append(respClock.getTime()) 
                    allsteptime.append('cookbook2 learn')
                    allsteptime.append(MenuClock.getTime())
                change=change+1
            
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Cookbook2.append(sum(Watchtime1))
                AllCookbook.append(sum(Watchtime1))
            #    allsteptime.append('cookbook2 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Cookbook2.append(sum(Watchtime1))
                AllCookbook.append(sum(Watchtime1))
            #    allsteptime.append('cookbook2 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            
            trials_26.addData('blender27.started', blender27.tStartRefresh)
            trials_26.addData('blender27.stopped', blender27.tStopRefresh)
            trials_26.addData('quickkey27.started', quickkey27.tStartRefresh)
            trials_26.addData('quickkey27.stopped', quickkey27.tStopRefresh)
            trials_26.addData('blenderquickkey27.started', blenderquickkey27.tStartRefresh)
            trials_26.addData('blenderquickkey27.stopped', blenderquickkey27.tStopRefresh)
            # the Routine "cookbook2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed videopath21 repeats of 'trials_26'
        
        thisExp.nextEntry()
        
    # completed totalpath2 repeats of 'trials_9'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=totalpath1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "menu1"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_menupath1.keys = []
        key_menupath1.rt = []
        _key_menupath1_allKeys = []
        MenuClock.reset(0)
        ExperienceClock.reset(0)
        path11=0
        path12=0
        path13=0
        path14=0
        path15=0
        path16=0
        path17=0
        
        showf=0
        Time1 = 0
        enter1=0
        blender=0
        newchange=0
        # setup some python lists for storing info about the mouse_33
        mouse_33.clicked_name = []
        gotValidClick = False  # until a click is received
        key_resp_32.keys = []
        key_resp_32.rt = []
        _key_resp_32_allKeys = []
        # keep track of which components have finished
        menu1Components = [key_menupath1, mouse_33, backmenu, close3, key_resp_32, blendermenu1, quickkeymenu1, blenderquickkey1]
        for thisComponent in menu1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        menu1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "menu1"-------
        while continueRoutine:
            # get current time
            t = menu1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=menu1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_menupath1* updates
            waitOnFlip = False
            if key_menupath1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_menupath1.frameNStart = frameN  # exact frame index
                key_menupath1.tStart = t  # local t and not account for scr refresh
                key_menupath1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_menupath1, 'tStartRefresh')  # time at next scr refresh
                key_menupath1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_menupath1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_menupath1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_menupath1.status == STARTED and not waitOnFlip:
                theseKeys = key_menupath1.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7'], waitRelease=False)
                _key_menupath1_allKeys.extend(theseKeys)
                if len(_key_menupath1_allKeys):
                    key_menupath1.keys = _key_menupath1_allKeys[-1].name  # just the last key pressed
                    key_menupath1.rt = _key_menupath1_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            if (showf%2)!=1:
                quickkeymenu1.setAutoDraw(False)
                blenderquickkey1.setAutoDraw(False)
            if (blender%2)!=1:
                blendermenu1.setAutoDraw(False)
            for key in event.getKeys():
                if key =='1':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    path11=1
                elif key =='2':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    path12=1       
                elif key =='3':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    path13=1
                elif key =='4':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    path14=1
                elif key =='5':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    path15=1
                elif key =='6':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    path16=1
                elif key =='7':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    path17=1
              
                elif key =='f':
                    countcontinue=countcontinue+1
                    showf=showf+1
                    if(showf%2)==1 and (enter1%2)==0:
                        quickkeymenu1.setAutoDraw(True)    
                        blenderquickkey1.setAutoDraw(False)
                    elif (showf%2)==1 and (enter1%2)==1:
                        blenderquickkey1.setAutoDraw(True) 
                        quickkeymenu1.setAutoDraw(False)   
                    else:
                        blenderquickkey1.setAutoDraw(False)
                        quickkeymenu1.setAutoDraw(False)
            # f/enter blender&learn time  
                if key =='return':  
                    countcontinue=countcontinue+1
                    enter1=enter1+1
                    blender=blender+1
                    countenter=countenter+1
                    newchange=newchange+1
                    if(showf%2)==1 and (enter1%2)==0:
                        quickkeymenu1.setAutoDraw(True)    
                        blenderquickkey1.setAutoDraw(False)
                    elif (showf%2)==1 and (enter1%2)==1:
                        blenderquickkey1.setAutoDraw(True) 
                        quickkeymenu1.setAutoDraw(False)   
                    else:
                        blenderquickkey1.setAutoDraw(False)
                        quickkeymenu1.setAutoDraw(False)
                    if(enter1%2)==1:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                        BlenderClock.reset(0)
                        blendermenu1.setAutoDraw(True)
                    else: 
                        BlenderTime.append(BlenderClock.getTime())  
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                        MenuClock.reset(0)
                        blendermenu1.setAutoDraw(False)
            # *mouse_33* updates
            if mouse_33.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_33.frameNStart = frameN  # exact frame index
                mouse_33.tStart = t  # local t and not account for scr refresh
                mouse_33.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_33, 'tStartRefresh')  # time at next scr refresh
                mouse_33.status = STARTED
                mouse_33.mouseClock.reset()
                prevButtonState = mouse_33.getPressed()  # if button is down already this ISN'T a new click
            if mouse_33.status == STARTED:  # only update if started and not finished!
                buttons = mouse_33.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [close3,]:
                            if obj.contains(mouse_33):
                                gotValidClick = True
                                mouse_33.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *backmenu* updates
            if backmenu.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                backmenu.frameNStart = frameN  # exact frame index
                backmenu.tStart = t  # local t and not account for scr refresh
                backmenu.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(backmenu, 'tStartRefresh')  # time at next scr refresh
                backmenu.setAutoDraw(True)
            
            # *close3* updates
            if close3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                close3.frameNStart = frameN  # exact frame index
                close3.tStart = t  # local t and not account for scr refresh
                close3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(close3, 'tStartRefresh')  # time at next scr refresh
                close3.setAutoDraw(True)
            
            # *key_resp_32* updates
            waitOnFlip = False
            if key_resp_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_32.frameNStart = frameN  # exact frame index
                key_resp_32.tStart = t  # local t and not account for scr refresh
                key_resp_32.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_32, 'tStartRefresh')  # time at next scr refresh
                key_resp_32.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_32.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_32.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_32.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_32.getKeys(keyList=['f', 'return'], waitRelease=False)
                _key_resp_32_allKeys.extend(theseKeys)
                if len(_key_resp_32_allKeys):
                    key_resp_32.keys = _key_resp_32_allKeys[-1].name  # just the last key pressed
                    key_resp_32.rt = _key_resp_32_allKeys[-1].rt
            
            # *blendermenu1* updates
            if blendermenu1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blendermenu1.frameNStart = frameN  # exact frame index
                blendermenu1.tStart = t  # local t and not account for scr refresh
                blendermenu1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blendermenu1, 'tStartRefresh')  # time at next scr refresh
                blendermenu1.setAutoDraw(True)
            
            # *quickkeymenu1* updates
            if quickkeymenu1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                quickkeymenu1.frameNStart = frameN  # exact frame index
                quickkeymenu1.tStart = t  # local t and not account for scr refresh
                quickkeymenu1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(quickkeymenu1, 'tStartRefresh')  # time at next scr refresh
                quickkeymenu1.setAutoDraw(True)
            
            # *blenderquickkey1* updates
            if blenderquickkey1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blenderquickkey1.frameNStart = frameN  # exact frame index
                blenderquickkey1.tStart = t  # local t and not account for scr refresh
                blenderquickkey1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blenderquickkey1, 'tStartRefresh')  # time at next scr refresh
                blenderquickkey1.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in menu1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "menu1"-------
        for thisComponent in menu1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_menupath1.keys in ['', [], None]:  # No response was made
            key_menupath1.keys = None
        trials_3.addData('key_menupath1.keys',key_menupath1.keys)
        if key_menupath1.keys != None:  # we had a response
            trials_3.addData('key_menupath1.rt', key_menupath1.rt)
        trials_3.addData('key_menupath1.started', key_menupath1.tStartRefresh)
        trials_3.addData('key_menupath1.stopped', key_menupath1.tStopRefresh)
        Experiencetime.append(ExperienceClock.getTime())
        
        if gotValidClick ==True:
            countchange.append(newchange)
            if (enter1%2)==1 :
                BlenderTime.append(BlenderClock.getTime())
                allsteptime.append('menu1 blender')
                allsteptime.append(BlenderClock.getTime())
            else:
                Menutime.append(MenuClock.getTime())
                AllWatchtime.append(MenuClock.getTime())
                allsteptime.append('menu1 learn')
                allsteptime.append(MenuClock.getTime())
            change=change+1
        # store data for trials_3 (TrialHandler)
        x, y = mouse_33.getPos()
        buttons = mouse_33.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [close3,]:
                if obj.contains(mouse_33):
                    gotValidClick = True
                    mouse_33.clicked_name.append(obj.name)
        trials_3.addData('mouse_33.x', x)
        trials_3.addData('mouse_33.y', y)
        trials_3.addData('mouse_33.leftButton', buttons[0])
        trials_3.addData('mouse_33.midButton', buttons[1])
        trials_3.addData('mouse_33.rightButton', buttons[2])
        if len(mouse_33.clicked_name):
            trials_3.addData('mouse_33.clicked_name', mouse_33.clicked_name[0])
        trials_3.addData('mouse_33.started', mouse_33.tStart)
        trials_3.addData('mouse_33.stopped', mouse_33.tStop)
        trials_3.addData('backmenu.started', backmenu.tStartRefresh)
        trials_3.addData('backmenu.stopped', backmenu.tStopRefresh)
        trials_3.addData('close3.started', close3.tStartRefresh)
        trials_3.addData('close3.stopped', close3.tStopRefresh)
        # check responses
        if key_resp_32.keys in ['', [], None]:  # No response was made
            key_resp_32.keys = None
        trials_3.addData('key_resp_32.keys',key_resp_32.keys)
        if key_resp_32.keys != None:  # we had a response
            trials_3.addData('key_resp_32.rt', key_resp_32.rt)
        trials_3.addData('key_resp_32.started', key_resp_32.tStartRefresh)
        trials_3.addData('key_resp_32.stopped', key_resp_32.tStopRefresh)
        trials_3.addData('blendermenu1.started', blendermenu1.tStartRefresh)
        trials_3.addData('blendermenu1.stopped', blendermenu1.tStopRefresh)
        trials_3.addData('quickkeymenu1.started', quickkeymenu1.tStartRefresh)
        trials_3.addData('quickkeymenu1.stopped', quickkeymenu1.tStopRefresh)
        trials_3.addData('blenderquickkey1.started', blenderquickkey1.tStartRefresh)
        trials_3.addData('blenderquickkey1.stopped', blenderquickkey1.tStopRefresh)
        # the Routine "menu1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler(nReps=path12, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_2')
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    exec('{} = thisTrial_2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video1_1"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_5.keys = []
            key_resp_5.rt = []
            _key_resp_5_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp11)!=0:
                movie_5.pause()
                movie_5.seek(int(remembertimestamp11[-1]))
                movie_5.play()
                Time1 = 0
            showf=0
            enter1=0    
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_5
            mouse_5.x = []
            mouse_5.y = []
            mouse_5.leftButton = []
            mouse_5.midButton = []
            mouse_5.rightButton = []
            mouse_5.time = []
            mouse_5.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_5.mouseClock.reset()
            # keep track of which components have finished
            video1_1Components = [key_resp_5, mouse_5, backvideo11, movie_5, closevideo_5, blender11, quickkey11, blenderquickkey11]
            for thisComponent in video1_1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video1_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video1_1"-------
            while continueRoutine:
                # get current time
                t = video1_1Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video1_1Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_5* updates
                waitOnFlip = False
                if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_5.frameNStart = frameN  # exact frame index
                    key_resp_5.tStart = t  # local t and not account for scr refresh
                    key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                    key_resp_5.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_5.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_5.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_5_allKeys.extend(theseKeys)
                    if len(_key_resp_5_allKeys):
                        key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                        key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey11.setAutoDraw(False)
                    blenderquickkey11.setAutoDraw(False)
                if (blender%2)!=1:
                    blender11.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_5.status == PLAYING:
                            movie_5.pause()
                            Time1 = 1
                        elif movie_5.status == PAUSED:
                            movie_5.play()  
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_5.pause()
                        ntime = max(0.0,movie_5.duration)
                        movie_5.seek(ntime)
                        movie_5.play()
                        Time1 = 0
                                                   
                    if movie_5.status == PLAYING:
                        if key=='period':          
                            movie_5.pause()
                            ntime = min(movie_5.getCurrentFrameTime( ) + 5.0, movie_5.duration)
                            movie_5.seek(ntime)
                            movie_5.play()
                            Time1 = 0
                            change=change+1
                   
                        elif key=='comma':            
                            movie_5.pause()
                            ntime = max(movie_5.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_5.seek(ntime)
                            movie_5.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey11.setAutoDraw(True) 
                                blenderquickkey11.setAutoDraw(False) 
                                movie_5.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey11.setAutoDraw(True) 
                                quickkey11.setAutoDraw(False)
                                movie_5.pause()
                            else:
                                blenderquickkey11.setAutoDraw(False) 
                                quickkey11.setAutoDraw(False)
                                movie_5.play()
                
                    elif movie_5.status == PAUSED:
                        if key=='period':
                            movie_5.pause()
                            ntime = min(movie_5.getCurrentFrameTime( ) + 5.0, movie_5.duration)
                            movie_5.seek(ntime)
                            movie_5.play()
                            Time1 = 0
                            change=change+1
                
                   
                        elif key=='comma':            
                            movie_5.pause()
                            ntime = max(movie_5.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_5.seek(ntime)
                            movie_5.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_5.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey11.setAutoDraw(True) 
                                blenderquickkey11.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey11.setAutoDraw(True) 
                                quickkey11.setAutoDraw(False)
                            else:
                                blenderquickkey11.setAutoDraw(False) 
                                quickkey11.setAutoDraw(False)
                                    
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey11.setAutoDraw(True) 
                            blenderquickkey11.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey11.setAutoDraw(True) 
                            quickkey11.setAutoDraw(False)
                        else:
                            blenderquickkey11.setAutoDraw(False) 
                            quickkey11.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video1-1 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender11.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video1-1 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender11.setAutoDraw(False)
                # *mouse_5* updates
                if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_5.frameNStart = frameN  # exact frame index
                    mouse_5.tStart = t  # local t and not account for scr refresh
                    mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
                    mouse_5.status = STARTED
                    prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
                if mouse_5.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_5.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_5,]:
                                if obj.contains(mouse_5):
                                    gotValidClick = True
                                    mouse_5.clicked_name.append(obj.name)
                            x, y = mouse_5.getPos()
                            mouse_5.x.append(x)
                            mouse_5.y.append(y)
                            buttons = mouse_5.getPressed()
                            mouse_5.leftButton.append(buttons[0])
                            mouse_5.midButton.append(buttons[1])
                            mouse_5.rightButton.append(buttons[2])
                            mouse_5.time.append(mouse_5.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo11* updates
                if backvideo11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo11.frameNStart = frameN  # exact frame index
                    backvideo11.tStart = t  # local t and not account for scr refresh
                    backvideo11.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo11, 'tStartRefresh')  # time at next scr refresh
                    backvideo11.setAutoDraw(True)
                
                # *movie_5* updates
                if movie_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_5.frameNStart = frameN  # exact frame index
                    movie_5.tStart = t  # local t and not account for scr refresh
                    movie_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_5, 'tStartRefresh')  # time at next scr refresh
                    movie_5.setAutoDraw(True)
                
                # *closevideo_5* updates
                if closevideo_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_5.frameNStart = frameN  # exact frame index
                    closevideo_5.tStart = t  # local t and not account for scr refresh
                    closevideo_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_5, 'tStartRefresh')  # time at next scr refresh
                    closevideo_5.setAutoDraw(True)
                
                # *blender11* updates
                if blender11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender11.frameNStart = frameN  # exact frame index
                    blender11.tStart = t  # local t and not account for scr refresh
                    blender11.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender11, 'tStartRefresh')  # time at next scr refresh
                    blender11.setAutoDraw(True)
                
                # *quickkey11* updates
                if quickkey11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey11.frameNStart = frameN  # exact frame index
                    quickkey11.tStart = t  # local t and not account for scr refresh
                    quickkey11.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey11, 'tStartRefresh')  # time at next scr refresh
                    quickkey11.setAutoDraw(True)
                
                # *blenderquickkey11* updates
                if blenderquickkey11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey11.frameNStart = frameN  # exact frame index
                    blenderquickkey11.tStart = t  # local t and not account for scr refresh
                    blenderquickkey11.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey11, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey11.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video1_1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video1_1"-------
            for thisComponent in video1_1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_5.keys in ['', [], None]:  # No response was made
                key_resp_5.keys = None
            trials_2.addData('key_resp_5.keys',key_resp_5.keys)
            if key_resp_5.keys != None:  # we had a response
                trials_2.addData('key_resp_5.rt', key_resp_5.rt)
            trials_2.addData('key_resp_5.started', key_resp_5.tStartRefresh)
            trials_2.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime()) 
                    allsteptime.append('video1-1 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video1-1 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_5.getCurrentFrameTime( )
                remembertimestamp11.append(nowtime)
            
            
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime111.append(sum(Watchtime1))
            #    allsteptime.append('video1-1 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime111.append(sum(Watchtime1))
            #    allsteptime.append('video1-1 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
                
            totalpath1=1
            # store data for trials_2 (TrialHandler)
            if len(mouse_5.x): trials_2.addData('mouse_5.x', mouse_5.x[0])
            if len(mouse_5.y): trials_2.addData('mouse_5.y', mouse_5.y[0])
            if len(mouse_5.leftButton): trials_2.addData('mouse_5.leftButton', mouse_5.leftButton[0])
            if len(mouse_5.midButton): trials_2.addData('mouse_5.midButton', mouse_5.midButton[0])
            if len(mouse_5.rightButton): trials_2.addData('mouse_5.rightButton', mouse_5.rightButton[0])
            if len(mouse_5.time): trials_2.addData('mouse_5.time', mouse_5.time[0])
            if len(mouse_5.clicked_name): trials_2.addData('mouse_5.clicked_name', mouse_5.clicked_name[0])
            trials_2.addData('mouse_5.started', mouse_5.tStart)
            trials_2.addData('mouse_5.stopped', mouse_5.tStop)
            trials_2.addData('backvideo11.started', backvideo11.tStartRefresh)
            trials_2.addData('backvideo11.stopped', backvideo11.tStopRefresh)
            movie_5.stop()
            trials_2.addData('closevideo_5.started', closevideo_5.tStartRefresh)
            trials_2.addData('closevideo_5.stopped', closevideo_5.tStopRefresh)
            trials_2.addData('blender11.started', blender11.tStartRefresh)
            trials_2.addData('blender11.stopped', blender11.tStopRefresh)
            trials_2.addData('quickkey11.started', quickkey11.tStartRefresh)
            trials_2.addData('quickkey11.stopped', quickkey11.tStopRefresh)
            trials_2.addData('blenderquickkey11.started', blenderquickkey11.tStartRefresh)
            trials_2.addData('blenderquickkey11.stopped', blenderquickkey11.tStopRefresh)
            # the Routine "video1_1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed path12 repeats of 'trials_2'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_4 = data.TrialHandler(nReps=path13, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_4')
        thisExp.addLoop(trials_4)  # add the loop to the experiment
        thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                exec('{} = thisTrial_4[paramName]'.format(paramName))
        
        for thisTrial_4 in trials_4:
            currentLoop = trials_4
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
            if thisTrial_4 != None:
                for paramName in thisTrial_4:
                    exec('{} = thisTrial_4[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video1_2"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_6.keys = []
            key_resp_6.rt = []
            _key_resp_6_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp12)!=0:
                movie_6.pause()
                movie_6.seek(int(remembertimestamp12[-1]))
                movie_6.play()
                Time1 = 0
            showf=0
            enter1=0    
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_6
            mouse_6.x = []
            mouse_6.y = []
            mouse_6.leftButton = []
            mouse_6.midButton = []
            mouse_6.rightButton = []
            mouse_6.time = []
            mouse_6.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_6.mouseClock.reset()
            # keep track of which components have finished
            video1_2Components = [key_resp_6, mouse_6, backvideo12, movie_6, closevideo_6, blender12, quickkey12, blenderquickkey12]
            for thisComponent in video1_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video1_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video1_2"-------
            while continueRoutine:
                # get current time
                t = video1_2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video1_2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_6* updates
                waitOnFlip = False
                if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_6.frameNStart = frameN  # exact frame index
                    key_resp_6.tStart = t  # local t and not account for scr refresh
                    key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                    key_resp_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_6.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_6.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_6_allKeys.extend(theseKeys)
                    if len(_key_resp_6_allKeys):
                        key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                        key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey12.setAutoDraw(False)
                    blenderquickkey12.setAutoDraw(False)
                if (blender%2)!=1:
                    blender12.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_6.status == PLAYING:
                            movie_6.pause()
                            Time1 = 1
                        elif movie_6.status == PAUSED:
                            movie_6.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_6.pause()
                        ntime = max(0.0,movie_6.duration)
                        movie_6.seek(ntime)
                        movie_6.play()
                        Time1 = 0
                
                    if movie_6.status == PLAYING:
                        if key=='period':          
                            movie_6.pause()
                            ntime = min(movie_6.getCurrentFrameTime( ) + 5.0, movie_6.duration)
                            movie_6.seek(ntime)
                            movie_6.play()
                            Time1 = 0
                            change=change+1
                   
                        elif key=='comma':            
                            movie_6.pause()
                            ntime = max(movie_6.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_6.seek(ntime)
                            movie_6.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey12.setAutoDraw(True)    
                                blenderquickkey12.setAutoDraw(False)
                                movie_6.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey12.setAutoDraw(True) 
                                quickkey12.setAutoDraw(False)
                                movie_6.pause()
                            else:
                                blenderquickkey12.setAutoDraw(False)
                                quickkey12.setAutoDraw(False)
                                movie_6.play()
                                    
                    elif movie_6.status == PAUSED:
                        if key=='period':
                            movie_6.pause()
                            ntime = min(movie_6.getCurrentFrameTime( ) + 5.0, movie_6.duration)
                            movie_6.seek(ntime)
                            movie_6.play()
                            Time1 = 0
                            change=change+1
                   
                        elif key=='comma':            
                            movie_6.pause()
                            ntime = max(movie_6.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_6.seek(ntime)
                            movie_6.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_6.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey12.setAutoDraw(True)    
                                blenderquickkey12.setAutoDraw(False)
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey12.setAutoDraw(True) 
                                quickkey12.setAutoDraw(False)
                            else:
                                blenderquickkey12.setAutoDraw(False)
                                quickkey12.setAutoDraw(False)
                                    
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey12.setAutoDraw(True)    
                            blenderquickkey12.setAutoDraw(False)
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey12.setAutoDraw(True) 
                            quickkey12.setAutoDraw(False)
                        else:
                            blenderquickkey12.setAutoDraw(False)
                            quickkey12.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video1-2 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender12.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video1-2 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender12.setAutoDraw(False)
                # *mouse_6* updates
                if mouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_6.frameNStart = frameN  # exact frame index
                    mouse_6.tStart = t  # local t and not account for scr refresh
                    mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
                    mouse_6.status = STARTED
                    prevButtonState = mouse_6.getPressed()  # if button is down already this ISN'T a new click
                if mouse_6.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_6.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_6,]:
                                if obj.contains(mouse_6):
                                    gotValidClick = True
                                    mouse_6.clicked_name.append(obj.name)
                            x, y = mouse_6.getPos()
                            mouse_6.x.append(x)
                            mouse_6.y.append(y)
                            buttons = mouse_6.getPressed()
                            mouse_6.leftButton.append(buttons[0])
                            mouse_6.midButton.append(buttons[1])
                            mouse_6.rightButton.append(buttons[2])
                            mouse_6.time.append(mouse_6.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo12* updates
                if backvideo12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo12.frameNStart = frameN  # exact frame index
                    backvideo12.tStart = t  # local t and not account for scr refresh
                    backvideo12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo12, 'tStartRefresh')  # time at next scr refresh
                    backvideo12.setAutoDraw(True)
                
                # *movie_6* updates
                if movie_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_6.frameNStart = frameN  # exact frame index
                    movie_6.tStart = t  # local t and not account for scr refresh
                    movie_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_6, 'tStartRefresh')  # time at next scr refresh
                    movie_6.setAutoDraw(True)
                
                # *closevideo_6* updates
                if closevideo_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_6.frameNStart = frameN  # exact frame index
                    closevideo_6.tStart = t  # local t and not account for scr refresh
                    closevideo_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_6, 'tStartRefresh')  # time at next scr refresh
                    closevideo_6.setAutoDraw(True)
                
                # *blender12* updates
                if blender12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender12.frameNStart = frameN  # exact frame index
                    blender12.tStart = t  # local t and not account for scr refresh
                    blender12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender12, 'tStartRefresh')  # time at next scr refresh
                    blender12.setAutoDraw(True)
                
                # *quickkey12* updates
                if quickkey12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey12.frameNStart = frameN  # exact frame index
                    quickkey12.tStart = t  # local t and not account for scr refresh
                    quickkey12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey12, 'tStartRefresh')  # time at next scr refresh
                    quickkey12.setAutoDraw(True)
                
                # *blenderquickkey12* updates
                if blenderquickkey12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey12.frameNStart = frameN  # exact frame index
                    blenderquickkey12.tStart = t  # local t and not account for scr refresh
                    blenderquickkey12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey12, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey12.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video1_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video1_2"-------
            for thisComponent in video1_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_6.keys in ['', [], None]:  # No response was made
                key_resp_6.keys = None
            trials_4.addData('key_resp_6.keys',key_resp_6.keys)
            if key_resp_6.keys != None:  # we had a response
                trials_4.addData('key_resp_6.rt', key_resp_6.rt)
            trials_4.addData('key_resp_6.started', key_resp_6.tStartRefresh)
            trials_4.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime())  
                    allsteptime.append('video1-2 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video1-2 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_6.getCurrentFrameTime( )
                remembertimestamp12.append(nowtime)
            
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime2.append(sum(Watchtime1))
            #    allsteptime.append('video1-2 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime2.append(sum(Watchtime1))
            #    allsteptime.append('video1-2 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            
            totalpath1=1
            # store data for trials_4 (TrialHandler)
            if len(mouse_6.x): trials_4.addData('mouse_6.x', mouse_6.x[0])
            if len(mouse_6.y): trials_4.addData('mouse_6.y', mouse_6.y[0])
            if len(mouse_6.leftButton): trials_4.addData('mouse_6.leftButton', mouse_6.leftButton[0])
            if len(mouse_6.midButton): trials_4.addData('mouse_6.midButton', mouse_6.midButton[0])
            if len(mouse_6.rightButton): trials_4.addData('mouse_6.rightButton', mouse_6.rightButton[0])
            if len(mouse_6.time): trials_4.addData('mouse_6.time', mouse_6.time[0])
            if len(mouse_6.clicked_name): trials_4.addData('mouse_6.clicked_name', mouse_6.clicked_name[0])
            trials_4.addData('mouse_6.started', mouse_6.tStart)
            trials_4.addData('mouse_6.stopped', mouse_6.tStop)
            trials_4.addData('backvideo12.started', backvideo12.tStartRefresh)
            trials_4.addData('backvideo12.stopped', backvideo12.tStopRefresh)
            movie_6.stop()
            trials_4.addData('closevideo_6.started', closevideo_6.tStartRefresh)
            trials_4.addData('closevideo_6.stopped', closevideo_6.tStopRefresh)
            trials_4.addData('blender12.started', blender12.tStartRefresh)
            trials_4.addData('blender12.stopped', blender12.tStopRefresh)
            trials_4.addData('quickkey12.started', quickkey12.tStartRefresh)
            trials_4.addData('quickkey12.stopped', quickkey12.tStopRefresh)
            trials_4.addData('blenderquickkey12.started', blenderquickkey12.tStartRefresh)
            trials_4.addData('blenderquickkey12.stopped', blenderquickkey12.tStopRefresh)
            # the Routine "video1_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed path13 repeats of 'trials_4'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_5 = data.TrialHandler(nReps=path14, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_5')
        thisExp.addLoop(trials_5)  # add the loop to the experiment
        thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                exec('{} = thisTrial_5[paramName]'.format(paramName))
        
        for thisTrial_5 in trials_5:
            currentLoop = trials_5
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
            if thisTrial_5 != None:
                for paramName in thisTrial_5:
                    exec('{} = thisTrial_5[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video1_3"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_7.keys = []
            key_resp_7.rt = []
            _key_resp_7_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp13)!=0:
                movie_7.pause()
                movie_7.seek(int(remembertimestamp13[-1]))
                movie_7.play()
                Time1 = 0
            showf=0
            enter1=0
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_7
            mouse_7.x = []
            mouse_7.y = []
            mouse_7.leftButton = []
            mouse_7.midButton = []
            mouse_7.rightButton = []
            mouse_7.time = []
            mouse_7.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_7.mouseClock.reset()
            # keep track of which components have finished
            video1_3Components = [key_resp_7, mouse_7, backvideo13, movie_7, closevideo_7, blender13, quickkey13, blenderquickkey13]
            for thisComponent in video1_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video1_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video1_3"-------
            while continueRoutine:
                # get current time
                t = video1_3Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video1_3Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_7* updates
                waitOnFlip = False
                if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_7.frameNStart = frameN  # exact frame index
                    key_resp_7.tStart = t  # local t and not account for scr refresh
                    key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                    key_resp_7.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_7.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_7.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_7_allKeys.extend(theseKeys)
                    if len(_key_resp_7_allKeys):
                        key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                        key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey13.setAutoDraw(False)
                    blenderquickkey13.setAutoDraw(False)
                if (blender%2)!=1:
                    blender13.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_7.status == PLAYING:
                            movie_7.pause()
                            Time1 = 1
                        elif movie_7.status == PAUSED:
                            movie_7.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_7.pause()
                        ntime = max(0.0,movie_7.duration)
                        movie_7.seek(ntime)
                        movie_7.play()
                        Time1 = 0
                
                    if movie_7.status == PLAYING:
                        if key=='period':            
                            movie_7.pause()
                            ntime = min(movie_7.getCurrentFrameTime( ) + 5.0, movie_7.duration)
                            movie_7.seek(ntime)
                            movie_7.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_7.pause()
                            ntime = max(movie_7.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_7.seek(ntime)
                            movie_7.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey13.setAutoDraw(True)  
                                blenderquickkey13.setAutoDraw(False)
                                movie_7.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey13.setAutoDraw(True) 
                                quickkey13.setAutoDraw(False)
                                movie_7.pause()
                            else:
                                blenderquickkey13.setAutoDraw(False)
                                quickkey13.setAutoDraw(False)
                                movie_7.play()
                         
                    elif movie_7.status == PAUSED:
                        if key=='period':            
                            movie_7.pause()
                            ntime = min(movie_7.getCurrentFrameTime( ) + 5.0, movie_7.duration)
                            movie_7.seek(ntime)
                            movie_7.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_7.pause()
                            ntime = max(movie_7.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_7.seek(ntime)
                            movie_7.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_7.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey13.setAutoDraw(True)  
                                blenderquickkey13.setAutoDraw(False)
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey13.setAutoDraw(True) 
                                quickkey13.setAutoDraw(False)
                            else:
                                blenderquickkey13.setAutoDraw(False)
                                quickkey13.setAutoDraw(False)
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey13.setAutoDraw(True)  
                            blenderquickkey13.setAutoDraw(False)
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey13.setAutoDraw(True) 
                            quickkey13.setAutoDraw(False)
                        else:
                            blenderquickkey13.setAutoDraw(False)
                            quickkey13.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video1-3 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender13.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video1-3 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender13.setAutoDraw(False)
                # *mouse_7* updates
                if mouse_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_7.frameNStart = frameN  # exact frame index
                    mouse_7.tStart = t  # local t and not account for scr refresh
                    mouse_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_7, 'tStartRefresh')  # time at next scr refresh
                    mouse_7.status = STARTED
                    prevButtonState = mouse_7.getPressed()  # if button is down already this ISN'T a new click
                if mouse_7.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_7.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_7,]:
                                if obj.contains(mouse_7):
                                    gotValidClick = True
                                    mouse_7.clicked_name.append(obj.name)
                            x, y = mouse_7.getPos()
                            mouse_7.x.append(x)
                            mouse_7.y.append(y)
                            buttons = mouse_7.getPressed()
                            mouse_7.leftButton.append(buttons[0])
                            mouse_7.midButton.append(buttons[1])
                            mouse_7.rightButton.append(buttons[2])
                            mouse_7.time.append(mouse_7.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo13* updates
                if backvideo13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo13.frameNStart = frameN  # exact frame index
                    backvideo13.tStart = t  # local t and not account for scr refresh
                    backvideo13.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo13, 'tStartRefresh')  # time at next scr refresh
                    backvideo13.setAutoDraw(True)
                
                # *movie_7* updates
                if movie_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_7.frameNStart = frameN  # exact frame index
                    movie_7.tStart = t  # local t and not account for scr refresh
                    movie_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_7, 'tStartRefresh')  # time at next scr refresh
                    movie_7.setAutoDraw(True)
                
                # *closevideo_7* updates
                if closevideo_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_7.frameNStart = frameN  # exact frame index
                    closevideo_7.tStart = t  # local t and not account for scr refresh
                    closevideo_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_7, 'tStartRefresh')  # time at next scr refresh
                    closevideo_7.setAutoDraw(True)
                
                # *blender13* updates
                if blender13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender13.frameNStart = frameN  # exact frame index
                    blender13.tStart = t  # local t and not account for scr refresh
                    blender13.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender13, 'tStartRefresh')  # time at next scr refresh
                    blender13.setAutoDraw(True)
                
                # *quickkey13* updates
                if quickkey13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey13.frameNStart = frameN  # exact frame index
                    quickkey13.tStart = t  # local t and not account for scr refresh
                    quickkey13.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey13, 'tStartRefresh')  # time at next scr refresh
                    quickkey13.setAutoDraw(True)
                
                # *blenderquickkey13* updates
                if blenderquickkey13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey13.frameNStart = frameN  # exact frame index
                    blenderquickkey13.tStart = t  # local t and not account for scr refresh
                    blenderquickkey13.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey13, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey13.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video1_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video1_3"-------
            for thisComponent in video1_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_7.keys in ['', [], None]:  # No response was made
                key_resp_7.keys = None
            trials_5.addData('key_resp_7.keys',key_resp_7.keys)
            if key_resp_7.keys != None:  # we had a response
                trials_5.addData('key_resp_7.rt', key_resp_7.rt)
            trials_5.addData('key_resp_7.started', key_resp_7.tStartRefresh)
            trials_5.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0:
                    Watchtime1.append(respClock.getTime())  
                    allsteptime.append('video1-3 blender')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video1-3 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_7.getCurrentFrameTime( )
                remembertimestamp13.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime3.append(sum(Watchtime1))
            #    allsteptime.append('video1-3 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime3.append(sum(Watchtime1))
            #    allsteptime.append('video1-3 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
                
            totalpath1=1
            # store data for trials_5 (TrialHandler)
            if len(mouse_7.x): trials_5.addData('mouse_7.x', mouse_7.x[0])
            if len(mouse_7.y): trials_5.addData('mouse_7.y', mouse_7.y[0])
            if len(mouse_7.leftButton): trials_5.addData('mouse_7.leftButton', mouse_7.leftButton[0])
            if len(mouse_7.midButton): trials_5.addData('mouse_7.midButton', mouse_7.midButton[0])
            if len(mouse_7.rightButton): trials_5.addData('mouse_7.rightButton', mouse_7.rightButton[0])
            if len(mouse_7.time): trials_5.addData('mouse_7.time', mouse_7.time[0])
            if len(mouse_7.clicked_name): trials_5.addData('mouse_7.clicked_name', mouse_7.clicked_name[0])
            trials_5.addData('mouse_7.started', mouse_7.tStart)
            trials_5.addData('mouse_7.stopped', mouse_7.tStop)
            trials_5.addData('backvideo13.started', backvideo13.tStartRefresh)
            trials_5.addData('backvideo13.stopped', backvideo13.tStopRefresh)
            movie_7.stop()
            trials_5.addData('closevideo_7.started', closevideo_7.tStartRefresh)
            trials_5.addData('closevideo_7.stopped', closevideo_7.tStopRefresh)
            trials_5.addData('blender13.started', blender13.tStartRefresh)
            trials_5.addData('blender13.stopped', blender13.tStopRefresh)
            trials_5.addData('quickkey13.started', quickkey13.tStartRefresh)
            trials_5.addData('quickkey13.stopped', quickkey13.tStopRefresh)
            trials_5.addData('blenderquickkey13.started', blenderquickkey13.tStartRefresh)
            trials_5.addData('blenderquickkey13.stopped', blenderquickkey13.tStopRefresh)
            # the Routine "video1_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed path14 repeats of 'trials_5'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_6 = data.TrialHandler(nReps=path15, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_6')
        thisExp.addLoop(trials_6)  # add the loop to the experiment
        thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
        if thisTrial_6 != None:
            for paramName in thisTrial_6:
                exec('{} = thisTrial_6[paramName]'.format(paramName))
        
        for thisTrial_6 in trials_6:
            currentLoop = trials_6
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
            if thisTrial_6 != None:
                for paramName in thisTrial_6:
                    exec('{} = thisTrial_6[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video1_4"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_8.keys = []
            key_resp_8.rt = []
            _key_resp_8_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp14)!=0:
                movie_8.pause()
                movie_8.seek(int(remembertimestamp14[-1]))
                movie_8.play()
                Time1 = 0
            showf=0
            enter1=0    
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_8
            mouse_8.x = []
            mouse_8.y = []
            mouse_8.leftButton = []
            mouse_8.midButton = []
            mouse_8.rightButton = []
            mouse_8.time = []
            mouse_8.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_8.mouseClock.reset()
            # keep track of which components have finished
            video1_4Components = [key_resp_8, mouse_8, backvideo14, movie_8, closevideo_8, blender14, quickkey14, blenderquickkey14]
            for thisComponent in video1_4Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video1_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video1_4"-------
            while continueRoutine:
                # get current time
                t = video1_4Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video1_4Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_8* updates
                waitOnFlip = False
                if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_8.frameNStart = frameN  # exact frame index
                    key_resp_8.tStart = t  # local t and not account for scr refresh
                    key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                    key_resp_8.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_8.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_8.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_8_allKeys.extend(theseKeys)
                    if len(_key_resp_8_allKeys):
                        key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                        key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey14.setAutoDraw(False)
                    blenderquickkey14.setAutoDraw(False)
                if (blender%2)!=1:
                    blender14.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_8.status == PLAYING:
                            movie_8.pause()
                            Time1 = 1
                        elif movie_8.status == PAUSED:
                            movie_8.play()
                            Time1 = 0
                    elif key=='s':
                        change=change+1
                        movie_8.pause()
                        ntime = max(0.0,movie_8.duration)
                        movie_8.seek(ntime)
                        movie_8.play()
                        Time1 = 0
                            
                    if movie_8.status == PLAYING:
                        if key=='period':
                            movie_8.pause()
                            ntime = min(movie_8.getCurrentFrameTime( ) + 5.0, movie_8.duration)
                            movie_8.seek(ntime)
                            movie_8.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_8.pause()
                            ntime = max(movie_8.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_8.seek(ntime)
                            movie_8.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey14.setAutoDraw(True) 
                                blenderquickkey14.setAutoDraw(False)
                                movie_8.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey14.setAutoDraw(True) 
                                quickkey14.setAutoDraw(False)
                                movie_8.pause()
                            else:
                                blenderquickkey14.setAutoDraw(False)
                                quickkey14.setAutoDraw(False)
                                movie_8.play()
                                
                    elif movie_8.status == PAUSED:
                        if key=='period':
                            movie_8.pause()
                            ntime = min(movie_8.getCurrentFrameTime( ) + 5.0, movie_8.duration)
                            movie_8.seek(ntime)
                            movie_8.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_8.pause()
                            ntime = max(movie_8.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_8.seek(ntime)
                            movie_8.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_8.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey14.setAutoDraw(True) 
                                blenderquickkey14.setAutoDraw(False)
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey14.setAutoDraw(True) 
                                quickkey14.setAutoDraw(False)
                            else:
                                blenderquickkey14.setAutoDraw(False)
                                quickkey14.setAutoDraw(False)
                           
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey14.setAutoDraw(True) 
                            blenderquickkey14.setAutoDraw(False)
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey14.setAutoDraw(True) 
                            quickkey14.setAutoDraw(False)
                        else:
                            blenderquickkey14.setAutoDraw(False)
                            quickkey14.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video1-4 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender14.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video1-4 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender14.setAutoDraw(False)
                # *mouse_8* updates
                if mouse_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_8.frameNStart = frameN  # exact frame index
                    mouse_8.tStart = t  # local t and not account for scr refresh
                    mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_8, 'tStartRefresh')  # time at next scr refresh
                    mouse_8.status = STARTED
                    prevButtonState = mouse_8.getPressed()  # if button is down already this ISN'T a new click
                if mouse_8.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_8.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_8,]:
                                if obj.contains(mouse_8):
                                    gotValidClick = True
                                    mouse_8.clicked_name.append(obj.name)
                            x, y = mouse_8.getPos()
                            mouse_8.x.append(x)
                            mouse_8.y.append(y)
                            buttons = mouse_8.getPressed()
                            mouse_8.leftButton.append(buttons[0])
                            mouse_8.midButton.append(buttons[1])
                            mouse_8.rightButton.append(buttons[2])
                            mouse_8.time.append(mouse_8.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo14* updates
                if backvideo14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo14.frameNStart = frameN  # exact frame index
                    backvideo14.tStart = t  # local t and not account for scr refresh
                    backvideo14.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo14, 'tStartRefresh')  # time at next scr refresh
                    backvideo14.setAutoDraw(True)
                
                # *movie_8* updates
                if movie_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_8.frameNStart = frameN  # exact frame index
                    movie_8.tStart = t  # local t and not account for scr refresh
                    movie_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_8, 'tStartRefresh')  # time at next scr refresh
                    movie_8.setAutoDraw(True)
                
                # *closevideo_8* updates
                if closevideo_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_8.frameNStart = frameN  # exact frame index
                    closevideo_8.tStart = t  # local t and not account for scr refresh
                    closevideo_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_8, 'tStartRefresh')  # time at next scr refresh
                    closevideo_8.setAutoDraw(True)
                
                # *blender14* updates
                if blender14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender14.frameNStart = frameN  # exact frame index
                    blender14.tStart = t  # local t and not account for scr refresh
                    blender14.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender14, 'tStartRefresh')  # time at next scr refresh
                    blender14.setAutoDraw(True)
                
                # *quickkey14* updates
                if quickkey14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey14.frameNStart = frameN  # exact frame index
                    quickkey14.tStart = t  # local t and not account for scr refresh
                    quickkey14.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey14, 'tStartRefresh')  # time at next scr refresh
                    quickkey14.setAutoDraw(True)
                
                # *blenderquickkey14* updates
                if blenderquickkey14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey14.frameNStart = frameN  # exact frame index
                    blenderquickkey14.tStart = t  # local t and not account for scr refresh
                    blenderquickkey14.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey14, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey14.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video1_4Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video1_4"-------
            for thisComponent in video1_4Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_8.keys in ['', [], None]:  # No response was made
                key_resp_8.keys = None
            trials_6.addData('key_resp_8.keys',key_resp_8.keys)
            if key_resp_8.keys != None:  # we had a response
                trials_6.addData('key_resp_8.rt', key_resp_8.rt)
            trials_6.addData('key_resp_8.started', key_resp_8.tStartRefresh)
            trials_6.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime())
                    allsteptime.append('video1-4 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video1-4 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_8.getCurrentFrameTime( )
                remembertimestamp14.append(nowtime) 
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime4.append(sum(Watchtime1))
            #    allsteptime.append('video1-4 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime4.append(sum(Watchtime1))
            #    allsteptime.append('video1-4 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
                
            totalpath1=1
            # store data for trials_6 (TrialHandler)
            if len(mouse_8.x): trials_6.addData('mouse_8.x', mouse_8.x[0])
            if len(mouse_8.y): trials_6.addData('mouse_8.y', mouse_8.y[0])
            if len(mouse_8.leftButton): trials_6.addData('mouse_8.leftButton', mouse_8.leftButton[0])
            if len(mouse_8.midButton): trials_6.addData('mouse_8.midButton', mouse_8.midButton[0])
            if len(mouse_8.rightButton): trials_6.addData('mouse_8.rightButton', mouse_8.rightButton[0])
            if len(mouse_8.time): trials_6.addData('mouse_8.time', mouse_8.time[0])
            if len(mouse_8.clicked_name): trials_6.addData('mouse_8.clicked_name', mouse_8.clicked_name[0])
            trials_6.addData('mouse_8.started', mouse_8.tStart)
            trials_6.addData('mouse_8.stopped', mouse_8.tStop)
            trials_6.addData('backvideo14.started', backvideo14.tStartRefresh)
            trials_6.addData('backvideo14.stopped', backvideo14.tStopRefresh)
            movie_8.stop()
            trials_6.addData('closevideo_8.started', closevideo_8.tStartRefresh)
            trials_6.addData('closevideo_8.stopped', closevideo_8.tStopRefresh)
            trials_6.addData('blender14.started', blender14.tStartRefresh)
            trials_6.addData('blender14.stopped', blender14.tStopRefresh)
            trials_6.addData('quickkey14.started', quickkey14.tStartRefresh)
            trials_6.addData('quickkey14.stopped', quickkey14.tStopRefresh)
            trials_6.addData('blenderquickkey14.started', blenderquickkey14.tStartRefresh)
            trials_6.addData('blenderquickkey14.stopped', blenderquickkey14.tStopRefresh)
            # the Routine "video1_4" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed path15 repeats of 'trials_6'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_7 = data.TrialHandler(nReps=path16, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_7')
        thisExp.addLoop(trials_7)  # add the loop to the experiment
        thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
        if thisTrial_7 != None:
            for paramName in thisTrial_7:
                exec('{} = thisTrial_7[paramName]'.format(paramName))
        
        for thisTrial_7 in trials_7:
            currentLoop = trials_7
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
            if thisTrial_7 != None:
                for paramName in thisTrial_7:
                    exec('{} = thisTrial_7[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video1_5"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_9.keys = []
            key_resp_9.rt = []
            _key_resp_9_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp15)!=0:
                movie_9.pause()
                movie_9.seek(int(remembertimestamp15[-1]))
                movie_9.play()
                Time1 = 0
            showf=0
            enter1=0    
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_9
            mouse_9.x = []
            mouse_9.y = []
            mouse_9.leftButton = []
            mouse_9.midButton = []
            mouse_9.rightButton = []
            mouse_9.time = []
            mouse_9.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_9.mouseClock.reset()
            # keep track of which components have finished
            video1_5Components = [key_resp_9, mouse_9, backvideo15, movie_9, closevideo_9, blender15, quickkey15, blenderquickkey15]
            for thisComponent in video1_5Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video1_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video1_5"-------
            while continueRoutine:
                # get current time
                t = video1_5Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video1_5Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_9* updates
                waitOnFlip = False
                if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_9.frameNStart = frameN  # exact frame index
                    key_resp_9.tStart = t  # local t and not account for scr refresh
                    key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
                    key_resp_9.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_9.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_9.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_9_allKeys.extend(theseKeys)
                    if len(_key_resp_9_allKeys):
                        key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                        key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey15.setAutoDraw(False)
                    blenderquickkey15.setAutoDraw(False)
                if (blender%2)!=1:
                    blender15.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_9.status == PLAYING:
                            movie_9.pause()
                            Time1 = 1
                        elif movie_9.status == PAUSED:
                            movie_9.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_9.pause()
                        ntime = max(0.0,movie_9.duration)
                        movie_9.seek(ntime)
                        movie_9.play()
                        Time1 = 0
                            
                    if movie_9.status == PLAYING:
                        if key=='period':
                            movie_9.pause()
                            ntime = min(movie_9.getCurrentFrameTime( ) + 5.0, movie_9.duration)
                            movie_9.seek(ntime)
                            movie_9.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_9.pause()
                            ntime = max(movie_9.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_9.seek(ntime)
                            movie_9.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey15.setAutoDraw(True)   
                                blenderquickkey15.setAutoDraw(False) 
                                movie_9.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey15.setAutoDraw(True) 
                                quickkey15.setAutoDraw(False)
                                movie_9.pause()
                            else:
                                blenderquickkey15.setAutoDraw(False) 
                                quickkey15.setAutoDraw(False)
                                movie_9.play()
                
                    elif movie_9.status == PAUSED:
                        if key=='period':
                            movie_9.pause()
                            ntime = min(movie_9.getCurrentFrameTime( ) + 5.0, movie_9.duration)
                            movie_9.seek(ntime)
                            movie_9.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_9.pause()
                            ntime = max(movie_9.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_9.seek(ntime)
                            movie_9.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_9.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey15.setAutoDraw(True)   
                                blenderquickkey15.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey15.setAutoDraw(True) 
                                quickkey15.setAutoDraw(False)
                            else:
                                blenderquickkey15.setAutoDraw(False) 
                                quickkey15.setAutoDraw(False)
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey15.setAutoDraw(True)   
                            blenderquickkey15.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey15.setAutoDraw(True) 
                            quickkey15.setAutoDraw(False)
                        else:
                            blenderquickkey15.setAutoDraw(False) 
                            quickkey15.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video1-5 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender15.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video1-5 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender15.setAutoDraw(False)
                # *mouse_9* updates
                if mouse_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_9.frameNStart = frameN  # exact frame index
                    mouse_9.tStart = t  # local t and not account for scr refresh
                    mouse_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_9, 'tStartRefresh')  # time at next scr refresh
                    mouse_9.status = STARTED
                    prevButtonState = mouse_9.getPressed()  # if button is down already this ISN'T a new click
                if mouse_9.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_9.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_9,]:
                                if obj.contains(mouse_9):
                                    gotValidClick = True
                                    mouse_9.clicked_name.append(obj.name)
                            x, y = mouse_9.getPos()
                            mouse_9.x.append(x)
                            mouse_9.y.append(y)
                            buttons = mouse_9.getPressed()
                            mouse_9.leftButton.append(buttons[0])
                            mouse_9.midButton.append(buttons[1])
                            mouse_9.rightButton.append(buttons[2])
                            mouse_9.time.append(mouse_9.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo15* updates
                if backvideo15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo15.frameNStart = frameN  # exact frame index
                    backvideo15.tStart = t  # local t and not account for scr refresh
                    backvideo15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo15, 'tStartRefresh')  # time at next scr refresh
                    backvideo15.setAutoDraw(True)
                
                # *movie_9* updates
                if movie_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_9.frameNStart = frameN  # exact frame index
                    movie_9.tStart = t  # local t and not account for scr refresh
                    movie_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_9, 'tStartRefresh')  # time at next scr refresh
                    movie_9.setAutoDraw(True)
                
                # *closevideo_9* updates
                if closevideo_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_9.frameNStart = frameN  # exact frame index
                    closevideo_9.tStart = t  # local t and not account for scr refresh
                    closevideo_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_9, 'tStartRefresh')  # time at next scr refresh
                    closevideo_9.setAutoDraw(True)
                
                # *blender15* updates
                if blender15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender15.frameNStart = frameN  # exact frame index
                    blender15.tStart = t  # local t and not account for scr refresh
                    blender15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender15, 'tStartRefresh')  # time at next scr refresh
                    blender15.setAutoDraw(True)
                
                # *quickkey15* updates
                if quickkey15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey15.frameNStart = frameN  # exact frame index
                    quickkey15.tStart = t  # local t and not account for scr refresh
                    quickkey15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey15, 'tStartRefresh')  # time at next scr refresh
                    quickkey15.setAutoDraw(True)
                
                # *blenderquickkey15* updates
                if blenderquickkey15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey15.frameNStart = frameN  # exact frame index
                    blenderquickkey15.tStart = t  # local t and not account for scr refresh
                    blenderquickkey15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey15, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey15.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video1_5Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video1_5"-------
            for thisComponent in video1_5Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_9.keys in ['', [], None]:  # No response was made
                key_resp_9.keys = None
            trials_7.addData('key_resp_9.keys',key_resp_9.keys)
            if key_resp_9.keys != None:  # we had a response
                trials_7.addData('key_resp_9.rt', key_resp_9.rt)
            trials_7.addData('key_resp_9.started', key_resp_9.tStartRefresh)
            trials_7.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime()) 
                    allsteptime.append('video1-5 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video1-5 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_9.getCurrentFrameTime( )
                remembertimestamp15.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime5.append(sum(Watchtime1))
            #    allsteptime.append('video1-5 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime5.append(sum(Watchtime1))
            #    allsteptime.append('video1-5 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
                
            totalpath1=1
            # store data for trials_7 (TrialHandler)
            if len(mouse_9.x): trials_7.addData('mouse_9.x', mouse_9.x[0])
            if len(mouse_9.y): trials_7.addData('mouse_9.y', mouse_9.y[0])
            if len(mouse_9.leftButton): trials_7.addData('mouse_9.leftButton', mouse_9.leftButton[0])
            if len(mouse_9.midButton): trials_7.addData('mouse_9.midButton', mouse_9.midButton[0])
            if len(mouse_9.rightButton): trials_7.addData('mouse_9.rightButton', mouse_9.rightButton[0])
            if len(mouse_9.time): trials_7.addData('mouse_9.time', mouse_9.time[0])
            if len(mouse_9.clicked_name): trials_7.addData('mouse_9.clicked_name', mouse_9.clicked_name[0])
            trials_7.addData('mouse_9.started', mouse_9.tStart)
            trials_7.addData('mouse_9.stopped', mouse_9.tStop)
            trials_7.addData('backvideo15.started', backvideo15.tStartRefresh)
            trials_7.addData('backvideo15.stopped', backvideo15.tStopRefresh)
            movie_9.stop()
            trials_7.addData('closevideo_9.started', closevideo_9.tStartRefresh)
            trials_7.addData('closevideo_9.stopped', closevideo_9.tStopRefresh)
            trials_7.addData('blender15.started', blender15.tStartRefresh)
            trials_7.addData('blender15.stopped', blender15.tStopRefresh)
            trials_7.addData('quickkey15.started', quickkey15.tStartRefresh)
            trials_7.addData('quickkey15.stopped', quickkey15.tStopRefresh)
            trials_7.addData('blenderquickkey15.started', blenderquickkey15.tStartRefresh)
            trials_7.addData('blenderquickkey15.stopped', blenderquickkey15.tStopRefresh)
            # the Routine "video1_5" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed path16 repeats of 'trials_7'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_8 = data.TrialHandler(nReps=path17, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_8')
        thisExp.addLoop(trials_8)  # add the loop to the experiment
        thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
        if thisTrial_8 != None:
            for paramName in thisTrial_8:
                exec('{} = thisTrial_8[paramName]'.format(paramName))
        
        for thisTrial_8 in trials_8:
            currentLoop = trials_8
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
            if thisTrial_8 != None:
                for paramName in thisTrial_8:
                    exec('{} = thisTrial_8[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video1_6"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_10.keys = []
            key_resp_10.rt = []
            _key_resp_10_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp16)!=0:
                movie_10.pause()
                movie_10.seek(int(remembertimestamp16[-1]))
                movie_10.play()
                Time1 = 0
            showf=0
            enter1=0   
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_10
            mouse_10.x = []
            mouse_10.y = []
            mouse_10.leftButton = []
            mouse_10.midButton = []
            mouse_10.rightButton = []
            mouse_10.time = []
            mouse_10.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_10.mouseClock.reset()
            # keep track of which components have finished
            video1_6Components = [key_resp_10, mouse_10, backvideo16, movie_10, closevideo_10, blender16, quickkey16, blenderquickkey16]
            for thisComponent in video1_6Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video1_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video1_6"-------
            while continueRoutine:
                # get current time
                t = video1_6Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video1_6Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_10* updates
                waitOnFlip = False
                if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_10.frameNStart = frameN  # exact frame index
                    key_resp_10.tStart = t  # local t and not account for scr refresh
                    key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
                    key_resp_10.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_10.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_10.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_10_allKeys.extend(theseKeys)
                    if len(_key_resp_10_allKeys):
                        key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                        key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey16.setAutoDraw(False)
                    blenderquickkey16.setAutoDraw(False)
                if (blender%2)!=1:
                    blender16.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_10.status == PLAYING:
                            movie_10.pause()
                            Time1 = 1
                        elif movie_10.status == PAUSED:
                            movie_10.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_10.pause()
                        ntime = max(0.0,movie_10.duration)
                        movie_10.seek(ntime)
                        movie_10.play()
                        Time1 = 0
                
                    if movie_10.status == PLAYING:
                        if key=='period':
                            movie_10.pause()
                            ntime = min(movie_10.getCurrentFrameTime( ) + 5.0, movie_10.duration)
                            movie_10.seek(ntime)
                            movie_10.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_10.pause()
                            ntime = max(movie_10.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_10.seek(ntime)
                            movie_10.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey16.setAutoDraw(True)    
                                blenderquickkey16.setAutoDraw(False) 
                                movie_10.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey16.setAutoDraw(True) 
                                quickkey16.setAutoDraw(False)
                                movie_10.pause()
                            else:
                                blenderquickkey16.setAutoDraw(False) 
                                quickkey16.setAutoDraw(False)
                                movie_10.play()
                                
                    elif movie_10.status == PAUSED:
                        if key=='period':
                            movie_10.pause()
                            ntime = min(movie_10.getCurrentFrameTime( ) + 5.0, movie_10.duration)
                            movie_10.seek(ntime)
                            movie_10.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_10.pause()
                            ntime = max(movie_10.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_10.seek(ntime)
                            movie_10.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_10.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey16.setAutoDraw(True)    
                                blenderquickkey16.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey16.setAutoDraw(True) 
                                quickkey16.setAutoDraw(False)
                            else:
                                blenderquickkey16.setAutoDraw(False) 
                                quickkey16.setAutoDraw(False)
                          
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey16.setAutoDraw(True)    
                            blenderquickkey16.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey16.setAutoDraw(True) 
                            quickkey16.setAutoDraw(False)
                        else:
                            blenderquickkey16.setAutoDraw(False) 
                            quickkey16.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video1-6 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender16.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video1-6 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender16.setAutoDraw(False)
                # *mouse_10* updates
                if mouse_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_10.frameNStart = frameN  # exact frame index
                    mouse_10.tStart = t  # local t and not account for scr refresh
                    mouse_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_10, 'tStartRefresh')  # time at next scr refresh
                    mouse_10.status = STARTED
                    prevButtonState = mouse_10.getPressed()  # if button is down already this ISN'T a new click
                if mouse_10.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_10.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_10,]:
                                if obj.contains(mouse_10):
                                    gotValidClick = True
                                    mouse_10.clicked_name.append(obj.name)
                            x, y = mouse_10.getPos()
                            mouse_10.x.append(x)
                            mouse_10.y.append(y)
                            buttons = mouse_10.getPressed()
                            mouse_10.leftButton.append(buttons[0])
                            mouse_10.midButton.append(buttons[1])
                            mouse_10.rightButton.append(buttons[2])
                            mouse_10.time.append(mouse_10.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo16* updates
                if backvideo16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo16.frameNStart = frameN  # exact frame index
                    backvideo16.tStart = t  # local t and not account for scr refresh
                    backvideo16.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo16, 'tStartRefresh')  # time at next scr refresh
                    backvideo16.setAutoDraw(True)
                
                # *movie_10* updates
                if movie_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_10.frameNStart = frameN  # exact frame index
                    movie_10.tStart = t  # local t and not account for scr refresh
                    movie_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_10, 'tStartRefresh')  # time at next scr refresh
                    movie_10.setAutoDraw(True)
                
                # *closevideo_10* updates
                if closevideo_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_10.frameNStart = frameN  # exact frame index
                    closevideo_10.tStart = t  # local t and not account for scr refresh
                    closevideo_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_10, 'tStartRefresh')  # time at next scr refresh
                    closevideo_10.setAutoDraw(True)
                
                # *blender16* updates
                if blender16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender16.frameNStart = frameN  # exact frame index
                    blender16.tStart = t  # local t and not account for scr refresh
                    blender16.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender16, 'tStartRefresh')  # time at next scr refresh
                    blender16.setAutoDraw(True)
                
                # *quickkey16* updates
                if quickkey16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey16.frameNStart = frameN  # exact frame index
                    quickkey16.tStart = t  # local t and not account for scr refresh
                    quickkey16.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey16, 'tStartRefresh')  # time at next scr refresh
                    quickkey16.setAutoDraw(True)
                
                # *blenderquickkey16* updates
                if blenderquickkey16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey16.frameNStart = frameN  # exact frame index
                    blenderquickkey16.tStart = t  # local t and not account for scr refresh
                    blenderquickkey16.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey16, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey16.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video1_6Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video1_6"-------
            for thisComponent in video1_6Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_10.keys in ['', [], None]:  # No response was made
                key_resp_10.keys = None
            trials_8.addData('key_resp_10.keys',key_resp_10.keys)
            if key_resp_10.keys != None:  # we had a response
                trials_8.addData('key_resp_10.rt', key_resp_10.rt)
            trials_8.addData('key_resp_10.started', key_resp_10.tStartRefresh)
            trials_8.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime())
                    allsteptime.append('video1-6 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video1-6 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_10.getCurrentFrameTime( )
                remembertimestamp16.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime6.append(sum(Watchtime1))
            #    allsteptime.append('video1-6 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime6.append(sum(Watchtime1))
            #    allsteptime.append('video1-6 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            totalpath1=1
            # store data for trials_8 (TrialHandler)
            if len(mouse_10.x): trials_8.addData('mouse_10.x', mouse_10.x[0])
            if len(mouse_10.y): trials_8.addData('mouse_10.y', mouse_10.y[0])
            if len(mouse_10.leftButton): trials_8.addData('mouse_10.leftButton', mouse_10.leftButton[0])
            if len(mouse_10.midButton): trials_8.addData('mouse_10.midButton', mouse_10.midButton[0])
            if len(mouse_10.rightButton): trials_8.addData('mouse_10.rightButton', mouse_10.rightButton[0])
            if len(mouse_10.time): trials_8.addData('mouse_10.time', mouse_10.time[0])
            if len(mouse_10.clicked_name): trials_8.addData('mouse_10.clicked_name', mouse_10.clicked_name[0])
            trials_8.addData('mouse_10.started', mouse_10.tStart)
            trials_8.addData('mouse_10.stopped', mouse_10.tStop)
            trials_8.addData('backvideo16.started', backvideo16.tStartRefresh)
            trials_8.addData('backvideo16.stopped', backvideo16.tStopRefresh)
            movie_10.stop()
            trials_8.addData('closevideo_10.started', closevideo_10.tStartRefresh)
            trials_8.addData('closevideo_10.stopped', closevideo_10.tStopRefresh)
            trials_8.addData('blender16.started', blender16.tStartRefresh)
            trials_8.addData('blender16.stopped', blender16.tStopRefresh)
            trials_8.addData('quickkey16.started', quickkey16.tStartRefresh)
            trials_8.addData('quickkey16.stopped', quickkey16.tStopRefresh)
            trials_8.addData('blenderquickkey16.started', blenderquickkey16.tStartRefresh)
            trials_8.addData('blenderquickkey16.stopped', blenderquickkey16.tStopRefresh)
            # the Routine "video1_6" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed path17 repeats of 'trials_8'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_25 = data.TrialHandler(nReps=path11, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_25')
        thisExp.addLoop(trials_25)  # add the loop to the experiment
        thisTrial_25 = trials_25.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_25.rgb)
        if thisTrial_25 != None:
            for paramName in thisTrial_25:
                exec('{} = thisTrial_25[paramName]'.format(paramName))
        
        for thisTrial_25 in trials_25:
            currentLoop = trials_25
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_25.rgb)
            if thisTrial_25 != None:
                for paramName in thisTrial_25:
                    exec('{} = thisTrial_25[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "cookbook1"-------
            continueRoutine = True
            # update component parameters for each repeat
            # setup some python lists for storing info about the mouse_26
            mouse_26.clicked_name = []
            gotValidClick = False  # until a click is received
            key_resp_26.keys = []
            key_resp_26.rt = []
            _key_resp_26_allKeys = []
            count=1
            respClock.reset(0)
            Time1=0
            ExperienceClock.reset(0)
            showf=0
            blender=0
            enter1=0 
            newchange=0
            # keep track of which components have finished
            cookbook1Components = [background, close, mouse_26, key_resp_26, BOOK2, BOOK3, BOOK4, BOOK5, BOOK6, BOOK7, BOOK1, blender18, quickkey18, blenderquickkey18]
            for thisComponent in cookbook1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            cookbook1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "cookbook1"-------
            while continueRoutine:
                # get current time
                t = cookbook1Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=cookbook1Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *background* updates
                if background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    background.frameNStart = frameN  # exact frame index
                    background.tStart = t  # local t and not account for scr refresh
                    background.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(background, 'tStartRefresh')  # time at next scr refresh
                    background.setAutoDraw(True)
                
                # *close* updates
                if close.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    close.frameNStart = frameN  # exact frame index
                    close.tStart = t  # local t and not account for scr refresh
                    close.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(close, 'tStartRefresh')  # time at next scr refresh
                    close.setAutoDraw(True)
                # *mouse_26* updates
                if mouse_26.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_26.frameNStart = frameN  # exact frame index
                    mouse_26.tStart = t  # local t and not account for scr refresh
                    mouse_26.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_26, 'tStartRefresh')  # time at next scr refresh
                    mouse_26.status = STARTED
                    mouse_26.mouseClock.reset()
                    prevButtonState = mouse_26.getPressed()  # if button is down already this ISN'T a new click
                if mouse_26.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_26.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [close,]:
                                if obj.contains(mouse_26):
                                    gotValidClick = True
                                    mouse_26.clicked_name.append(obj.name)
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *key_resp_26* updates
                waitOnFlip = False
                if key_resp_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_26.frameNStart = frameN  # exact frame index
                    key_resp_26.tStart = t  # local t and not account for scr refresh
                    key_resp_26.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_26, 'tStartRefresh')  # time at next scr refresh
                    key_resp_26.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_26.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_26.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_26.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_26.getKeys(keyList=['left', 'right', '1', '2', '3', '4', '5', '6', '7', 'f', 'return'], waitRelease=False)
                    _key_resp_26_allKeys.extend(theseKeys)
                    if len(_key_resp_26_allKeys):
                        key_resp_26.keys = _key_resp_26_allKeys[-1].name  # just the last key pressed
                        key_resp_26.rt = _key_resp_26_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey18.setAutoDraw(False)
                    blenderquickkey18.setAutoDraw(False)
                if (blender%2)!=1:
                    blender18.setAutoDraw(False)
                for key in event.getKeys():
                    if key=='right':
                        countcontinue=countcontinue+1
                        count=count+1
                        if count>=7:
                            count=7
                            BOOK1.setAutoDraw(False)
                            BOOK2.setAutoDraw(False)
                            BOOK3.setAutoDraw(False)
                            BOOK4.setAutoDraw(False)
                            BOOK5.setAutoDraw(False)
                            BOOK6.setAutoDraw(False)
                            BOOK7.setAutoDraw(True)
                        elif count==2:
                            BOOK1.setAutoDraw(False)
                            BOOK2.setAutoDraw(True)
                            BOOK3.setAutoDraw(False)
                            BOOK4.setAutoDraw(False)
                            BOOK5.setAutoDraw(False)
                            BOOK6.setAutoDraw(False)
                            BOOK7.setAutoDraw(False)
                        elif count==3:
                            BOOK1.setAutoDraw(False)
                            BOOK2.setAutoDraw(False)
                            BOOK3.setAutoDraw(True)
                            BOOK4.setAutoDraw(False)
                            BOOK5.setAutoDraw(False)
                            BOOK6.setAutoDraw(False)
                            BOOK7.setAutoDraw(False)
                        elif count==4:
                            BOOK1.setAutoDraw(False)
                            BOOK2.setAutoDraw(False)
                            BOOK3.setAutoDraw(False)
                            BOOK4.setAutoDraw(True)
                            BOOK5.setAutoDraw(False)
                            BOOK6.setAutoDraw(False)
                            BOOK7.setAutoDraw(False)
                        elif count==5:
                            BOOK1.setAutoDraw(False)
                            BOOK2.setAutoDraw(False)
                            BOOK3.setAutoDraw(False)
                            BOOK4.setAutoDraw(False)
                            BOOK5.setAutoDraw(True)
                            BOOK6.setAutoDraw(False)
                            BOOK7.setAutoDraw(False)
                        elif count==6:
                            BOOK1.setAutoDraw(False)
                            BOOK2.setAutoDraw(False)
                            BOOK3.setAutoDraw(False)
                            BOOK4.setAutoDraw(False)
                            BOOK5.setAutoDraw(False)
                            BOOK6.setAutoDraw(True)
                            BOOK7.setAutoDraw(False)
                            
                    elif key=='left':
                        countcontinue=countcontinue+1
                        count=count-1
                        if count<=1:
                            count=1
                            BOOK1.setAutoDraw(True)
                            BOOK2.setAutoDraw(False)
                            BOOK3.setAutoDraw(False)
                            BOOK4.setAutoDraw(False)
                            BOOK5.setAutoDraw(False)
                            BOOK6.setAutoDraw(False)
                            BOOK7.setAutoDraw(False)
                        elif count==2:
                            BOOK1.setAutoDraw(False)
                            BOOK2.setAutoDraw(True)
                            BOOK3.setAutoDraw(False)
                            BOOK4.setAutoDraw(False)
                            BOOK5.setAutoDraw(False)
                            BOOK6.setAutoDraw(False)
                            BOOK7.setAutoDraw(False)
                        elif count==3:
                            BOOK1.setAutoDraw(False)
                            BOOK2.setAutoDraw(False)
                            BOOK3.setAutoDraw(True)
                            BOOK4.setAutoDraw(False)
                            BOOK5.setAutoDraw(False)
                            BOOK6.setAutoDraw(False)
                            BOOK7.setAutoDraw(False)
                            
                        elif count==4:
                            BOOK1.setAutoDraw(False)
                            BOOK2.setAutoDraw(False)
                            BOOK3.setAutoDraw(False)
                            BOOK4.setAutoDraw(True)
                            BOOK5.setAutoDraw(False)
                            BOOK6.setAutoDraw(False)
                            BOOK7.setAutoDraw(False)
                
                        elif count==5:
                            BOOK1.setAutoDraw(False)
                            BOOK2.setAutoDraw(False)
                            BOOK3.setAutoDraw(False)
                            BOOK4.setAutoDraw(False)
                            BOOK5.setAutoDraw(True)
                            BOOK6.setAutoDraw(False)
                            BOOK7.setAutoDraw(False)
                
                        elif count==6:
                            BOOK1.setAutoDraw(False)
                            BOOK2.setAutoDraw(False)
                            BOOK3.setAutoDraw(False)
                            BOOK4.setAutoDraw(False)
                            BOOK5.setAutoDraw(False)
                            BOOK6.setAutoDraw(True)
                            BOOK7.setAutoDraw(False)
                            
                    elif key=='1':
                        count=1
                        change=change+1
                        BOOK1.setAutoDraw(True)
                        BOOK2.setAutoDraw(False)
                        BOOK3.setAutoDraw(False)
                        BOOK4.setAutoDraw(False)
                        BOOK5.setAutoDraw(False)
                        BOOK6.setAutoDraw(False)
                        BOOK7.setAutoDraw(False)
                    elif key=='2':
                        count=2
                        change=change+1
                        BOOK1.setAutoDraw(False)
                        BOOK2.setAutoDraw(True)
                        BOOK3.setAutoDraw(False)
                        BOOK4.setAutoDraw(False)
                        BOOK5.setAutoDraw(False)
                        BOOK6.setAutoDraw(False)
                        BOOK7.setAutoDraw(False)
                    elif key=='3':
                        count=3
                        change=change+1
                        BOOK1.setAutoDraw(False)
                        BOOK2.setAutoDraw(False)
                        BOOK3.setAutoDraw(True)
                        BOOK4.setAutoDraw(False)
                        BOOK5.setAutoDraw(False)
                        BOOK6.setAutoDraw(False)
                        BOOK7.setAutoDraw(False)
                    elif key=='4':
                        count=4
                        change=change+1
                        BOOK1.setAutoDraw(False)
                        BOOK2.setAutoDraw(False)
                        BOOK3.setAutoDraw(False)
                        BOOK4.setAutoDraw(True)
                        BOOK5.setAutoDraw(False)
                        BOOK6.setAutoDraw(False)
                        BOOK7.setAutoDraw(False)
                    elif key=='5':
                        count=5
                        change=change+1
                        BOOK1.setAutoDraw(False)
                        BOOK2.setAutoDraw(False)
                        BOOK3.setAutoDraw(False)
                        BOOK4.setAutoDraw(False)
                        BOOK5.setAutoDraw(True)
                        BOOK6.setAutoDraw(False)
                        BOOK7.setAutoDraw(False)
                    elif key=='6':
                        count=6
                        change=change+1
                        BOOK1.setAutoDraw(False)
                        BOOK2.setAutoDraw(False)
                        BOOK3.setAutoDraw(False)
                        BOOK4.setAutoDraw(False)
                        BOOK5.setAutoDraw(False)
                        BOOK6.setAutoDraw(True)
                        BOOK7.setAutoDraw(False)
                    elif key=='7':
                        count=7
                        change=change+1
                        BOOK1.setAutoDraw(False)
                        BOOK2.setAutoDraw(False)
                        BOOK3.setAutoDraw(False)
                        BOOK4.setAutoDraw(False)
                        BOOK5.setAutoDraw(False)
                        BOOK6.setAutoDraw(False)
                        BOOK7.setAutoDraw(True)
                
                    elif key =='f':
                        countcontinue=countcontinue+1
                        showf=showf+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey18.setAutoDraw(True)  
                            blenderquickkey18.setAutoDraw(False)
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey18.setAutoDraw(True) 
                            quickkey18.setAutoDraw(False)  
                        else:
                            blenderquickkey18.setAutoDraw(False)
                            quickkey18.setAutoDraw(False)
                # f/enter blender&learn time  
                    if key =='return':  
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey18.setAutoDraw(True)  
                            blenderquickkey18.setAutoDraw(False)
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey18.setAutoDraw(True) 
                            quickkey18.setAutoDraw(False)  
                        else:
                            blenderquickkey18.setAutoDraw(False)
                            quickkey18.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('cookbook1 learn')
                            allsteptime.append(MenuClock.getTime())
                            BlenderClock.reset(0)
                            blender18.setAutoDraw(True)
                        else: 
                            BlenderTime.append(BlenderClock.getTime())  
                            allsteptime.append('cookbook1 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            blender18.setAutoDraw(False)
                
                # *BOOK2* updates
                if BOOK2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK2.frameNStart = frameN  # exact frame index
                    BOOK2.tStart = t  # local t and not account for scr refresh
                    BOOK2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK2, 'tStartRefresh')  # time at next scr refresh
                    BOOK2.setAutoDraw(True)
                
                # *BOOK3* updates
                if BOOK3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK3.frameNStart = frameN  # exact frame index
                    BOOK3.tStart = t  # local t and not account for scr refresh
                    BOOK3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK3, 'tStartRefresh')  # time at next scr refresh
                    BOOK3.setAutoDraw(True)
                
                # *BOOK4* updates
                if BOOK4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK4.frameNStart = frameN  # exact frame index
                    BOOK4.tStart = t  # local t and not account for scr refresh
                    BOOK4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK4, 'tStartRefresh')  # time at next scr refresh
                    BOOK4.setAutoDraw(True)
                
                # *BOOK5* updates
                if BOOK5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK5.frameNStart = frameN  # exact frame index
                    BOOK5.tStart = t  # local t and not account for scr refresh
                    BOOK5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK5, 'tStartRefresh')  # time at next scr refresh
                    BOOK5.setAutoDraw(True)
                
                # *BOOK6* updates
                if BOOK6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK6.frameNStart = frameN  # exact frame index
                    BOOK6.tStart = t  # local t and not account for scr refresh
                    BOOK6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK6, 'tStartRefresh')  # time at next scr refresh
                    BOOK6.setAutoDraw(True)
                
                # *BOOK7* updates
                if BOOK7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK7.frameNStart = frameN  # exact frame index
                    BOOK7.tStart = t  # local t and not account for scr refresh
                    BOOK7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK7, 'tStartRefresh')  # time at next scr refresh
                    BOOK7.setAutoDraw(True)
                
                # *BOOK1* updates
                if BOOK1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BOOK1.frameNStart = frameN  # exact frame index
                    BOOK1.tStart = t  # local t and not account for scr refresh
                    BOOK1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BOOK1, 'tStartRefresh')  # time at next scr refresh
                    BOOK1.setAutoDraw(True)
                
                # *blender18* updates
                if blender18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender18.frameNStart = frameN  # exact frame index
                    blender18.tStart = t  # local t and not account for scr refresh
                    blender18.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender18, 'tStartRefresh')  # time at next scr refresh
                    blender18.setAutoDraw(True)
                
                # *quickkey18* updates
                if quickkey18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey18.frameNStart = frameN  # exact frame index
                    quickkey18.tStart = t  # local t and not account for scr refresh
                    quickkey18.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey18, 'tStartRefresh')  # time at next scr refresh
                    quickkey18.setAutoDraw(True)
                
                # *blenderquickkey18* updates
                if blenderquickkey18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey18.frameNStart = frameN  # exact frame index
                    blenderquickkey18.tStart = t  # local t and not account for scr refresh
                    blenderquickkey18.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey18, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey18.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cookbook1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "cookbook1"-------
            for thisComponent in cookbook1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_25.addData('background.started', background.tStartRefresh)
            trials_25.addData('background.stopped', background.tStopRefresh)
            trials_25.addData('close.started', close.tStartRefresh)
            trials_25.addData('close.stopped', close.tStopRefresh)
            # store data for trials_25 (TrialHandler)
            x, y = mouse_26.getPos()
            buttons = mouse_26.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [close,]:
                    if obj.contains(mouse_26):
                        gotValidClick = True
                        mouse_26.clicked_name.append(obj.name)
            trials_25.addData('mouse_26.x', x)
            trials_25.addData('mouse_26.y', y)
            trials_25.addData('mouse_26.leftButton', buttons[0])
            trials_25.addData('mouse_26.midButton', buttons[1])
            trials_25.addData('mouse_26.rightButton', buttons[2])
            if len(mouse_26.clicked_name):
                trials_25.addData('mouse_26.clicked_name', mouse_26.clicked_name[0])
            trials_25.addData('mouse_26.started', mouse_26.tStart)
            trials_25.addData('mouse_26.stopped', mouse_26.tStop)
            # check responses
            if key_resp_26.keys in ['', [], None]:  # No response was made
                key_resp_26.keys = None
            trials_25.addData('key_resp_26.keys',key_resp_26.keys)
            if key_resp_26.keys != None:  # we had a response
                trials_25.addData('key_resp_26.rt', key_resp_26.rt)
            trials_25.addData('key_resp_26.started', key_resp_26.tStartRefresh)
            trials_25.addData('key_resp_26.stopped', key_resp_26.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==1 :
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('cookbook1 blender')
                    allsteptime.append(BlenderClock.getTime())
                else:
                    Watchtime1.append(respClock.getTime()) 
                    allsteptime.append('cookbook1 learn')
                    allsteptime.append(MenuClock.getTime())
                change=change+1
            
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Cookbook1.append(sum(Watchtime1))
                AllCookbook.append(sum(Watchtime1))
            #    allsteptime.append('cookbook1 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Cookbook1.append(sum(Watchtime1))
                AllCookbook.append(sum(Watchtime1))
            #    allsteptime.append('cookbook1 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
                
            totalpath1=1
            trials_25.addData('BOOK2.started', BOOK2.tStartRefresh)
            trials_25.addData('BOOK2.stopped', BOOK2.tStopRefresh)
            trials_25.addData('BOOK3.started', BOOK3.tStartRefresh)
            trials_25.addData('BOOK3.stopped', BOOK3.tStopRefresh)
            trials_25.addData('BOOK4.started', BOOK4.tStartRefresh)
            trials_25.addData('BOOK4.stopped', BOOK4.tStopRefresh)
            trials_25.addData('BOOK5.started', BOOK5.tStartRefresh)
            trials_25.addData('BOOK5.stopped', BOOK5.tStopRefresh)
            trials_25.addData('BOOK6.started', BOOK6.tStartRefresh)
            trials_25.addData('BOOK6.stopped', BOOK6.tStopRefresh)
            trials_25.addData('BOOK7.started', BOOK7.tStartRefresh)
            trials_25.addData('BOOK7.stopped', BOOK7.tStopRefresh)
            trials_25.addData('BOOK1.started', BOOK1.tStartRefresh)
            trials_25.addData('BOOK1.stopped', BOOK1.tStopRefresh)
            trials_25.addData('blender18.started', blender18.tStartRefresh)
            trials_25.addData('blender18.stopped', blender18.tStopRefresh)
            trials_25.addData('quickkey18.started', quickkey18.tStartRefresh)
            trials_25.addData('quickkey18.stopped', quickkey18.tStopRefresh)
            trials_25.addData('blenderquickkey18.started', blenderquickkey18.tStartRefresh)
            trials_25.addData('blenderquickkey18.stopped', blenderquickkey18.tStopRefresh)
            # the Routine "cookbook1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed path11 repeats of 'trials_25'
        
        thisExp.nextEntry()
        
    # completed totalpath1 repeats of 'trials_3'
    
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=totalpath4, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "menu5_1"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_menupath2.keys = []
        key_menupath2.rt = []
        _key_menupath2_allKeys = []
        MenuClock.reset(0)
        quickkeymenu4.setAutoDraw(False)
        ExperienceClock.reset(0)
        goto1=0
        goto2=0
        goto3=0
        goto4=0
        showf=0
        Time1 = 0
        enter1=0
        blender=0
        newchange=0
        # setup some python lists for storing info about the mouse_34
        mouse_34.clicked_name = []
        gotValidClick = False  # until a click is received
        key_resp_33.keys = []
        key_resp_33.rt = []
        _key_resp_33_allKeys = []
        # keep track of which components have finished
        menu5_1Components = [key_menupath2, mouse_34, backmenu5, close5, key_resp_33, blendermenu4, quickkeymenu4, blenderquickkey4]
        for thisComponent in menu5_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        menu5_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "menu5_1"-------
        while continueRoutine:
            # get current time
            t = menu5_1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=menu5_1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_menupath2* updates
            waitOnFlip = False
            if key_menupath2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_menupath2.frameNStart = frameN  # exact frame index
                key_menupath2.tStart = t  # local t and not account for scr refresh
                key_menupath2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_menupath2, 'tStartRefresh')  # time at next scr refresh
                key_menupath2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_menupath2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_menupath2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_menupath2.status == STARTED and not waitOnFlip:
                theseKeys = key_menupath2.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
                _key_menupath2_allKeys.extend(theseKeys)
                if len(_key_menupath2_allKeys):
                    key_menupath2.keys = _key_menupath2_allKeys[-1].name  # just the last key pressed
                    key_menupath2.rt = _key_menupath2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            if (showf%2)!=1:
                quickkeymenu4.setAutoDraw(False)
                blenderquickkey4.setAutoDraw(False)
            if (blender%2)!=1:
                blendermenu4.setAutoDraw(False)
            for key in event.getKeys():
                if key =='1':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    goto1=1
                elif key =='2':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    goto2=1
                elif key =='3':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    goto3=1
                elif key =='4':
                    countchange.append(newchange)
                    countcontinue=countcontinue+1
                    if (enter1%2)==1 :
                        BlenderTime.append(BlenderClock.getTime())
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                    else:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                    goto4=1
                    
                elif key =='f':
                    countcontinue=countcontinue+1
                    showf=showf+1
                    if(showf%2)==1 and (enter1%2)==0:
                        quickkeymenu4.setAutoDraw(True) 
                        blenderquickkey4.setAutoDraw(False)
                    elif (showf%2)==1 and (enter1%2)==1:
                        blenderquickkey4.setAutoDraw(True) 
                        quickkeymenu4.setAutoDraw(False)  
                    else:
                        quickkeymenu4.setAutoDraw(False)
                        blenderquickkey4.setAutoDraw(False)
            # f/enter blender&learn time  
            
                if key =='return':  
                    countcontinue=countcontinue+1
                    enter1=enter1+1
                    blender=blender+1
                    countenter=countenter+1
                    newchange=newchange+1
                    if(showf%2)==1 and (enter1%2)==0:
                        quickkeymenu4.setAutoDraw(True) 
                        blenderquickkey4.setAutoDraw(False)
                    elif (showf%2)==1 and (enter1%2)==1:
                        blenderquickkey4.setAutoDraw(True) 
                        quickkeymenu4.setAutoDraw(False)  
                    else:
                        quickkeymenu4.setAutoDraw(False)
                        blenderquickkey4.setAutoDraw(False)
                    if(enter1%2)==1:
                        Menutime.append(MenuClock.getTime())
                        AllWatchtime.append(MenuClock.getTime())
                        allsteptime.append('menu1 learn')
                        allsteptime.append(MenuClock.getTime())
                        BlenderClock.reset(0)
                        blendermenu4.setAutoDraw(True)  
                    else: 
                        BlenderTime.append(BlenderClock.getTime())  
                        allsteptime.append('menu1 blender')
                        allsteptime.append(BlenderClock.getTime())
                        MenuClock.reset(0)
                        blendermenu4.setAutoDraw(False)
            # *mouse_34* updates
            if mouse_34.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_34.frameNStart = frameN  # exact frame index
                mouse_34.tStart = t  # local t and not account for scr refresh
                mouse_34.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_34, 'tStartRefresh')  # time at next scr refresh
                mouse_34.status = STARTED
                mouse_34.mouseClock.reset()
                prevButtonState = mouse_34.getPressed()  # if button is down already this ISN'T a new click
            if mouse_34.status == STARTED:  # only update if started and not finished!
                buttons = mouse_34.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [close5,]:
                            if obj.contains(mouse_34):
                                gotValidClick = True
                                mouse_34.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *backmenu5* updates
            if backmenu5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                backmenu5.frameNStart = frameN  # exact frame index
                backmenu5.tStart = t  # local t and not account for scr refresh
                backmenu5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(backmenu5, 'tStartRefresh')  # time at next scr refresh
                backmenu5.setAutoDraw(True)
            
            # *close5* updates
            if close5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                close5.frameNStart = frameN  # exact frame index
                close5.tStart = t  # local t and not account for scr refresh
                close5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(close5, 'tStartRefresh')  # time at next scr refresh
                close5.setAutoDraw(True)
            
            # *key_resp_33* updates
            waitOnFlip = False
            if key_resp_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_33.frameNStart = frameN  # exact frame index
                key_resp_33.tStart = t  # local t and not account for scr refresh
                key_resp_33.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_33, 'tStartRefresh')  # time at next scr refresh
                key_resp_33.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_33.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_33.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_33.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_33.getKeys(keyList=['f', 'return'], waitRelease=False)
                _key_resp_33_allKeys.extend(theseKeys)
                if len(_key_resp_33_allKeys):
                    key_resp_33.keys = _key_resp_33_allKeys[-1].name  # just the last key pressed
                    key_resp_33.rt = _key_resp_33_allKeys[-1].rt
            
            # *blendermenu4* updates
            if blendermenu4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blendermenu4.frameNStart = frameN  # exact frame index
                blendermenu4.tStart = t  # local t and not account for scr refresh
                blendermenu4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blendermenu4, 'tStartRefresh')  # time at next scr refresh
                blendermenu4.setAutoDraw(True)
            
            # *quickkeymenu4* updates
            if quickkeymenu4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                quickkeymenu4.frameNStart = frameN  # exact frame index
                quickkeymenu4.tStart = t  # local t and not account for scr refresh
                quickkeymenu4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(quickkeymenu4, 'tStartRefresh')  # time at next scr refresh
                quickkeymenu4.setAutoDraw(True)
            
            # *blenderquickkey4* updates
            if blenderquickkey4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blenderquickkey4.frameNStart = frameN  # exact frame index
                blenderquickkey4.tStart = t  # local t and not account for scr refresh
                blenderquickkey4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blenderquickkey4, 'tStartRefresh')  # time at next scr refresh
                blenderquickkey4.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in menu5_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "menu5_1"-------
        for thisComponent in menu5_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_menupath2.keys in ['', [], None]:  # No response was made
            key_menupath2.keys = None
        trials.addData('key_menupath2.keys',key_menupath2.keys)
        if key_menupath2.keys != None:  # we had a response
            trials.addData('key_menupath2.rt', key_menupath2.rt)
        trials.addData('key_menupath2.started', key_menupath2.tStartRefresh)
        trials.addData('key_menupath2.stopped', key_menupath2.tStopRefresh)
        Experiencetime.append(ExperienceClock.getTime())
        
        if gotValidClick ==True:
            countchange.append(newchange)
            if (enter1%2)==1 :
                BlenderTime.append(BlenderClock.getTime())
                allsteptime.append('menu4 blender')
                allsteptime.append(BlenderClock.getTime())
            else:
                Menutime.append(MenuClock.getTime())
                AllWatchtime.append(MenuClock.getTime())
                allsteptime.append('menu4 learn')
                allsteptime.append(MenuClock.getTime())
            change=change+1
        # store data for trials (TrialHandler)
        x, y = mouse_34.getPos()
        buttons = mouse_34.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [close5,]:
                if obj.contains(mouse_34):
                    gotValidClick = True
                    mouse_34.clicked_name.append(obj.name)
        trials.addData('mouse_34.x', x)
        trials.addData('mouse_34.y', y)
        trials.addData('mouse_34.leftButton', buttons[0])
        trials.addData('mouse_34.midButton', buttons[1])
        trials.addData('mouse_34.rightButton', buttons[2])
        if len(mouse_34.clicked_name):
            trials.addData('mouse_34.clicked_name', mouse_34.clicked_name[0])
        trials.addData('mouse_34.started', mouse_34.tStart)
        trials.addData('mouse_34.stopped', mouse_34.tStop)
        trials.addData('backmenu5.started', backmenu5.tStartRefresh)
        trials.addData('backmenu5.stopped', backmenu5.tStopRefresh)
        trials.addData('close5.started', close5.tStartRefresh)
        trials.addData('close5.stopped', close5.tStopRefresh)
        # check responses
        if key_resp_33.keys in ['', [], None]:  # No response was made
            key_resp_33.keys = None
        trials.addData('key_resp_33.keys',key_resp_33.keys)
        if key_resp_33.keys != None:  # we had a response
            trials.addData('key_resp_33.rt', key_resp_33.rt)
        trials.addData('key_resp_33.started', key_resp_33.tStartRefresh)
        trials.addData('key_resp_33.stopped', key_resp_33.tStopRefresh)
        trials.addData('blendermenu4.started', blendermenu4.tStartRefresh)
        trials.addData('blendermenu4.stopped', blendermenu4.tStopRefresh)
        trials.addData('quickkeymenu4.started', quickkeymenu4.tStartRefresh)
        trials.addData('quickkeymenu4.stopped', quickkeymenu4.tStopRefresh)
        trials.addData('blenderquickkey4.started', blenderquickkey4.tStartRefresh)
        trials.addData('blenderquickkey4.stopped', blenderquickkey4.tStopRefresh)
        # the Routine "menu5_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        videopath5_1 = data.TrialHandler(nReps=goto1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='videopath5_1')
        thisExp.addLoop(videopath5_1)  # add the loop to the experiment
        thisVideopath5_1 = videopath5_1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisVideopath5_1.rgb)
        if thisVideopath5_1 != None:
            for paramName in thisVideopath5_1:
                exec('{} = thisVideopath5_1[paramName]'.format(paramName))
        
        for thisVideopath5_1 in videopath5_1:
            currentLoop = videopath5_1
            # abbreviate parameter names if possible (e.g. rgb = thisVideopath5_1.rgb)
            if thisVideopath5_1 != None:
                for paramName in thisVideopath5_1:
                    exec('{} = thisVideopath5_1[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "VIDEO"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp)!=0:
                movie.pause()
                movie.seek(int(remembertimestamp[-1]))
                movie.play()
                Time1 = 0
            newchange=0
            #出現快捷鍵圖
            showf=0
            #判斷enter是否被按下
            enter1=0 
            #出現BLENDER 操作中 的依據
            blender=0
            #出現BLENDER 操作中 的依據
            stopblender=0
            #判斷按enter之後按space不紀錄時間
            enterspace=0
            
            # setup some python lists for storing info about the mouse
            mouse.x = []
            mouse.y = []
            mouse.leftButton = []
            mouse.midButton = []
            mouse.rightButton = []
            mouse.time = []
            mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse.mouseClock.reset()
            # keep track of which components have finished
            VIDEOComponents = [key_resp, mouse, backvideo5, movie, closevideo, blender41, quickkey41, blenderquickkey41]
            for thisComponent in VIDEOComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            VIDEOClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "VIDEO"-------
            while continueRoutine:
                # get current time
                t = VIDEOClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=VIDEOClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp* updates
                waitOnFlip = False
                if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp.frameNStart = frameN  # exact frame index
                    key_resp.tStart = t  # local t and not account for scr refresh
                    key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                    key_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                if key_resp.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_allKeys.extend(theseKeys)
                    if len(_key_resp_allKeys):
                        key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                        key_resp.rt = _key_resp_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey41.setAutoDraw(False)
                    blenderquickkey41.setAutoDraw(False)
                if (blender%2)!=1:
                    blender41.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie.status == PLAYING:
                            movie.pause()
                            Time1 = 1
                        elif movie.status == PAUSED:
                            movie.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie.pause()
                        ntime = max(0.0,movie.duration)
                        movie.seek(ntime)
                        movie.play()
                        Time1 = 0
                            
                    if movie.status == PLAYING:
                        if key=='period':
                            movie.pause()
                            ntime = min(movie.getCurrentFrameTime( ) + 5.0, movie.duration)
                            movie.seek(ntime)
                            movie.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma':
                            movie.pause()
                            ntime = max(movie.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie.seek(ntime)
                            movie.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey41.setAutoDraw(True)    
                                blenderquickkey41.setAutoDraw(False)
                                movie.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey41.setAutoDraw(True) 
                                quickkey41.setAutoDraw(False)
                                movie.pause()
                            else:
                                blenderquickkey41.setAutoDraw(False)
                                quickkey41.setAutoDraw(False)
                                movie.play()
                                    
                    elif movie.status == PAUSED:
                        if key=='period':
                            movie.pause()
                            ntime = min(movie.getCurrentFrameTime( ) + 5.0, movie.duration)
                            movie.seek(ntime)
                            movie.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma':
                            movie.pause()
                            ntime = max(movie.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie.seek(ntime)
                            movie.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey41.setAutoDraw(True)    
                                blenderquickkey41.setAutoDraw(False)
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey41.setAutoDraw(True) 
                                quickkey41.setAutoDraw(False)
                            else:
                                blenderquickkey41.setAutoDraw(False)
                                quickkey41.setAutoDraw(False)
                
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1 
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey41.setAutoDraw(True)    
                            blenderquickkey41.setAutoDraw(False)
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey41.setAutoDraw(True) 
                            quickkey41.setAutoDraw(False)
                        else:
                            blenderquickkey41.setAutoDraw(False)
                            quickkey41.setAutoDraw(False)
                            
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video4-1 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender41.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video4-1 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender41.setAutoDraw(False)
                # *mouse* updates
                if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse.frameNStart = frameN  # exact frame index
                    mouse.tStart = t  # local t and not account for scr refresh
                    mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                    mouse.status = STARTED
                    prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
                if mouse.status == STARTED:  # only update if started and not finished!
                    buttons = mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo,]:
                                if obj.contains(mouse):
                                    gotValidClick = True
                                    mouse.clicked_name.append(obj.name)
                            x, y = mouse.getPos()
                            mouse.x.append(x)
                            mouse.y.append(y)
                            buttons = mouse.getPressed()
                            mouse.leftButton.append(buttons[0])
                            mouse.midButton.append(buttons[1])
                            mouse.rightButton.append(buttons[2])
                            mouse.time.append(mouse.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo5* updates
                if backvideo5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo5.frameNStart = frameN  # exact frame index
                    backvideo5.tStart = t  # local t and not account for scr refresh
                    backvideo5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo5, 'tStartRefresh')  # time at next scr refresh
                    backvideo5.setAutoDraw(True)
                
                # *movie* updates
                if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie.frameNStart = frameN  # exact frame index
                    movie.tStart = t  # local t and not account for scr refresh
                    movie.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
                    movie.setAutoDraw(True)
                
                # *closevideo* updates
                if closevideo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo.frameNStart = frameN  # exact frame index
                    closevideo.tStart = t  # local t and not account for scr refresh
                    closevideo.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo, 'tStartRefresh')  # time at next scr refresh
                    closevideo.setAutoDraw(True)
                
                # *blender41* updates
                if blender41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender41.frameNStart = frameN  # exact frame index
                    blender41.tStart = t  # local t and not account for scr refresh
                    blender41.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender41, 'tStartRefresh')  # time at next scr refresh
                    blender41.setAutoDraw(True)
                
                # *quickkey41* updates
                if quickkey41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey41.frameNStart = frameN  # exact frame index
                    quickkey41.tStart = t  # local t and not account for scr refresh
                    quickkey41.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey41, 'tStartRefresh')  # time at next scr refresh
                    quickkey41.setAutoDraw(True)
                
                # *blenderquickkey41* updates
                if blenderquickkey41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey41.frameNStart = frameN  # exact frame index
                    blenderquickkey41.tStart = t  # local t and not account for scr refresh
                    blenderquickkey41.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey41, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey41.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in VIDEOComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "VIDEO"-------
            for thisComponent in VIDEOComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp.keys in ['', [], None]:  # No response was made
                key_resp.keys = None
            videopath5_1.addData('key_resp.keys',key_resp.keys)
            if key_resp.keys != None:  # we had a response
                videopath5_1.addData('key_resp.rt', key_resp.rt)
            videopath5_1.addData('key_resp.started', key_resp.tStartRefresh)
            videopath5_1.addData('key_resp.stopped', key_resp.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime()) 
                    allsteptime.append('video4-1 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video4-1 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie.getCurrentFrameTime( )
                remembertimestamp.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime21.append(sum(Watchtime1))
            #    allsteptime.append('video4-1 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime21.append(sum(Watchtime1))
            #    allsteptime.append('video4-1 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            
            totalpath5=1
            # store data for videopath5_1 (TrialHandler)
            if len(mouse.x): videopath5_1.addData('mouse.x', mouse.x[0])
            if len(mouse.y): videopath5_1.addData('mouse.y', mouse.y[0])
            if len(mouse.leftButton): videopath5_1.addData('mouse.leftButton', mouse.leftButton[0])
            if len(mouse.midButton): videopath5_1.addData('mouse.midButton', mouse.midButton[0])
            if len(mouse.rightButton): videopath5_1.addData('mouse.rightButton', mouse.rightButton[0])
            if len(mouse.time): videopath5_1.addData('mouse.time', mouse.time[0])
            if len(mouse.clicked_name): videopath5_1.addData('mouse.clicked_name', mouse.clicked_name[0])
            videopath5_1.addData('mouse.started', mouse.tStart)
            videopath5_1.addData('mouse.stopped', mouse.tStop)
            videopath5_1.addData('backvideo5.started', backvideo5.tStartRefresh)
            videopath5_1.addData('backvideo5.stopped', backvideo5.tStopRefresh)
            movie.stop()
            videopath5_1.addData('closevideo.started', closevideo.tStartRefresh)
            videopath5_1.addData('closevideo.stopped', closevideo.tStopRefresh)
            videopath5_1.addData('blender41.started', blender41.tStartRefresh)
            videopath5_1.addData('blender41.stopped', blender41.tStopRefresh)
            videopath5_1.addData('quickkey41.started', quickkey41.tStartRefresh)
            videopath5_1.addData('quickkey41.stopped', quickkey41.tStopRefresh)
            videopath5_1.addData('blenderquickkey41.started', blenderquickkey41.tStartRefresh)
            videopath5_1.addData('blenderquickkey41.stopped', blenderquickkey41.tStopRefresh)
            # the Routine "VIDEO" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed goto1 repeats of 'videopath5_1'
        
        
        # set up handler to look after randomisation of conditions etc
        videopath5_2 = data.TrialHandler(nReps=goto2, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='videopath5_2')
        thisExp.addLoop(videopath5_2)  # add the loop to the experiment
        thisVideopath5_2 = videopath5_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisVideopath5_2.rgb)
        if thisVideopath5_2 != None:
            for paramName in thisVideopath5_2:
                exec('{} = thisVideopath5_2[paramName]'.format(paramName))
        
        for thisVideopath5_2 in videopath5_2:
            currentLoop = videopath5_2
            # abbreviate parameter names if possible (e.g. rgb = thisVideopath5_2.rgb)
            if thisVideopath5_2 != None:
                for paramName in thisVideopath5_2:
                    exec('{} = thisVideopath5_2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video2"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_2.keys = []
            key_resp_2.rt = []
            _key_resp_2_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp2)!=0:
                movie_2.pause()
                movie_2.seek(int(remembertimestamp2[-1]))
                movie_2.play()
                Time1 = 0
            showf=0
            enter1=0    
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_2
            mouse_2.x = []
            mouse_2.y = []
            mouse_2.leftButton = []
            mouse_2.midButton = []
            mouse_2.rightButton = []
            mouse_2.time = []
            mouse_2.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_2.mouseClock.reset()
            # keep track of which components have finished
            video2Components = [key_resp_2, mouse_2, backvideo52, movie_2, closevideo_2, blender42, quickkey42, blenderquickkey42]
            for thisComponent in video2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video2"-------
            while continueRoutine:
                # get current time
                t = video2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_2* updates
                waitOnFlip = False
                if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_2.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                        key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey42.setAutoDraw(False)
                    blenderquickkey42.setAutoDraw(False)
                if (blender%2)!=1:
                    blender42.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_2.status == PLAYING:
                            movie_2.pause()
                            Time1 = 1
                        elif movie_2.status == PAUSED:
                            movie_2.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_2.pause()
                        ntime = max(0.0,movie_2.duration)
                        movie_2.seek(ntime)
                        movie_2.play()
                        Time1 = 0
                
                    if movie_2.status == PLAYING:
                        if key=='period':
                            movie_2.pause()
                            ntime = min(movie_2.getCurrentFrameTime( ) + 5.0, movie_2.duration)
                            movie_2.seek(ntime)
                            movie_2.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_2.pause()
                            ntime = max(movie_2.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_2.seek(ntime)
                            movie_2.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey42.setAutoDraw(True)    
                                blenderquickkey42.setAutoDraw(False) 
                                movie_2.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey42.setAutoDraw(True) 
                                quickkey42.setAutoDraw(False)
                                movie_2.pause()
                            else:
                                blenderquickkey42.setAutoDraw(False) 
                                quickkey42.setAutoDraw(False)
                                movie_2.play()
                                
                    elif movie_2.status == PAUSED:
                        if key=='period':
                            movie_2.pause()
                            ntime = min(movie_2.getCurrentFrameTime( ) + 5.0, movie_2.duration)
                            movie_2.seek(ntime)
                            movie_2.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_2.pause()
                            ntime = max(movie_2.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_2.seek(ntime)
                            movie_2.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_2.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey42.setAutoDraw(True)    
                                blenderquickkey42.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey42.setAutoDraw(True) 
                                quickkey42.setAutoDraw(False)
                            else:
                                blenderquickkey42.setAutoDraw(False) 
                                quickkey42.setAutoDraw(False)
                             
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey42.setAutoDraw(True)    
                            blenderquickkey42.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey42.setAutoDraw(True) 
                            quickkey42.setAutoDraw(False)
                        else:
                            blenderquickkey42.setAutoDraw(False) 
                            quickkey42.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video4-2 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender42.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video4-2 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender42.setAutoDraw(False)
                # *mouse_2* updates
                if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_2.frameNStart = frameN  # exact frame index
                    mouse_2.tStart = t  # local t and not account for scr refresh
                    mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
                    mouse_2.status = STARTED
                    prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
                if mouse_2.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_2.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_2,]:
                                if obj.contains(mouse_2):
                                    gotValidClick = True
                                    mouse_2.clicked_name.append(obj.name)
                            x, y = mouse_2.getPos()
                            mouse_2.x.append(x)
                            mouse_2.y.append(y)
                            buttons = mouse_2.getPressed()
                            mouse_2.leftButton.append(buttons[0])
                            mouse_2.midButton.append(buttons[1])
                            mouse_2.rightButton.append(buttons[2])
                            mouse_2.time.append(mouse_2.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo52* updates
                if backvideo52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo52.frameNStart = frameN  # exact frame index
                    backvideo52.tStart = t  # local t and not account for scr refresh
                    backvideo52.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo52, 'tStartRefresh')  # time at next scr refresh
                    backvideo52.setAutoDraw(True)
                
                # *movie_2* updates
                if movie_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_2.frameNStart = frameN  # exact frame index
                    movie_2.tStart = t  # local t and not account for scr refresh
                    movie_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_2, 'tStartRefresh')  # time at next scr refresh
                    movie_2.setAutoDraw(True)
                
                # *closevideo_2* updates
                if closevideo_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_2.frameNStart = frameN  # exact frame index
                    closevideo_2.tStart = t  # local t and not account for scr refresh
                    closevideo_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_2, 'tStartRefresh')  # time at next scr refresh
                    closevideo_2.setAutoDraw(True)
                
                # *blender42* updates
                if blender42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender42.frameNStart = frameN  # exact frame index
                    blender42.tStart = t  # local t and not account for scr refresh
                    blender42.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender42, 'tStartRefresh')  # time at next scr refresh
                    blender42.setAutoDraw(True)
                
                # *quickkey42* updates
                if quickkey42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey42.frameNStart = frameN  # exact frame index
                    quickkey42.tStart = t  # local t and not account for scr refresh
                    quickkey42.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey42, 'tStartRefresh')  # time at next scr refresh
                    quickkey42.setAutoDraw(True)
                
                # *blenderquickkey42* updates
                if blenderquickkey42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey42.frameNStart = frameN  # exact frame index
                    blenderquickkey42.tStart = t  # local t and not account for scr refresh
                    blenderquickkey42.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey42, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey42.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video2"-------
            for thisComponent in video2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_2.keys in ['', [], None]:  # No response was made
                key_resp_2.keys = None
            videopath5_2.addData('key_resp_2.keys',key_resp_2.keys)
            if key_resp_2.keys != None:  # we had a response
                videopath5_2.addData('key_resp_2.rt', key_resp_2.rt)
            videopath5_2.addData('key_resp_2.started', key_resp_2.tStartRefresh)
            videopath5_2.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime())  
                    allsteptime.append('video4-2 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video4-2 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_2.getCurrentFrameTime( )
                remembertimestamp2.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime22.append(sum(Watchtime1))
            #    allsteptime.append('video4-2 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime22.append(sum(Watchtime1))
            #    allsteptime.append('video4-2 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
                
            totalpath5=1
            # store data for videopath5_2 (TrialHandler)
            if len(mouse_2.x): videopath5_2.addData('mouse_2.x', mouse_2.x[0])
            if len(mouse_2.y): videopath5_2.addData('mouse_2.y', mouse_2.y[0])
            if len(mouse_2.leftButton): videopath5_2.addData('mouse_2.leftButton', mouse_2.leftButton[0])
            if len(mouse_2.midButton): videopath5_2.addData('mouse_2.midButton', mouse_2.midButton[0])
            if len(mouse_2.rightButton): videopath5_2.addData('mouse_2.rightButton', mouse_2.rightButton[0])
            if len(mouse_2.time): videopath5_2.addData('mouse_2.time', mouse_2.time[0])
            if len(mouse_2.clicked_name): videopath5_2.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
            videopath5_2.addData('mouse_2.started', mouse_2.tStart)
            videopath5_2.addData('mouse_2.stopped', mouse_2.tStop)
            videopath5_2.addData('backvideo52.started', backvideo52.tStartRefresh)
            videopath5_2.addData('backvideo52.stopped', backvideo52.tStopRefresh)
            movie_2.stop()
            videopath5_2.addData('closevideo_2.started', closevideo_2.tStartRefresh)
            videopath5_2.addData('closevideo_2.stopped', closevideo_2.tStopRefresh)
            videopath5_2.addData('blender42.started', blender42.tStartRefresh)
            videopath5_2.addData('blender42.stopped', blender42.tStopRefresh)
            videopath5_2.addData('quickkey42.started', quickkey42.tStartRefresh)
            videopath5_2.addData('quickkey42.stopped', quickkey42.tStopRefresh)
            videopath5_2.addData('blenderquickkey42.started', blenderquickkey42.tStartRefresh)
            videopath5_2.addData('blenderquickkey42.stopped', blenderquickkey42.tStopRefresh)
            # the Routine "video2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed goto2 repeats of 'videopath5_2'
        
        
        # set up handler to look after randomisation of conditions etc
        videopath5_3 = data.TrialHandler(nReps=goto3, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='videopath5_3')
        thisExp.addLoop(videopath5_3)  # add the loop to the experiment
        thisVideopath5_3 = videopath5_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisVideopath5_3.rgb)
        if thisVideopath5_3 != None:
            for paramName in thisVideopath5_3:
                exec('{} = thisVideopath5_3[paramName]'.format(paramName))
        
        for thisVideopath5_3 in videopath5_3:
            currentLoop = videopath5_3
            # abbreviate parameter names if possible (e.g. rgb = thisVideopath5_3.rgb)
            if thisVideopath5_3 != None:
                for paramName in thisVideopath5_3:
                    exec('{} = thisVideopath5_3[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video3"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_3.keys = []
            key_resp_3.rt = []
            _key_resp_3_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp3)!=0:
                movie_3.pause()
                movie_3.seek(int(remembertimestamp3[-1]))
                movie_3.play()
                Time1 = 0
            showf=0
            enter1=0  
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_3
            mouse_3.x = []
            mouse_3.y = []
            mouse_3.leftButton = []
            mouse_3.midButton = []
            mouse_3.rightButton = []
            mouse_3.time = []
            mouse_3.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_3.mouseClock.reset()
            # keep track of which components have finished
            video3Components = [key_resp_3, mouse_3, backvideo53, movie_3, closevideo_3, blender43, quickkey43, blenderquickkey43]
            for thisComponent in video3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video3"-------
            while continueRoutine:
                # get current time
                t = video3Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video3Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_3* updates
                waitOnFlip = False
                if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.tStart = t  # local t and not account for scr refresh
                    key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_3.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_3.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_3_allKeys.extend(theseKeys)
                    if len(_key_resp_3_allKeys):
                        key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                        key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey43.setAutoDraw(False)
                    blenderquickkey43.setAutoDraw(False)
                if (blender%2)!=1:
                    blender43.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_3.status == PLAYING:
                            movie_3.pause()
                            Time1 = 1
                        elif movie_3.status == PAUSED:
                            movie_3.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_3.pause()
                        ntime = max(0.0,movie_3.duration)
                        movie_3.seek(ntime)
                        movie_3.play()
                        Time1 = 0
                
                    if movie_3.status == PLAYING:
                        if key=='period':
                            movie_3.pause()
                            ntime = min(movie_3.getCurrentFrameTime( ) + 5.0, movie_3.duration)
                            movie_3.seek(ntime)
                            movie_3.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_3.pause()
                            ntime = max(movie_3.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_3.seek(ntime)
                            movie_3.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey43.setAutoDraw(True)    
                                blenderquickkey43.setAutoDraw(False) 
                                movie_3.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey43.setAutoDraw(True) 
                                quickkey43.setAutoDraw(False)
                                movie_3.pause()
                            else:
                                blenderquickkey43.setAutoDraw(False) 
                                quickkey43.setAutoDraw(False)
                                movie_3.play()
                
                    elif movie_3.status == PAUSED:
                        if key=='period':
                            movie_3.pause()
                            ntime = min(movie_3.getCurrentFrameTime( ) + 5.0, movie_3.duration)
                            movie_3.seek(ntime)
                            movie_3.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_3.pause()
                            ntime = max(movie_3.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_3.seek(ntime)
                            movie_3.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_3.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey43.setAutoDraw(True)    
                                blenderquickkey43.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey43.setAutoDraw(True) 
                                quickkey43.setAutoDraw(False)
                            else:
                                blenderquickkey43.setAutoDraw(False) 
                                quickkey43.setAutoDraw(False)
                             
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey43.setAutoDraw(True)    
                            blenderquickkey43.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey43.setAutoDraw(True) 
                            quickkey43.setAutoDraw(False)
                        else:
                            blenderquickkey43.setAutoDraw(False) 
                            quickkey43.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video4-3 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender43.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video4-3 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender43.setAutoDraw(False)
                # *mouse_3* updates
                if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_3.frameNStart = frameN  # exact frame index
                    mouse_3.tStart = t  # local t and not account for scr refresh
                    mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
                    mouse_3.status = STARTED
                    prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
                if mouse_3.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_3.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_3,]:
                                if obj.contains(mouse_3):
                                    gotValidClick = True
                                    mouse_3.clicked_name.append(obj.name)
                            x, y = mouse_3.getPos()
                            mouse_3.x.append(x)
                            mouse_3.y.append(y)
                            buttons = mouse_3.getPressed()
                            mouse_3.leftButton.append(buttons[0])
                            mouse_3.midButton.append(buttons[1])
                            mouse_3.rightButton.append(buttons[2])
                            mouse_3.time.append(mouse_3.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo53* updates
                if backvideo53.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo53.frameNStart = frameN  # exact frame index
                    backvideo53.tStart = t  # local t and not account for scr refresh
                    backvideo53.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo53, 'tStartRefresh')  # time at next scr refresh
                    backvideo53.setAutoDraw(True)
                
                # *movie_3* updates
                if movie_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_3.frameNStart = frameN  # exact frame index
                    movie_3.tStart = t  # local t and not account for scr refresh
                    movie_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_3, 'tStartRefresh')  # time at next scr refresh
                    movie_3.setAutoDraw(True)
                
                # *closevideo_3* updates
                if closevideo_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_3.frameNStart = frameN  # exact frame index
                    closevideo_3.tStart = t  # local t and not account for scr refresh
                    closevideo_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_3, 'tStartRefresh')  # time at next scr refresh
                    closevideo_3.setAutoDraw(True)
                
                # *blender43* updates
                if blender43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender43.frameNStart = frameN  # exact frame index
                    blender43.tStart = t  # local t and not account for scr refresh
                    blender43.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender43, 'tStartRefresh')  # time at next scr refresh
                    blender43.setAutoDraw(True)
                
                # *quickkey43* updates
                if quickkey43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey43.frameNStart = frameN  # exact frame index
                    quickkey43.tStart = t  # local t and not account for scr refresh
                    quickkey43.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey43, 'tStartRefresh')  # time at next scr refresh
                    quickkey43.setAutoDraw(True)
                
                # *blenderquickkey43* updates
                if blenderquickkey43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey43.frameNStart = frameN  # exact frame index
                    blenderquickkey43.tStart = t  # local t and not account for scr refresh
                    blenderquickkey43.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey43, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey43.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video3"-------
            for thisComponent in video3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_3.keys in ['', [], None]:  # No response was made
                key_resp_3.keys = None
            videopath5_3.addData('key_resp_3.keys',key_resp_3.keys)
            if key_resp_3.keys != None:  # we had a response
                videopath5_3.addData('key_resp_3.rt', key_resp_3.rt)
            videopath5_3.addData('key_resp_3.started', key_resp_3.tStartRefresh)
            videopath5_3.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime())  
                    allsteptime.append('video4-3 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video4-3 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_3.getCurrentFrameTime( )
                remembertimestamp3.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime23.append(sum(Watchtime1))
            #    allsteptime.append('video4-3 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime23.append(sum(Watchtime1))
            #    allsteptime.append('video4-3 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
                
            totalpath5=1
            # store data for videopath5_3 (TrialHandler)
            if len(mouse_3.x): videopath5_3.addData('mouse_3.x', mouse_3.x[0])
            if len(mouse_3.y): videopath5_3.addData('mouse_3.y', mouse_3.y[0])
            if len(mouse_3.leftButton): videopath5_3.addData('mouse_3.leftButton', mouse_3.leftButton[0])
            if len(mouse_3.midButton): videopath5_3.addData('mouse_3.midButton', mouse_3.midButton[0])
            if len(mouse_3.rightButton): videopath5_3.addData('mouse_3.rightButton', mouse_3.rightButton[0])
            if len(mouse_3.time): videopath5_3.addData('mouse_3.time', mouse_3.time[0])
            if len(mouse_3.clicked_name): videopath5_3.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
            videopath5_3.addData('mouse_3.started', mouse_3.tStart)
            videopath5_3.addData('mouse_3.stopped', mouse_3.tStop)
            videopath5_3.addData('backvideo53.started', backvideo53.tStartRefresh)
            videopath5_3.addData('backvideo53.stopped', backvideo53.tStopRefresh)
            movie_3.stop()
            videopath5_3.addData('closevideo_3.started', closevideo_3.tStartRefresh)
            videopath5_3.addData('closevideo_3.stopped', closevideo_3.tStopRefresh)
            videopath5_3.addData('blender43.started', blender43.tStartRefresh)
            videopath5_3.addData('blender43.stopped', blender43.tStopRefresh)
            videopath5_3.addData('quickkey43.started', quickkey43.tStartRefresh)
            videopath5_3.addData('quickkey43.stopped', quickkey43.tStopRefresh)
            videopath5_3.addData('blenderquickkey43.started', blenderquickkey43.tStartRefresh)
            videopath5_3.addData('blenderquickkey43.stopped', blenderquickkey43.tStopRefresh)
            # the Routine "video3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed goto3 repeats of 'videopath5_3'
        
        
        # set up handler to look after randomisation of conditions etc
        videopath5_4 = data.TrialHandler(nReps=goto4, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='videopath5_4')
        thisExp.addLoop(videopath5_4)  # add the loop to the experiment
        thisVideopath5_4 = videopath5_4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisVideopath5_4.rgb)
        if thisVideopath5_4 != None:
            for paramName in thisVideopath5_4:
                exec('{} = thisVideopath5_4[paramName]'.format(paramName))
        
        for thisVideopath5_4 in videopath5_4:
            currentLoop = videopath5_4
            # abbreviate parameter names if possible (e.g. rgb = thisVideopath5_4.rgb)
            if thisVideopath5_4 != None:
                for paramName in thisVideopath5_4:
                    exec('{} = thisVideopath5_4[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "video4"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_4.keys = []
            key_resp_4.rt = []
            _key_resp_4_allKeys = []
            respClock.reset(0)
            ExperienceClock.reset(0)
            if len(remembertimestamp4)!=0:
                movie_4.pause()
                movie_4.seek(int(remembertimestamp4[-1]))
                movie_4.play()
                Time1 = 0
            showf=0
            enter1=0   
            blender=0
            enterspace=0
            stopblender=0
            newchange=0
            # setup some python lists for storing info about the mouse_4
            mouse_4.x = []
            mouse_4.y = []
            mouse_4.leftButton = []
            mouse_4.midButton = []
            mouse_4.rightButton = []
            mouse_4.time = []
            mouse_4.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_4.mouseClock.reset()
            # keep track of which components have finished
            video4Components = [key_resp_4, mouse_4, backvideo, movie_4, closevideo_4, blender44, quickkey44, blenderquickkey44]
            for thisComponent in video4Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            video4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "video4"-------
            while continueRoutine:
                # get current time
                t = video4Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=video4Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_4* updates
                waitOnFlip = False
                if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_4.frameNStart = frameN  # exact frame index
                    key_resp_4.tStart = t  # local t and not account for scr refresh
                    key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                    key_resp_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_4.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_4.getKeys(keyList=['space', '<', '>', 'f', 'return', 's'], waitRelease=False)
                    _key_resp_4_allKeys.extend(theseKeys)
                    if len(_key_resp_4_allKeys):
                        key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                        key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                if (showf%2)!=1:
                    quickkey44.setAutoDraw(False)
                    blenderquickkey44.setAutoDraw(False)
                if (blender%2)!=1:
                    blender44.setAutoDraw(False)
                for key in event.getKeys():
                    if key =='space':
                        countcontinue=countcontinue+1
                        if movie_4.status == PLAYING:
                            movie_4.pause()
                            Time1 = 1
                        elif movie_4.status == PAUSED:
                            movie_4.play()
                            Time1 = 0
                            
                    elif key=='s':
                        change=change+1
                        movie_4.pause()
                        ntime = max(0.0,movie_4.duration)
                        movie_4.seek(ntime)
                        movie_4.play()
                        Time1 = 0
                
                    if movie_4.status == PLAYING:
                        if key=='period':
                            movie_4.pause()
                            ntime = min(movie_4.getCurrentFrameTime( ) + 5.0, movie_4.duration)
                            movie_4.seek(ntime)
                            movie_4.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_4.pause()
                            ntime = max(movie_4.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_4.seek(ntime)
                            movie_4.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey44.setAutoDraw(True)    
                                blenderquickkey44.setAutoDraw(False) 
                                movie_4.pause()
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey44.setAutoDraw(True) 
                                quickkey44.setAutoDraw(False)
                                movie_4.pause()
                            else:
                                blenderquickkey44.setAutoDraw(False) 
                                quickkey44.setAutoDraw(False)
                                movie_4.play()
                                           
                    elif movie_4.status == PAUSED:
                        if key=='period':
                            movie_4.pause()
                            ntime = min(movie_4.getCurrentFrameTime( ) + 5.0, movie_4.duration)
                            movie_4.seek(ntime)
                            movie_4.play()
                            Time1 = 0
                            change=change+1
                       
                        elif key=='comma': 
                            movie_4.pause()
                            ntime = max(movie_4.getCurrentFrameTime( ) - 5.0, 0.0)
                            movie_4.seek(ntime)
                            movie_4.play()
                            Time1 = 0
                            change=change+1
                        elif key =='f':
                            movie_4.pause()
                            countcontinue=countcontinue+1
                            showf=showf+1
                            if(showf%2)==1 and (enter1%2)==0:
                                quickkey44.setAutoDraw(True)    
                                blenderquickkey44.setAutoDraw(False) 
                            elif (showf%2)==1 and (enter1%2)==1:
                                blenderquickkey44.setAutoDraw(True) 
                                quickkey44.setAutoDraw(False)
                            else:
                                blenderquickkey44.setAutoDraw(False) 
                                quickkey44.setAutoDraw(False)
                             
                    if key =='return': 
                        countcontinue=countcontinue+1
                        enter1=enter1+1
                        blender=blender+1
                        countenter=countenter+1
                        newchange=newchange+1
                        if(showf%2)==1 and (enter1%2)==0:
                            quickkey44.setAutoDraw(True)    
                            blenderquickkey44.setAutoDraw(False) 
                        elif (showf%2)==1 and (enter1%2)==1:
                            blenderquickkey44.setAutoDraw(True) 
                            quickkey44.setAutoDraw(False)
                        else:
                            blenderquickkey44.setAutoDraw(False) 
                            quickkey44.setAutoDraw(False)
                        if(enter1%2)==1:
                            Watchtime1.append(respClock.getTime())
                            allsteptime.append('video4-4 learn')
                            allsteptime.append(respClock.getTime())
                            BlenderClock.reset(0)
                            blender44.setAutoDraw(True)
                            enterspace=enterspace+1
                        else:
                            BlenderTime.append(BlenderClock.getTime())
                            allsteptime.append('video4-4 blender')
                            allsteptime.append(BlenderClock.getTime())
                            respClock.reset(0)
                            enterspace=0
                            blender44.setAutoDraw(False)
                # *mouse_4* updates
                if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_4.frameNStart = frameN  # exact frame index
                    mouse_4.tStart = t  # local t and not account for scr refresh
                    mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
                    mouse_4.status = STARTED
                    prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
                if mouse_4.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_4.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [closevideo_4,]:
                                if obj.contains(mouse_4):
                                    gotValidClick = True
                                    mouse_4.clicked_name.append(obj.name)
                            x, y = mouse_4.getPos()
                            mouse_4.x.append(x)
                            mouse_4.y.append(y)
                            buttons = mouse_4.getPressed()
                            mouse_4.leftButton.append(buttons[0])
                            mouse_4.midButton.append(buttons[1])
                            mouse_4.rightButton.append(buttons[2])
                            mouse_4.time.append(mouse_4.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *backvideo* updates
                if backvideo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    backvideo.frameNStart = frameN  # exact frame index
                    backvideo.tStart = t  # local t and not account for scr refresh
                    backvideo.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(backvideo, 'tStartRefresh')  # time at next scr refresh
                    backvideo.setAutoDraw(True)
                
                # *movie_4* updates
                if movie_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    movie_4.frameNStart = frameN  # exact frame index
                    movie_4.tStart = t  # local t and not account for scr refresh
                    movie_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(movie_4, 'tStartRefresh')  # time at next scr refresh
                    movie_4.setAutoDraw(True)
                
                # *closevideo_4* updates
                if closevideo_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    closevideo_4.frameNStart = frameN  # exact frame index
                    closevideo_4.tStart = t  # local t and not account for scr refresh
                    closevideo_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(closevideo_4, 'tStartRefresh')  # time at next scr refresh
                    closevideo_4.setAutoDraw(True)
                
                # *blender44* updates
                if blender44.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blender44.frameNStart = frameN  # exact frame index
                    blender44.tStart = t  # local t and not account for scr refresh
                    blender44.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blender44, 'tStartRefresh')  # time at next scr refresh
                    blender44.setAutoDraw(True)
                
                # *quickkey44* updates
                if quickkey44.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quickkey44.frameNStart = frameN  # exact frame index
                    quickkey44.tStart = t  # local t and not account for scr refresh
                    quickkey44.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quickkey44, 'tStartRefresh')  # time at next scr refresh
                    quickkey44.setAutoDraw(True)
                
                # *blenderquickkey44* updates
                if blenderquickkey44.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blenderquickkey44.frameNStart = frameN  # exact frame index
                    blenderquickkey44.tStart = t  # local t and not account for scr refresh
                    blenderquickkey44.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blenderquickkey44, 'tStartRefresh')  # time at next scr refresh
                    blenderquickkey44.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in video4Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "video4"-------
            for thisComponent in video4Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_4.keys in ['', [], None]:  # No response was made
                key_resp_4.keys = None
            videopath5_4.addData('key_resp_4.keys',key_resp_4.keys)
            if key_resp_4.keys != None:  # we had a response
                videopath5_4.addData('key_resp_4.rt', key_resp_4.rt)
            videopath5_4.addData('key_resp_4.started', key_resp_4.tStartRefresh)
            videopath5_4.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
            Experiencetime.append(ExperienceClock.getTime())
            
            if gotValidClick ==True:
                countchange.append(newchange)
                if (enter1%2)==0 :
                    Watchtime1.append(respClock.getTime())  
                    allsteptime.append('video4-4 learn')
                    allsteptime.append(respClock.getTime())
                else:
                    BlenderTime.append(BlenderClock.getTime())
                    allsteptime.append('video4-4 blender')
                    allsteptime.append(BlenderClock.getTime())
                change=change+1
                nowtime=movie_4.getCurrentFrameTime( )
                remembertimestamp4.append(nowtime)
                
            if sum(Watchtime1) > 20 :
                Max20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime24.append(sum(Watchtime1))
            #    allsteptime.append('video4-4 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            elif sum(Watchtime1) <= 20 :
                Min20.append(sum(Watchtime1))
                AllWatchtime.append(sum(Watchtime1))
                Watchtime24.append(sum(Watchtime1))
            #    allsteptime.append('video4-4 learn')
            #    allsteptime.append(sum(Watchtime1))
                Watchtime1.clear()
            
            totalpath5=1
            # store data for videopath5_4 (TrialHandler)
            if len(mouse_4.x): videopath5_4.addData('mouse_4.x', mouse_4.x[0])
            if len(mouse_4.y): videopath5_4.addData('mouse_4.y', mouse_4.y[0])
            if len(mouse_4.leftButton): videopath5_4.addData('mouse_4.leftButton', mouse_4.leftButton[0])
            if len(mouse_4.midButton): videopath5_4.addData('mouse_4.midButton', mouse_4.midButton[0])
            if len(mouse_4.rightButton): videopath5_4.addData('mouse_4.rightButton', mouse_4.rightButton[0])
            if len(mouse_4.time): videopath5_4.addData('mouse_4.time', mouse_4.time[0])
            if len(mouse_4.clicked_name): videopath5_4.addData('mouse_4.clicked_name', mouse_4.clicked_name[0])
            videopath5_4.addData('mouse_4.started', mouse_4.tStart)
            videopath5_4.addData('mouse_4.stopped', mouse_4.tStop)
            videopath5_4.addData('backvideo.started', backvideo.tStartRefresh)
            videopath5_4.addData('backvideo.stopped', backvideo.tStopRefresh)
            movie_4.stop()
            videopath5_4.addData('closevideo_4.started', closevideo_4.tStartRefresh)
            videopath5_4.addData('closevideo_4.stopped', closevideo_4.tStopRefresh)
            videopath5_4.addData('blender44.started', blender44.tStartRefresh)
            videopath5_4.addData('blender44.stopped', blender44.tStopRefresh)
            videopath5_4.addData('quickkey44.started', quickkey44.tStartRefresh)
            videopath5_4.addData('quickkey44.stopped', quickkey44.tStopRefresh)
            videopath5_4.addData('blenderquickkey44.started', blenderquickkey44.tStartRefresh)
            videopath5_4.addData('blenderquickkey44.stopped', blenderquickkey44.tStopRefresh)
            # the Routine "video4" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed goto4 repeats of 'videopath5_4'
        
        thisExp.nextEntry()
        
    # completed totalpath4 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 200.0 repeats of 'trials_27'


# ------Prepare to start Routine "showdata"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
showdataComponents = []
for thisComponent in showdataComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
showdataClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "showdata"-------
while continueRoutine:
    # get current time
    t = showdataClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=showdataClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in showdataComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "showdata"-------
for thisComponent in showdataComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "showdata" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
for changetime in countchange:
    if changetime>8:
        morefivechange.append(changetime)
    else:
        lessfivechange.append(changetime)    

totalaction=change+countcontinue
globecore=((countcontinue-change)/totalaction)
globe=(change/totalaction)*11
sequential=(countcontinue/totalaction)*11

SumAllWatchtime=sum(AllWatchtime)
SumBlenderTime=sum(BlenderTime)
SumCookbook=sum(AllCookbook)
SumMax20=sum(Max20)
SumMin20=sum(Min20)
SumMenu=sum(Menutime)
SumMovie=SumAllWatchtime-SumCookbook-SumMenu
SumExperiencetime=sum(Experiencetime)

#結果
FinalActiveOrReflective=Decimal(((SumBlenderTime-SumAllWatchtime)/SumExperiencetime)*11).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
FinalSensingOrIntuitive=Decimal(((SumMax20-SumMin20)/SumAllWatchtime)*11).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
FinalVisualOrVerbal=Decimal(((SumMovie-SumCookbook)/SumAllWatchtime)*11).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")

#每個領域
FinalAllWatchtime=Decimal(((SumBlenderTime)/SumExperiencetime)*11).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
FinalBlenderTime=Decimal(((SumAllWatchtime)/SumExperiencetime)*11).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
FinalMax=Decimal(((sum(Max20))/SumAllWatchtime)*11).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
FinalMin=Decimal(((sum(Min20))/SumAllWatchtime)*11).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
FinalMovie=Decimal((SumMovie/SumAllWatchtime)*11).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
FinalCookbook=Decimal((SumCookbook/SumAllWatchtime)*11).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
Finalglobecore=Decimal(globecore*11).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")

#輸出
sheet1.write(1,0,str(FinalActiveOrReflective))
sheet1.write(1,1,str(FinalSensingOrIntuitive))
sheet1.write(1,2,str(FinalVisualOrVerbal))
sheet1.write(1,3,str(Finalglobecore))

#八個各別
sheet1.write(3,0,str(FinalAllWatchtime))
sheet1.write(3,1,str(FinalBlenderTime))
sheet1.write(3,2,str(FinalMax))
sheet1.write(3,3,str(FinalMin))
sheet1.write(3,4,str(FinalMovie))
sheet1.write(3,5,str(FinalCookbook))
sheet1.write(3,6,str(sequential))
sheet1.write(3,7,str(globe))

#總和
sheet1.write(5,0,str(SumAllWatchtime))
sheet1.write(5,1,str(SumBlenderTime))
sheet1.write(5,2,str(SumMenu))
sheet1.write(5,3,str(SumMax20))
sheet1.write(5,4,str(SumMin20))
sheet1.write(5,5,str(SumMovie))
sheet1.write(5,6,str(SumCookbook))

#全部內容
sheet1.write(7,0,str(AllWatchtime))
sheet1.write(7,1,str(BlenderTime))
sheet1.write(7,2,str(Menutime))
sheet1.write(7,3,str(Max20))
sheet1.write(7,4,str(Min20))

#每個影片的時間
sheet1.write(9,0,str(Watchtime111))
sheet1.write(9,1,str(Watchtime2))
sheet1.write(9,2,str(Watchtime3))
sheet1.write(9,3,str(Watchtime4))
sheet1.write(9,4,str(Watchtime5))
sheet1.write(9,5,str(Watchtime6))

sheet1.write(9,7,str(Watchtime8))
sheet1.write(9,8,str(Watchtime9))
sheet1.write(9,9,str(Watchtime10))
sheet1.write(9,10,str(Watchtime11))
sheet1.write(9,11,str(Watchtime12))
sheet1.write(9,12,str(Watchtime13))
sheet1.write(9,13,str(Watchtime14))
sheet1.write(9,14,str(Watchtime15))
sheet1.write(9,15,str(Watchtime16))
sheet1.write(9,16,str(Watchtime17))
sheet1.write(9,17,str(Watchtime18))
sheet1.write(9,18,str(Watchtime19))
sheet1.write(9,19,str(Watchtime20))
sheet1.write(9,20,str(Watchtime21))
sheet1.write(9,21,str(Watchtime22))
sheet1.write(9,22,str(Watchtime23))
sheet1.write(9,23,str(Watchtime24))
sheet1.write(9,24,str(Cookbook1))
sheet1.write(9,25,str(Cookbook2))
sheet1.write(9,26,str(Cookbook3))

sheet1.write(11,0,str(change))
sheet1.write(11,1,str(countcontinue))
sheet1.write(11,2,str(countenter))

sheet1.write(13,0,str(SumExperiencetime))
sheet1.write(13,1,str(Experiencetime))

sheet1.write(15,0,str(allsteptime))

sheet1.write(17,0,str(countchange))
sheet1.write(17,1,str(sum(morefivechange)))
sheet1.write(17,2,str(sum(lessfivechange)))

book.save( filename + '.xls')


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
