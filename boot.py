#boot.py
import machine
import pyb
#pyb.main('main.py') # main script to run after this one
#pyb.usb_mode('CDC+MSC') # act as a serial and a storage device
pyb.usb_mode('CDC+HID',hid=pyb.hid_keyboard)
