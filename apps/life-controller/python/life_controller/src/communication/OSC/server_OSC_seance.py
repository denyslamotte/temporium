'''
Created on 10 mai 2014

@author: ensadlab
'''
import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server
import threading
class server_OSC_seance(threading.Thread):
    '''
    classdocs
    '''
    

    def __init__(self, un_seance_controller, ip, port):
        '''
        init the dispatcher : what to do dpending on the pattern 
        '''
        
        threading.Thread.__init__(self)
        
        self.seance_controller = un_seance_controller
        
        self.ip = ip 
        self.port= port
        
        self.dispatcher = dispatcher.Dispatcher()
        self.dispatcher.map("/debug", print)
        
        
        self.dispatcher.map("/seance_end", self._seance_end)
        self.dispatcher.map("/action", self._action)
        
        """not used"""
        self.dispatcher.map("/first_photo", self.start_formation_rate) 

        self.server = osc_server.ThreadingOSCUDPServer((self.ip, self.port), self.dispatcher)
        
        self.start()
        
        
    
    def _seance_end(self, msg):
        """what to do when finished"""
        
        self.seance_controller.current_state.set_current_film_state("film",False)
        print(msg)
        
    
    def _action(self, order):
        """what to do when action asked"""
        print(order)
    
    def run(self):
        """start teh server in a thread"""
        print("Serving on {}".format(self.server.server_address))
        self.server.serve_forever()
    
    """not used"""
    def start_formation_rate(self, msg):
        print ("first_photo received")
        """strat the thread : ask to analyse photo"""
        """self.seance_controller.start()"""