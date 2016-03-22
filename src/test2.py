import micro_annot

x = [0]*20
y = [0]*20
z = [0]*20
annot = [0]*20

for i in range(0,5):
    annot[i] = 2

x[0] = 100
y[0] = 100
z[0] = 100

for j in range(10,15):
    annot[j] = 2

x[12] = 100
y[12] = 100
z[12] = 100


new_annot = micro_annot.micro_annotate(x,y,z,annot)

print annot
print new_annot



#for i in range(len(new_annot)):
#    if new_annot[i] != annot [i]:
#        print "Wrong"
