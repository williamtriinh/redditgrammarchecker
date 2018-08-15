import praw
import configparser


config = configparser.ConfigParser()
config.read("config.ini")

# Create an authorized Reddit instance.
reddit = praw.Reddit(client_id=config["config"]["client_id"],
                     client_secret=config["config"]["client_secret"],
                     user_agent=config["config"]["user_agent"],
                     username=config["config"]["username"],
                     password=config["config"]["password"]
)

# Obtain subreddit instance.
subreddit = reddit.subreddit(config["config"]["subreddit"])

print("r/" + subreddit.display_name)
print(subreddit.title)

for submission in subreddit.new(limit=3):
    submission.comment_sort = "new"

input("press enter to close")