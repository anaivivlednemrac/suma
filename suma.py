# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'prueba de sumacion'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
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
    originPath='C:\\Users\\saezr\\OneDrive\\Escritorio\\prueba de sumacion\\prueba de sumacion.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0,1.0,1.0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICION" ---
text = visual.TextStim(win=win, name='text',
    text='¿Cuán probable es que se presente la imagen y el sonido desagradable?',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
jaja = visual.ImageStim(
    win=win,
    name='jaja', 
    image=EXCITADOR_DE_TRANSFERENCIA_ADQUISICION, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
ESCALA_EXPECTATIVA_PDS_1 = visual.Slider(win=win, name='ESCALA_EXPECTATIVA_PDS_1',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Poco probable" , "Muy probable"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-2, readOnly=False)
eiiiiiii = visual.ImageStim(
    win=win,
    name='eiiiiiii', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
eiiiiisonido = sound.Sound(EI_SONIDO, secs=0.7, stereo=True, hamming=True,
    name='eiiiiisonido')
eiiiiisonido.setVolume(1.0)
cruz_de_fijacion = visual.ShapeStim(
    win=win, name='cruz_de_fijacion', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "ESTIMULO_COMPUESTO_INHIBIDOR" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='¿Cuán probable es que se presente la imagen y el sonido desagradable?',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
jeje = visual.ImageStim(
    win=win,
    name='jeje', 
    image=INHIBIDOR_A_PRUEBA_ADQUISICION, mask=None, anchor='center',
    ori=0.0, pos=(1.0, 0.0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
jiji = visual.ImageStim(
    win=win,
    name='jiji', 
    image=EXCITADOR_DE_TRANSFERENCIA_ADQUISICION, mask=None, anchor='center',
    ori=0.0, pos=(0.0, 1.0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Poco probable" , "Muy probable"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-3, readOnly=False)
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "ESTIMULO_COMPUESTO_NEUTRO" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='¿Cuán probable es que se presente la imagen y el sonido desagradable?',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
jojo = visual.ImageStim(
    win=win,
    name='jojo', 
    image=ESTIMULO_NEUTRO_ADQUISICION, mask=None, anchor='center',
    ori=0.0, pos=(1.0, 0.0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
juju = visual.ImageStim(
    win=win,
    name='juju', 
    image=EXCITADOR_DE_TRANSFERENCIA_ADQUISICION, mask=None, anchor='center',
    ori=0.0, pos=(0, 1.0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
slider_2 = visual.Slider(win=win, name='slider_2',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Poco probable" , "Muy probable"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-3, readOnly=False)
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "ESTIMULO_EXCITATORIO_PDS_ADQUISICION" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='¿Cuán probable es que se presente la imagen y el sonido desagradable?',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
joasjoas = visual.ImageStim(
    win=win,
    name='joasjoas', 
    image=ESTIMULO_EXCITATORIO_ADQUISICION, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
slider_3 = visual.Slider(win=win, name='slider_3',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Poco probable" , "Muy probable"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-2, readOnly=False)
ei = visual.ImageStim(
    win=win,
    name='ei', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
eisonido = sound.Sound(EI_SONIDO, secs=0.7, stereo=True, hamming=True,
    name='eisonido')
eisonido.setVolume(1.0)
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICION" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ESCALA_EXPECTATIVA_PDS_1.reset()
eiiiiiii.setImage(EI_FOTO)
eiiiiisonido.setSound(EI_SONIDO, secs=0.7, hamming=True)
eiiiiisonido.setVolume(1.0, log=False)
# keep track of which components have finished
ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICIONComponents = [text, jaja, ESCALA_EXPECTATIVA_PDS_1, eiiiiiii, eiiiiisonido, cruz_de_fijacion]
for thisComponent in ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICIONComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICION" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            text.setAutoDraw(False)
    
    # *jaja* updates
    if jaja.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        jaja.frameNStart = frameN  # exact frame index
        jaja.tStart = t  # local t and not account for scr refresh
        jaja.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(jaja, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'jaja.started')
        jaja.setAutoDraw(True)
    if jaja.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > jaja.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            jaja.tStop = t  # not accounting for scr refresh
            jaja.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'jaja.stopped')
            jaja.setAutoDraw(False)
    
    # *ESCALA_EXPECTATIVA_PDS_1* updates
    if ESCALA_EXPECTATIVA_PDS_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        ESCALA_EXPECTATIVA_PDS_1.frameNStart = frameN  # exact frame index
        ESCALA_EXPECTATIVA_PDS_1.tStart = t  # local t and not account for scr refresh
        ESCALA_EXPECTATIVA_PDS_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ESCALA_EXPECTATIVA_PDS_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ESCALA_EXPECTATIVA_PDS_1.started')
        ESCALA_EXPECTATIVA_PDS_1.setAutoDraw(True)
    if ESCALA_EXPECTATIVA_PDS_1.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 4-frameTolerance:
            # keep track of stop time/frame for later
            ESCALA_EXPECTATIVA_PDS_1.tStop = t  # not accounting for scr refresh
            ESCALA_EXPECTATIVA_PDS_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ESCALA_EXPECTATIVA_PDS_1.stopped')
            ESCALA_EXPECTATIVA_PDS_1.setAutoDraw(False)
    
    # *eiiiiiii* updates
    if eiiiiiii.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
        # keep track of start time/frame for later
        eiiiiiii.frameNStart = frameN  # exact frame index
        eiiiiiii.tStart = t  # local t and not account for scr refresh
        eiiiiiii.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eiiiiiii, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'eiiiiiii.started')
        eiiiiiii.setAutoDraw(True)
    if eiiiiiii.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > eiiiiiii.tStartRefresh + 0.7-frameTolerance:
            # keep track of stop time/frame for later
            eiiiiiii.tStop = t  # not accounting for scr refresh
            eiiiiiii.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'eiiiiiii.stopped')
            eiiiiiii.setAutoDraw(False)
    # start/stop eiiiiisonido
    if eiiiiisonido.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
        # keep track of start time/frame for later
        eiiiiisonido.frameNStart = frameN  # exact frame index
        eiiiiisonido.tStart = t  # local t and not account for scr refresh
        eiiiiisonido.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('eiiiiisonido.started', tThisFlipGlobal)
        eiiiiisonido.play(when=win)  # sync with win flip
    if eiiiiisonido.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > eiiiiisonido.tStartRefresh + 0.7-frameTolerance:
            # keep track of stop time/frame for later
            eiiiiisonido.tStop = t  # not accounting for scr refresh
            eiiiiisonido.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'eiiiiisonido.stopped')
            eiiiiisonido.stop()
    
    # *cruz_de_fijacion* updates
    if cruz_de_fijacion.status == NOT_STARTED and slider.rating:
        # keep track of start time/frame for later
        cruz_de_fijacion.frameNStart = frameN  # exact frame index
        cruz_de_fijacion.tStart = t  # local t and not account for scr refresh
        cruz_de_fijacion.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cruz_de_fijacion, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cruz_de_fijacion.started')
        cruz_de_fijacion.setAutoDraw(True)
    if cruz_de_fijacion.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cruz_de_fijacion.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            cruz_de_fijacion.tStop = t  # not accounting for scr refresh
            cruz_de_fijacion.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cruz_de_fijacion.stopped')
            cruz_de_fijacion.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICIONComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICION" ---
for thisComponent in ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICIONComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ESCALA_EXPECTATIVA_PDS_1.response', ESCALA_EXPECTATIVA_PDS_1.getRating())
thisExp.addData('ESCALA_EXPECTATIVA_PDS_1.rt', ESCALA_EXPECTATIVA_PDS_1.getRT())
eiiiiisonido.stop()  # ensure sound has stopped at end of routine
# the Routine "ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICION" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "ESTIMULO_COMPUESTO_INHIBIDOR" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
slider.reset()
# keep track of which components have finished
ESTIMULO_COMPUESTO_INHIBIDORComponents = [text_2, jeje, jiji, slider, polygon]
for thisComponent in ESTIMULO_COMPUESTO_INHIBIDORComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ESTIMULO_COMPUESTO_INHIBIDOR" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.stopped')
            text_2.setAutoDraw(False)
    
    # *jeje* updates
    if jeje.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        jeje.frameNStart = frameN  # exact frame index
        jeje.tStart = t  # local t and not account for scr refresh
        jeje.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(jeje, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'jeje.started')
        jeje.setAutoDraw(True)
    if jeje.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > jeje.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            jeje.tStop = t  # not accounting for scr refresh
            jeje.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'jeje.stopped')
            jeje.setAutoDraw(False)
    
    # *jiji* updates
    if jiji.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        jiji.frameNStart = frameN  # exact frame index
        jiji.tStart = t  # local t and not account for scr refresh
        jiji.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(jiji, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'jiji.started')
        jiji.setAutoDraw(True)
    if jiji.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > jiji.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            jiji.tStop = t  # not accounting for scr refresh
            jiji.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'jiji.stopped')
            jiji.setAutoDraw(False)
    
    # *slider* updates
    if slider.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        slider.frameNStart = frameN  # exact frame index
        slider.tStart = t  # local t and not account for scr refresh
        slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'slider.started')
        slider.setAutoDraw(True)
    if slider.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            slider.tStop = t  # not accounting for scr refresh
            slider.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider.stopped')
            slider.setAutoDraw(False)
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and slider.rating:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'polygon.started')
        polygon.setAutoDraw(True)
    if polygon.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            polygon.tStop = t  # not accounting for scr refresh
            polygon.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon.stopped')
            polygon.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ESTIMULO_COMPUESTO_INHIBIDORComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ESTIMULO_COMPUESTO_INHIBIDOR" ---
for thisComponent in ESTIMULO_COMPUESTO_INHIBIDORComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider.response', slider.getRating())
thisExp.addData('slider.rt', slider.getRT())
# the Routine "ESTIMULO_COMPUESTO_INHIBIDOR" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "ESTIMULO_COMPUESTO_NEUTRO" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
slider_2.reset()
# keep track of which components have finished
ESTIMULO_COMPUESTO_NEUTROComponents = [text_3, jojo, juju, slider_2, polygon_2]
for thisComponent in ESTIMULO_COMPUESTO_NEUTROComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ESTIMULO_COMPUESTO_NEUTRO" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.stopped')
            text_3.setAutoDraw(False)
    
    # *jojo* updates
    if jojo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        jojo.frameNStart = frameN  # exact frame index
        jojo.tStart = t  # local t and not account for scr refresh
        jojo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(jojo, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'jojo.started')
        jojo.setAutoDraw(True)
    if jojo.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > jojo.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            jojo.tStop = t  # not accounting for scr refresh
            jojo.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'jojo.stopped')
            jojo.setAutoDraw(False)
    
    # *juju* updates
    if juju.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        juju.frameNStart = frameN  # exact frame index
        juju.tStart = t  # local t and not account for scr refresh
        juju.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(juju, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'juju.started')
        juju.setAutoDraw(True)
    if juju.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 4-frameTolerance:
            # keep track of stop time/frame for later
            juju.tStop = t  # not accounting for scr refresh
            juju.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'juju.stopped')
            juju.setAutoDraw(False)
    
    # *slider_2* updates
    if slider_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        slider_2.frameNStart = frameN  # exact frame index
        slider_2.tStart = t  # local t and not account for scr refresh
        slider_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'slider_2.started')
        slider_2.setAutoDraw(True)
    if slider_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider_2.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            slider_2.tStop = t  # not accounting for scr refresh
            slider_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_2.stopped')
            slider_2.setAutoDraw(False)
    
    # *polygon_2* updates
    if polygon_2.status == NOT_STARTED and slider.rating:
        # keep track of start time/frame for later
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.tStart = t  # local t and not account for scr refresh
        polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'polygon_2.started')
        polygon_2.setAutoDraw(True)
    if polygon_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_2.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            polygon_2.tStop = t  # not accounting for scr refresh
            polygon_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_2.stopped')
            polygon_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ESTIMULO_COMPUESTO_NEUTROComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ESTIMULO_COMPUESTO_NEUTRO" ---
for thisComponent in ESTIMULO_COMPUESTO_NEUTROComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider_2.response', slider_2.getRating())
thisExp.addData('slider_2.rt', slider_2.getRT())
# the Routine "ESTIMULO_COMPUESTO_NEUTRO" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "ESTIMULO_EXCITATORIO_PDS_ADQUISICION" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
slider_3.reset()
ei.setImage(EI_FOTO)
eisonido.setSound(EI_SONIDO, secs=0.7, hamming=True)
eisonido.setVolume(1.0, log=False)
# keep track of which components have finished
ESTIMULO_EXCITATORIO_PDS_ADQUISICIONComponents = [text_4, joasjoas, slider_3, ei, eisonido, polygon_3]
for thisComponent in ESTIMULO_EXCITATORIO_PDS_ADQUISICIONComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ESTIMULO_EXCITATORIO_PDS_ADQUISICION" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_4.started')
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.stopped')
            text_4.setAutoDraw(False)
    
    # *joasjoas* updates
    if joasjoas.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        joasjoas.frameNStart = frameN  # exact frame index
        joasjoas.tStart = t  # local t and not account for scr refresh
        joasjoas.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(joasjoas, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'joasjoas.started')
        joasjoas.setAutoDraw(True)
    if joasjoas.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > joasjoas.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            joasjoas.tStop = t  # not accounting for scr refresh
            joasjoas.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'joasjoas.stopped')
            joasjoas.setAutoDraw(False)
    
    # *slider_3* updates
    if slider_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        slider_3.frameNStart = frameN  # exact frame index
        slider_3.tStart = t  # local t and not account for scr refresh
        slider_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'slider_3.started')
        slider_3.setAutoDraw(True)
    if slider_3.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 4-frameTolerance:
            # keep track of stop time/frame for later
            slider_3.tStop = t  # not accounting for scr refresh
            slider_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_3.stopped')
            slider_3.setAutoDraw(False)
    
    # *ei* updates
    if ei.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
        # keep track of start time/frame for later
        ei.frameNStart = frameN  # exact frame index
        ei.tStart = t  # local t and not account for scr refresh
        ei.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ei, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ei.started')
        ei.setAutoDraw(True)
    if ei.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ei.tStartRefresh + 0.7-frameTolerance:
            # keep track of stop time/frame for later
            ei.tStop = t  # not accounting for scr refresh
            ei.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ei.stopped')
            ei.setAutoDraw(False)
    # start/stop eisonido
    if eisonido.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
        # keep track of start time/frame for later
        eisonido.frameNStart = frameN  # exact frame index
        eisonido.tStart = t  # local t and not account for scr refresh
        eisonido.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('eisonido.started', tThisFlipGlobal)
        eisonido.play(when=win)  # sync with win flip
    if eisonido.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > eisonido.tStartRefresh + 0.7-frameTolerance:
            # keep track of stop time/frame for later
            eisonido.tStop = t  # not accounting for scr refresh
            eisonido.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'eisonido.stopped')
            eisonido.stop()
    
    # *polygon_3* updates
    if polygon_3.status == NOT_STARTED and slider.rating:
        # keep track of start time/frame for later
        polygon_3.frameNStart = frameN  # exact frame index
        polygon_3.tStart = t  # local t and not account for scr refresh
        polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'polygon_3.started')
        polygon_3.setAutoDraw(True)
    if polygon_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_3.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            polygon_3.tStop = t  # not accounting for scr refresh
            polygon_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_3.stopped')
            polygon_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ESTIMULO_EXCITATORIO_PDS_ADQUISICIONComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ESTIMULO_EXCITATORIO_PDS_ADQUISICION" ---
for thisComponent in ESTIMULO_EXCITATORIO_PDS_ADQUISICIONComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider_3.response', slider_3.getRating())
thisExp.addData('slider_3.rt', slider_3.getRT())
eisonido.stop()  # ensure sound has stopped at end of routine
# the Routine "ESTIMULO_EXCITATORIO_PDS_ADQUISICION" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
