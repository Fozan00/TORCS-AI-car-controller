
import msgParser
from pynput.keyboard import Key, Listener
from threading import Thread
import carState
import carControl
import keyboard
import numpy as np
import pandas as pd
import scikeras
from scikeras.wrappers import KerasRegressor
import tensorflow as tf
import pprint
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
import reading_data

from keras.models import load_model
loaded_model = load_model('./new_model.h5')

class Driver(object):
    '''
    A driver object for the SCRC
    '''

    def __init__(self, stage):
        '''Constructor'''
        self.WARM_UP = 0
        self.QUALIFYING = 1
        self.RACE = 2
        self.UNKNOWN = 3
        self.stage = stage
        print("-------stage : ", stage)
        
        self.parser = msgParser.MsgParser()
        self.move = 0
        self.state = carState.CarState()
        
        self.control = carControl.CarControl()
        self.steer_lock = 0.785398
        self.var = None
        self.val =None
        self.max_speed = 150
        self.count = 0
        self.prev_rpm = None
        self.prev_speed = None

    def init(self):
        '''Return init string with rangefinder angles'''
        self.angles = [0 for x in range(19)]

        for i in range(5):
            self.angles[i] = -90 + i * 15
            self.angles[18 - i] = 90 - i * 15
        
        for i in range(5, 9):
            self.angles[i] = -20 + (i-5) * 5
            self.angles[18 - i] = 20 - (i-5) * 5
        
        return self.parser.stringify({'init': self.angles})
    
    def drive(self, msg):
        self.state.setFromMsg(msg)
        move = self.control.getSteer()
        sensors_data = self.state.sensors
        if move > 0:
            move -= 0.01
        elif move < 0:
            move += 0.01
        self.steer(sensors_data)
        self.gear()
        # self.speed()
        self.control.setSteer(move)
        return self.control.toMsg()
    
    def steer(self, dict_1):
        self.val = []
        self.val.append(float(dict_1['angle'][0]))
        self.val.append(float(dict_1['curLapTime'][0]))
        self.val.append(float(dict_1['damage'][0]))
        self.val.append(float(dict_1['distFromStart'][0]))
        self.val.append(float(dict_1['distRaced'][0]))
        self.val.append(float(dict_1['fuel'][0]))
        self.val.append(float(dict_1['gear'][0]))
        self.val.append(float(dict_1['lastLapTime'][0]))
        self.val.append(float(dict_1['racePos'][0]))
        self.val.append(float(dict_1['rpm'][0]))
        self.val.append(float(dict_1['speedX'][0]))
        self.val.append(float(dict_1['speedY'][0]))
        self.val.append(float(dict_1['speedZ'][0]))
        tracks = dict_1['track']
        for t in range(len(tracks)):
            tracks[t] = float(tracks[t])
        self.val.extend(tracks)
        self.val.append(float(dict_1['trackPos'][0]))
        self.val.append(float(dict_1['wheelSpinVel'][0]))
        self.val.append(float(dict_1['wheelSpinVel'][1]))
        self.val.append(float(dict_1['wheelSpinVel'][2]))
        self.val.append(float(dict_1['wheelSpinVel'][3]))
        list_1 = self.val
        if self.count > 15:
            self.count = 0
            thread_1 = Thread(target=self.calc_steer, args=[list_1])
            thread_1.start()
        self.count += 1

    def calc_steer(self, list_1):
        speed = self.state.getSpeedX()
        var = loaded_model.predict([list_1])
        acc = var[0][0]
        # if acc > 0.2:
        #     if speed < self.max_speed:
        #         acc = 0.8
        #     else:
        #         acc = 0
        # else:
        #     acc = 0


        acc *= 0.75
        if acc > 0.8:
            acc = 0.8
        move = var[0][2]
        stop = var[0][1]
        if stop < 0.5:
            stop = 0
        else:
            stop = 0.5

        self.control.setSteer(move)
        self.control.setAccel(acc)
        self.control.setBrake(stop)

    def gear(self):
        rpm = self.state.getRpm()
        gear = self.state.getGear()
        speed = self.state.getSpeedX()
        if self.prev_rpm is None:
            up = True
        else:
            if (self.prev_rpm - rpm) < 0:
                up = True
            else:
                up = False

        if not up and rpm < 3000:
            if gear > 1:
                gear -= 1

        if self.prev_speed is None:
            self.prev_speed = 0
        speed_down = False
        if speed - self.prev_speed <= 0:
            speed_down = True
        if speed_down and speed < 35:
            gear = 1
        elif speed_down and speed < 70:
            gear = 2
        elif speed_down and speed < 110:
            gear = 3
        elif speed_down and speed < 135:
            gear = 4
        elif up and rpm > 7000:
            if gear < 5:
                gear += 1

        if keyboard.is_pressed('r'):
            gear = -1

        self.prev_speed = speed
        self.control.setGear(gear)
    
    def speed(self):
        speed = self.state.getSpeedX()
        accel = self.control.getAccel()

        if speed < self.max_speed:
            # if keyboard.is_pressed('w'):
            accel += 0.2
            if accel > 0.8:
                accel = 0.8
        else:
            accel -= 0.1
            if accel < 0:
                accel = 0.0
        if keyboard.is_pressed('s'):
            accel -= 0.3
        self.control.setAccel(accel)

    def onShutDown(self):
        pass
    
    def onRestart(self):
        pass

