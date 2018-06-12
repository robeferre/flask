from lutils import md5
from lusers.models.m_user import Users
from flask import current_app as app


def login(_user, _password):

    _encode = app.config['PASS_CHARSET_ENCODE']
    _key = app.config['PASS_SALT']
    _result = False

    _hash = md5.generate(_password, _user, _key, _encode)

    user = Users.get_user(_user)

    if user:
        if bytes(user[0].get("hash"), _encode) == _hash:
            _result = True

    return _result
