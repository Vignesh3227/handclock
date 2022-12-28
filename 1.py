n=input('Enter time: ').split(":")
if int((n[0]))>12:
     hr=int(n[0])-12
else:
    hr=int(n[0])
mm=int(n[1])
d=0

if hr<13 and mm<60:
    d=((hr*360)//12+(mm*360)//(12*60))-(mm*360)//60
if d>180:
    d=360-d
if d<0:
    print(str(-d)+chr(176))
else:
    print(str(d)+chr(176))
