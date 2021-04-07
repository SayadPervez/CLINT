import sys
import os

def leo(string):#list em out
    ret=string.split(' ')
    x=ret.count("")
    for _ in range(x):
        ret.remove("")
    return(ret)

import sys
sys.path.insert(0,'P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Spec_Functions')
import Pvz_Functions as P

def keys(exceptions=None):
    key=P.extract("P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Modular_Files\\Modular_Info\\Defined_Modules.txt",'^@^^#')
    if(exceptions!=None) and (type(exceptions)==type("fd")):
        key.append(exceptions)
    elif(exceptions!=None) and (type(exceptions)==type([])):
        for _ in range(len(exceptions)):
            key.append(exceptions[_])
    return(key)

def summation(string,wordIndex):
    stli=string.split(' ')
    x=stli.count("")
    for _ in range(x):
        stli.remove('')
    li=stli[:wordIndex]
    rest=' '.join(li)
    ret=len(rest)
    return(ret+1)

def segregate(string,key,excep):
    '''
    string takes the whole raw input string
    key takes the return value of key function
    exception takes the key word to ignore...... (i.e.) play for play.py and so on

    returns:
    the string to work with and the string to be returned as it is
    '''
    lis=list()
    #replacing multiple empty spaces with single one !!
    l=string.split(' ')
    q=l.count('')
    for _ in range(q):
        l.remove("")
    string=' '.join(l)
    if type(excep)==type("kdj"):
        try:
            key.remove(excep)
        except Exception as e:
            pass
    elif type(key)==type([]):
        for _ in range(len(excep)):
            try:
                key.remove(excep[_])
            except Exception as e:
                pass
    i=0
    while(i<len(key)):
        if(key[i] in leo(string)):
            w=leo(string).index(key[i])
            lis.append(summation(string,w))
        i+=1
    if(lis==[]):
        return(string,"")
    else:
        m=min(lis)
        workPiece=string[:m]
        rets=string[m:]
        return(workPiece,rets)

def remSymb(string):
    for _ in range(len(string)):
        curr=string[_]
        if(97<=ord(curr)<=122) or (65<=ord(curr)<=90) or (48<=ord(curr)<=57) or ord(curr)==46:
            pass
        else:
            string=string.replace(curr," ")
    return(string)

def segs(a,k,ex):
    '''
    ADVANCED version of segregate function !!
    '''
    if(type(ex)==type([])):
        ex=ex[0]
    arg,rets=segregate(a,k,ex)
    wds=arg.split(' ')
    wds[wds.index(ex)]='&^%$#'
    arg=' '.join(wds)
    arg1,rets1=segregate(arg,keys(),'&^%$#')
    rets=rets1+" "+rets
    arg=arg1.replace('&^%$#',ex)
    return(arg,rets)
