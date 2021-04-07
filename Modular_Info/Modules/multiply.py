import sys
sys.path.insert(0,'P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Spec_Functions')
import Pvz_Functions as P
import re
from Modular_Functions import *

def rmStr(str,rempart):
    if rempart in str:
        mod_str=str.replace(rempart,'',1)
        return(mod_str)

def reDirect(string):

    words=string.split()
    ind=words.index("multiply")
    words.remove("multiply")
    words.insert(ind," into  ")
    try:
        words.remove('by')
    except Exception as e:
        pass
    return(' '.join(words))

def RUN(arg):
    arg=P.akapi(remSymb(arg))
    arg,ret=segregate(arg,keys(),['multiply','by'])
    s=arg.index("multiply")
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
        wk=reDirect(arg)
        print(wk+" "+ret)
        exit()
    else:
        addendum=re.findall(r"[-+]?\d*\.?\d+|[-+]?\d+",arg)
        addendum=[float(i) for i in addendum]
        ans=1
        for _ in range(len(addendum)):
            ans*=addendum[_]
        print(str(ans)+"  "+ret)

this="5 multiplied by 5 multiplied by 5"
if len(sys.argv)>1:
    RUN(sys.argv[1])
else:
    RUN(this)
