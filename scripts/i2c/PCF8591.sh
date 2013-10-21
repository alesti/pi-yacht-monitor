# Adresse rausfinden mit "i2cdetect -y 1"
# In diesem Fall 0x48
#      0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
# 00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
# 10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
# 20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
# 30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
# 40: -- -- -- -- -- -- -- -- 48 -- -- -- -- -- -- -- 
# 50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
# 60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
# 70: -- -- -- -- -- -- -- --

# Es gibt 4 Analog-Ports (0 - 3)
# Es soll der 4. abgefragt werden (also nummer 3)
i2cset -y 1 0x48 0x03

# Wert auslesen
i2cget -y 1 0x48

# Beispiel:
# Ausgabe: 0x9b
# => 155
# Wenn der Spannungsteiler auf 10V ausgelegt ist, 
# ist die Spannung am Port nun: (10/255)*155
# => 6.0784 V



