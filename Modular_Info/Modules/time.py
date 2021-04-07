import sys
sys.path.insert(0,'P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Spec_Functions')
import Pvz_Functions as P
from Modular_Functions import *

def RUN(arg):
    def APM():
        x='AM' if P.hours()<=12 else 'PM'
        return(x)
    arg=P.akapi(remSymb(arg))
    arg,rets=segregate(arg,keys(['and','then']),['time','display','show'])
    print(f'$-$print("{abs(P.hours() if 0>P.hours()<=12 else P.hours()-12)}:{P.minutes()}:{P.seconds()} {APM()}")\nP.say("{abs(P.hours() if 0>P.hours()<=12 else P.hours()-12)}:{P.minutes()}:{P.seconds()} {APM()}") %-%-%{rets}')

if len(sys.argv)>1:
    RUN(sys.argv[1])
