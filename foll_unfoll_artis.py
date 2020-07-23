""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
from random import randint
import time


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy(username="YOUR_USERNAME", 
        password="YOUR_PASSWORD")

with smart_run(session):
	#accounts
    accs = [
    'marcelotwelve','thehughjackman','snoopdogg','dualipa','vanessahudgens','jbalvin','dovecameron','lilyjcollins',
    'teddysphotos','nickyjampr','daddyyankee','leonardodicaprio','charlieputh','reesewitherspoon','theellenshow',
    'samsmith','taylorswift','beyonce','leomessi','emmawatson','selenagomez','robertdowneyjr','nusr_et','neymarjr',
    'cristiano','arianagrande','justinbieber','ronaldinho','shawnmendes','kingjames','therock','vindiesel','davidbeckham','justintimberlake',
    'champagnepapi','shakira','badgalriri','kevinhart4real','jlo','katyperry','ddlovato','mileycyrus','kendalljenner',
    'kourtneykardash','krisjenner','kyliejenner','bellahadid','khloekardashian','gigihadid','victoriabeckham','kimkardashian',
    'nickiminaj','chrisbrownofficial','camila_cabello','shaymitchell','lucyhale','karimbenzema','50cent','amandacerny','iamcardib',
    'jamesrodriguez10','garethbale11','priyankachopra','anitta','paulpogba','brunamarquezine','lelepons','sergioramos','willsmith',
    'k.mbappe','marinaruybarbosa','jacquelinef143','ivetesangalo','danbilzerian','wizkhalifa','antogriezmann','wesleysafadao',
    'luansantana','ciara','letthelordbewithyou','eljuanpazurita','zachking','marshmellomusic','parishilton','sunnyleone','sabrinasato',
    'kevinho','fernandasouzaoficial','amberrose','eliana','gusttavolima','milliebobbybrown'
    ]
    
    accs2 = [
    'nasa','marvel','manchesterunited','natgeo','9gag','nike','instagram', 'realmadrid','fcbarcelona','championsleague','nba',
    'chanelofficial','adidas','zara','5.min.crafts','hm','premierleague','juventus',
    'dolcegabbana','prada',
    
    'fashion_cosmopolitan','fashion.selection','fashioninmagazine','fashionzine',
    'fashionactive','fashions.tv','fashions.universe','fashionnova','fashions.sense',
    'fashion.hub','fashionweek','dior','louisvuitton','gucci','voguemagazine','vogue',
    
    'raffinagita1717','gisel_la','lunamaya','chelseaoliviaa','shireensungkar', 'prillylatuconsina96', 'ayutingting92', 'ivan_gunawan', 
    'showimah', 'riaricis1795', 'glennalinskie','sarwendah29', 'agnezmo', 'alghazali7', 'raisa6690', 'laudyacynthiabella', 'princessyahrini',
    'maiaestiantyreal','ashanty_ash', 'pevpearce', 'bramastavrl','viavallen','iqbaal.e','nissa_sabyan','bclsinclair','ollaramlanaufar',
    'zaskiadyamecca','ichasoebandono','ramadhaniabakrie'
    ]
    
    while 1 :
        print ('Selanjutnya masuk ke proses unfollow')
        session.unfollow_users(amount=500, customList=(True, accs, "all"), style="FIFO", unfollow_after=None, sleep_delay=10)
        print ('Selanjutnya masuk ke proses follow')
        session.follow_by_list(accs, times=100, sleep_delay=10, interact=False)
        
        lama_tunggu = randint(1000,1200)
        print ('Tunggu untuk unfoll foll selanjutnya selama '+str(lama_tunggu)+'second')
        time.sleep(lama_tunggu)
        
        print ('Selanjutnya masuk ke proses unfollow')
        session.unfollow_users(amount=500, customList=(True, accs2, "all"), style="FIFO", unfollow_after=None, sleep_delay=10)
        print ('Selanjutnya masuk ke proses follow')
        session.follow_by_list(accs2, times=100, sleep_delay=10, interact=False)
        
        lama_tunggu2 = randint(3000, 4000)
        print ('You have to wait '+str(lama_tunggu2)+'second')
        time.sleep(lama_tunggu2)