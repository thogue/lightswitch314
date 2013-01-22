#!/usr/bin/python
# This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>#
# 
# Lightswitch314  by thogue 01.02.2013
#
from time import sleep
from flask import Flask, render_template, redirect, url_for
#
import RPi.GPIO as GPIO
#
# GPIO pins -> button mapping. change as needed
ONE=18
TWO=24
THREE=25
GPIO.setmode(GPIO.BCM)
GPIO.setup(ONE, GPIO.OUT)
GPIO.setup(TWO, GPIO.OUT)
GPIO.setup(THREE, GPIO.OUT)
# Make sure pins are low
# do we need todo this?
#
GPIO.output(ONE,False)
GPIO.output(TWO,False)
GPIO.output(THREE,False)
#
# Momentarily go HIGH to simulate button push on remote
# Adjust sleep for longer "pushes"
#
class switch:
	def one(self):
		GPIO.output(ONE,True)
		sleep(.2) 
		GPIO.output(ONE,False)
	def two(self):
		GPIO.output(TWO,True)
		sleep(.2)
		GPIO.output(TWO,False)
	def three(self):
		GPIO.output(THREE,True)
		sleep(.2)
		GPIO.output(THREE,False)

app = Flask(__name__)

swit = switch()

# Return bootstrap template.
@app.route('/')
def index():
	return render_template('index.html')

# Trigger switches and return /
@app.route('/switchone')
def switchone():
	# Trigger switch 1
	swit.one()
	# After switch, return the index, preventing accidental pushes on refreshes or mobile devices
	return redirect(url_for('index'))

@app.route('/switchtwo')
def switchtwo():
	# Trigger switch 2
	swit.two()
	return redirect(url_for('index'))

@app.route('/switchthree')
def switchthree():
	# Trigger switch 3
	swit.three()
	return redirect(url_for('index'))

# Flask dev webserver
if __name__ =='__main__':
	app.run( host='0.0.0.0',port=5000)
# Add gpio cleanup
