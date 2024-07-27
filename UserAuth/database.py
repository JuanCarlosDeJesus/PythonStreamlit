from deta import Deta

DETA_KEY = "S8A1uc2Z_cxQmv1mqFjsaWgz3doo3vHHLB6Nv8U17"

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("user_db")

def insert_user(username, name, password):
    """Returns the user on a successful user creation, otherwise raiss an error"""
    return db.put({"key": username, "name": name, "password": password})

insert_user("pparker", "Peter Parker", "abc123")