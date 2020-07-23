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

    comments = ['Nice! @{}',
        'Fotonya bagus kak :thumbsup:',
        'Kerennnn :open_mouth:',
        'MasyaAllah @{}',
        'Bagus sekali kak @{}',
        'Mantap kak @{}',
        ':raised_hands: Yes!',
        'Semangat kak :muscle:']
    comments_eng = ['Nice! @{}',
        'Best pic !:thumbsup:',
        'Cool :open_mouth:',
        'Woww @{}',
        'The best pic! @{}',
        'Awesomeee @{}',
        ':raised_hands: Yes!',
        'wow! awesome :muscle:']
	#accounts
    accs = ['marcelotwelve','thehughjackman','snoopdogg','dualipa','vanessahudgens','jbalvin','dovecameron','lilyjcollins',
    'eljuanpazurita','teddysphotos','nickyjampr','daddyyankee','leonardodicaprio','charlieputh','reesewitherspoon','theellenshow',
    'samsmith','taylorswift','beyonce','leomessi','emmawatson','selenagomez','robertdowneyjr','nusr_et','neymarjr','instagram',
    'cristiano','arianagrande','justinbieber','ronaldinho','shawnmendes','kingjames','therock','vindiesel','davidbeckham','justintimberlake',
    'champagnepapi','shakira','badgalriri','kevinhart4real','jlo','katyperry','nike','ddlovato','mileycyrus','kendalljenner','natgeo',
    '9gag','kourtneykardash','krisjenner','kyliejenner','bellahadid','khloekardashian','gigihadid','victoriabeckham','kimkardashian',
    'nickiminaj','chrisbrownofficial','camila_cabello','shaymitchell','lucyhale','karimbenzema','50cent','amandacerny',
    'dior','louisvuitton','gucci','voguemagazine','nasa','marvel','manchesterunited',
    
    'shireensungkar', 'prillylatuconsina96', 'ayutingting92', 'ivan_gunawan', 'showimah', 'riaricis1795', 'glennalinskie',
    'sarwendah29', 'agnezmo', 'titi_kamal', 'alghazali7', 'raisa6690', 'laudyacynthiabella', 'princessyahrini', 'maiaestiantyreal',
    'ashanty_ash', 'pevpearce'
    ]
	
    session.unfollow_users(amount=100, customList=(True, accs, "all"), style="FIFO", unfollow_after=None, sleep_delay=60)
	
    session.follow_by_list(accs, times=1, sleep_delay=60, interact=False)
    
    session.comment_by_locations(['7607961'], amount=5)
    session.set_do_comment(enabled=True, percentage=1)
    session.set_comments(comments)
    session.comment_by_locations(['916084370'], amount=5)
    session.set_do_comment(enabled=True, percentage=1)
    session.set_comments(comments)
    session.like_by_tags(['gamis'], amount=3, media='Photo')
    session.set_do_comment(enabled=True, percentage=1)
    session.set_comments(comments)
    session.like_by_tags(['gaun'], amount=3, media='Photo')
    session.set_do_comment(enabled=True, percentage=1)
    session.set_comments(comments)
    session.like_by_tags(['inspirasigaun'], amount=3, media='Photo')
    session.set_do_comment(enabled=True, percentage=1)
    session.set_comments(comments)
    session.like_by_tags(['rumahjahit'], amount=3, media='Photo')
    session.set_do_comment(enabled=True, percentage=1)
    session.set_comments(comments)
    session.like_by_tags(['menjahit'], amount=3, media='Photo')
    session.set_do_comment(enabled=True, percentage=1)
    session.set_comments(comments)
    session.like_by_tags(['jahit'], amount=3, media='Photo')
    session.set_do_comment(enabled=True, percentage=1)
    session.set_comments(comments)
    session.like_by_tags(['tukangjahit'], amount=3, media='Photo')
    session.set_do_comment(enabled=True, percentage=1)
    session.set_comments(comments)
    session.like_by_tags(['penjahit'], amount=3, media='Photo')
    session.set_do_comment(enabled=True, percentage=1)
    session.set_comments(comments)
    session.like_by_tags(['tailor'], amount=3, media='Photo')
    session.set_do_comment(enabled=True, percentage=1)
    session.set_comments(comments_eng)
    session.like_by_tags(['sewing'], amount=3, media='Photo')
    session.set_do_comment(enabled=True, percentage=1)
    session.set_comments(comments_eng)
    session.like_by_tags(['tailoring'], amount=3, media='Photo')
    session.set_do_comment(enabled=True, percentage=1)
    session.set_comments(comments_eng)