# Introduction
This is a python program to continuously check for game updates and updating a Postgres database 

# Prerequisites
## Ubuntu
This program is created using Ubuntu 21.10. It may work flawlessly on other distros or may require some tinkering.

## Postgres 
The database used is Postgres version 13.7. It can be installed in Ubuntu from the commandline using
`sudo apt-get install postgresql`.
A database with the name `roblox-game-tracker` will need to be manually created in Postgres, perhaps using the
following steps after installing Postgres. 

`sudo -u postgres createuser user` where user will be running the Python program.



## Python
This program uses Python 3.9.7 in a virtualenv created by Pycharm. Interaction between Python and Postgres will be done
using psycopg2 module. A `requirements.txt` file is included to facilitate installation of required modules. The virtual
environment is not included

## Chromium and Selenium
This program will utilize the Selenium testing framework together with the Chromium browser to access Roblox


