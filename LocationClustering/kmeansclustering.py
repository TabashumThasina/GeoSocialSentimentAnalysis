import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from xlwt import Workbook
style.use("ggplot")
from sklearn.cluster import KMeans
from statistics import mode

wb=Workbook()
sheet1=wb.add_sheet('location')
sheet1.col(0).width=1000
sheet1.col(1).width=10000
sheet1.col(2).width=1000
X=np.empty((9000,2))
counter =1
index1=0
xl =pd.ExcelFile('demo.xlsx')
df = xl.parse("Sheet1")

def KmeanLocation(index1,index2,newsId):
    print "News ID ",newsId
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X[index1:index2+1][:])

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_


    colors = ["g.","r.","c.","y."]



    vote_label1=[]
    vote_label2=[]
    vote_label3=[]
    vote_label4=[]
    #for i in range(len(labels)):
        #if(labels[i] == 0):
            #if df['Sen'][i] == 'neg':
                #vote_label1.append(df['Sen'][i])
        #elif (labels[i]==1):
            #if df['Sen'][i]=='neg':
                #vote_label2.append(df['Sen'][i])
    #if len(vote_label1)>len(vote_label2):
        #mode_label1='neg'
        #mode_label2='pos'
    #else:
        #mode_label1='pos'
        #mode_label2='neg'
    for i in range(len(labels)):
        if(labels[i] == 0):
            vote_label1.append(df['Sen'][i])
        elif (labels[i]==1):
            vote_label2.append(df['Sen'][i])
        elif(labels[i] == 2):
            vote_label3.append(df['Sen'][i])
   
    mode_label1=mode(vote_label1)
    mode_label2=mode(vote_label2)
    mode_label3=mode(vote_label3)
   

    print mode_label1,mode_label2,mode_label3

    if mode_label1 == 'neg':
                               colors[0]="r"
    elif mode_label1 == 'pos':
                               colors[0]="g"
    if mode_label2 == 'neg':
                               colors[1]="r"
    elif mode_label2 == 'pos':
                               colors[1]="g"
    if mode_label3 == 'neg':
                               colors[2]="r"
    elif mode_label3 == 'pos':
                               colors[2]="g"
    sub=1
    if newsId==1:
        sub=0
    
    for i in range(len(X[index1:index2+1][:])):
        if i>index2:
            break
        print("coordinate:",X[i], "label:", labels[i])
        plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)
        sheet1.write(i+index1-sub,0,newsId)
        sheet1.write(i+index1-sub,1,labels[i])
        if labels[i]==0:
            sheet1.write(i+index1-sub,2,mode_label1)
        elif labels[i]==1:
            sheet1.write(i+index1-sub,2,mode_label2)
        elif labels[i]==2:
            sheet1.write(i+index1-sub,2,mode_label3)
        

    #plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

    #plt.show()


for i in df.index:
    newsId=df["NewsId"][i]
    if(newsId == counter+1):
        try:
            KmeanLocation(index1,i-1,counter)
        except:
            counter=counter+1
        index1=i
    x=df['lat'][i]
    y=df['long'][i]
    X[i][0]=x
    X[i][1]=y

wb.save('LocationCluster2.xls')
