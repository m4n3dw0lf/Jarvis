# Jarvis

Jarvis is a python voice command assistant library that i have been developing as feature of my pentest framework PytheM
link: https://github.com/m4n3dw0lf/PytheM<br/>
the aim of this Jarvis project is to enable any developer to use Jarvis in their work<br/>
 

# Installation 
- $sudo git clone https://github.com/m4n3dw0lf/PytheM

##Jarvis needs external libraries such SpeechRecognition and pyttsx, to install the libraries you need to run: <br />

- $cd Jarvis
- $sudo pip install -r requirements.txt <br />
 (if PyAudio gcc error)<br />
 $sudo apt-get update<br />
 $sudo apt-get install libasound-dev libjack-jackd2-dev portaudio19-dev python-pyaudio<br />
 $sudo pip install -r requiremenst.txt<br /> 
 (Close PyAudio error) <br />

move the jarvis.py script to the folder of your project create a new script and import jarvis<br />

### Example
```
#!/usr/bin/python2.7

# or another directory like core.jarvis
from jarvis import Jarvis

jarvis = Jarvis()

jarvis.Say("Hello World!")
jarvis.Say("What is your name?")
response = jarvis.Listen()
print response
jarvis.Say(response)
```


