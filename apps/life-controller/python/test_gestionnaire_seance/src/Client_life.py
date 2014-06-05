import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__": # Permet de rentrer dans la boucle seulement si le script est execute tout seul (alors __name__ = "__main__", __name__ est automatiquement cree par python)
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
    help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=3334,
    help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.UDPClient(args.ip, args.port)

    while True : 
        a = input("msg to send : 1 = first photo, 2 = film end, 3 = quit : \n")
        if a =="1" : 
            msg = osc_message_builder.OscMessageBuilder(address = "/first_photo")
            msg.add_arg(1)
            msg = msg.build()
            client.send(msg)
        if a =="2" : 
            msg = osc_message_builder.OscMessageBuilder(address = "/seance_end")
            msg.add_arg(1)
            msg = msg.build()
            client.send(msg) 
        if a =="3" : 
            break
        if a =="4" : 
            msg = osc_message_builder.OscMessageBuilder(address = "/debug")
            msg.add_arg(1)
            msg = msg.build()
            client.send(msg) 
    print ("End client_seance_simu")