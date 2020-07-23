""" Quickstart script for InstaPy usage """

#banda aceh 7607961/banda-aceh-indonesia/
#blangpidie 916084370/kota-blangpidie
#prov aceh 882390850/provinsi-aceh/
#kota b aceh 272586749/di-kota-banda-aceh/

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
from random import randint
import time


# login credentials 'Cek timeline kami kakk :open_mouth:', . Tetap semangat kak :muscle:
insta_username = 'YOUR_USERNAME'
insta_password = 'YOUR_PASSWORD'

comments = ['YOK KAK!! Lihat timeline kami banyak BAJU-BAJU bagus. JAHIT BAJU bisa sama kami untuk daerah BANDA ACEH dan BLANGPIDIE @{}',
        'KAK!! Lihat timeline kami banyak BAJU-BAJU bagus. JAHIT BAJU bisa sama kami untuk daerah BANDA ACEH dan BLANGPIDIE :thumbsup:',
        'Cek timeline kami kakk, banyak BAJU-BAJU bagus :)',
        'Lihat timeline kami kakk, JAHIT BAJU bisa sama kami :)',
        'JAHIT BAJU bisa sama kami untuk daerah BANDA ACEH dan BLANGPIDIE :D']
location = ['499428321/blangpidie/',
            '7607961/banda-aceh-indonesia/',
            '518897174/aceh/',       
            '664310512/kota-banda-aceh/',
            '359549567/kota-banda-aceh/',           
            ]

locBP = ['499428321/blangpidie/']
locBA = ['7607961/banda-aceh-indonesia/']
locA = ['518897174/aceh/']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    while 1:
    
        session.set_do_comment(True, percentage=100)
        session.set_comments(comments)
        session.like_by_locations(locBP, amount=300, skip_top_posts=True)
        
        lama_tunggu = randint(1000,1200)
        print ('Tunggu untuk comment selanjutnya Banda Aceh selama '+str(lama_tunggu)+'second')
        time.sleep(lama_tunggu)

        session.set_do_comment(True, percentage=100)
        session.set_comments(comments)
        session.like_by_locations(locBA, amount=300, skip_top_posts=True)
        
        lama_tunggu = randint(1000,1200)
        print ('Tunggu untuk comment selanjutnya Aceh selama '+str(lama_tunggu)+'second')
        time.sleep(lama_tunggu)
        
        session.set_do_comment(True, percentage=100)
        session.set_comments(comments)
        session.like_by_locations(locA, amount=300, skip_top_posts=True)
        
        lama_tunggu = randint(1000,1200)
        print ('Tunggu untuk comment selanjutnya Blangpidie selama '+str(lama_tunggu)+'second')
        time.sleep(lama_tunggu)
        
        
        
        
        session.set_do_comment(True, percentage=100)
        session.set_comments(comments)
        session.like_by_locations(locBP, amount=300, skip_top_posts=False)
        
        lama_tunggu = randint(1000,1200)
        print ('Tunggu untuk comment selanjutnya Banda Aceh selama '+str(lama_tunggu)+'second')
        time.sleep(lama_tunggu)

        session.set_do_comment(True, percentage=100)
        session.set_comments(comments)
        session.like_by_locations(locBA, amount=300, skip_top_posts=False)
        
        lama_tunggu = randint(1000,1200)
        print ('Tunggu untuk comment selanjutnya Aceh selama '+str(lama_tunggu)+'second')
        time.sleep(lama_tunggu)
        
        session.set_do_comment(True, percentage=100)
        session.set_comments(comments)
        session.like_by_locations(locA, amount=300, skip_top_posts=False)
        
        lama_tunggu = randint(1000,1200)
        print ('Tunggu untuk comment selanjutnya Blangpidie selama '+str(lama_tunggu)+'second')
        time.sleep(lama_tunggu)