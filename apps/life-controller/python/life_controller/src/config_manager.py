'''
Created on Jun 2, 2014

@author: Cactus
'''

import threading
from communication.OSC.server_OSC_config_manager import *

class config_manager(object):
    '''
    object which gather all values for cycle like time of emptying ... etc.
    '''


    def __init__(self, a_current_state):
        '''
        value are stored in dictionnary
        '''
        self.current_state = a_current_state
        
        """lock to prevent from reading a value and upload the value at the same time"""
        
        self.lock = threading.Lock()
        
        """Value of configuration"""
        self._renew_light_AQ_value = {"TIME" :0}
        self._auto_AQ_filtration_value = {"TIME" :0 }
        self._BRBU_controller_value = {"BR_FULL" :0,\
                                       "BU_FULL" :0,\
                                       "BU_EMPTY" :0,\
                                       "FILLING_BR_BU" :0,\
                                       }
        
        
        
        """read the config at first"""
        self.read_config()
        
        """start the server who will listen if config need to be read"""
        self.server_OSC_config_manager = server_OSC_config_manager(self, 'localhost', 8005 )
    
    def read_config(self):
        """take the lock to make impossible reading and writing the values at the same time"""
        self.lock.acquire()
        
        file = open("config/config_real_time.txt","r")
        
        for ligne in file : 
            
            """Take out the end symbols (\n)"""
            ligne = ligne.strip()
            """split on  ':' """
            list = ligne.split(":")
            
            key = list[0].strip()
            """if renew_light_AQ is yes, then set auto_start to True"""
            if key  == "renew_light_AQ" :
                name = list[1].strip()
                value = float(list[2].strip())
                self._set_renew_light_AQ(name, value)
             
            elif key  == "auto_AQ_filtration" :
                name = list[1].strip()
                value = float(list[2].strip())
                self._set_auto_AQ_filtration(name, value)
            
            elif key  == "BRBU_controller" :
                name = list[1].strip()
                value = float(list[2].strip())
                self._set_BRBU_controller(name, value)   
        
        """release the lock to enable access to the value"""
        self.lock.release()
                
    """RENEW LIGHT AQ"""           
    def _set_renew_light_AQ(self, name, value):
        self._renew_light_AQ_value[name] = value      
     
    
    """return the value corresponding to the name you asked : ex "TIME" here""" 
    def get_renew_light_AQ(self, name):
        self.lock.acquire()
        value = self._renew_light_AQ_value[name]      
        self.lock.release()
        return value
    
    """AUTO FILTRATION AQ"""
    def _set_auto_AQ_filtration(self, name, value):
        self._auto_AQ_filtration_value[name] = value      
        
    
    """return the value corresponding to the name you asked : ex "TIME" here""" 
    def get_auto_AQ_filtration(self, name):
        self.lock.acquire()
        value = self._auto_AQ_filtration_value[name]      
        self.lock.release()
        return value      
    
    """BRBU CONTROLLER"""
    def _set_BRBU_controller(self, name, value):
        
        self._BRBU_controller_value[name] = value      
    
    
    """return the value corresponding to the name you asked : ex "BU_FULL" here""" 
    def get_BRBU_controller(self, name):
        self.lock.acquire()
        value = self._BRBU_controller_value[name]    
        self.lock.release()
        return value      
                