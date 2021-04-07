import sys
sys.path.insert(0,'P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Spec_Functions')
import Pvz_Functions as P
from Modular_Functions import *


def RUN(for_sure_it_will_be_cls):
    for_sure_it_will_be_cls=P.akapi(for_sure_it_will_be_cls)
    arg,ret=segregate(for_sure_it_will_be_cls,keys(),'cls')
    print(f'''
$-$
import sys
sys.path.insert(0,"P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Spec_Functions")
import Pvz_Functions as P
import os
os.system(P.decode("enu"))
%-%-%{ret}''')

if len(sys.argv)>1:
    RUN(sys.argv[1])
