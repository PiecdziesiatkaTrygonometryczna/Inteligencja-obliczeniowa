import praw

# Set up your Reddit API credentials
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='YOUR_USER_AGENT',
)

subreddit = reddit.subreddit("learnpython")

# Fetch posts
posts = subreddit.search(query="#learnpython", limit=100)

# Save posts to file
with open("reddit_posts.txt", "w") as file:
    for post in posts:
        file.write(post.title + "\n")  # Or write more details as needed
