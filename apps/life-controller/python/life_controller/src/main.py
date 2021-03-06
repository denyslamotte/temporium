'''
Created on 9 mai 2014

@author: ensadlab

'''
from GUI.window import *
from current_state import *
from com_arduino import *
from communication.TCP.server import *
from BRBU_controller import *
from seance_controller import *
from BRBU_controller import *
from security_EL import *
from config_manager import *
from current_state_order import *
from aquarium_controller import *
import sys

if __name__ == "__main__":
    """test must be set to False when using with terminal mode"""
    test = False
    for i in sys.argv : 
        if i.strip() == "test" : 
            test = True
    
    co_ard = com_arduino(test)
    cu_state = current_state(co_ard)
    co_ard.set_current_state(cu_state)
    co_ard.__readPin__()
    le_server = server('',8000,cu_state)
    BRBU_cont = BRBU_controller(cu_state)
    seance_cont = seance_controller(cu_state)
    aq_controller = aquarium_controller(cu_state)
    config_m = config_manager(cu_state)
    
    cu_state.set_seance_controller(seance_cont)
    cu_state.set_config_manager(config_m)
    cu_state.set_BRBU_controller(BRBU_cont)
    cu_state.set_server(le_server)
    cu_state.set_aquarium_controller(aq_controller)
    
    

    le_server.start()
    BRBU_cont.start()
    s = security_EL(cu_state)
    cu_state.set_security_EL(s)
    
    """will be an option later"""
    GUI = True
    if GUI : 
        current_state_o = current_state_order(cu_state)
        w = window(None, cu_state,current_state_o )
        cu_state.set_windows(w)
        w.title("Temporium : Beta")
        w.mainloop()

    