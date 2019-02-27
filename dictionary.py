a="server=s;dbname=d;user=u;passwd=p"

def exa():
	b=a.split(";")
	n=len(b)
	c=[]
	for i in range (0,n):
		c.append(b[i].split("="))
	nl=len(c)
	d={}
	for i in range (0,nl):
		d[c[i][0]]=c[i][1]
	return d

print(exa())		
