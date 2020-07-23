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
    session.unfollow_users(amount=1000, allFollowing=True, style="FIFO", unfollow_after=1, sleep_delay=10)