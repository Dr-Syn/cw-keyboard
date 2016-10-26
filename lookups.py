#lookups.py
morse = {
	'.-': 'a',
	'-...': 'b',
	'-.-.': 'c',
	'-..': 'd',
	'.': 'e',
	'..-.': 'f',
	'--.': 'g',
	'....': 'h',
	'..': 'i',
	'.---': 'j',
	'-.-': 'k',
	'.-..': 'l',
	'--': 'm',
	'-.': 'n',
	'---': 'o',
	'.--.': 'p',
	'--.-': 'q',
	'.-.': 'r',
	'...': 's',
	'-': 't',
	'..-': 'u',
	'...-': 'v',
	'.--': 'w',
	'-..-': 'x',
	'-.--': 'y',
	'--..': 'z',
	'-----': '0',
	'.----': '1',
	'..---': '2',
	'...--': '3',
	'....-': '4',
	'.....': '5',
	'-....': '6',
	'--...': '7',
	'---..': '8',
	'----.': '9',
	'.-.-': 'cr', #carriage return
	'.-.-.-': '.',
	'--..--': ',',
	'-....-': '-',
	'.-...': 'sp', #space
	'--.-.-': 'sh', #shift
	'........': 'er' #error - backspace
	'....-.-.': 'esc' #escape key
}


kbmap = dict()
kbmap['a'] = (0x04)
kbmap['b'] = (0x05)
kbmap['c'] = (0x06)
kbmap['d'] = (0x07)
kbmap['e'] = (0x08)
kbmap['f'] = (0x09)
kbmap['g'] = (0x0A)
kbmap['h'] = (0x0B)
kbmap['i'] = (0x0C)
kbmap['j'] = (0x0D)
kbmap['k'] = (0x0E)
kbmap['l'] = (0x0F)
kbmap['m'] = (0x10)
kbmap['n'] = (0x11)
kbmap['o'] = (0x12)
kbmap['p'] = (0x13)
kbmap['q'] = (0x14)
kbmap['r'] = (0x15)
kbmap['s'] = (0x16)
kbmap['t'] = (0x17)
kbmap['u'] = (0x18)
kbmap['v'] = (0x19)
kbmap['w'] = (0x1A)
kbmap['x'] = (0x1B)
kbmap['y'] = (0x1C)
kbmap['z'] = (0x1D)
kbmap['1'] = (0x1E)
kbmap['2'] = (0x1F)
kbmap['3'] = (0x20)
kbmap['4'] = (0x21)
kbmap['5'] = (0x22)
kbmap['6'] = (0x23)
kbmap['7'] = (0x24)
kbmap['8'] = (0x25)
kbmap['9'] = (0x26)
kbmap['0'] = (0x27)
kbmap['sp'] = (0x2C)
kbmap['cr'] = (0x28)
kbmap['-'] = (0x2D)
kbmap['.'] = (0x37)
kbmap[','] = (0x36)
kbmap['er'] = (0x2A)
kbmap['esc'] = (0x29)

