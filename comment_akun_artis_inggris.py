""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# login credentials
insta_username = 'YOUR_USERNAME'
insta_password = 'YOUR_PASSWORD'

comments = ['Nice! @{}',
        'Best pic !:thumbsup:',
        'Cool :open_mouth:',
        'Woww @{}',
        'The best pic! @{}',
        'Awesomeee @{}',
        ':raised_hands: Yes!',
        'wow! awesome :muscle:']
accs = ['marcelotwelve','thehughjackman','snoopdogg','dualipa','vanessahudgens','jbalvin','dovecameron','lilyjcollins',
    'eljuanpazurita','teddysphotos','nickyjampr','daddyyankee','leonardodicaprio','charlieputh','reesewitherspoon','theellenshow',
    'samsmith','taylorswift','beyonce','leomessi','emmawatson','selenagomez','robertdowneyjr','nusr_et','neymarjr','instagram',
    'cristiano','arianagrande','justinbieber','ronaldinho','shawnmendes','kingjames','therock','vindiesel','davidbeckham','justintimberlake',
    'champagnepapi','shakira','badgalriri','kevinhart4real','jlo','katyperry','nike','ddlovato','mileycyrus','kendalljenner','natgeo',
    '9gag','kourtneykardash','krisjenner','kyliejenner','bellahadid','khloekardashian','gigihadid','victoriabeckham','kimkardashian',
    'nickiminaj','chrisbrownofficial','camila_cabello','shaymitchell','lucyhale','karimbenzema','50cent','amandacerny',
    'dior','louisvuitton','gucci','voguemagazine','nasa','marvel','manchesterunited'
    ]

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    session.set_comments(comments)
    session.set_do_comment(enabled=True, percentage=80)
    #session.set_do_like(True, percentage=70)
    session.interact_by_users(accs, amount=5, randomize=True, media='Photo')