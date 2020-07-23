""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy(username="YOUR_USERNAME", 
        password="YOUR_PASSWORD")

with smart_run(session):
	#accounts
    accs = ['marcelotwelve','thehughjackman','snoopdogg','dualipa','vanessahudgens','jbalvin','dovecameron','lilyjcollins','eljuanpazurita','teddysphotos','nickyjampr','daddyyankee','leonardodicaprio','charlieputh','reesewitherspoon','theellenshow','samsmith','taylorswift','beyonce','leomessi','emmawatson','selenagomez','robertdowneyjr','nusr_et','neymarjr','instagram','cristiano','arianagrande','justinbieber','ronaldinho','shawnmendes','kingjames','therock','vindiesel','davidbeckham','justintimberlake','champagnepapi','shakira','badgalriri','kevinhart4real','jlo','katyperry','nike','ddlovato','mileycyrus','kendalljenner','natgeo','9gag','kourtneykardash','krisjenner','kyliejenner','bellahadid','khloekardashian','gigihadid','victoriabeckham','kimkardashian','nickiminaj','chrisbrownofficial','prillylatuconsina96','camila_cabello','shaymitchell','lucyhale','karimbenzema','50cent','amandacerny','dior','louisvuitton','gucci','voguemagazine','nasa','marvel','manchesterunited']
	
    session.unfollow_users(amount=100, customList=(True, accs, "all"), style="FIFO", unfollow_after=None, sleep_delay=60)
	
    session.follow_by_list(accs, times=1, sleep_delay=60, interact=False)