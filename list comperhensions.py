x=1
y=1
z=3
n=3





print([[i,j,k]  for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if (i+j+k)!=n])
