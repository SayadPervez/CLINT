import sys
sys.path.insert(0,"P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Spec_Functions")
import Pvz_Functions as P
from Modular_Functions import *

def RUN(arg):
    stuff="""
Hey there. myself CLINT , Command Line Interface NLP Tool. Version 87.3

I was built by Pervez, in order to be a personal assistant, and help him with his projects.
JARVIS was the inspiration behind my idea.
Even though am not perfect yet, I soon will be.
    """
    arg=P.akapi(arg)
    if('introduce yourself' in arg):
        arg=arg.replace('introduce yourself','intro')
    #print(arg)
    print("arg:"+str(arg))
    arg,ret=segregate(arg,keys(['and','then']),'intro')

    print(f"""
$-$
P.say('''{stuff}''')
%-%-%{ret}
    """)

if len(sys.argv)>1:
    RUN(sys.argv[1])
else:
    RUN('introduce yourself and exit')
