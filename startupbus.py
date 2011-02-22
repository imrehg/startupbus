#!/usr/bin/env python
import random

## Constans for roles
DEV_ROLE = 0
UX_ROLE = 1
PR_ROLE = 2
OTHER_ROLE = 3

class Bus:
    """ On if the many StartubBusses """

    def __init__(self, origin):
        self.origin = origin
        self.passlist = []

    def addPassenger(self, passenger):
        self.passlist += [passenger]

    def isOnTheBus(self, passenger):
        return passenger in self.passlist


class SFBus(Bus):
    """ The San Francisco -> Austin bus """

    def __init__(self):
        Bus.__init__(self, 'San Francisco')


class NYBus(Bus):
    """ The New York -> Austin bus """

    def __init__(self):
        Bus.__init__(self, 'New York')

class CHBus(Bus):
    """ The Chicago -> Austin bus """

    def __init__(self):
        Bus.__init__(self, 'Chicago')

class CLBus(Bus):
    """ The Cleveland -> Austin bus """

    def __init__(self):
        Bus.__init__(self, 'Cleveland')

class MIBus(Bus):
    """ Miami -> Austin bus """

    def __init__(self):
        Bus.__init__(self, 'Miami')


def deliberate(bus, passenger):
    """ Find out who travels """

    # There has to be a method but for me it looks like
    # this, even if I might be generous with 1% chance
    if random.random() < 0.01:
        bus.addPassenger(passenger)

