#!/usr/bin/python
#Filename: cal_OPT.py
import math
import os

print "##############################################################################\n#This program only produces POSCAR accroding to your specified value(s)\n#Creat dirctories in CURRENT dirctory with name of different lattice parameter\n#           All job will be submitted !!!!!\n#WARNING this program is for lattice parameter calclulation ONLY! \n##############################################################################\n"

def frange(start, end=None, inc=None):
    "A range function, that does accept float increments..."

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next == end+0.000000000000001:
            L.append(next)
            break
        elif inc > 0 and next > end+0.000000000000001:
            break
        elif inc < 0 and next == end-0.000000000000001:
            L.append(next)
            break
        elif inc < 0 and next < end-0.000000000000001:
            break
        L.append(next)

    return L

#a_min=raw_input("input the value of a_min: ")
#a_max=raw_input("input the value of a_max: ")
#a_step==raw_input("input the value of a_step: ")
#b_min=raw_input("input the value of b_min: ")
#b_max=raw_input("input the value of b_max: ")
#b_step==raw_input("input the value of b_step: ")
#c_min=raw_input("input the value of c_min: ")
#c_max=raw_input("input the value of c_max: ")
#c_step==raw_input("input the value of b_step: ")

POSCAR_file=raw_input("input the name of POSCAR source: ")
print ''
#========================import data=================================
file = open(POSCAR_file, "r")
content = [x.rstrip("\n") for x in file]
data = [x.split()[:5] for x in content[2:5]]
file.close()

#convert datatype
for i in (0,1,2):
    for j in (0,1,2):
        data[i][j]=float(data[i][j])

#check symmetry
a_org = math.sqrt(data[0][0]*data[0][0]+data[0][1]*data[0][1]+data[0][2]*data[0][2])
b_org = math.sqrt(data[1][0]*data[1][0]+data[1][1]*data[1][1]+data[1][2]*data[1][2])
c_org = math.sqrt(data[2][0]*data[2][0]+data[2][1]*data[2][1]+data[2][2]*data[2][2])

a_org_n = int(a_org*100000)             #to examine if same
b_org_n = int(b_org*100000)
c_org_n = int(c_org*100000)

if a_org_n == b_org_n:
    if a_org_n == c_org_n:
        print 'a=b=c\n'
        axis_min=raw_input("input the value of axis_min(all): ")
        axis_max=raw_input("input the value of axis_max(all): ")
        axis_step=raw_input("input the value of axis_step(all): ")
        #set all to same=====================
        a_step=axis_step
        a_min=axis_min
        a_max=axis_max
        b_step=axis_step
        b_min=axis_min
        b_max=axis_max
        c_step=axis_step
        c_min=axis_min
        c_max=axis_max
    else:
        print 'a=b!=c\n'
        ab_min=raw_input("input the value of a_min and b_min(SAME A AND B): ")
        ab_max=raw_input("input the value of a_max and b_max(SAME A AND B): ")
        ab_step=raw_input("input the value of a_step and b_step(SAME A AND B): ")
        a_step=ab_step
        a_min=ab_min
        a_max=ab_max
        b_step=ab_step
        b_min=ab_min
        b_max=ab_max
        c_min=raw_input("input the value of c_min: ")
        c_max=raw_input("input the value of c_max: ")
        c_step=raw_input("input the value of c_step: ")
if a_org_n == c_org_n:
    if b_org_n != c_org_n:
        print 'a=c!=b\n'
        ac_min=raw_input("input the value of a_min and c_min(SAME A AND C): ")
        ac_max=raw_input("input the value of a_max and c_max(SAME A AND C): ")
        ac_step=raw_input("input the value of a_step and c_step(SAME A AND C): ")
        a_step=ac_step
        a_min=ac_min
        a_max=ac_max
        c_step=ac_step
        c_min=ac_min
        c_max=ac_max
        b_min=raw_input("input the value of b_min: ")
        b_max=raw_input("input the value of b_max: ")
        b_step=raw_input("input the value of b_step: ")
if a_org_n != b_org_n:
    if b_org_n == c_org_n:
        print 'a!=b=c\n'
        bc_min=raw_input("input the value of b_min and c_min(SAME B AND C): ")
        bc_max=raw_input("input the value of b_max and c_max(SAME B AND C): ")
        bc_step=raw_input("input the value of b_step and c_step(SAME B AND C): ")
        b_step=bc_step
        b_min=bc_min
        b_max=bc_max
        c_step=bc_step
        c_min=bc_min
        c_max=bc_max
        a_min=raw_input("input the value of a_min: ")
        a_max=raw_input("input the value of a_max: ")
        a_step=raw_input("input the value of a_step: ")
    else:
        print 'ALL AXIS ARE DIFFERENT\n'
        a_min=raw_input("input the value of a_min: ")
        a_max=raw_input("input the value of a_max: ")
        a_step=raw_input("input the value of a_step: ")
        b_min=raw_input("input the value of b_min: ")
        b_max=raw_input("input the value of b_max: ")
        b_step=raw_input("input the value of b_step: ")
        c_min=raw_input("input the value of c_min: ")
        c_max=raw_input("input the value of c_max: ")
        c_step=raw_input("input the value of b_step: ")

#convert data type
a_min=float(a_min)
a_max=float(a_max)
a_step=float(a_step)
b_min=float(b_min)
b_max=float(b_max)
b_step=float(b_step)
c_min=float(c_min)
c_max=float(c_max)
c_step=float(c_step)

extration = []
#===================================================================================================
if a_org_n == b_org_n:
    if a_org_n == c_org_n:
        print 'a=b=c\n'
        #=====================================

        for a_sum in frange(a_min,a_max,a_step):

            #=====================a opt================================
            if int(data[0][0])==0:
                if int(data[0][1])==0:
                    if data[0][2]>0:
                        data[0][2]=a_sum               #if a1=0 and a2=0 then a3 is alone
                    elif data[0][2]<0:
                        data[0][2]=(-1)*a_sum
                else:                              #if a1=0 and a2<>0 then use a2 as constant
                    data_a_2_1=data[0][2]/data[0][1]
                    if data[0][1]>0:
                        data[0][1]=a_sum/math.sqrt(1+data_a_2_1*data_a_2_1)
                    elif data[0][1]<0:
                        data[0][1]=(-1)*a_sum/math.sqrt(1+data_a_2_1*data_a_2_1)
                    data[0][2]=data[0][1]*data_a_2_1
            else:
                data_a_1_0=data[0][1]/data[0][0]
                data_a_2_0=data[0][2]/data[0][0]
                if data[0][0]>0:
                    data[0][0]=a_sum/math.sqrt(1+data_a_2_0*data_a_2_0+data_a_1_0*data_a_1_0)
                elif data[0][0]<0:
                    data[0][0]=(-1)*a_sum/math.sqrt(1+data_a_2_0*data_a_2_0+data_a_1_0*data_a_1_0)
                data[0][1]=data[0][0]*data_a_1_0
                data[0][2]=data[0][0]*data_a_2_0
            #======================================

            #=====================b opt================================
            if int(data[1][0])==0:
                if int(data[1][1])==0:
                    if data[1][2]>0:
                        data[1][2]=a_sum
                    elif data[1][2]<0:
                        data[1][2]=(-1)*a_sum
                else:
                    data_b_2_1=data[1][2]/data[1][1]
                    if data[1][1]>0:
                        data[1][1]=a_sum/math.sqrt(1+data_b_2_1*data_b_2_1)
                    elif data[1][1]<0:
                        data[1][1]=(-1)*a_sum/math.sqrt(1+data_b_2_1*data_b_2_1)
                    data[1][2]=data[1][1]*data_b_2_1
            else:
                data_b_1_0=data[1][1]/data[1][0]
                data_b_2_0=data[1][2]/data[1][0]
                if data[1][0]>0:
                    data[1][0]=a_sum/math.sqrt(1+data_b_2_0*data_b_2_0+data_b_1_0*data_b_1_0)
                elif data[1][0]<0:
                    data[1][0]=(-1)*a_sum/math.sqrt(1+data_b_2_0*data_b_2_0+data_b_1_0*data_b_1_0)
                data[1][1]=data[1][0]*data_b_1_0
                data[1][2]=data[1][0]*data_b_2_0
            #======================================

            #=====================c opt================================
            if int(data[2][0])==0:
                if int(data[2][1])==0:
                    if data[2][2]>0:
                        data[2][2]=a_sum
                    elif data[2][2]<0:
                        data[2][2]=(-1)*a_sum
                else:
                    data_c_2_1=data[2][2]/data[2][1]
                    if data[2][1]>0:
                        data[2][1]=a_sum/math.sqrt(1+data_c_2_1*data_c_2_1)
                    elif data[2][1]<0:
                        data[2][1]=(-1)*a_sum/math.sqrt(1+data_c_2_1*data_c_2_1)
                    data[2][2]=data[2][1]*data_c_2_1
            else:
                data_c_1_0=data[2][1]/data[2][0]
                data_c_2_0=data[2][2]/data[2][0]
                if data[2][0]>0:
                    data[2][0]=a_sum/math.sqrt(1+data_c_2_0*data_c_2_0+data_c_1_0*data_c_1_0)
                elif data[2][0]<0:
                    data[2][0]=(-1)*a_sum/math.sqrt(1+data_c_2_0*data_c_2_0+data_c_1_0*data_c_1_0)
                data[2][1]=data[2][0]*data_c_1_0
                data[2][2]=data[2][0]*data_c_2_0
            #======================================
            fileHandle = open('POSCAR','a')
            #fileHandle = open(str(a_sum)+str(b_sum)+str(c_sum),'a') #TEST PURPOSE ONLY
            file = open(POSCAR_file,'r')
            lineNum=0
            for line in file.readlines()[0:2]:
                fileHandle.write(line)
            file.close()
            fileHandle.write('      '+str(data[0][0])+'     '+str(data[0][1])+'     '+str(data[0][2])+'\n')
            fileHandle.write('      '+str(data[1][0])+'     '+str(data[1][1])+'     '+str(data[1][2])+'\n')
            fileHandle.write('      '+str(data[2][0])+'     '+str(data[2][1])+'     '+str(data[2][2])+'\n')
            filename = POSCAR_file
            ffopen = open(filename)
            next (ffopen)
            next (ffopen)
            next (ffopen)
            next (ffopen)
            next (ffopen)

            for e in ffopen:
                fileHandle.write(e)
            ffopen.close()
            fileHandle.close()


            #starting calculation
            #os.system("./run.sh")                                                      #LOCAL CALCULATION ONLY
            #os.system(yhrun -p TH_BM -n 24 /vol6/home/zjumsejjz4/bin/vasp5.3.5-neb)
            #mvcont='mv CONTCAR'+' CONTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
            #mvpos='mv POSCAR'+' POSCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
            #mvout='mv OUTCAR'+' OUTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
            os.system('mkdir'+' '+str(a_sum)+str(a_sum)+str(a_sum))
            os.system('cp INCAR POTCAR KPOINTS std.pbs POSCAR vdw_kernel.bindat'+' '+str(a_sum)+str(a_sum)+str(a_sum))
            os.chdir('./'+str(a_sum)+str(a_sum)+str(a_sum))
#            os.system('yhbatch -p TH_BM -n 12 -JXCC_OPT run.sh')                       #open this if want to submit job automatically
            os.system('qsub -N '+str(a_sum)+str(a_sum)+str(a_sum)+' std.pbs')
            os.chdir('../')
            os.system('rm POSCAR')
            extration.append("'"+str(a_sum)+str(a_sum)+str(a_sum)+"'")
#=================================generate data_extration.py=================================
        devide = ','
        extration_all = devide.join(extration)
        #print extration_all
        file_extration = open('data_extration.py','a')
        file_extration.write('import os'+'\n')
        file_extration.write('for i in ('+extration_all+'):'+'\n')
        file_extration.write('    print i'+'\n')
        file_extration.write('    os.chdir(i)'+'\n')
        file_extration.write('''    os.system("grep 'energy(sigma->0) =' OUTCAR | tail -1")'''+'\n')
        file_extration.write('    print '+r"'\n'"+'\n')
        file_extration.write('    print '+r"'\n'"+'\n')
        file_extration.write("    os.chdir('../')"+'\n')

    else:
        print 'a=b!=c\n'
        #=====================================

        for a_sum in frange(a_min,a_max,a_step):
            for c_sum in frange(c_min,c_max,c_step):
                #=====================a opt================================
                if int(data[0][0])==0:
                    if int(data[0][1])==0:
                        if data[0][2]>0:
                            data[0][2]=a_sum
                        elif data[0][2]<0:
                            data[0][2]=(-1)*a_sum           #if a1=0 and a2=0 then a3 is alone
                    else:                              #if a1=0 and a2<>0 then use a2 as constant
                        data_a_2_1=data[0][2]/data[0][1]
                        if data[0][1]>0:
                            data[0][1]=a_sum/math.sqrt(1+data_a_2_1*data_a_2_1)
                        elif data[0][1]<0:
                            data[0][1]=(-1)*a_sum/math.sqrt(1+data_a_2_1*data_a_2_1)
                        data[0][2]=data[0][1]*data_a_2_1
                else:
                    data_a_1_0=data[0][1]/data[0][0]
                    data_a_2_0=data[0][2]/data[0][0]
                    if data[0][0]>0:
                        data[0][0]=a_sum/math.sqrt(1+data_a_2_0*data_a_2_0+data_a_1_0*data_a_1_0)
                    elif data[0][0]<0:
                        data[0][0]=(-1)*a_sum/math.sqrt(1+data_a_2_0*data_a_2_0+data_a_1_0*data_a_1_0)
                    data[0][1]=data[0][0]*data_a_1_0
                    data[0][2]=data[0][0]*data_a_2_0
                #======================================

                #=====================b opt================================
                if int(data[1][0])==0:
                    if int(data[1][1])==0:
                        if data[1][2]>0:
                            data[1][2]=a_sum
                        elif data[1][2]<0:
                            data[1][2]=(-1)*a_sum
                    else:
                        data_b_2_1=data[1][2]/data[1][1]
                        if data[1][1]>0:
                            data[1][1]=a_sum/math.sqrt(1+data_b_2_1*data_b_2_1)
                        elif data[1][1]<0:
                            data[1][1]=(-1)*a_sum/math.sqrt(1+data_b_2_1*data_b_2_1)
                        data[1][2]=data[1][1]*data_b_2_1
                else:
                    data_b_1_0=data[1][1]/data[1][0]
                    data_b_2_0=data[1][2]/data[1][0]
                    if data[1][0]>0:
                        data[1][0]=a_sum/math.sqrt(1+data_b_2_0*data_b_2_0+data_b_1_0*data_b_1_0)
                    elif data[1][0]<0:
                        data[1][0]=(-1)*a_sum/math.sqrt(1+data_b_2_0*data_b_2_0+data_b_1_0*data_b_1_0)
                    data[1][1]=data[1][0]*data_b_1_0
                    data[1][2]=data[1][0]*data_b_2_0
                #======================================

                #=====================c opt================================
                if int(data[2][0])==0:
                    if int(data[2][1])==0:
                        if data[2][2]>0:
                            data[2][2]=c_sum
                        elif data[2][2]<0:
                            data[2][2]=(-1)*c_sum
                    else:
                        data_c_2_1=data[2][2]/data[2][1]
                        if data[2][1]>0:
                            data[2][1]=c_sum/math.sqrt(1+data_c_2_1*data_c_2_1)
                        elif data[2][1]<0:
                            data[2][1]=(-1)*c_sum/math.sqrt(1+data_c_2_1*data_c_2_1)
                        data[2][2]=data[2][1]*data_c_2_1
                else:
                    data_c_1_0=data[2][1]/data[2][0]
                    data_c_2_0=data[2][2]/data[2][0]
                    if data[2][0]>0:
                        data[2][0]=c_sum/math.sqrt(1+data_c_2_0*data_c_2_0+data_c_1_0*data_c_1_0)
                    elif data[2][0]<0:
                        data[2][0]=(-1)*c_sum/math.sqrt(1+data_c_2_0*data_c_2_0+data_c_1_0*data_c_1_0)
                    data[2][1]=data[2][0]*data_c_1_0
                    data[2][2]=data[2][0]*data_c_2_0
                #======================================
                fileHandle = open('POSCAR','a')
                #fileHandle = open(str(a_sum)+str(b_sum)+str(c_sum),'a') #TEST PURPOSE ONLY
                file = open(POSCAR_file,'r')
                lineNum=0
                for line in file.readlines()[0:2]:
                    fileHandle.write(line)
                file.close()
                fileHandle.write('      '+str(data[0][0])+'     '+str(data[0][1])+'     '+str(data[0][2])+'\n')
                fileHandle.write('      '+str(data[1][0])+'     '+str(data[1][1])+'     '+str(data[1][2])+'\n')
                fileHandle.write('      '+str(data[2][0])+'     '+str(data[2][1])+'     '+str(data[2][2])+'\n')
                filename = POSCAR_file
                ffopen = open(filename)
                next (ffopen)
                next (ffopen)
                next (ffopen)
                next (ffopen)
                next (ffopen)

                for e in ffopen:
                    fileHandle.write(e)
                ffopen.close()
                fileHandle.close()


                #starting calculation
                #os.system("./run.sh")                                                      #LOCAL CALCULATION ONLY
                #os.system(yhrun -p TH_BM -n 24 /vol6/home/zjumsejjz4/bin/vasp5.3.5-neb)
                #mvcont='mv CONTCAR'+' CONTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                #mvpos='mv POSCAR'+' POSCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                #mvout='mv OUTCAR'+' OUTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                os.system('mkdir'+' '+str(a_sum)+str(a_sum)+str(c_sum))
                os.system('cp INCAR POTCAR KPOINTS std.pbs POSCAR vdw_kernel.bindat'+' '+str(a_sum)+str(a_sum)+str(c_sum))
                os.chdir('./'+str(a_sum)+str(a_sum)+str(c_sum))
#                os.system('yhbatch -p TH_BM -n 12 -JXCC_OPT run.sh')                       #open this if want to submit job automatically
                os.system('qsub -N '+str(a_sum)+str(a_sum)+str(a_sum)+' std.pbs')
                os.chdir('../')
                os.system('rm POSCAR')
                extration.append("'"+str(a_sum)+str(a_sum)+str(c_sum)+"'")
#=================================generate data_extration.py=================================
        devide = ','
        extration_all = devide.join(extration)
        #print extration_all
        file_extration = open('data_extration.py','a')
        file_extration.write('import os'+'\n')
        file_extration.write('for i in ('+extration_all+'):'+'\n')
        file_extration.write('    print i'+'\n')
        file_extration.write('    os.chdir(i)'+'\n')
        file_extration.write('''    os.system("grep 'energy(sigma->0) =' OUTCAR | tail -1")'''+'\n')
        file_extration.write('    print '+r"'\n'"+'\n')
        file_extration.write('    print '+r"'\n'"+'\n')
        file_extration.write("    os.chdir('../')"+'\n')

if a_org_n == c_org_n:
    if b_org_n != c_org_n:
        print 'a=c!=b\n'
        #=====================================

        for a_sum in frange(a_min,a_max,a_step):
            for b_sum in frange(b_min,b_max,b_step):
                #=====================a opt================================
                if int(data[0][0])==0:
                    if int(data[0][1])==0:
                        if data[0][2]>0:
                            data[0][2]=a_sum               #if a1=0 and a2=0 then a3 is alone
                        elif data[0][2]<0:
                            data[0][2]=(-1)*a_sum
                    else:                              #if a1=0 and a2<>0 then use a2 as constant
                        data_a_2_1=data[0][2]/data[0][1]
                        if data[0][1]>0:
                            data[0][1]=a_sum/math.sqrt(1+data_a_2_1*data_a_2_1)
                        elif data[0][1]<0:
                            data[0][1]=(-1)*a_sum/math.sqrt(1+data_a_2_1*data_a_2_1)
                        data[0][2]=data[0][1]*data_a_2_1
                else:
                    data_a_1_0=data[0][1]/data[0][0]
                    data_a_2_0=data[0][2]/data[0][0]
                    if data[0][0]>0:
                        data[0][0]=a_sum/math.sqrt(1+data_a_2_0*data_a_2_0+data_a_1_0*data_a_1_0)
                    elif data[0][0]<0:
                        data[0][0]=(-1)*a_sum/math.sqrt(1+data_a_2_0*data_a_2_0+data_a_1_0*data_a_1_0)
                    data[0][1]=data[0][0]*data_a_1_0
                    data[0][2]=data[0][0]*data_a_2_0
                #======================================

                #=====================b opt================================
                if int(data[1][0])==0:
                    if int(data[1][1])==0:
                        if data[1][2]>0:
                            data[1][2]=b_sum
                        elif data[1][2]<0:
                            data[1][2]=(-1)*b_sum
                    else:
                        data_b_2_1=data[1][2]/data[1][1]
                        if data[1][1]>0:
                            data[1][1]=b_sum/math.sqrt(1+data_b_2_1*data_b_2_1)
                        elif data[1][1]<0:
                            data[1][1]=(-1)*b_sum/math.sqrt(1+data_b_2_1*data_b_2_1)
                        data[1][2]=data[1][1]*data_b_2_1
                else:
                    data_b_1_0=data[1][1]/data[1][0]
                    data_b_2_0=data[1][2]/data[1][0]
                    if data[1][0]>0:
                        data[1][0]=b_sum/math.sqrt(1+data_b_2_0*data_b_2_0+data_b_1_0*data_b_1_0)
                    elif data[1][0]<0:
                        data[1][0]=(-1)*b_sum/math.sqrt(1+data_b_2_0*data_b_2_0+data_b_1_0*data_b_1_0)
                    data[1][1]=data[1][0]*data_b_1_0
                    data[1][2]=data[1][0]*data_b_2_0
                #======================================

                #=====================c opt================================
                if int(data[2][0])==0:
                    if int(data[2][1])==0:
                        if data[2][2]>0:
                            data[2][2]=a_sum
                        elif data[2][2]<0:
                            data[2][2]=(-1)*a_sum
                    else:
                        data_c_2_1=data[2][2]/data[2][1]
                        if data[2][1]>0:
                            data[2][1]=a_sum/math.sqrt(1+data_c_2_1*data_c_2_1)
                        elif data[2][1]<0:
                            data[2][1]=(-1)*a_sum/math.sqrt(1+data_c_2_1*data_c_2_1)
                        data[2][2]=data[2][1]*data_c_2_1
                else:
                    data_c_1_0=data[2][1]/data[2][0]
                    data_c_2_0=data[2][2]/data[2][0]
                    if data[2][0]>0:
                        data[2][0]=a_sum/math.sqrt(1+data_c_2_0*data_c_2_0+data_c_1_0*data_c_1_0)
                    elif data[2][0]<0:
                        data[2][0]=(-1)*a_sum/math.sqrt(1+data_c_2_0*data_c_2_0+data_c_1_0*data_c_1_0)
                    data[2][1]=data[2][0]*data_c_1_0
                    data[2][2]=data[2][0]*data_c_2_0
                #======================================
                fileHandle = open('POSCAR','a')
                #fileHandle = open(str(a_sum)+str(b_sum)+str(c_sum),'a') #TEST PURPOSE ONLY
                file = open(POSCAR_file,'r')
                lineNum=0
                for line in file.readlines()[0:2]:
                    fileHandle.write(line)
                file.close()
                fileHandle.write('      '+str(data[0][0])+'     '+str(data[0][1])+'     '+str(data[0][2])+'\n')
                fileHandle.write('      '+str(data[1][0])+'     '+str(data[1][1])+'     '+str(data[1][2])+'\n')
                fileHandle.write('      '+str(data[2][0])+'     '+str(data[2][1])+'     '+str(data[2][2])+'\n')
                filename = POSCAR_file
                ffopen = open(filename)
                next (ffopen)
                next (ffopen)
                next (ffopen)
                next (ffopen)
                next (ffopen)

                for e in ffopen:
                    fileHandle.write(e)
                ffopen.close()
                fileHandle.close()


                #starting calculation
                #os.system("./run.sh")                                                      #LOCAL CALCULATION ONLY
                #os.system(yhrun -p TH_BM -n 24 /vol6/home/zjumsejjz4/bin/vasp5.3.5-neb)
                #mvcont='mv CONTCAR'+' CONTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                #mvpos='mv POSCAR'+' POSCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                #mvout='mv OUTCAR'+' OUTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                os.system('mkdir'+' '+str(a_sum)+str(b_sum)+str(a_sum))
                os.system('cp INCAR POTCAR KPOINTS std.pbs POSCAR vdw_kernel.bindat'+' '+str(a_sum)+str(b_sum)+str(a_sum))
                os.chdir('./'+str(a_sum)+str(b_sum)+str(a_sum))
#                os.system('yhbatch -p TH_BM -n 12 -JXCC_OPT run.sh')                       #open this if want to submit job automatically
                os.system('qsub -N '+str(a_sum)+str(a_sum)+str(a_sum)+' std.pbs')
                os.chdir('../')
                os.system('rm POSCAR')
                extration.append("'"+str(a_sum)+str(b_sum)+str(a_sum)+"'")
#=================================generate data_extration.py=================================
        devide = ','
        extration_all = devide.join(extration)
        #print extration_all
        file_extration = open('data_extration.py','a')
        file_extration.write('import os'+'\n')
        file_extration.write('for i in ('+extration_all+'):'+'\n')
        file_extration.write('    print i'+'\n')
        file_extration.write('    os.chdir(i)'+'\n')
        file_extration.write('''    os.system("grep 'energy(sigma->0) =' OUTCAR | tail -1")'''+'\n')
        file_extration.write('    print '+r"'\n'"+'\n')
        file_extration.write('    print '+r"'\n'"+'\n')
        file_extration.write("    os.chdir('../')"+'\n')

if a_org_n != b_org_n:
    if b_org_n == c_org_n:
        print 'a!=b=c\n'
        #=====================================

        for a_sum in frange(a_min,a_max,a_step):
            for b_sum in frange(b_min,b_max,b_step):
                #=====================a opt================================
                if int(data[0][0])==0:
                    if int(data[0][1])==0:
                        if data[0][2]>0:
                            data[0][2]=a_sum               #if a1=0 and a2=0 then a3 is alone
                        elif data[0][2]<0:
                            data[0][2]=(-1)*a_sum
                    else:                              #if a1=0 and a2<>0 then use a2 as constant
                        data_a_2_1=data[0][2]/data[0][1]
                        if data[0][1]>0:
                            data[0][1]=a_sum/math.sqrt(1+data_a_2_1*data_a_2_1)
                        elif data[0][1]<0:
                            data[0][1]=(-1)*a_sum/math.sqrt(1+data_a_2_1*data_a_2_1)
                        data[0][2]=data[0][1]*data_a_2_1
                else:
                    data_a_1_0=data[0][1]/data[0][0]
                    data_a_2_0=data[0][2]/data[0][0]
                    if data[0][0]>0:
                        data[0][0]=a_sum/math.sqrt(1+data_a_2_0*data_a_2_0+data_a_1_0*data_a_1_0)
                    elif data[0][0]<0:
                        data[0][0]=(-1)*a_sum/math.sqrt(1+data_a_2_0*data_a_2_0+data_a_1_0*data_a_1_0)
                    data[0][1]=data[0][0]*data_a_1_0
                    data[0][2]=data[0][0]*data_a_2_0
                #======================================

                #=====================b opt================================
                if int(data[1][0])==0:
                    if int(data[1][1])==0:
                        if data[1][2]>0:
                            data[1][2]=b_sum
                        elif data[1][2]<0:
                            data[1][2]=(-1)*b_sum
                    else:
                        data_b_2_1=data[1][2]/data[1][1]
                        if data[1][1]>0:
                            data[1][1]=b_sum/math.sqrt(1+data_b_2_1*data_b_2_1)
                        elif data[1][1]<0:
                            data[1][1]=(-1)*b_sum/math.sqrt(1+data_b_2_1*data_b_2_1)
                        data[1][2]=data[1][1]*data_b_2_1
                else:
                    data_b_1_0=data[1][1]/data[1][0]
                    data_b_2_0=data[1][2]/data[1][0]
                    if data[1][0]>0:
                        data[1][0]=b_sum/math.sqrt(1+data_b_2_0*data_b_2_0+data_b_1_0*data_b_1_0)
                    elif data[1][0]<0:
                        data[1][0]=(-1)*b_sum/math.sqrt(1+data_b_2_0*data_b_2_0+data_b_1_0*data_b_1_0)
                    data[1][1]=data[1][0]*data_b_1_0
                    data[1][2]=data[1][0]*data_b_2_0
                #======================================

                #=====================c opt================================
                if int(data[2][0])==0:
                    if int(data[2][1])==0:
                        if data[2][2]>0:
                            data[2][2]=b_sum
                        elif data[2][2]<0:
                            data[2][2]=(-1)*b_sum
                    else:
                        data_c_2_1=data[2][2]/data[2][1]
                        if data[2][1]>0:
                            data[2][1]=b_sum/math.sqrt(1+data_c_2_1*data_c_2_1)
                        elif data[2][1]<0:
                            data[2][1]=(-1)*b_sum/math.sqrt(1+data_c_2_1*data_c_2_1)
                        data[2][2]=data[2][1]*data_c_2_1
                else:
                    data_c_1_0=data[2][1]/data[2][0]
                    data_c_2_0=data[2][2]/data[2][0]
                    if data[2][0]>0:
                        data[2][0]=b_sum/math.sqrt(1+data_c_2_0*data_c_2_0+data_c_1_0*data_c_1_0)
                    elif data[2][0]<0:
                        data[2][0]=(-1)*b_sum/math.sqrt(1+data_c_2_0*data_c_2_0+data_c_1_0*data_c_1_0)
                    data[2][1]=data[2][0]*data_c_1_0
                    data[2][2]=data[2][0]*data_c_2_0
                #======================================
                fileHandle = open('POSCAR','a')
                #fileHandle = open(str(a_sum)+str(b_sum)+str(c_sum),'a') #TEST PURPOSE ONLY
                file = open(POSCAR_file,'r')
                lineNum=0
                for line in file.readlines()[0:2]:
                    fileHandle.write(line)
                file.close()
                fileHandle.write('      '+str(data[0][0])+'     '+str(data[0][1])+'     '+str(data[0][2])+'\n')
                fileHandle.write('      '+str(data[1][0])+'     '+str(data[1][1])+'     '+str(data[1][2])+'\n')
                fileHandle.write('      '+str(data[2][0])+'     '+str(data[2][1])+'     '+str(data[2][2])+'\n')
                filename = POSCAR_file
                ffopen = open(filename)
                next (ffopen)
                next (ffopen)
                next (ffopen)
                next (ffopen)
                next (ffopen)

                for e in ffopen:
                    fileHandle.write(e)
                ffopen.close()
                fileHandle.close()


                #starting calculation
                #os.system("./run.sh")                                                      #LOCAL CALCULATION ONLY
                #os.system(yhrun -p TH_BM -n 24 /vol6/home/zjumsejjz4/bin/vasp5.3.5-neb)
                #mvcont='mv CONTCAR'+' CONTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                #mvpos='mv POSCAR'+' POSCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                #mvout='mv OUTCAR'+' OUTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                os.system('mkdir'+' '+str(a_sum)+str(b_sum)+str(b_sum))
                os.system('cp INCAR POTCAR KPOINTS std.pbs POSCAR vdw_kernel.bindat'+' '+str(a_sum)+str(b_sum)+str(b_sum))
                os.chdir('./'+str(a_sum)+str(b_sum)+str(b_sum))
#                os.system('yhbatch -p TH_BM -n 12 -JXCC_OPT run.sh')                       #open this if want to submit job automatically
                os.system('qsub -N '+str(a_sum)+str(a_sum)+str(a_sum)+' std.pbs')
                os.chdir('../')
                os.system('rm POSCAR')
                extration.append("'"+str(a_sum)+str(b_sum)+str(b_sum)+"'")
#=================================generate data_extration.py=================================
        devide = ','
        extration_all = devide.join(extration)
        #print extration_all
        file_extration = open('data_extration.py','a')
        file_extration.write('import os'+'\n')
        file_extration.write('for i in ('+extration_all+'):'+'\n')
        file_extration.write('    print i'+'\n')
        file_extration.write('    os.chdir(i)'+'\n')
        file_extration.write('''    os.system("grep 'energy(sigma->0) =' OUTCAR | tail -1")'''+'\n')
        file_extration.write('    print '+r"'\n'"+'\n')
        file_extration.write('    print '+r"'\n'"+'\n')
        file_extration.write("    os.chdir('../')"+'\n')

                #os.system(mvpos)
                #os.system(mvout)
    else:
        print 'ALL AXIS ARE DIFFERENT\n'
        #=====================================

        for a_sum in frange(a_min,a_max,a_step):
            for b_sum in frange(b_min,b_max,b_step):
                for c_sum in frange(c_min,c_max,c_step):
                    #=====================a opt================================
                    if int(data[0][0])==0:
                        if int(data[0][1])==0:
                            if data[0][2]>0:
                                data[0][2]=a_sum               #if a1=0 and a2=0 then a3 is alone
                            elif data[0][2]<0:
                                data[0][2]=(-1)*a_sum
                        else:                              #if a1=0 and a2<>0 then use a2 as constant
                            data_a_2_1=data[0][2]/data[0][1]
                            if data[0][1]>0:
                                data[0][1]=a_sum/math.sqrt(1+data_a_2_1*data_a_2_1)
                            elif data[0][1]<0:
                                data[0][1]=(-1)*a_sum/math.sqrt(1+data_a_2_1*data_a_2_1)
                            data[0][2]=data[0][1]*data_a_2_1
                    else:
                        data_a_1_0=data[0][1]/data[0][0]
                        data_a_2_0=data[0][2]/data[0][0]
                        if data[0][0]>0:
                            data[0][0]=a_sum/math.sqrt(1+data_a_2_0*data_a_2_0+data_a_1_0*data_a_1_0)
                        elif data[0][0]<0:
                            data[0][0]=(-1)*a_sum/math.sqrt(1+data_a_2_0*data_a_2_0+data_a_1_0*data_a_1_0)
                        data[0][1]=data[0][0]*data_a_1_0
                        data[0][2]=data[0][0]*data_a_2_0
                    #======================================

                    #=====================b opt================================
                    if int(data[1][0])==0:
                        if int(data[1][1])==0:
                            if data[1][2]>0:
                                data[1][2]=b_sum
                            elif data[1][2]<0:
                                data[1][2]=(-1)*b_sum
                        else:
                            data_b_2_1=data[1][2]/data[1][1]
                            if data[1][1]>0:
                                data[1][1]=b_sum/math.sqrt(1+data_b_2_1*data_b_2_1)
                            elif data[1][1]<0:
                                data[1][1]=(-1)*b_sum/math.sqrt(1+data_b_2_1*data_b_2_1)
                            data[1][2]=data[1][1]*data_b_2_1
                    else:
                        data_b_1_0=data[1][1]/data[1][0]
                        data_b_2_0=data[1][2]/data[1][0]
                        if data[1][0]>0:
                            data[1][0]=b_sum/math.sqrt(1+data_b_2_0*data_b_2_0+data_b_1_0*data_b_1_0)
                        elif data[1][0]<0:
                            data[1][0]=(-1)*b_sum/math.sqrt(1+data_b_2_0*data_b_2_0+data_b_1_0*data_b_1_0)
                        data[1][1]=data[1][0]*data_b_1_0
                        data[1][2]=data[1][0]*data_b_2_0
                    #======================================

                    #=====================c opt================================
                    if int(data[2][0])==0:
                        if int(data[2][1])==0:
                            if data[2][2]>0:
                                data[2][2]=c_sum
                            elif data[2][2]<0:
                                data[2][2]=(-1)*c_sum
                        else:
                            data_c_2_1=data[2][2]/data[2][1]
                            if data[2][1]>0:
                                data[2][1]=c_sum/math.sqrt(1+data_c_2_1*data_c_2_1)
                            elif data[2][1]<0:
                                data[2][1]=(-1)*c_sum/math.sqrt(1+data_c_2_1*data_c_2_1)
                            data[2][2]=data[2][1]*data_c_2_1
                    else:
                        data_c_1_0=data[2][1]/data[2][0]
                        data_c_2_0=data[2][2]/data[2][0]
                        if data[2][0]>0:
                            data[2][0]=c_sum/math.sqrt(1+data_c_2_0*data_c_2_0+data_c_1_0*data_c_1_0)
                        elif data[2][0]<0:
                            data[2][0]=(-1)*c_sum/math.sqrt(1+data_c_2_0*data_c_2_0+data_c_1_0*data_c_1_0)
                        data[2][1]=data[2][0]*data_c_1_0
                        data[2][2]=data[2][0]*data_c_2_0
                    #======================================
                    fileHandle = open('POSCAR','a')
                    #fileHandle = open(str(a_sum)+str(b_sum)+str(c_sum),'a') #TEST PURPOSE ONLY
                    file = open(POSCAR_file,'r')
                    lineNum=0
                    for line in file.readlines()[0:2]:
                        fileHandle.write(line)
                    file.close()
                    fileHandle.write('      '+str(data[0][0])+'     '+str(data[0][1])+'     '+str(data[0][2])+'\n')
                    fileHandle.write('      '+str(data[1][0])+'     '+str(data[1][1])+'     '+str(data[1][2])+'\n')
                    fileHandle.write('      '+str(data[2][0])+'     '+str(data[2][1])+'     '+str(data[2][2])+'\n')
                    filename = POSCAR_file
                    ffopen = open(filename)
                    next (ffopen)
                    next (ffopen)
                    next (ffopen)
                    next (ffopen)
                    next (ffopen)

                    for e in ffopen:
                        fileHandle.write(e)
                    ffopen.close()
                    fileHandle.close()


                    #starting calculation
                    #os.system("./run.sh")                                                      #LOCAL CALCULATION ONLY
                    #os.system(yhrun -p TH_BM -n 24 /vol6/home/zjumsejjz4/bin/vasp5.3.5-neb)
                    #mvcont='mv CONTCAR'+' CONTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                    #mvpos='mv POSCAR'+' POSCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                    #mvout='mv OUTCAR'+' OUTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                    os.system('mkdir'+' '+str(a_sum)+str(b_sum)+str(c_sum))
                    os.system('cp INCAR POTCAR KPOINTS std.pbs POSCAR vdw_kernel.bindat'+' '+str(a_sum)+str(b_sum)+str(c_sum))
                    os.chdir('./'+str(a_sum)+str(b_sum)+str(c_sum))
#                    os.system('yhbatch -p TH_BM -n 12 -JXCC_OPT run.sh')                       #open this if want to submit job automatically
                    os.system('qsub -N '+str(a_sum)+str(a_sum)+str(a_sum)+' std.pbs')
                    os.chdir('../')
                    os.system('rm POSCAR')
                    extration.append("'"+str(a_sum)+str(b_sum)+str(c_sum)+"'")
#=================================generate data_extration.py=================================
        devide = ','
        extration_all = devide.join(extration)
        #print extration_all
        file_extration = open('data_extration.py','a')
        file_extration.write('import os'+'\n')
        file_extration.write('for i in ('+extration_all+'):'+'\n')
        file_extration.write('    print i'+'\n')
        file_extration.write('    os.chdir(i)'+'\n')
        file_extration.write('''    os.system("grep 'energy(sigma->0) =' OUTCAR | tail -1")'''+'\n')
        file_extration.write('    print '+r"'\n'"+'\n')
        file_extration.write('    print '+r"'\n'"+'\n')
        file_extration.write("    os.chdir('../')"+'\n')

#===================================================================================================



print 'done'
