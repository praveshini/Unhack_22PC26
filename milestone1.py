import csv
import math

careArea=[]
care="KLA\\Dataset-0\\Dataset-0\\1st\\CareAreas.csv"
metadata="KLA\\Dataset-0\\Dataset-0\\1st\\metadata.csv"
mainField=0
mSide=0
subSide=0
subField=0
points=[]
mainCoord=[]


def distance(val1,val2):
    x_coord1=float(val1[0])
    y_coord1=float(val1[1])
    x_coord2=float(val2[0])
    y_coord2=float(val2[1])

    return math.sqrt((x_coord1-x_coord2)**2+(y_coord1-y_coord2)**2)


def componentArea():

    global mainField
    global subField
    global mSide
    global subSide
    with open(metadata,'r') as datafile:
        rows=[]
        fd=csv.reader(datafile)
        fields=next(fd)
        for i in fd:
            rows.append(i)
        
        mSide=float(rows[0][0])
        subSide=float(rows[0][1])
        mainField=float(rows[0][0])**2
        subField=float(rows[0][1])**2


    with open(care,'r') as datafile:
        fd=csv.reader(datafile)
        for i in fd:
            val1=[i[1],i[3]]
            val2=[i[2],i[4]]
            points.append([val1,val2])
            careArea.append(distance(val1,val2)**2/2)
        #print(points)
            

def mainFieldCoord():

    file = open('mainCoord.csv', 'w+', newline ='')
    w=csv.writer(file)
    temp=[]
    for i in range(169):
        c1=[points[i][0][0],points[i][0][1]]
        c2=[str(float(points[i][0][0])+mSide),str(float(points[i][0][1])+mSide)]
        temp=[i,c1[0],c2[0],c1[1],c2[1]]
        w.writerow(temp)


def subFieldCoord():
    file = open('subCoord.csv', 'w+', newline ='')
    w=csv.writer(file)
    h=-1


    for i in range(len(careArea)):
        temp=[]
        c1=[float(points[i][0][0]),float(points[i][0][1])]
        c2=[float(points[i][1][0]),float(points[i][1][1])]

        area=careArea[i]
        noOfSub=math.ceil(area/subField)
        #print(noOfSub)
        #print(100/5.12)
        careSide=math.sqrt(area)
        boxRow=math.ceil(careSide/subSide)
        cty1=c1[1]
        cty2=c1[1]+subSide

        for k in range(boxRow):
            ctx1=c1[0]
            ctx2=c1[0]+subSide
            
            for j in  range(boxRow):
                temp=[]
                h=h+1
                temp=[h,ctx1,ctx2,cty1,cty2,i]
                ctx1=ctx1+subSide
                ctx2=ctx2=ctx2+subSide

                
                w.writerow(temp)
            cty1=cty1+subSide
            cty2=cty2+subSide
                

        







componentArea()
mainFieldCoord()
subFieldCoord()



