sudo pip3 install django==2.0
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/nginx.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#gunicorn -b 0.0.0.0:8000 hello:wsgi_application &

#git clone https://github.com/Dmitrii-Kozlov/web

sudo /etc/init.d/mysql start

mysql -uroot -e "create database web;"

mysql -uroot -e "create user 'box'@'localhost' identified by '1234';"

mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"

cd ask

python3 manage.py makemigrations

python3 manage.py migrate

gunicorn -b 0.0.0.0:8000 ask.wsgi

