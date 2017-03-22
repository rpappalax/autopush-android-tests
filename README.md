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

# virtualbox
* if installing on VirtualBox, make sure to choose: "install this system permanently to your hard disk"

# install nvm
0. sudo apt-get update -y
1. sudo apt-get remove --purge node 
2. sudo apt install build-essential python3-pip python3-dev libffi-dev python3-venv checkinstall -y
3. sudo apt install libssl-dev virtualenv  -y
4. curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh | bash 
5. exec bash
6. nvm install 5.0
7. nvm use 5.0
8. nvm alias default node 

# install appium server
9. npm install -g appium

# install pip and virtualenv
10. sudo apt install python-pip -y

# install android sdk
11. download android tools (not studio) from here:  https://developer.android.com/studio
    note: the link for tools is just below that for studio.
12. cp *.zip /usr/local
13. sudo unzip /usr/local/*.zip


Test Setup
-----

1. virtualenv venv
2. pip install -r requirements.txt
3. appium &
