Rede Globo Login API
====================

This the documentation for the Rede Globo login api.


# Setup

## Mac OS Setup

### System dependencies install

	$ brew install python
	$ brew install pyenv pyenv-virtualenv

### Virtual-env setup

 * Include on ~/.bash_profile

		eval "$(pyenv init -)"
		eval "$(pyenv virtualenv-init -)"

 * Open a new terminal or execute the commands above if using the same terminal.

 * Create a virtual-env

		pyenv shell 2.7.9
		virtualenv venv

 * Activate the virtual-env

 		 . .venv/bin/activate

 * From now on, all python packages installed will be installed on *venv* virtual-env

 * Clone from gitlab

		$ 
		$ cd tvg-login

 * Checkout the branch you want to work with (for instance *develop*)

 		$ git checkout tvg-login-dev

 * Install ldm requirements

 		$ pip install -r requirements.txt
 		$ pip install -r requirements-dev.txt # Just needed for development.

# Tests

To run the test suite, you need cd into the project, then run Nose tests.

    $ cd tvg-login
    $ nosetests

Authotization Token format
TvgLogin apikey=bruno.ramos.DduJKg.jHm9-3btOdmJt0rVolqgEL9MYB4
