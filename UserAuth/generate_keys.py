import pickle
from pathlib import Path

from streamlit_authenticator.utilities.hasher import Hasher

names = ["Peter Parker", "Mary Jane Watson"]
usernames = ["pparker", "mjwatson"]
passwords = ["******", "******"] # rewrote password after running file

hashed_passwords = Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pk1"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)