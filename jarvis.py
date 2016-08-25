#!/usr/bin/env python2.7
#coding=UTF-8

# Copyright (c) 2016 Angelo Moura
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


from core.processor import Processor
import os,sys


path = os.path.abspath(os.path.dirname(sys.argv[0]))
processor = Processor()

version = "1.0"
if __name__ == "__main__":
	try:
		if sys.argv[1] == "--verbose" or sys.argv[1] == "-v":
			processor.start()
		elif sys.argv[1] == "--stop" or sys.argv[1] == "-s":
			os.system("killall python")
		elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
			processor.help(version)
		else:
			processor.backgroundstart(path)
	except IndexError:
		processor.backgroundstart(path)
