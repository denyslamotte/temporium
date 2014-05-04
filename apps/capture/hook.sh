#!/bin/bash
#
# waits the camera actions and send OSC orders depending on state
# 
# @author Benoît VERJAT
# @since  01.02.2014
# 

self=`basename $0`

case "$ACTION" in
    init)

        ;;
    start)
        echo "$self: START"
        python $(dirname $0)/osc/sender.py 127.0.0.1 4242 flash
        ;;
    download)
        python $(dirname $0)/osc/sender.py 127.0.0.1 4242 expose
        echo "$self: DOWNLOAD to $ARGUMENT" 
        ;;
    stop)
        echo "$self: STOP"
        ;;
    *)
        echo "$self: Unknown action: $ACTION"
        ;;
esac

exit 0