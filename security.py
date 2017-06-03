from werkzeug.security import safe_str_cmp
from src.models.user import UserModel

'''
users = []

username_mapping = {u.username: u for u in users}
id_mapping = {u.id: u for u in users}
'''


def authenticate(username, password):
    # user = username_mapping.get(username, None)
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(password, user.password):
        return user


def identity(payload):
    # user = id_mapping.get(payload['identity'], None)
    user = UserModel.find_by_id(payload['identity'])
    return user
