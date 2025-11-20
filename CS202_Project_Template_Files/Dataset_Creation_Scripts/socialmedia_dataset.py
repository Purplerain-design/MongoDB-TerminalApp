import os
from pymongo import MongoClient
from faker import Faker
from datetime import datetime, timedelta
import random
from bson.objectid import ObjectId

# --- MongoDB Connection ---
# Students, insert your MongoDB connection URI here
# For example: "mongodb+srv://<username>:<password>@<cluster-url>/<dbname>?retryWrites=true&w=majority"
# MONGO_URI = #add your uri here
DB_NAME = "social_media_db"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# --- Faker Initialization ---
fake = Faker('en_US')

# --- Configuration ---
NUM_USERS = 70
MIN_POSTS_PER_USER = 5
MAX_POSTS_PER_USER = 15
MIN_LIKES_PER_POST = 0
MAX_LIKES_PER_POST = 30
MIN_COMMENTS_PER_POST = 0
MAX_COMMENTS_PER_POST = 10
MIN_FRIENDS_PER_USER = 5
MAX_FRIENDS_PER_USER = 20

def generate_users(num_users):
    users = []
    for _ in range(num_users):
        user = {
            "_id": ObjectId(),
            "username": fake.unique.user_name(),
            "email": fake.unique.email(),
            "profile": {
                "bio": fake.sentence(nb_words=8),
                "location": fake.city(),
            },
            "friends": [],
            "following_tags": random.sample(fake.words(nb=5, unique=True), k=random.randint(1, 4)),
            "recent_activity": []
        }
        users.append(user)
    print(f"Generated {len(users)} users.")
    return users

def establish_friendships(users):
    user_ids = [user["_id"] for user in users]
    for user in users:
        num_friends = random.randint(MIN_FRIENDS_PER_USER, MAX_FRIENDS_PER_USER)
        possible_friends = [uid for uid in user_ids if uid != user["_id"]]
        
        friends_to_add = random.sample(possible_friends, k=min(num_friends, len(possible_friends)))
        
        user["friends"].extend(friends_to_add)
        
        for friend_id in friends_to_add:
            db.users.update_one({"_id": friend_id}, {"$addToSet": {"friends": user["_id"]}})
        db.users.update_one({"_id": user["_id"]}, {"$set": {"friends": user["friends"]}})
    print("Established friendships.")

def generate_posts(users):
    posts = []
    for user in users:
        num_posts = random.randint(MIN_POSTS_PER_USER, MAX_POSTS_PER_USER)
        for _ in range(num_posts):
            post_date = fake.date_time_between(start_date="-1y", end_date="now")
            post = {
                "_id": ObjectId(),
                "user_id": user["_id"],
                "username": user["username"],
                "content": fake.paragraph(nb_sentences=random.randint(1, 5)),
                "date": post_date,
                "tags": random.sample(fake.words(nb=5, unique=True), k=random.randint(0, 3)),
                "likes": [],
                "comments": [],
                "engagement_count": { "likes": 0, "comments": 0 }
            }
            posts.append(post)
            db.users.update_one({"_id": user["_id"]}, {"$push": {"recent_activity": {"type": "post", "post_id": post["_id"], "date": post_date}}})
    print(f"Generated {len(posts)} posts.")
    return posts

def populate_likes_and_comments(posts, users):
    user_ids = [user["_id"] for user in users]

    for post in posts:
        # Add Likes
        num_likes = random.randint(MIN_LIKES_PER_POST, MAX_LIKES_PER_POST)
        if num_likes > 0 and len(user_ids) > 0:
            likers = random.sample(user_ids, k=min(num_likes, len(user_ids)))
            post["likes"] = likers
            post["engagement_count"]["likes"] = len(likers)

        # Add Comments (embedded)
        num_comments = random.randint(MIN_COMMENTS_PER_POST, MAX_COMMENTS_PER_POST)
        for _ in range(num_comments):
            commenter = random.choice(users)
            comment_date = fake.date_time_between(start_date=post["date"], end_date="now")
            comment = {
                "comment_id": ObjectId(),
                "user_id": commenter["_id"],
                "username": commenter["username"],
                "text": fake.sentence(nb_words=random.randint(5, 15)),
                "date": comment_date,
            }
            post["comments"].append(comment)
            db.users.update_one({"_id": commenter["_id"]}, {"$push": {"recent_activity": {"type": "comment", "post_id": post["_id"], "date": comment_date}}})
        post["engagement_count"]["comments"] = len(post["comments"])

        db.posts.update_one({"_id": post["_id"]}, {"$set": {"likes": post["likes"], "comments": post["comments"], "engagement_count": post["engagement_count"]}})
    print("Populated likes and comments.")

def main():
    print(f"Connecting to MongoDB at {MONGO_URI}...")
    db.users.drop()
    db.posts.drop()
    print("Dropped existing collections.")

    users_data = generate_users(NUM_USERS)
    db.users.insert_many(users_data)

    establish_friendships(users_data) 

    posts_data = generate_posts(users_data)
    db.posts.insert_many(posts_data)

    populate_likes_and_comments(posts_data, users_data)

    print("\nDataset generation complete!")
    client.close()
    print("MongoDB connection closed.")

if __name__ == "__main__":
    main()