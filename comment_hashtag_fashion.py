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
hashtag = ['fashion','gamis','gown','instafashion',
        'modiste','tailor','sewing','dressmaker','inspirasigaun',
        'fashions','tailormade']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    session.set_smart_hashtags(hashtag, limit=5, sort='top', log_tags=True)
    session.like_by_tags(amount=5, use_smart_hashtags=True)
    session.set_comments(comments)
    session.set_do_comment(enabled=True, percentage=80)