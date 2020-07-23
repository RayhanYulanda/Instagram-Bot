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

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
  # Joining Engagement Pods
  session.set_smart_hashtags(['fashion', 'gamis'], limit=10, sort='top', log_tags=True)
  session.set_do_comment(enabled=True, percentage=35)
  session.set_comments(comments)
session.join_pods()