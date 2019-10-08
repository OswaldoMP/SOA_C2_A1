
import datetime

now = datetime.datetime.now()

r = open('/home/oswaldo/UPCH/NovenoCuatrimestre/SOA/C2/A1/TXT.txt','r')#para almacenar el archivo

content = r.read()

print(content)

w = open('/home/oswaldo/UPCH/NovenoCuatrimestre/SOA/C2/A1/TXT.txt','w')#write

w.write(content + '\nHora : ' + str(now))
w.close()


#########################################