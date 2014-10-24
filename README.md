##CSHub Club Site

### Description
York University's official Computer Science Club website! A social hub for students to connect with one another, keep up to date with events, and get information fast. With some simple modification you can use this for any club web page.

### Tech Stack
* [Django](https://www.djangoproject.com/) : an awesome web application framework
* [BootStrap 3.1.1](http://getbootstrap.com/) : flat UI responsive front-end framework
* [PureCSS](http://purecss.io/) : for the pretty form styling
* [fontawesome](http://fortawesome.github.io/Font-Awesome/) : for beautiful, scalable icons
* [Redis](http://redis.io/) : as a session engine and cache backend
* [South]() : schema and data migrations
* JQuery, AJAX, Google maps API, and whatever database backend you like. 


### Features
#### General
Built with Django, using their CMS (may switch to [wagtail](http://wagtail.io/) in the future).
AJAX form submissions allow for form submissions without reloading pages. 
Submit buttons inserted to DOM with JavaScript to prevent some spam. 
Emails are sent on event creation to keep all members up to date. 


#### General members abilities
Signup, create/edit profiles with images and links to profile images, keep up-to-date contact information, earn badges, view/comment/confirm attendance on events

#### Admins
Create new events and notifications, change home banner images, and view member contact information.

### Set-up Instructions
*there will be an installation script later down the road*
* create a secrets.json file with all relevant server settings. (you can find whats required by going through the settings.py file)
* install Redis server.
* clone this repo, into a virtualenv
* pip install -r requirements.txt


### Detailed Instructions
1. Set up python and pip
- Windows : http://arunrocks.com/guide-to-install-python-or-pip-on-windows/
- Mac : http://docs.python-guide.org/en/latest/starting/install/osx/#doing-it-right
- Linux : http://docs.python-guide.org/en/latest/starting/install/linux/#setuptools-pip

> At this point you should be able to open a terminal window type `python --version` to get output `Python 2.7.8` and type `pip --version` to get an output like `pip 1.5.6 from /usr/local/Cellar/ ...`

2. Set up virtual env.
Run the following commands on a terminal
- `pip install virtualenv`
- Mac/Linux : `pip install virtualenvwrapper`
- Windows : `pip install virtualenvwrapper-win`

3. Configure virtualenvwrapper
- Mac/Linux : Append the following lines to your shell initialization file. (Usually `~/.bashrc`)
```  
# Virtual env wrapper  
export WORKON_HOME=$HOME/.virtualenvs  
export PROJECT_HOME=$HOME/dev  
source /usr/local/bin/virtualenvwrapper.sh  
```

> At this point you should be able to type `virtualenv --version` and `virtualenvwrapper` in a shell window and not get any errors. (you might have to re-open terminal windows)

4. Install Redis
- Mac : `brew install redis`
- Linux : https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis
- Windows : https://github.com/ServiceStack/redis-windows#running-microsofts-native-port-of-redis

5. Set up git
- Follow the instructions for your platform : http://git-scm.com/downloads
- Optionally, you can download a git gui like SourceTree or GitHub for Mac/Windows

> At this point if you open a new terminal window and type `git --version`, you should see the output `git version 1.9`

6. Set up nodejs and npm
- Mac/Linux/Windows: http://blog.nodeknockout.com/post/65463770933/how-to-install-node-js-and-npm

7. Clone the respository.

8. Setting up the environment.
Open a shell and enter the following commands.
- `mkvirtualenv cshub` 
- `workon cshub`
- `cd` in to the root of the cloned repository. 
- Mac/Linux : `setvirtualenvproject $VIRTUAL_ENV $(pwd)`
- Windows : `setprojectdir .`

9. Install dependencies
- `pip install --allow-all-external --allow-unverified wadofstuff-django-serializers -r requirements.txt`
- `npm install`

10. Set up configuration
- `cd` in to the repository root.
- Copy secrets_example.json to secrets.json
- `python manage.py syncdb` 
- `python manage.py migrate`

### Starting development server
- Toggle the virtualenv : `workon cshub`
- Start redis server : `redis-server`
- `python manage.py runserver`

### Ending development
- Deactivate virtualenv : `deactivate`


If you experience any problems setting up or incorrect instructions please let us know by creating a new github issue. 


https://thecshub.ca
