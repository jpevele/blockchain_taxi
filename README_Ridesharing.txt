GITHUB REPO
https://github.com/jpevele/blockchain_taxi
VIDEO EXPLANATION
https://youtu.be/LlfSukxc-Eg

///////////////////////////////////Read Me\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
Consider the following libraries for the Blockchain Taxi 
***Python version***
     v.3.9.1
***Libraries***
Install these libraries using pip install in the command prompt
	PyQt5
	datetime
	numpy
	web3
	sys
	solcx
You might encounter some issues during the installation of the web3 library, if that's case review this link.
	https://github.com/ethereum/web3.py/issues/1578
You can run the program on either Microsoft Visual Studio or other IDE or directly on the python IDLE or command prompt or 
Double Clicking on the file of the project with ".py" extension. 


//////////////////////////////////HOW TO (walkthrough of the program characteristics)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
1. Type the driver credentials. 
	Address> 
	Key>  
2. Press the button "Driver Login"
	This will save the previously input data (driver credntials). 
3. Type the passenger credentials.
	Address> 
	Key>
4. Press the button "Passenger Login"

To fulfill the Ride Offer
	//////Driver's Point Of View\\\\\\\
5. Set a price in Ethereum that you wish to receive.
6. Set an arrival location (i.e. mayors> Coyoacan, Tlalpan, Benito Juárez, Tláhuac, Iztapalapa, etc.)
7. Set the number of seats that you have for your trip (i.e. 1, 2, 3, 4).
8. Set a date and time, in the box you can change these parameters with the up and down arrows. 
9. Set the approximate duration of the trip in minutes, remember that you can not set others trips while one trip's time in happening. 
10. Press the "Publish Ride Offer"
	This will publish the offer on the blockchain, associating it on the smart contract. 
	///////Riders's Point Of View\\\\\\\\
Rider can check the ongoing offers (trips) and bid on the one that suits better. Rider can navigate to search for a trip by selecting Location, month and day. 
11. You can search the trips associated with the LOCATION, select the down arrow to change the mayor location.
12. Select the month by clicking the down arrow to check if any trips are ocurring on that month.
13. Select day where the trip will ocurr. 
14. Set a bid offer, this quantity will be uploaded to the contract to check if is enough for the driver. 
15. Press the button of Filter ride offers to check the offers on the OFFERS text box. 
16. Press the button of the Publish bid offer once everything is ready to upload on the bockchain. 


	////////////Fulfilled Requirements\\\\\\\\\\\\
The sections of the code will be pasted along the requirements, please check the github repository for a complete analysis. 
1. Contract must be able to deal with errors such as duplicate reservation of cars using functions such as requirements, assert, revert. 
Line 265
try:
                                    basePriceDurationAndSeats=contractExtracted.functions.basePriceDurationAndSeats().call()#Obtain base price, duration and seats in a list from contract
                                    dateAndLocation=contractExtracted.functions.dateAndLocation().call()#Obtain dateTime and location in a list from contract
                                    t1_start=datetime.strptime(dateAndLocation[0].replace('. ', '').replace('.', ''), '%d/%m/%Y %I:%M %p')#Start time of ride from contract#
                                    t1_end=t1_start+timedelta(minutes=int(basePriceDurationAndSeats[1])) #End time of ride from contract
                                    t2_start=rideTime#Start time of ride from settings
                                    t2_end=t2_start+timedelta(minutes=int(currentDuration))#End time of ride from settings

                                    #Check if there is overlapping of time#                                    
                                    if((t2_start<t1_start and t2_end>t1_start) or (t2_start>=t1_start and t2_start<t1_end)):
                                        overlapping=True
                                        pass    
                                except:
                                    pass

2. Contracts must expire, preventing the same from being carried out after the initial period.
Line 505

function auctionEnd()public {
        if (block.timestamp < auctionEndTime){
            revert("Auction has not ended yet");
        }
        if (ended){
            revert("Function auctionEnded has already been called");
        }
3. Contracts must prevent a client from making a reservation without having sufficient funds to carry out the same (use of functions like events/emit).
Line 485
function bid (uint _account_balance, address _bidder, uint _amount) public payable{
        if (block.timestamp > auctionEndTime){
            //revert("Auction has already ended");
        }
        if (_account_balance< basePrice){
            revert("You don't have sufficient funds to carry out the reservation");
            //emit fundInsufficient(basePrice,_account_balance);
        }

4. System must have a digital wallet (wallet)
Implemented using Metamask extension of google chrome browser. 





	