# py-jemma-lametric-button-server

Simple python server listening to triggers from lametric app

# How does it work

This is a simple python server running on port 9999.

It just listens to http://192.168.1.196:9999/lametric-server/<program> and runs a dedicated function on button press.

# Available programs

- **normal**: all lights normal
- **red**: all lights red
- **discoparty**: starts/stops a thread running discoparty

# Requirements

- A lametric device
- A JEMMA installation
- Some Philips UE lightbulbs

# Related projects

- [ismb/py-jemma-dal-rest-client](https://github.com/ismb/py-jemma-dal-rest-client)

# HowTo

- Clone this repo on your gateway e.g. Raspberry PI
- hook it in the startup scripts
- Make a simple button application with the trigger link of your server and program
	- e.g. ```http://192.168.1.196:9999/lametric-server/normal```



