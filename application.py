#!/usr/bin/env python
"""
StartupBus application
"""
import startupbus as sb

class Greg:
    """ Just me """

    def __init__(self):
        """ Get that party started """
        self.enthusiasm = True
        self.happy = None
        self.role = sb.DEV_ROLE

    def StartHackingLikeCrazy(self):
        """ Well, of course """
        print("Now get to work...")

    def StartHackingLikeCrazyToGetOnBusNextTime(self):
        """ Too awesome not to """
        print("Well, there are a lot of awesome devs out there.")
        self.StartHackingLikeCrazy()

if __name__ == "__main__":
    me = Greg()

    buses = [sb.SFBus(), sb.NYBus()]
    for bus in buses:
        sb.deliberate(bus, me)

    for bus in buses:
        if bus.isOnTheBus(me):
            me.happy = True
            print("Yeah, I'm on the %s StartupBus!" %(bus.origin))
            break

    if me.happy is True:
        me.StartHackingLikeCrazy()
    else:
        me.StartHackingLikeCrazyToGetOnBusNextTime()
