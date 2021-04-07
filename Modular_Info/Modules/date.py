import sys
sys.path.insert(0,'P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Spec_Functions')
import Pvz_Functions as P
from Modular_Functions import *

def RUN(arg):
    arg=P.akapi(remSymb(arg))
    arg,rets=segregate(arg,keys(['and','then']),['date','display','show'])
    print(f'$-$print("{P.date()} {P.month()} {P.year()}")\nP.say("{P.date()} {P.month()} {P.year()}") %-%-%{rets}')

if len(sys.argv)>1:
    RUN(sys.argv[1])
