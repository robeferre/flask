# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request

from lusers.business import b_user
from lutils.decorators import requires_api_key, requires_json

api = Blueprint('api', __name__, url_prefix='/api/v1/users')


@api.route('/login', methods=['POST'])
@requires_json
@requires_api_key
def login_user():

    r = request.json
    login = r.get("login")
    password = r.get("password")
    result = b_user.login(login, password)

    ''' 
    TODO Implement JWT 
    '''
    return jsonify({'token': 'h34758vGGj899khbvfgh67568trdftyc4c908'}) if result else jsonify({'token': ''}), \
        200 if result else 401
