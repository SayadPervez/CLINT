import sys

def RUN(arg):
    print(f"""
$-$
P.say('{arg[arg.index("say")+3:]}')""")

if len(sys.argv)>1:
    RUN(sys.argv[1])
