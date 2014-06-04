#!/usr/bin/env python

import serial
import threading
from arduino.arduino_alive_thread import *

"""/!\ arduino_alive_thread launch at the end of output, make sure to launch it otherwose the arduino will keep stopping"""

class arduino_mega(object):

    __OUTPUT_PINS = -1

    def __init__(self, port, a_com_arduino, baudrate=115200):
        self.serial = serial.Serial(port, baudrate)
        self.serial.write(bytearray('99','utf-8'))
        
        self.com_arduino = a_com_arduino
        """to secure the access to the arduino to only one person at the same time"""
        self.lock = threading.Lock()
 

    def __str__(self):
        return "Arduino is on port %s at %d baudrate" %(self.serial.port, self.serial.baudrate)

    def output(self, pinArray):
        """ask access to the arduino"""
        self.lock.acquire()
        
        self.__sendData(len(pinArray))

        if(isinstance(pinArray, list) or isinstance(pinArray, tuple)):
            self.__OUTPUT_PINS = pinArray
            for each_pin in pinArray:
                self.__sendData(each_pin)
                
        """release access to the arduino"""
        self.lock.release()
        
        """after having set the output, launch arduin_alive_thread"""
        self.arduino_alive_thread = arduino_alive_thread(self) 
        
        return True

    def setLow(self, pin):
        """ask access to the arduino"""
        self.lock.acquire()
        
        self.__sendData('0')
        self.__sendData(pin)
        
        """release access to the arduino"""
        self.lock.release()
        return True

    def setHigh(self, pin):
        """ask access to the arduino"""
        self.lock.acquire()
        
        self.__sendData('1')
        self.__sendData(pin)
        
        """release access to the arduino"""
        self.lock.release()
        return True

    def getState(self, pin):
        """ask access to the arduino"""
        self.lock.acquire()
        
        self.__sendData('2')
        self.__sendData(pin)
        
        value = self.__formatPinState(self.__getData()[0])
        
        """release access to the arduino"""
        self.lock.release()
        
        return value

    def analogWrite(self, pin, value):
        """ask access to the arduino"""
        self.lock.acquire()
        
        self.__sendData('3')
        self.__sendData(pin)
        self.__sendData(value)
        
        """release access to the arduino"""
        self.lock.release()
        return True

    def analogRead(self, pin):
        """ask access to the arduino"""
        self.lock.acquire()
        
        self.__sendData('4')
        self.__sendData(pin)
        
        value = self.__getData()
        
        """release access to the arduino"""
        self.lock.release()
        return value

    def turnOff(self):
        """ask access to the arduino"""
        self.lock.acquire()
        
        for each_pin in self.__OUTPUT_PINS:
            self.setLow(each_pin)
        
        """release access to the arduino"""
        self.lock.release()
        return True
    
    """signal to send every 5 sec to inform the arduino that life_controller is alive, otherwise, the rduino set all his pin to false"""
    def alive(self):
        self.lock.acquire()
        self.__sendData('5')
        self.lock.release()
        

    def __sendData(self, serial_data):
        while(self.__getData()[0] != "w"):
            pass
        self.serial.write(bytearray(str(serial_data),"utf-8"))

    def __getData(self):
        return self.serial.readline().strip().decode("utf-8")

    def __formatPinState(self, pinValue):
        if pinValue == '1':
            return True
        else:
            return False

    def close(self):
        """ask access to the arduino"""
        self.lock.acquire()
        
        self.serial.close()
        
        """release access to the arduino"""
        self.lock.release()
        return True
