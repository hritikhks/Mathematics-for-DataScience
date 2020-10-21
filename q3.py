import random
import numpy


def  PrintCounterExamp(Mat, x):
	print("----counter example: ",count, " ------------------------ ")
	print("matrix Mat:")
	for i in range(0, len(Mat)):
		print(Mat[i])
	print("vector X:")
	print(x)


count=0
x = [1,3]
Mat = [[0,1],[1,0]]

while count <=10:
    vec_x1=[random.randrange(-10,10),random.randrange(-10,10)]
    vec_x2 =[random.randrange(-10,10),random.randrange(-10,10)]

    dif=0
    while dif == 0:
        Mat = [[random.randrange(-100,100),random.randrange(-100,100)],[random.randrange(-100,100),random.randrange(-100,100)]]
        dif = Mat[0][1] - Mat[1][0]

   
    a = random.uniform(0,1)
    temp1 = [i*a for i in vec_x1]
    temp2 =  [i*(1-a) for i in vec_x2]
    res = []
    for i in range(0, len(temp2)):
    	res.append(temp1[i] + temp2[i])

    l = numpy.dot( numpy.dot(res,Mat), res)
    r = a* numpy.dot( numpy.dot(vec_x1,Mat), vec_x1) + (1-a)* numpy.dot( numpy.dot(vec_x2,Mat), vec_x2)
    
    if r < l :
    	count += 1
    	PrintCounterExamp(Mat, x)
    



