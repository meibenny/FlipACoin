"""
    Create a GUI for the Coin Class
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

from Coin import *
import random
from tkinter import *

class coinGUI:
    """This class creates a GUI for the Coin Object"""

#-- Constructor ---------------------------------------------------------
    def __init__(self):
        
        #create coin object
        self.__coin = Coin()

        #create instance of Tk()
        self.__root = Tk()

        #change title of window
        self.__root.title("FlipACoin")

        #change Tk background color
        #self.__root.configure(background = "red")

        #create flip button
        self.__flipButton = Button(self.__root, text = "Flip", command =\
                                   self.flipCoin)
        self.__flipButton.grid(row = 3, column = 2)

        #change flip button color
        #self.__flipButton.configure(background = "red")

        #create header for flip label
        self.__flipHeader = Label(self.__root, text = "Outcome", width = 10)
        self.__flipHeader.grid(row = 1, column = 1)

        #change header for flip label color
        #self.__flipHeader.configure(background = "red")

        #create label to display heads or tails
        self.__flipLabelText = self.__coin.getStatus()
        self.__flipLabelVar = StringVar()
        self.__flipLabelVar.set(self.__flipLabelText)
        self.__flipLabel = Label(self.__root, textvariable = self.__flipLabelVar,\
                          width = 20)
        self.__flipLabel.grid(row = 1, column = 3)

        #change label color
        #self.__flipLabel.configure(background = "red")

    #create label to display randomly generated number

        #create header for random number display
        self.__ranNumHeader = Label(self.__root, text = "Random Num Used", width = 20)
        self.__ranNumHeader.grid(row = 2, column = 1)

        #change header for random number display color
        #self.__ranNumHeader.configure(background = "red")

        #create label to display random number
        self.__ranNumText = self.__coin.getNumber()
        self.__ranNumVar = StringVar()
        self.__ranNumVar.set(self.__ranNumText)
        self.__ranNumLabel = Label(self.__root, textvariable = self.__ranNumVar, \
                                   width = 20)
        self.__ranNumLabel.grid(row = 2, column = 3)

        #change label to display random number color
        #self.__ranNumLabel.configure(background = "red")
        
        #initialize GUI
        mainloop()

    #define function to flip coin
    def flipCoin(self):
        self.__coin.flipCoin()
        self.__flipLabelVar.set(self.__coin.getStatus())
        self.__ranNumVar.set(self.__coin.getNumber())
        
        

coinGUI()
