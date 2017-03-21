Autopush-vapid-tests
====================

End-to-end Android emulator (client-side) tests for testing Mozilla autopush server.

Todo
----

* Get mup test
 * open Firefox Browser
 * open test URL
* Run on Jenkins-dv Linux slave
* Move to rmozilla-services
* add test to service book
* url checks
 
One-time Setup
-----

# install nvm
0. sudo apt-get update 
1. sudo apt-get remove --purge node 
2. sudo apt-get install build-essential python3-pip python3-dev libffi-dev python3-venv checkinstall 
3. sudo apt-get install libssl-dev virtualenv 
4. curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh | bash 
5. nvm install 5.0
6. nvm use 5.0
7. nvm alias default node 

# install appium server
8. npm install -g appium

# install pip and virtualenv
9. sudo apt install python-pip

# install android sdk
10. download android studio from:  https://developer.android.com/studio
11. cp *.zip /usr/local
12. sudo unzip /usr/local/*.zip




Test Setup
-----

1. virtualenv venv
2. pip install -r requirements.txt
3. appium &
