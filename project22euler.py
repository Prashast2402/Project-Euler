with open("p022_names.txt","r") as f:
    for line in f:
        name=[str(v.strip('"')) for v in line.split(",")]
name.sort()
tot=0
for i in range(len(name)):
        tot=tot+(sum(ord(letter)-64 for letter in name[i])*(i+1))
print(tot)
'''2nd method'''
name=[]
with open("p022_names.txt","r") as f:
    for line in f:
        name.extend(v.strip('"') for v in line.split(","))
name.sort()
tot=0
for i in range(len(name)):
        tot=tot+(sum(ord(letter)-64 for letter in name[i])*(i+1))
print(tot)


    
    



