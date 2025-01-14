# SpaceXphotos

This code downloads astronomical images from different services, for example: SpaceX, Epic, APOD and other... and publishes them in a telegram channel
![image](https://github.com/user-attachments/assets/b1121438-80e5-4723-abe5-225f174464de)



## How to install

In this project { NASA APIs } requires a key.
Link to the site: 
```
https://api.nasa.gov/#epic
```

Also you should add the bot token to the .env file.
All tokens and sensitive data should be hidden in the .env file!
![image](https://github.com/user-attachments/assets/bc52b02b-ba73-4d17-a84a-d31489daa793)


1.create your virtual environment in Python on the operating system (Linux/macOS):




```python
python3 -m venv venv
```





(windows):
```python
python -m venv
```

2.Activate (Linux/macOS):
```python
source venv/bin/activate
```
(Windows):
```python
venv\Scripts\activate
```

3.Install dependencies
```python
pip install -r requirements.txt
```

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:


In this project, the code is handled via the command line using the argparse library.
![image](https://github.com/user-attachments/assets/307ea0cb-351d-4be2-b92f-a8b10277d8cc)


Go to the your directory where locate your files project
and paste this command:

![image](https://github.com/user-attachments/assets/4b5f6fc1-286c-4760-add5-5710643ffdd7)


```python
python {name of file}
```
This command is the default

Command with all arguments(for example):

```python
python apod.py --folder newimages
```
apod.py - name file
--folder newimages - folder in which you will download images
![image](https://github.com/user-attachments/assets/996b191b-b692-4406-9475-ef52ae785b6f)


Use --help to view how it work



![image](https://github.com/user-attachments/assets/8d8577fa-fc1a-457f-907a-f4e1e657a3bd)



![image](https://github.com/user-attachments/assets/d3cc2f53-c80c-47fb-b2f2-7ab026766def)


to the channel(on the default is random img from dir)
