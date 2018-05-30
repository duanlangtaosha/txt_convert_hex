import re
import struct

patt = " *([0-9a-fA-F]{1,2}) +"

with open("raw2.txt", 'rb' ) as fd:
    content = fd.read()
    test = re.findall(patt, content)

with open("test.raw", 'wb') as fd:
    if (test != None):
        for i in test:
            bytes = struct.pack('B', int(i, 16))
            fd.write(bytes)


a = ['unsigned char raw[] = {']

count = 0;
if (test != None):
    for i in test:

        a.append( str(hex(int(i, 16))) + ',  ')
        count = count + 1
        if (count == 10):
            count = 0
            a.append('\n\r')

a.append('}')

a = ''.join(a)
print a
with open("array.txt", 'w') as fd:
    fd.write(a)