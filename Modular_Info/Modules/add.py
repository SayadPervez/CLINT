#                  ADD
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
    ind=words.index("add")
    words.remove("add")
    words.insert(ind," plus ")
    return(' '.join(words))


def RUN(arg):
    arg,ret=segregate(arg,keys(),'add')
    s=arg.index("add")
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




    wk=arg
    addendum=re.findall(r"[-+]?\d*\.?\d+|[-+]?\d+",wk)
    ans=0
    numb = 0
    whateverVar = len(addendum)
    while(numb<whateverVar):
        ans+=float(addendum[numb])
        numb+=1
    mod_str = arg.replace(wk,' '+str(ans)+' ')
    print(mod_str+" "+ret)


if len(sys.argv)>1:
    RUN(sys.argv[1])
