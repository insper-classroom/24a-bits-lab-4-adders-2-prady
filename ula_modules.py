#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():

        soma.next = ((not a) and b) or (a and (not b))
        carry.next = a and b


    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]

    # s1 = Signal(bool(0))
    # s2 = Signal(bool(0))
    # s3 = Signal(bool(0))

    half_1 = halfAdder(a, b, s[1], s[2])
    half_2 = halfAdder(c, s[1], soma, s[3])

    @always_comb
    def comb():
        carry.next = s[2] or s[3]

    return instances()


@block
def adder2bits(x, y, soma, carry):
    return instances()


@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        pass

    return instances()
