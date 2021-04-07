import sys

def RUN(arg):
    d=int(arg[arg.index('timer')+5:])
    print(f"""
$-$
P.delay(15)
P.say('start')
P.delay({int(d/2)-4})
P.say('half')
P.delay({int(d/4)-3})
P.say('quarter')
x={int(d/4)}
while(x!=0):
    x-=1
    P.say(x)
P.say("OVER AND OVER")
""")

if len(sys.argv)>1:
    RUN(sys.argv[1])
