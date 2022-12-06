f = open('in.in','r')

l = f.read()

buf = []

for i in range(0, len(l)):
    buf = l[i:i+14]
    bufset = set(buf)
    if(len(bufset) == 14):
        print(i+14)
        break
