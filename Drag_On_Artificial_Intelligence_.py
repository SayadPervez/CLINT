import sys
sys.path.insert(0,'P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Spec_Functions')
import Pvz_Functions as P
import time
import subprocess
from colorama import init
import pyttsx3
from termcolor import colored
init()
import os
ud_txt="P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Modular_Files\\Modular_Info\\Undefined_Modules..txt"
d_txt="P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Modular_Files\\Modular_Info\\Defined_Modules.txt"

akaFile="P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Modular_Files\\Modular_Info\\aka_dictionary.txt"

def leo(string):#list em out
    ret=string.split(' ')
    x=ret.count("")
    for _ in range(x):
        ret.remove("")
    return(ret)

def csvList(string):
    try:
        li=string.split(',')
        return(li)
    except Exception as e:
        print(e)

def akaReadLine(i):
    try:
        with open(akaFile,'r') as f:
            return(f.readlines()[i])
    except Exception as e:
        print(e)

def akaDisplay(clr="red"):
    try:
        n=P.lenline(akaFile)
        for _ in range(n):
            P.colour(str(_)+"\t--->"+akaReadLine(_).replace("\n",""),"white",clr)
    except Exception as e:
        print(e)

def __all():
    try:
        all=[]
        for _ in range(P.lenline(akaFile)):
            all.append(akaReadLine(_).replace("\n",""))
        a=[]
        for _ in range(len(all)):
            a+=all[_].split(',')
        x=a.count('')
        for _ in range(x):
            a.remove("")
        return(a)
    except Exception as e:
        print(e)

def akaAdd(addendum=None):
    try:
        if(addendum!=None):
            inp=addendum
            if inp in __all():
                P.colour("Given command pre-exists !!","red","black")
            elif(inp==""):
                P.colour("Can't add empty cmd !!","red","black")
            elif(P.compress(P.elements(inp))==[" "]):
                P.colour("Can't add empty cmd !!","red","black")
            else:
                with open(akaFile,'a') as f:
                    f.write(inp+",\n")
        else:
            akaDisplay()
            P.colour("Give index if cmd-type pre-exists\nElse give the cmd to be added:","white","red")
            inp=input("@k@pi->")
            if inp in __all():
                P.colour("Given command pre-exists !!","red","black")
            elif(inp==""):
                P.colour("Can't add empty cmd !!","red","black")
            elif(P.compress(P.elements(inp))==[" "]):
                P.colour("Can't add empty cmd !!","red","black")
            else:
                if(P.input_type(inp)=="$#Alpha_type#$"):
                    with open(akaFile,'a') as f:
                        f.write(inp+",\n")
                else:
                    ln=int(inp)
                    inp=input("Give cmd\n@k@pi->")
                    all=[]
                    for _ in range(P.lenline(akaFile)):
                        all.append(akaReadLine(_))
                    all[ln]=all[ln].replace("\n",inp+",\n")
                    with open(akaFile,'w') as w:
                        w.write(''.join(all))
                akaDisplay("green")
    except Exception as e:
        print(e)

def akaMod():
    try:
        akaDisplay()
        P.colour("Give the index of cmd you want to delete/modify:\nEnter $ followed by index if you want to delete a set of cmds:","white","red")
        ln=input("@k@pi->")
        if("$" in ln):
            ln=int(ln[ln.index('$')+1:])
            all=[]
            for _ in range(P.lenline(akaFile)):
                all.append(akaReadLine(_))
            all[ln]=all[ln].replace(all[ln],"")
            with open(akaFile,'w') as w:
                w.write(''.join(all))
            akaDisplay("green")
        else:
            ln=int(ln)
            n=P.lenline(akaFile)
            if (not(ln<=n-1)):
                P.colour("Given index doesn't exist !!","red","black")
            else:
                all=[]
                for _ in range(P.lenline(akaFile)):
                    all.append(akaReadLine(_))
                P.colour(f"{all[ln]}\nGive the cmd in this line you wish to modify/delete:","white","red")
                inp=input("@k@pi->")
                if(inp in all[ln]):
                    P.colour("Give the replacement command\nHit ENTER if you wish to not replace the deleted cmd:","white","red")
                    rpl=input("@k@pi->")
                    if rpl in __all():
                        P.colour("Given command pre-exists !!","red","black")
                    else:
                        if(rpl==""):
                            all[ln]=all[ln].replace(inp+",",rpl)
                        elif(P.compress(P.elements(rpl))==[" "]):
                            all[ln]=all[ln].replace(inp+",",rpl)
                        else:
                            all[ln]=all[ln].replace(inp,rpl)
                        with open(akaFile,'w') as w:
                            w.write(''.join(all))
                        akaDisplay("green")
                else:
                    P.colour("Given cmd doesn't exist !!","red","black")
    except Exception as e:
        print(e)

def akaDel():
    try:
        akaDisplay()
        P.colour("Give the index of cmd you want to delete:\nEnter $ followed by index if you want to delete a set of cmds:","white","red")
        ln=input("@k@pi->")
        if("$" in ln):
            ln=int(ln[ln.index('$')+1:])
            all=[]
            for _ in range(P.lenline(akaFile)):
                all.append(akaReadLine(_))
            all[ln]=all[ln].replace(all[ln],"")
            with open(akaFile,'w') as w:
                w.write(''.join(all))
            akaDisplay("green")
        else:
            ln=int(ln)
            n=P.lenline(akaFile)
            if (not(ln<=n-1)):
                P.colour("Given index doesn't exist !!","red","black")
            else:
                all=[]
                for _ in range(P.lenline(akaFile)):
                    all.append(akaReadLine(_))
                P.colour(f"{all[ln]}\nGive the cmd in this line you wish to delete:","white","red")
                inp=input("@k@pi->")
                if(inp+',' in all[ln]):
                    if(all[ln].count(',')==1 or all[ln].count(',')==0):
                        all[ln]=all[ln].replace(all[ln],"")
                    else:
                        all[ln]=all[ln].replace(inp,"")
                    with open(akaFile,'w') as w:
                        w.write(''.join(all))
                    akaDisplay("green")
                else:
                    P.colour("Given cmd doesn't exist !!","red","black")
    except Exception as e:
        print(e)

def akapiMode():
    P.colour("In Akapi Mode:","cyan","black")
    quitModeRandomVarThatIsNotEqualToZero=1
    while(quitModeRandomVarThatIsNotEqualToZero!=0):
        inp=P.caps(input(">>-@k@pi->>"))
        actInp=inp
        if("akapi" not in inp):
            inp+=" akapi"
        if("display" in inp) or ("dplay" in inp):
            akaDisplay("cyan")
        elif("exit" in inp and "akapi" in inp and "mode" in inp) or ("close" in inp and "akapi" in inp and "mode" in inp) or ("quit" in inp and "akapi" in inp and "mode" in inp):
            break
        elif("mod" in inp and "akapi" in inp) or ("mod" in inp and "cmd" in inp) or ("mod" in inp and "akapi" in inp):
            akaMod()
        elif("add" in inp and "akapi" in inp) or ("new" in inp and "akapi" in inp):
            akaAdd()
        elif("del" in inp and "akapi" in inp) or ("delete" in inp and "akapi" in inp) or ("remove" in inp and "akapi" in inp):
            akaDel()
        elif("all" in inp and "akapi" in inp):
            P.colour(__all(),"green","black")
        else:
            akaAdd(actInp)

def navigate():
    os.chdir("P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Modular_Files\\Modular_Info\\Modules")

def navigate_back():
    os.chdir("P:\\Pvz_Program_Files\\Other programs")

def liplay(li,c="red"):
    nl=len(li)-1
    ssssssssss=0
    while(ssssssssss<=nl):
        abracadabra=str(ssssssssss)+str("\t-->>")+str(li[ssssssssss])
        colour(abracadabra,c,"white")
        ssssssssss+=1

def initialize():
    P.delements(dictionary)
    li=P.extract("P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Modular_Files\\Modular_Info\\Defined_Modules.txt","^@^^#")
    for ele in range(len(li)):
        dictionary.append(li[ele])
    for _ in li:
        if(' ' in _):
            dictionary_.append(_)

def preExist_(param):
    fin=P.extract(d_txt,"^@^^#")
    if (param in fin):
        return(1)
    else:
        return(0)

def preExist(parameter):
    file="P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Modular_Files\\Modular_Info\\Undefined_Modules..txt"
    fin=P.extract(d_txt,"^@^^#")
    finale=P.extract(file,"^@^^#")
    if (parameter in finale):
        return(1)
    else:
        pass
    if (parameter in fin):
        return(1)
    else:
        return(0)

def clock():
    sundial=time.ctime()
    return(sundial)

def colour(String,colour,bg_colour="black"):
    try:
        if(P.caps(bg_colour)=="black"):
            print(colored('{0}'.format(String),'{0}'.format(colour)))
        elif(P.caps(colour)=="black"):
            print("Black text not possible!!")
        else:
            print(colored('{0}'.format(String), '{0}'.format(P.caps(colour)), 'on_{0}'.format(P.caps(bg_colour))))
    except Exception:
        print("The given colour combination is not possible")

def say(to_say):
    wts = pyttsx3.init()
    wts.say(str(to_say))
    wts.runAndWait()

def alias():
    c_name=P.extract(d_txt,"^@^^#")
    c_type=P.extract(d_txt,"+|>")
    f_ad=P.extract(d_txt,")-)")
    colour("INDEX\tCMD_NAME\tCMD_TYPE\tCMD_FILE_ADDRESS","blue","black")
    for i in range(len(c_name)):
        colour("{0} ==> {1} -- > {2} --> {3}".format(i,c_name[i],c_type[i],f_ad[i]),"blue","black")
    colour("Give the index of the parent file from which this command will be aliased:","cyan","black")
    ind=int(input(">==>"))
    return(f_ad[ind])

def Undefined(Cmd_Name,Cmd_Type,w=""):#undefined will write in the undefined txt file and the third arguement describes the necessity to write to the file or append to it.
    file_u="P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Modular_Files\\Modular_Info\\Undefined_Modules..txt"
    if(w==""):
        with open(file_u,'a') as f:
            f.write("^@^^#"+Cmd_Name+"#^^@^\t"+"+|>"+Cmd_Type+"<|+\n")
    else:
        with open(file_u,'w') as f:
            f.write("^@^^#"+Cmd_Name+"#^^@^\t"+"+|>"+Cmd_Type+"<|+\n")

def Defined(Cmd_Name,Cmd_Type,Cmd_File_Address):#defined will first write to the defined.txt file and then will clear the record from undefined file...
    file_u="P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Modular_Files\\Modular_Info\\Defined_Modules.txt"
    if(Cmd_File_Address=="alias"):
        Cmd_File_Address=alias()
    else:
        pass
    all=list()
    with open(file_u,'a') as f:
        f.write("^@^^#"+Cmd_Name+"#^^@^\t"+"+|>"+Cmd_Type+"<|+\t"+")-)"+Cmd_File_Address+"(-(\n")
    #From here,We are modifying the undefined file....
    Cmd_Names=P.extract("P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Modular_Files\\Modular_Info\\Undefined_Modules..txt","^@^^#")
    Cmd_Types=P.extract("P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Modular_Files\\Modular_Info\\Undefined_Modules..txt","+|>")
    try:
        ind=Cmd_Names.index(Cmd_Name)
        Cmd_Names.remove(Cmd_Names[ind])
        Cmd_Types.remove(Cmd_Types[ind])
    except Exception as e:
        return
    if(len(Cmd_Names)==0):
        with open("P:\\Pvz_Program_Files\\Drag_On_Program_Files\\Drag_On_Modular_Files\\Modular_Info\\Undefined_Modules..txt",'w') as q:
            q.write("")
        return
    Undefined(Cmd_Names[0],Cmd_Types[0],"reset")
    y=1
    while(y<len(Cmd_Names)):
        Undefined(Cmd_Names[y],Cmd_Types[y])
        y+=1

def readwriter(f_type,carrier_type,line):
    if(f_type==1):
        with open('P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Master_Files\Master_File_1.txt','a') as f:
            check_time=clock()
            f.write("{0} {1:>50} {2:>50}".format(line,"[(<{0}>)]".format(carrier_type),check_time))
            f.write("\n")
    elif(f_type==2):
        with open('P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Master_Files\Master_File_1.txt','r') as f:
            pass
    elif(f_type==3):
        with open('P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Master_Files\Master_File_1.txt','r+') as f:
            pass
    elif(f_type==4):
        with open('P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Master_Files\Master_File_1.txt','w') as f:
            pass
    else:
        print("Invalid type declaration")

def rm_cmd(file,comd):
    li=P.extract(file,"^@^^#")
    ind=li.index(comd)
    all=list()
    with open(file,"r") as f:
        for i in range(P.lenline(file)):
            ap=f.readline()
            if(i==ind):
                colour("The command edited was =>\n{}".format(ap),"red","black")
                readwriter(1,"Cmd Mode","The command removed was => {} ------ from the file => {}".format(ap.replace('\n',''),file))
            else:
                pass
            all.append(ap)
    with open(file,"w") as d:
        d.write("")
    with open(file,"a") as a:
        for j in range(len(all)):
            if(j==ind):
                continue
            a.write(all[j])

def Delete_Cmd():
    colour("Red displayed text are undefined commands;\nBlue displayed text are already defined !\n","green","black")
    li1=P.extract(ud_txt,"^@^^#")
    li2=P.extract(d_txt,"^@^^#")
    liplay(li1)
    liplay(li2,"Blue")
    colour("If you want to delete an undefined command, type \"UD\";\nTo delete an already defined command, type \"D\"","red","cyan")
    del_cmd=P.Caps(input("])>:"))
    if(del_cmd=="UD"):
        liplay(li1)
        rm_cmd(ud_txt,P.caps(input("Give Command to be deleted:")))
    else:
        liplay(li2,"Blue")
        rm_cmd(d_txt,P.caps(input("Give Command to be deleted:")))

def displayCmdMode():
    ud1=P.extract(ud_txt,"^@^^#")
    ud2=P.extract(ud_txt,"+|>")
    d1=P.extract(d_txt,"^@^^#")
    d2=P.extract(d_txt,"+|>")
    d3=P.extract(d_txt,")-)")
    colour("Undefined Modules:",'green','black')
    for _ in range(len(ud1)):
        if(len(ud1[_])>5 and len(ud1[_])<=10):
            colour(f"{_} \t {ud1[_]} \t\t {ud2[_]}","red","black")
        elif(len(ud1[_])>10):
            colour(f"{_} \t {ud1[_]} \t {ud2[_]}","red","black")
        else:
            colour(f"{_} \t {ud1[_]} \t\t\t {ud2[_]}","red","black")
    colour("Defined Modules:",'green','black')
    for _ in range(len(d1)):
        if(len(d1[_])>5 and len(d1[_])<=10):
            colour(f"{_} \t {d1[_]} \t\t {d2[_]} \t\t\t {d3[_]}","blue","black")
        elif(len(d1[_])>10):
            colour(f"{_} \t {d1[_]} \t {d2[_]} \t\t\t {d3[_]}","blue","black")
        else:
            colour(f"{_} \t {d1[_]} \t\t\t {d2[_]} \t\t\t {d3[_]}","blue","black")

def Command_Line():
    colour("In command mode","white","cyan")
    Img_Var=1
    Cmd_Mode_All=list()
    while(Img_Var<=999999999999999999999999999999):
        if(Img_Var==1):
            readwriter(1,"Interactive Mode","Cmd_Mode")
        else:
            pass
        INP=P.caps(input("Cmd::"))
        readwriter(1,"Cmd Mode",INP)
        if(INP==P.caps("Exit_Cmd_Mode")):
            readwriter(1,"Cmd Mode",INP)
            break
        elif(INP==P.caps("Define_Module")):
            li=P.extract(ud_txt,"^@^^#")
            liplay(li)
            INP_=P.caps(input("Give the command you want to define:"))
            readwriter(1,"Cmd Mode","__Defining__ "+INP_)
            if(preExist_(INP_)==1):
                colour("This command already exists","red","black")
                readwriter(1,"Cmd Mode",INP_+" __preExists__")
            else:
                try:
                    IND=li.index(INP_)
                    ty=P.extract(ud_txt,"+|>")
                    INP_TYPE=P.caps(ty[IND])
                except Exception:
                    INP_TYPE=P.caps(input("Give the type of command::"))
                FILE_LOC=P.caps(input("Give file location::"))
                readwriter(1,"Cmd Mode","__Succesfully defined__ =>"+INP_+">>"+INP_TYPE+">>"+FILE_LOC)
                Defined(INP_,INP_TYPE,FILE_LOC)
        elif(INP==P.caps("Delete_Cmd")):
            Delete_Cmd()
        elif(INP=="display" or INP=="dplay"):
            displayCmdMode()
        elif(INP==P.caps("Mod_Cmd")):
            colour("Red displayed text are undefined commands and Blue displayed text are already defined !!\n","green","black")
            li1=P.extract(ud_txt,"^@^^#")
            li2=P.extract(d_txt,"^@^^#")
            liplay(li1)
            liplay(li2,"Blue");print("\n")
            colour("If you want to modify an undefined command, type \"UD\";\nTo modify an already defined command, type \"D\"","red","cyan")
            mod_cmd=P.caps(input("])>:"))
            if(P.Caps(mod_cmd)=="UD"):
                liplay(li1);print("\n")
                m_cmd=P.caps(input("Give Command to be modified:"))
                rm_cmd(ud_txt,m_cmd)
                c2=P.caps(input("Give Cmd Type:"))
                c3=P.caps(input("Give Cmd_File_Address:"))
                Defined(m_cmd,c2,c3)
                readwriter(1,"Cmd Mode","Command replaced as >>{}=-={}=-={}".format(m_cmd,c2,c3))
                li1=P.extract(ud_txt,'^@^^#')
                typ1=P.extract(ud_txt,'+|>')
                INDEX = li1.index(m_cmd)
                P.colour(f'The command was edited as {li1[INDEX]} of type {typ1[INDEX]}\n^@^^# {li1[INDEX]} #^^@^\t+|> {typ1[INDEX]} <|+','red','black')
            else:
                liplay(li2,"Blue");print("\n")
                m_cmd=P.caps(input("Give Command to be modified:"))
                rm_cmd(d_txt,m_cmd)
                c2=P.caps(input("Give Cmd Type:"))
                c3=P.caps(input("Give Cmd_File_Address:"))
                Defined(m_cmd,c2,c3)
                readwriter(1,"Cmd Mode","Command replaced as >>{}=-={}=-={}".format(m_cmd,c2,c3))
                li1=P.extract(d_txt,'^@^^#')
                typ1=P.extract(d_txt,'+|>')
                pth1=P.extract(d_txt,')-)')
                INDEX = li1.index(m_cmd)
                P.colour(f'The command was edited as {li1[INDEX]} of type {typ1[INDEX]} located at {pth1[INDEX]}\n^@^^# {li1[INDEX]} #^^@^\t+|> {typ1[INDEX]} <|+\t)-) {pth1[INDEX]} (-(','red','black')
        else:
            if(preExist(INP)==1):
                colour("This command already exists","red","white")
            else:
                INP_TYPE=P.caps(input("Give the type of command::"))
                Undefined(INP,INP_TYPE)

def Special_Executable_Command():
    colour("In spexec Mode....Work CAREFULLY!!!!","blue","white")
    say("Spexec Mode activated....Be CAREFUL")
    Spec_Var=0
    ln_number=0
    Ml_Cmd=list()
    all_spexec_inputs=list()
    while(Spec_Var<=1):
        if(Spec_Var==0):
            readwriter(1,"Interactive Mode","spexec")
            Spec_Var+=1
        else:
            pass
        Spec_Inp=input(">->")
        all_spexec_inputs.append(Spec_Inp)
        if(Spec_Inp=="Execute"):
            all_spexec_inputs.append("EXECUTE !!")
            Spec_Var+=1
        elif(Spec_Inp=="Mod_spexe_cmd_line"):
            try:
                modify=int(input("Give line number to delete code line >>"))
                all_spexec_inputs.append("modify={0}\t<{1}>".format(Ml_Cmd[modify],modify))
                Ml_Cmd.remove(Ml_Cmd[modify])
                replacement=input("Give the replacement code line::")
                all_spexec_inputs.append("replacement={0}".format(replacement))
                Ml_Cmd.insert(modify,replacement)
                Mod_Cmd_Var=0
                nMod_Cmd=len(Ml_Cmd)-1
                while(Mod_Cmd_Var<=nMod_Cmd):
                    colour(Ml_Cmd[Mod_Cmd_Var],"blue","white")
                    Mod_Cmd_Var+=1
            except IndexError:
                colour("List_Index_Out_of_Range","red","white")
            except Exception:
                colour("Something went wrong...Try again CAREFULLY!!!")
        else:
            Ml_Cmd.append(Spec_Inp)
            colour(("{0:>30} {1}".format("^^^^ln_num",ln_number)),"white","red")
            ln_number+=1
    try:
        nMl_Cmd=len(Ml_Cmd)-1
        Mlv=0
        start_var='some_value'
        while(Mlv<=nMl_Cmd):
            executable=Ml_Cmd[Mlv]
            exec(executable)
            Mlv+=1
    except Exception as e:
        colour("The given code throws error.......Check for possible erros and try again","white","red")
        colour(">>>{0}".format(str(e)),"white","red")
    end_var='some_value'
    all_spec_input_var=0
    n_all_spec_input=len(all_spexec_inputs)-1
    while(all_spec_input_var<=n_all_spec_input):
        spec_inp=all_spexec_inputs[all_spec_input_var]
        readwriter(1,"Spexec Mode",spec_inp)
        all_spec_input_var+=1
    dec_vars=list(locals())
    start_val=dec_vars.index('start_var')+1
    end_val=dec_vars.index('end_var')
    spec_vars=dec_vars[start_val:end_val]
    try:
        spec_vars.remove('executable')
    except Exception:
        pass
    nnnnnnn=0
    while(nnnnnnn<=len(spec_vars)-1):
        delete_var=spec_vars[nnnnnnn]
        exec("del({0})".format(delete_var))
        nnnnnnn+=1

def inlineExecutable(arg):
    if('%-%-%' in arg):
        r=arg[arg.index('%-%-%')+5:]
        arg=arg[:arg.index('%-%-%')]
        exec(arg)
        return(r)
    else:
        exec(arg)
        return("")

def Interactive_Mode(par):
    def check_no_keys(string):
        nKeys=0
        for iiIii in range(len(dictionary)):
            key=dictionary[iiIii]
            if (key in leo(string)):
                string=string.replace(key,'^')
                nKeys+=1
            else:
                pass
        for _ in dictionary:
            if(_ in string):
                nKeys+=1
        return(nKeys)

    def check_address(keyword):
        _1=P.extract(d_txt,"^@^^#")
        _2=P.extract(d_txt,")-)")
        return(_2[_1.index(keyword)])

    letters=list()
    words=par.split()
    nw=len(words)-1
    nI=len(par)-1
    iI=0
    while(iI<=nI):
        lett=par[iI]
        letters.append(lett)
        iI+=1
    #colour(words,"white","blue")
    sentences=' '.join(words)
    #colour(sentences,"white","blue")
    readwriter(1,"Interactive Mode",sentences)
    #colour(letters,"white","blue")
    #colour(dictionary,"white","blue")
    while(check_no_keys(par)!=0):
        colour(par,"blue")
        for ind in range(len(words)):
            __wd__=words[ind]
            i=0
            if(__wd__ in dictionary):
                address=check_address(__wd__)
                #P.colour(address,'blue','black')
                navigate()
                if "play" in leo(par):
                    par=subprocess.getoutput('python "{}" "{}"'.format(address,par))
                    if("%-%-%" in par):
                        par=par[par.index('%-%-%')+5:]
                    else:
                        par=""
                elif("$-$" in par):
                    par=inlineExecutable(par[par.index('$-$')+3:])
                else:
                    par=subprocess.getoutput('python "{}" "{}"'.format(address,par))
                if("$-$" in par):
                    par=inlineExecutable(par[par.index('$-$')+3:])
                words=par.split(' ')
                break
            elif(sentences in dictionary):
                address=check_address(sentences)
                #P.colour(address,'blue','black')
                navigate()
                if "play" in leo(par):
                    par=subprocess.getoutput('python "{}" "{}"'.format(address,par),shell=True)
                    if("%-%-%" in par):
                        par=par[par.index('%-%-%')+5:]
                    else:
                        par=""
                elif("$-$" in par):
                    par=inlineExecutable(par[par.index('$-$')+3:])
                else:
                    par=subprocess.getoutput('python "{}" "{}"'.format(address,par))
                if("$-$" in par):
                    par=inlineExecutable(par[par.index('$-$')+3:])
                words=par.split(' ')
                break
            else:
                i=0
                for _ in dictionary_:
                    if _ in sentences:
                        address=check_address(_)
                        #P.colour(address,'blue','black')
                        navigate()
                        if "play" in leo(par):
                            par=subprocess.getoutput('python "{}" "{}"'.format(address,par),shell=True)
                            if("%-%-%" in par):
                                par=par[par.index('%-%-%')+5:]
                            else:
                                par=""
                        elif("$-$" in par):
                            par=inlineExecutable(par[par.index('$-$')+3:])
                        else:
                            par=subprocess.getoutput('python "{}" "{}"'.format(address,par))
                        if("$-$" in par):
                            par=inlineExecutable(par[par.index('$-$')+3:])
                        words=par.split(' ')
                        break
                    else:
                        pass#print("\nError condition to be initiated at 649\n")
    print(par)
    P.say(par)


readwriter(1,"__Notification__Restarting__","COMMAND_LINE_HAS_BEEN_RESTARTED_!!")
jdlsfjhkehgfgbvdsjcvbfdjfvjdsbjbsdjvbjsdbjhfsbddbjbvdsbbs=1
dictionary=list()
dictionary_=list()
while(jdlsfjhkehgfgbvdsjcvbfdjfvjdsbjbsdjvbjsdbjhfsbddbjbvdsbbs==1):
    try:
        initialize()
        inp=P.caps(input(">>>"))
        if(inp=="cmd_mode"):
            Command_Line()
        elif(inp=="spexec"):
            Special_Executable_Command()
        elif("akapi" in inp or ("akapi" in inp and "mode" in inp) or ("aka" in inp and "mode" in inp)):
            akapiMode()
        else:
            Interactive_Mode(P.akapi(inp+" "))
    except Exception as e:
        print(str(e))
        readwriter(1,"Error",f"{str(e)}")
