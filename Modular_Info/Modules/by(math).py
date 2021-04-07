import sys
sys.path.insert(0,'P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Spec_Functions')
import Pvz_Functions as P
import re
from Modular_Functions import *

def rmStr(str,rempart):
    if rempart in str:
        mod_str=str.replace(rempart,'',1)
        return(mod_str)

def RUN(arg):
    arg=P.akapi(remSymb(arg))
    arg,ret=segs(arg,keys(),'by')
    s=arg.index("by")
    pre_,post_=arg[:s],arg[s+3:]
    if "-" not in pre_:
        pre=re.findall(r'[-+]?\d*\.\d+|\d+',pre_)
    else:
        pre=re.findall(r'[-+]?\d*\.\d+|\d+',pre_)[0]
        pre=float(pre)*-1
        pre=[pre]
    if "-" not in post_:
        post=re.findall(r'[-+]?\d*\.\d+|\d+',post_)
    else:
        post=re.findall(r'[-+]?\d*\.\d+|\d+',post_)[0]
        post=float(post)*-1
        post=[post]
    if len(pre)>0 and len(post)>0:
        ans=float(pre[-1])/float(post[0])
        print(str(ans)+"  "+ret)

this="5 into 6 multiplied by 7"
if len(sys.argv)>1:
    RUN(sys.argv[1])
else:
    RUN(this)
