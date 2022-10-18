import tweepy 

bearer_token = "EDIT-ME"

client = tweepy.Client(bearer_token=bearer_token)

afkham_id = client.get_user(username="Afkham_plus").data.id

afkham_plus_followers = client.get_users_followers(id=afkham_id).data

for follower in afkham_plus_followers:
    print(follower.data)