
Copyright 2013 Thomas Guething under GPLv3
Lightswitch 314 v0.1 by Thogue

A simple web application to control remote power switches. Powered by a Raspberry Pi, Flask, and Bootstrap. The goal being a simple, sleek, affordable home automation. 

Requirements:
1. rPi
2. python + flask ( http://flask.pocoo.org/docs/installation/#installation )
3. bootstrap (included) ( http://twitter.github.com/bootstrap/ )
4. Cheap remote outlets. like: http://www.amazon.com/gp/product/B0064PKG3Q
5. 6x 1k ohm resistor, 3x 100k ohm resistor, 3x NPN Transistor, 3x PNP Transistor 

This uses the flask built-in webserver which is only for development. Please see : http://flask.pocoo.org/docs/deploying/

Instructions: 

Wire it all up.... 
To find the input on the remote use a multimeter to find backside of the buttons. (the side that measures 0v when the button is not pushed and should measure 5-12v with the button pushed)
See: imggurlink

Usage:
Edit lightswitch314.py, Look at the comment for GPIO mapping
To start the server simply run the lightswitch314.py, if you want to start this at boot I would recommend looking into the above statement about deploying this with a webserver. However, a simpler, not recommended method be to use screen. For example in rc.local "screen -d -m /usr/bin/python /path/to/lightswitch314.py"
To control input http://ip:5000 into your favorite browser (Designed with mobile devices in mind)

Notes:
v0.1 : First push, hardware still on a breadboard. I assume the wiring and choice of components could still use improvement. I used what I had at the time.


Diagram w/ powering remote via rpi. 
Remove the battery from the remote. 

	<blockquote>

	a.(1 per button)
	
																						   								   	  	  				 _/ -E-- > 5V rPi
																					  	_/-C-- > [1kohm R2]-- >Base PNP2907 <_
	rPi i/o out --[1kohm R1]-- > Base NPN2222<  _	  										      				\ -C--|-- > input on remote
																					  	 \-E-- > Ground rPi < ------[100k ohm R3]---|

	b.
	-Remote -- > Ground rPi
	5v rPi -- > +Remote
	</blockquote>
