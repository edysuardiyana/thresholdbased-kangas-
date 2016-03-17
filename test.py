import operator

a = [1,2,3,4,5,6,6,7,0]

index, val = min(enumerate(a),key=operator.itemgetter(1))

print index
print val

z = abs(4-10)
print z

x = []

for i in range(3):
    m = i
    n = i+1
    x.append([m,n])

print x
