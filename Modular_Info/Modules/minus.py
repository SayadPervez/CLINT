import sys
sys.path.insert(0,'P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Spec_Functions')
import Pvz_Functions as P
import re
from Modular_Functions import *

def RUN(arg):
    arg,rets=segs(arg,keys(),['minus'])

    i=arg.index("minus")
    pre_=arg[:i]
    post_=arg[i+5:]
    pre=re.findall(r'[-+]?\d*\.?\d+|[-+]?\d+',pre_)
    post=re.findall(r'[-+]?\d*\.?\d+|[-+]?\d+',post_)
    pre=[float(i) for i in pre]
    post=[float(i) for i in post]

    result = float(pre[-1]) - float(post[0])
    print(str("")+str(result)+" "+str(rets))

if len(sys.argv)>1:
    RUN(sys.argv[1])
