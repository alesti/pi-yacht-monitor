from webiopi.devices.digital import PCF8574

# Setup a PCF8574 on I2C slave 0x20 (default)
pcf0 = PCF8574()
# or
pcf0 = PCF8574(slave=0x20)

# Setup a PCF8574 on I2C slave 0x21
pcf1 = PCF8574(slave=0x21)