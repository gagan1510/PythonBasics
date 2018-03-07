import struct

x = 10
y = "p"
z = 4.5
m = struct.pack("if", x, z) # stores the values of variables in the form of a string
print(m)
up = struct.unpack("if",m) # gives back the stored values in the string in the form of a tuple
print(up)