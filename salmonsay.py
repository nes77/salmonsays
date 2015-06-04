#!/usr/bin/python2.7

from __future__ import print_function
__author__ = 'nsamson'

import textwrap
import string
import fileinput

fish = """
                                          `-::
                      ``````          .:+sysss:                            oy`
         ``.-:://++ossssyyhyyyyyssoosydyyysssss/                          -hh+
   `.:/++o+/++//////++//+oo+ososyyhhdddddddhhyys+.                       .yhhs
  `/+ooo++o::/:-:/::::/:::+::/++/+oososyyyhdddddy+.`                    `syyho
  ::-//////:++/-:-::/:/:---::-:/://+/+++ssssyhhhhhdhy+/-.`              +yyyh:
   ``.-::://+////:::://::::--:/--::/://///+ooossssssyhhdhyo:-`        .+yyoos`
       ``.-----:---:-::::::::::::::::::::::::/++++++++oossyhdhyo/-.`-+yysooo`
            `+ooo+/:------------::::::::::::::::::::/++//++++ossyyyyddmddh/`
             .o:++//.`.............-.---::::///:::/:/:://////+////o+syyy+.
                `:::      ```.....---------------::://///:::/::://////-`
                  .`              ```.-/:///::-.-----:::::::::::://-`
                                       .s+syso+:    ```` `/sssssss:
                                         ``/sooo           oyyso:`
                                            .oo+            -/-`
                                              ``
"""

if __name__ == "__main__":

    hyphens = "-"*80 + "\n"

    for arg in fileinput.input():
        formatted_text = hyphens

        just_test = []
        for elem in textwrap.wrap(arg, width=76):
            just_test.append(string.ljust(elem, 77))

        final_text = ["| " + elem + "|\n" for elem in just_test]

        formatted_text += "".join(final_text)
        formatted_text += hyphens

        print(formatted_text)
        print(fish)