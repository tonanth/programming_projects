# Introduction
This is a python program to continuously check for game updates.

# Prerequisites
## Ubuntu
This program is created using Ubuntu 21.10. It may work flawlessly on other distros or may require some tinkering.

## PostgreSQL
The database used is PostgreSQL version 13.7. It can be installed in Ubuntu from the commandline using \
`sudo apt-get install postgresql` \
A database with the name `roblox-game-tracker` will need to be manually created in PostgreSQL, perhaps using the
following steps after installing \
`sudo -u postgres createuser $user` where $user will run the program

## Python
This program uses Python 3.9.7 in a virtualenv created by Pycharm. Interaction between Python and Postgres will be done
using psycopg module. 

## Chromium and Selenium


