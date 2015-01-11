#!/bin/sh


function install_brew_dependancies {
  for pkg in redis node; do
    if brew list -1 | grep -q "^${pkg}\$"; then
      echo "Package '$pkg' already installed"
    else
      echo "installing '$pkg'"
      sudo -H -u nobody bash -c "brew install $pkg"
    fi
  done
}

function has_dependancy {
  if [ -z "$1" ]; then
    echo "please pass an argument."
  else
    if which ${1}; then
      return 0
    else
      return 1
    fi
  fi
}

function macosx_install {
  echo "installing system dependancies <MAC OSX>"
  if has_dependancy "easy_install"; then
    echo "Package easy_install already installed"
  else
    echo "installing python-setuptools"
    curl https://bootstrap.pypa.io/ez_setup.py -o - | python > setup.log
  fi

  if has_dependancy "pip"; then
    echo "Package pip already installed"
  else
    echo "installing pip"
    easy_install pip >> setup.log
  fi

  echo "installing virtualenv"
  pip install virtualenv >> setup.log
  install_brew_dependancies
}

function debian_install {
  echo "installing system dependancies <Linux> ..."
  echo "installing pip"
  apt-get install -y python-pip > setup.log
  echo "installing python-setuptools"
  apt-get install -y python-setuptools >> setup.log
  echo "installing virtualenv"
  sudo pip install virtualenv >> setup.log
  echo "installing redis-server"
  sudo apt-get install redis-server >> setup.log
}

function windows_install {
  echo "Currently unsupported. Sorry."
}

function structure_app {
  echo Creating virtualenv and restructuring app ...

  cd ..
  virtualenv --no-site-packages cshub_site_dev

  . cshub_site_dev/bin/activate
  cp -R cshub_site cshub_site_dev

  cd cshub_site_dev/cshub_site

  pip install https://wadofstuff.googlecode.com/files/wadofstuff-django-serializers-1.1.0.tar.gz
  pip install -r requirements.txt

  cp secrets_example.json secrets.json
  mv secrets.json ../
  mkdir ../logs

  chgrp -R $SUDO_USER ../../cshub_site_dev
  chown -R $SUDO_USER ../../cshub_site_dev
}

function next_steps_instructions {
  echo "1. go in to the cshub_site_dev directory"
  echo "2. . bin/activiate"
  echo "3. ./manage.py syncdb"
  echo "4. ./manage.py collectstatic -n"
  echo "5. ./manage.py runserver"
}


if [ "$(uname)" == "Darwin" ]; then
  # Do something under Mac OS X platform
  if has_dependancy "brew"; then
    macosx_install
  else
    echo "you need to install homebrew before continuing."
    exit
  fi
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  # Do something under Linux platform
  debian_install

elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
  # Do something under Windows NT platform
  windows_install
  exit
fi

structure_app
echo "DONE"

#syncdb
#collectstatic -n
#runserver
