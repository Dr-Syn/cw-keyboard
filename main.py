import pyb
from pyb import Pin
from pyb import LED
import lookups

p_in = Pin('X2', Pin.IN, Pin.PULL_UP)
led = LED(2)
kb = pyb.USB_HID()
kbuf = bytearray(8)

# Pin X2 bridged to ground via key
# 10hz sample rate - 1 tick = .1 sec

state = 0 #initialize state to 0
shift = 0 #initialize shift to 0
charbuf = '0'
#charbuf = 0 for empty; . for dot; - for dash


def getpin(pin):
	led.off()
#	cur_value = not pin.value()
	cur_value = 1 #hardcoding this b/c maybe pin.value is screwing up
	active = 0
	inactive = 0
	while active < 200:
		if pin.value() != cur_value:
			active += 1
			pyb.delay(1)
			inactive = 0
		else:
			active = 0
			pyb.delay(1)
			inactive += 1
			if inactive < 600:
				return '0'
	while active < 400:
		led.on()
		if pin.value() != cur_value:
			active += 1
			pyb.delay(1)
		else: 
			led.off()
			return '.'
	while active < 600:
		led.on()
		if pin.value() != cur_value:
			active += 1
			pyb.delay(1)
		else:
			led.off()
			return '-'
	while (pin.value() != cur_value):
		pyb.delay(1)
	led.off()
	pyb.delay (200) # delay for rekey
	return '-'

def sendchar(charbuf, shift):
	result = lookups.morse[charbuf]
#	print("Result is %s" % result)
	if result == 'sh':
		if shift == 0:
			shift = 1
		else:
			shift = 0
		charbuf = 0
		return '0'
	if shift == 0:
		kbuf[0] = 0x00
	if shift == 1:
		kbuf[0] = 0x02
	kbuf[2] = lookups.kbmap[result]
	kb.send(kbuf)
#	print("Sent character")
	pyb.delay(10) # This delay required else it repeats the key
	kbuf[0] = 0x00
	kbuf[2] = 0x00 # Must reset else it's like holding the key down
	kb.send(kbuf)
	pyb.delay(10)
	return '0'

while(1):
	pyb.delay(200) # recovery
	state = getpin(p_in)
	if (state == '.'):
		if charbuf == '0':
			charbuf = state
		else:
			charbuf += state
#		print ("The state is %s\n" % state)
#		print ("charbuf is %s\n" % charbuf)
	if (state == '-'):
		if charbuf == '0':
			charbuf = state
		else:
			charbuf += state
#		print ("The state is %s\n" % state)
#		print ("charbuf is %s\n" % charbuf)
	if (state == '0'):
		if (charbuf != '0'):
#			print("Attempting to send character\n")
			sendchar(charbuf, shift)
			charbuf = '0'
			state = '0'
#			print("State restored")
	pyb.delay(10)
