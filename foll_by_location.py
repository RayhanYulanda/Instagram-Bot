""" Quickstart script for InstaPy usage """

#banda aceh 7607961/banda-aceh-indonesia/
#blangpidie 916084370/kota-blangpidie
#prov aceh 882390850/provinsi-aceh/
#kota b aceh 272586749/di-kota-banda-aceh/

# imports
from random import randint
import time
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy(username="YOUR_USERNAME", 
        password="YOUR_PASSWORD")

with smart_run(session):	
    #blangpidie
    print ('Blangpidie')
    session.follow_by_locations(['916084370'], amount=100)
    session.set_do_follow(enabled=True, percentage=50, times=1)
    print ('Wait to follow banda aceh')
    lama_tunggu = randint(3000, 4000)
    print ('You have to wait '+str(lama_tunggu))
    time.sleep(lama_tunggu)
    #banda aceh
    print ('Banda aceh')
    session.follow_by_locations(['7607961'], amount=100)
    session.set_do_follow(enabled=True, percentage=50, times=1)