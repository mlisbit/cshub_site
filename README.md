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
* JQuery, AJAX, Google maps API, and whatever backend you like. 


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

  
