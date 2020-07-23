""" Quickstart script for InstaPy usage """

#banda aceh 7607961/banda-aceh-indonesia/
#blangpidie 916084370/kota-blangpidie
#prov aceh 882390850/provinsi-aceh/
#kota b aceh 272586749/di-kota-banda-aceh/

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# login credentials
insta_username = 'YOUR_USERNAME'
insta_password = 'YOUR_PASSWORD'

comments = ['Nice! @{}',
        'Fotonya bagus kak :thumbsup:',
        'Kerennnn :open_mouth:',
        'MasyaAllah @{}',
        'Bagus sekali kak @{}',
        'Mantap kak @{}',
        ':raised_hands: Yes!',
        'Semangat kak :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
  # Joining Engagement Pods
  session.comment_by_locations(['7607961'], amount=10, skip_top_posts=False)
  
  session.set_do_comment(enabled=True, percentage=1)
  session.set_comments(comments)
session.join_pods()
