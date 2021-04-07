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
    try:
        words.remove('by')
    except Exception as e:
        pass
    ind=words.index("divide")
    words.remove("divide")
    words.insert(ind," by  ")
    return(' '.join(words))

def RUN(arg):
    arg=P.akapi(remSymb(arg))
    arg,ret=segregate(arg,keys(),['divide','by'])
    print(arg)
    s=arg.index("divide")
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
        ans=float(addendum[0])/float(addendum[1])
        print(str(ans)+"  "+ret)


this="15 divide by 5 divide by 3"
if len(sys.argv)>1:
    RUN(sys.argv[1])
else:
    RUN(this)
