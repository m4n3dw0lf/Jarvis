# Jarvis v1.0

Jarvis, python voice controlled assistant.
 

## Installation 

### Dependencies
- libasound-dev 
- libjack-jackd2-dev 
- portaudio19-dev 
- python-pyaudio 
- build-essential 
- python-dev 
- libespeak1


### Installation Guide
- $sudo apt-get install libasound-dev libjack-jackd2-dev portaudio19-dev python-pyaudio build-essential python-dev libespeak1
- $sudo git clone https://github.com/m4n3dw0lf/Jarvis
- $cd Jarvis
- $sudo pip install -r requirements.txt
- $sudo ./jarvis.py -h


## Basics

- Start Jarvis as subprocess.
```
./jarvis.py
```

- Help message.
```
./jarvis.py -h
     or
./jarvis.py --help
```

- Stop Jarvis process running in background.
```
./jarvis.py -s
     or
./jarvis.py --stop
```

- Start Jarvis in verbose mode.
```
./jarvis.py -v
     or
./jarvis.py --verbose
```

