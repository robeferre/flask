#!/usr/bin/venv python
# -*- coding: utf-8 -*-
from flask_migrate import MigrateCommand
from flask_script import Manager

from lusers import create_app


app = create_app()

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def about():
    print('TV Globo Login API')

'''
@manager.command
def load():
    from tests.dummy_data import create_all
    create_all()
'''


@manager.option('-u', dest='user', help='User name')
@manager.option('-e', dest='environment', help='Environment name [Development | Staging | Production]')
def generate_api_key(environment, user):
    import sys
    from itsdangerous import TimestampSigner
    from lusers import config

    if environment not in ['Development', 'Staging', 'Production']:
        print('Invalid environment')
        sys.exit(1)

    config_env = getattr(config, '{0}Config'.format(environment))

    signer = TimestampSigner(config_env.SIGNER_KEY)
    print('APIKEY: {0}'.format(signer.sign(user)))


if __name__ == '__main__':
    manager.run()
