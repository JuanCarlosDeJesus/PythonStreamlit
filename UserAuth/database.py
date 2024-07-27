from deta import Deta
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("user_db")

def insert_user(username, name, password):
    """Returns the user on a successful user creation, otherwise raiss an error"""
    return db.put({"key": username, "name": name, "password": password})

# insert_user("pparker", "Peter Parker", "abc123")

def fetch_all_users():
    """Returns a dict of all users"""
    res = db.fetch()
    return res.items

# print(fetch_all_users())

def get_users(username):
    """If not found, the function will return None"""
    return db.get(username)


def update_user(username, updates):
    """If the item is updated, returns None. Otherwise, an exception is raised"""
    return db.update(updates, username)

# update_user("mjwatson", updates={"name": "Mary Jane Parker"})

def delete_user(username):
    """Always returns None, even is the key does not exist"""
    return db.delete(username)

# delete_user("mjwatson")