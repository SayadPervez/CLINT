#                  SUBTRACT
import sys
sys.path.insert(0,'P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Spec_Functions')
import Pvz_Functions as P
file="P:\\Pvz_Program_Files\\Common trial notepad file.txt"
import re
from Modular_Functions import *#

def rmStr(str,rempart):
    if rempart in str:
        mod_str=str.replace(rempart,'',1)
        return(mod_str)

def reDirect(string):

    words=string.split()
    ind=words.index("subtract")
    words.remove("subtract")
    words.insert(ind," minus ")
    return(' '.join(words))

def RUN(arg):
        arg,ret=segs(arg,keys(),'subtract')
        s=arg.index("subtract")
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
            if 'from' in arg:
                addendum=re.findall(r"[-+]?\d*\.?\d+|[-+]?\d+",arg)
                addendum=[float(i) for i in addendum]
                mod_str=addendum[1]-addendum[0]
            else:
                mod_str=""
        #addendum=re.findall(r"[-+]?\d*\.?\d+|[-+]?\d+",arg)

        print(str(mod_str)+" "+ret)


if len(sys.argv)>1:
    RUN(sys.argv[1])
