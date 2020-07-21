import re
f1=open("log.txt")
msg=f1.read()
target_msg=re.findall(r"\n\n(\S+)",msg)
print(target_msg)
res=[]
for item in target_msg:
    item += "\n"
    res.append(item)
print(res)
f2=open("write.txt","w")
f2.writelines(res)
f1.close()
f2.close()