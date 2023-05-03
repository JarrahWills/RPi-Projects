
import usb.core
import usb.util
import time
from zero_hid import HidDevice, KeyboardKeycode

# Define keycodes for Windows key and "r"
windows_key = KeyboardKeycode.GUI
r_key = KeyboardKeycode.R

# Define username and password as variables
username = "outreach.itmc"
password = "1337H4kerM4n"

# Define format string for unlock command with placeholders for username and password
unlock_command = "net user {} {} /domain"

# Format the unlock command string with the username and password variables
formatted_command = unlock_command.format(username, password)

# Define delay time to allow time for Run dialog box to appear
run_delay = 2

# Find HID device for sending keyboard inputs
device = usb.core.find(idVendor=0x1d6b, idProduct=0x0002)
if device is None:
    raise ValueError('Device not found')
    
# Create HID device object
hid_device = HidDevice(device)

# Send Windows + R key combination to open Run dialog box
hid_device.write(windows_key, r_key)
time.sleep(run_delay)

# Send unlock command to Run dialog box
for char in formatted_command:
    hid_device.write(char)
time.sleep(0.5)

# Send enter key to execute command
hid_device.write(KeyboardKeycode.ENTER)
