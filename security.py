from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    """
    Called when user calls /auth endpoint
    :param username: Username in string format.
    :param password: Unencrypted password in string format.
    :return: User if auth is successful, otherwise None.
    """
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    """
    Called when user already authenticated and Flask-JWT verifies that
    auth header is correct
    :param payload: Dictionary with 'identity' key (user id)
    :return: UserModel object
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
