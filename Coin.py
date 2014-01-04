"""
    Create a class that simulates a coin for a coin toss.
    Copyright (C) 2013  Benny Mei
    meibenny@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


#import random module to determine state of coin toss
import random

class Coin(object):
    "This class simulates a coin for a coin toss"""

#-- Class Variables ---------------------------------
    STATUS = ["Heads",
              "Tails"]

#-- Constructor -------------------------------------
    def __init__(self):
        """Creates the coin class"""
        
        #set variable to keep track of random number
        self.__rnumber = "Not yet flipped"

        #set variable to status to track if coin is heads or tails
        self.__status = "Not yet flipped"

        #set variable to track of status number (number used to determine flip)
        self.__flipNum = "Not yet flipped"

#-- Accessors ----------------------------------------
    def getStatus(self):
        """Returns status of coin."""
        return self.__status

    def getStatusNumber(self):
        """Returns the number used to determine coin flip"""
        return self.__flipNum

    def getNumber(self):
        """Returns the randomly generated number used for the coin toss"""
        return self.__rnumber

#-- Mutators -----------------------------------------
    def setRNumber(self):
        """Sets random number used to generate coin coss. The lower bound is
        0, the upperbound is the number of bits in 2 kilobytes"""
        self.__rnumber = random.randint(0,16384)

    def flipCoin(self):
        """Simulates a coin flip."""
        #write instructions to randomly generate number
        Coin.setRNumber(self)
        
        
        #set flipNum to randomly generated number
        flipNum = self.__rnumber

        #determine if statusNum is even or odd
        statusNum = flipNum % 2
        self.__flipNum = statusNum
        if statusNum == 0:
            self.__status = Coin.STATUS[0]
        else:
            self.__status = Coin.STATUS[1]
            
        
        
        


        
