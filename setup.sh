#/bin/sh

echo installing system dependancies
echo ==============================
echo installing pip
apt-get install -y python-pip > setup.log
echo installing python-setuptools
apt-get install -y python-setuptools >> setup.log
echo installing virtualenv
sudo pip install virtualenv >> setup.log

echo ==============================
echo     creating virtual env
echo ==============================

cd ..
virtualenv --no-site-packages cshub_site_dev

. cshub_site_dev/bin/activate
cp -R cshub_site cshub_site_dev

cd cshub_site_dev/cshub_site

pip install https://wadofstuff.googlecode.com/files/wadofstuff-django-serializers-1.1.0.tar.gz
pip install -r requirements.txt

mv secrets_example.json secrets.json
mv secrets.json ../
mkdir ../logs

chgrp -R $SUDO_USER ../../cshub_site_dev
chown -R $SUDO_USER ../../cshub_site_dev

echo DONE

#syncdb
#collectstatic -n
#runserver
