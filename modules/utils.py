#!/usr/bin/env python2.7
#coding=UTF-8

# Copyright (c) 2016 m4n3dw0lf
#
# This file is part of the program Jarvis
#
# Jarvis is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA


def print_help(version):
	print """\n
[ Jarvis - Personal Assistence - v{} ]

[*] help:	 	Print this help message.

[*] exit:	 	Terminate the program.

[*] sleep:		Sleep untill you say "Jarvis"

[*] newspaper:		Read the top trending news from reddit.

[*] say [message]:      Ask Jarbas to say something.

 examples:

  say i like donnuts
  say my name is jarvis

[*] run [script]:	Run .sh script that you place on the scripts folder with chmod +x

  example:

   run firewall		| Place a firewall.sh on the scripts folder and give execution privilege first

[*] start [program]:	Ask Jarbas to start a program.

	* ARDUINO LEONARDO REQUIRED *

voice commands:

 browser   = start google-chrome browser
 terminal  = start a terminal

[*] editor: 		Start the editor mode.

	* ARDUINO LEONARDO REQUIRED *

	[EDITOR MODE]

voice commands: (anything else will be typed)

 forward   = tab
 back      = (shift+tab)
 up        = up arrow
 down      = down arrow
 right     = right arrow
 left      = left arrow
 super     = super/windows
 slash     = slash(/)
 backspace = backspace(erase character)
 erase	   = press backspace 10 times
 space     = space(spacebar)
 enter     = enter(return)
 close	   = close(alt+f4)
 escape    = escape(esc)

 exit	   = leaves editor mode


by: m4n3dw0lf
""".format(version)
