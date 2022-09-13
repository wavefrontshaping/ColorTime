
Color Time
==========

## Table of Content
1. [What is it?](#what)
2. [How does it work?](#how)
3. [Build it](#build)

## What is it? <a name="what"></a>
During scientific talks it is sometimes difficult, or akward, for the chairmen to warn speakers that they are exceeding their allotted time.
We developped a device, 
designed to be placed between the speaker and the audiance, 
that indicates using a color coded light how much time they have left. 
It also signals the time for question and the end of the allotted time with color flashes.

## How does it work? <a name="how"></a>


## Build it
### Bill of materials
* 1x Raspberry Pi Pico
* 1x 61-LED [[buy](https://www.amazon.fr/gp/product/B07L7ZPPV9/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)] [[instructions](https://www.make-it.ca/ws2812-neopixel-ring-to-attiny85/)]
* 1x HC-05 (or HC-06) Bluetooth board [Optional]
* White and black (or colored) PLA for 3d printed parts

### Assembly

### Soldering

#### LEDs
Simply follow the tutorial [here](https://www.make-it.ca/ws2812-neopixel-ring-to-attiny85/) for soldering the different rings. 
Then solder the DI digital input to GPIO 20. Use VBUS (usb power) for VCC and any GND pin for ground.

<img src="pictures/pinoutLEDs.png"  width="300">

![image](pictures/pinoutLEDs.png)

### Blueooth [optional]

Once every thing soldered, place the pico board so that the 
micro-usb socket is propery in place. 
You should be able to plug a power cord without moving the board.
You can keep the Pico in place with one drop of glue gun in the corners of the board.

![image](pictures/assembly_1.jpg)

![image](pictures/assembly_2.jpg)

### Final assembly

Use a glue gun to keep the leds in place and final snap the top white dome onto the base. 
And you are done!

## Usage


### Button commands
### Bluetooth communication

Communication is done using ASCII text message over a serial protocol. 

#### Commands
Commands are the following:
* `START`: start the countdown,
* `PAUSE`: pause the countdown, 
* `RESUME`: resume the countdown after pause,
* `STOP`: stop the countdown and swith of the LEDs
* `T{X}`: specify the time (in minutes) for a countdown and starts it, 
for instance T20 sets a countdonw for a 20-minute talk,
* `C{X}`: change the remaining time to `X` minutes.

#### Android phone

Download and install [Serial Bluetooth Terminal](https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal). 
Use the serial terminal to send commands or use buttons. 
To configure a button, long press on it, give it a name and set the commands. This is how it looks like:

![image](pictures/android.png)