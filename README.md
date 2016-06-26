# Jarvis

Jarvis is a python voice command assistant that uses the Arduino Leonardo keyboard library more speech recognition
Google API to control the GNU / Linux operating systems by voice commands, for example , browse the web and input , delete, and press the keystrokes like Return or TAB with the keyboard using the bridge between the voice recognition and Arduino Leonardo keyboard library.

# Installation 

To enable all Jarvis functions correctly it will be necessary to have an Arduino Leonardo and a GNU/Linux gnome graphic environment.

Steps>
open a terminal <br />
$sudo git clone https://github.com/m4n3dw0lf/Jarvis/ <br />

(OPTIONAL)<br />
plug your Arduino Leonardo <br />
open the arduino IDE > Tools > Board then select Arduino Leonardo <br />
go to Tools> Serial port and check the serial port of the Arduino Leonardo <br />
press CTRL+O <br />
navigate to the directory: path/../Jarvis/core/heart/jarvis/ <br />
select the jarvis.ino file then upload to the Arduino Leonardo. <br />
(CLOSE OPTIONAL) <br />

$cd Jarvis <br/>
$sudo pip install -r requirements.txt <br />
$sudo ./jarvis.py<br />

# Voice Commands

- help:	 		Print a help message.<br />

- exit:		 	Terminate the program.<br />

- sleep:		Sleep untill you say "Jarvis".<br />

- newspaper:		Read the top trending news from reddit.<br />

- say [message]:      	Ask Jarvis to say something.<br />

 examples:<br />

  say i like donnuts<br />
  say my name is jarvis<br />

- run [script]:		Run .sh script the you place on the scripts folder with chmod +x<br />

 example:<br />

  run firewall		| Place a firewall.sh on the scripts folder and give execution privilege first<br />

- start [program]:	Ask Jarbas to start a program below.<br />

	* ARDUINO LEONARDO REQUIRED *<br />

 browser   = start google-chrome browser<br />
 terminal  = start a terminal<br />

- editor: 		Start the editor mode.<br />

	* ARDUINO LEONARDO REQUIRED * <br />

	[EDITOR MODE]

voice commands: (anything else will be typed)<br />

 - forward   = tab
 - back      = (shift+tab)
 - up        = up arrow
 - down      = down arrow
 - right     = right arrow
 - left      = left arrow
 - super     = super/windows
 - slash     = slash(/)
 - backspace = backspace(erase character)
 - erase     = press backspace 10 times
 - space     = space(spacebar)
 - enter     = enter(return)
 - close     = close(alt+f4)
 - escape    = escape(esc)
 - exit	     = leaves editor mode<br />


by: m4n3dw0lf
