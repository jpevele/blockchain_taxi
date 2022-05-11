#!/usr/bin/env python3

# Filename: pycalc.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""PyCalc is a simple calculator built using Python and PyQt5."""

import sys

from functools import partial

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDateTimeEdit
from PyQt5.QtWidgets import QDateEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
import datetime
from PyQt5.QtGui import QFont
from datetime import datetime

__version__ = "0.1"
__author__ = "Leodanis Pozo Ramos"

ERROR_MSG = "ERROR"


# Create a subclass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QMainWindow):
    """PyCalc's View (GUI)."""

    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle("Tec Community Peer to Peer Ridesharing")
        self.setFixedSize(550,650)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons

        
        """Create the display.
        # Create the display widget
        self.display = QLineEdit()
        # Set some display's properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)
        """

        self.driverTitle = QVBoxLayout()
        self.sendRideOfferText=QLabel('Send ride offfer:')
        self.sendRideOfferText.setFont(QFont('Arial',20))
        self.driverTitle.addWidget(self.sendRideOfferText)
        self.generalLayout.addLayout(self.driverTitle)

        #Create the buttons.
        driverLayout = QGridLayout()

        self.locations=QComboBox()
        self.locations.addItems(["Coyoacan","Tlalpan","BenitoJuarez","Tlahuac","Iztapalapa"])
        self.positions=QComboBox()
        self.positions.addItems(["1","2","3","4","5"])
        
        self.dateTime = QDateTimeEdit(QDateTime(datetime.now().year,datetime.now().month,datetime.now().day,datetime.now().hour,datetime.now().minute))

        self.priceText=QLabel('Price:')
        self.priceText.setFont(QFont('Arial',15))
        self.locationText=QLabel('Location:')
        self.locationText.setFont(QFont('Arial',15))
        self.positionsText=QLabel('Positions:')
        self.positionsText.setFont(QFont('Arial',15))
        self.dateAndTimeText=QLabel('Date and Time:')
        self.dateAndTimeText.setFont(QFont('Arial',15))
        self.durationText=QLabel('Duration(Minutes):')
        self.durationText.setFont(QFont('Arial',15))

        self.priceEdit=QLineEdit("")
        self.durationEdit=QLineEdit("")
        
        driverLayout.addWidget(self.priceText, 0, 0)
        driverLayout.addWidget(self.priceEdit, 0, 1)
        driverLayout.addWidget(self.locationText, 0, 2)
        driverLayout.addWidget(self.locations, 0, 3)
        driverLayout.addWidget(self.positionsText, 1, 0)
        driverLayout.addWidget(self.positions, 1, 1)
        #driverLayout.addWidget(QLabel("Price:"), 1, 2)
        #driverLayout.addWidget(QLineEdit(""), 1, 3)
        driverLayout.addWidget(self.dateAndTimeText, 2, 0)
        driverLayout.addWidget(self.dateTime, 2, 1)
        driverLayout.addWidget(self.durationText, 2, 2)
        driverLayout.addWidget(self.durationEdit, 2, 3)
        
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(driverLayout)

        self.ridePub = QVBoxLayout()
        self.ridePubBttn=QPushButton("Publish ride offer!")
        self.ridePubBttn.setFont(QFont('Arial',15))
        self.ridePubBttn.clicked.connect(self.ridePubFunc)
        self.ridePub.addWidget(self.ridePubBttn)
        self.generalLayout.addLayout(self.ridePub)

########################Bids offers#########################################

        """self.bidsOffersText = QVBoxLayout()
        self.bidsOffersText.addWidget(QLabel('Bids offers:'))
        self.generalLayout.addLayout(self.bidsOffersText)
        

        self.bidsOffers=QComboBox()
        self.bidsOffers.addItems([])
        self.generalLayout.addWidget(self.bidsOffers)


        self.acceptBid = QVBoxLayout()
        self.acceptBidBttn=QPushButton('Accept Bid offer!')
        self.acceptBidBttn.clicked.connect(self.acceptBidFunc)
        self.acceptBid.addWidget(self.acceptBidBttn)
        self.generalLayout.addLayout(self.acceptBid)"""



#        self.requestTitle = QVBoxLayout()
 #       self.requestTitle.addWidget(QLabel('Request ride offer:'))
        self.requestRideOfferText=QLabel('Request ride offer:')
        self.requestRideOfferText.setFont(QFont('Arial',20))
        self.generalLayout.addWidget(self.requestRideOfferText)

    


        passengerLayout = QGridLayout()
        self.rideOffers=QComboBox()
        self.rideOffers.addItems([])

        self.offersText=QLabel('Offers:')
        self.offersText.setFont(QFont('Arial',15))
        self.bidsText=QLabel('Bid:')
        self.bidsText.setFont(QFont('Arial',15))
        self.bidOffer=QLineEdit("")
        
        passengerLayout.addWidget(self.offersText, 0, 0)
        passengerLayout.addWidget(self.rideOffers, 0, 1)
        passengerLayout.addWidget(self.bidsText, 1, 0)
        passengerLayout.addWidget(self.bidOffer, 1, 1)
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(passengerLayout)

        
    
        self.bidPubBttn=QPushButton('Publish bid offer!')
        self.bidPubBttn.setFont(QFont('Arial',15))
        self.bidPubBttn.clicked.connect(self.bidPubFunc)
        self.generalLayout.addWidget(self.bidPubBttn)


        self.myFutureTravelsText=QLabel('My future travels:')
        self.myFutureTravelsText.setFont(QFont('Arial',20))
        self.generalLayout.addWidget(self.myFutureTravelsText)
        
        #Create the display.
        # Create the display widget
        self.futureTravels = QLineEdit()
        # Set some display's properties
        self.futureTravels.setFixedHeight(35)
        self.futureTravels.setAlignment(Qt.AlignRight)
        self.futureTravels.setReadOnly(True)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.futureTravels)

    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")
    """def acceptBidFunc(self):
        print("Bid accepted")"""
    def ridePubFunc(self):
        print("Offer Published")
        currentPrice=self.priceEdit.text()
        currentLocation=self.locations.currentText()
        currentPosition=self.positions.currentText()
        currentDateAndTime=self.dateTime.text()
        currentDuration=self.durationEdit.text()
        
        #price=self.display.text()
        #self.rideOffers.addItems([str(currentPrice)+str(currentLocation)])
        if(currentPrice==""):
            print("Please enter the price")
        elif(currentDuration==""):
            print("Please enter the duration in minutes")
        else:
            self.rideOffers.addItems(["$: "+str(currentPrice)+"||"+str(currentLocation)+"||Positions: "+str(currentPosition)+"||"+str(currentDateAndTime)+"||minutes: "+str(currentDuration)])
    def bidPubFunc(self):
        if(self.bidOffer.text()==""):
            print("Please enter bid")
        else:
            currentRideOffers=self.rideOffers.currentText()
            self.futureTravels.setText(currentRideOffers+"✅")
            #self.futureTravels.setFocus()
            #self.rideOffers.addItems([currentRideOffers+"✅"])
        print("Bid Published")


# Create a Model to handle the calculator's operation
def evaluateExpression(expression):
    """Evaluate an expression."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result

# Create a Controller class to connect the GUI and the model
class PyCalcCtrl:
    """PyCalc's Controller."""

    def __init__(self, model, view):
        #Controller initializer.
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        #self._connectSignals()
        
    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)
"""
    def _connectSignals(self):
        #Connect signals and slots.
        for btnText, btn in self._view.buttons.items():
            if btnText not in {"=", "C"}:
                btn.clicked.connect(partial(self._buildExpression, btnText))
"""
        #self._view.buttons["="].clicked.connect(self._calculateResult)
        #self._view.display.returnPressed.connect(self._calculateResult)
        #self._view.buttons["C"].clicked.connect(self._view.clearDisplay)
        #self._view.buttons["C"].clicked.connect(self._view.clearDisplay)
# Client code
def main():
    """Main function."""
    # Create an instance of `QApplication`
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()
    # Create instances of the model and the controller
    model = evaluateExpression
    #PyCalcCtrl(model=model, view=view)
    # Execute calculator's main loop
    sys.exit(pycalc.exec_())


if __name__ == "__main__":
    main()