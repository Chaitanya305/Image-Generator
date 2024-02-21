with open("file.txt", 'r') as f:
    lines=f.readlines()
    Nlines=[]
    for index, i in enumerate(lines):
        if index < 3 :
            i=i.strip("\n")
            Nlines.append(i)
        else:
            break
    #lines=[j.strip("\n") if i < 2 else break for i, j in enumerate(lines)]
    #print (lines)
    #print(Nlines)
    
## for python version  
line1=Nlines[0]
#print (line1.split(" "))
p_v = line1.split(" ")[2].capitalize()
#print(p_v.capitalize())
#for R version 
line2=Nlines[1]
#print (line2.split(" "))
r_v = line2.split(" ")[2].capitalize()
#print(r_v)
#base os
line3=Nlines[2]
#print (line3.split(" "))
base_os = line3.split(" ")[2]
#print(base_os)
if p_v in ["3.8.0", "3.9.0", "3.10.0"] and r_v in ["3.6", "4.3"] and base_os=="centos":
    print ("build docker image for p and R both")
elif p_v in ["3.8.0", "3.9.0", "3.10.0"] and r_v=="False" and base_os=="centos":
    print("build python image alone")
elif p_v=="False" and r_v in ["3.6", "4.3"] and base_os=="centos":
    print("build R image alone")
elif p_v in ["3.8.0", "3.9.0", "3.10.0"] and r_v in ["3.6", "4.3"] and base_os=="debian":
    print ("build docker image for p and R both")
elif p_v in ["3.8.0", "3.9.0", "3.10.0"] and r_v=="False" and base_os=="debian":
    print("build python image alone")
elif p_v=="False" and r_v in ["3.6", "4.3"] and base_os=="debian":
    print("build R image alone")
else:
    print ("provide correct details")