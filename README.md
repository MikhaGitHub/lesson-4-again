# SpaceXphotos

This code downloads astronomical images from different services, for example: SpaceX, Epic, APOD and other... and publishes them in a telegram channel


## How to install

In this project { NASA APIs } requires a key.
Link to the site: https://api.nasa.gov/#epic

Also you should add the bot token to the code.
All tokens and sensitive data should be hidden in the .env file.

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```pip install -r requirements.txt```

In this project, the code is handled via the command line using the argparse library.
![image](https://github.com/user-attachments/assets/c78147a6-773d-42dd-bfa1-152426c311f5)

Go to the your directory where locate your files project
and paste this command:

```python main.py```
This command is the default

Command with all arguments(for example):

```python main.py 4 spaceX_1.jpg```

4 is frequency of publication
(on the default is 4 hour)
spaceX_1.jpg is name of file which you want to publicate to the channel(on the default is random img from dir)
