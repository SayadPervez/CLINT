import sys
sys.path.insert(0,'P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Spec_Functions')
import Pvz_Functions as P
from Modular_Functions import *

def RUN(arg):
    def day():
        x=P.caps(P.day())
        if(x=='sun'):
            return("Sunday")
        elif(x=='mon'):
            return("Monday")
        elif(x=="tue"):
            return("Tuesday")
        elif(x=="wed"):
            return("Wednesday")
        elif(x[:3] in 'thursday'):
            return("Thursday")
        elif(x=='fri'):
            return("Friday")
        elif(x=="sat"):
            return("Saturday")
    def order():
        return(f"A {day()} of {P.month()} {P.date()} {P.year()}")
    arg=P.akapi(remSymb(arg))
    arg,rets=segregate(arg,keys(['and','then']),['today','display','show'])
    print(f'$-$print("{order()}")\nP.say("{order()}") %-%-%{rets}')

if len(sys.argv)>1:
    RUN(sys.argv[1])
