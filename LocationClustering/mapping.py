from mpl_toolkits.basemap import Basemap
import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from xlwt import Workbook

xl =pd.ExcelFile('Cluster3.xlsx')
df = xl.parse("Sheet1")

sent1_pos=0
sent2_pos=0
sent0_pos=0
sent1_neg=0
sent2_neg=0
sent0_neg=0
lat_clust0=[]
lon_clust0=[]
lat_clust1=[]
lon_clust1=[]
lat_clust2=[]
lon_clust2=[]
counter=0

    # draw parallels and meridians
    #m.drawmapboundary(fill_color='aqua')
def percentage(part, whole):
    try:
        return 100 * float(part)/float(whole)
    except:
        return 0

def draw():
    m = Basemap(projection='mill',llcrnrlat=21,urcrnrlat=29,
                llcrnrlon=86,urcrnrlon=94,resolution='c')
    #m = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,
                #llcrnrlon=-180,urcrnrlon=180,resolution='c')

    m.fillcontinents(color='coral',lake_color='aqua')
    m.drawcountries()
    m.drawstates()
    print 'cluster 0'
    print ('Percentage Of negative ',percentage(sent0_neg,sent0_neg+sent0_pos))
    print ('Percentage Of positive',percentage(sent0_pos,sent0_neg+sent0_pos))
    print 'cluster 1'
    print ('Percentage Of negative ',percentage(sent1_neg,sent1_neg+sent1_pos))
    print ('Percentage Of positive ',percentage(sent1_pos,sent1_neg+sent1_pos))
    print 'cluster 2'
    print ('Percentage Of negative ',percentage(sent2_neg,sent2_neg+sent2_pos))
    print ('Percentage Of postive ',percentage(sent2_pos,sent2_neg+sent2_pos))
    print 'error'
    x0,y0 = m(np.mean(lon_clust0),np.mean(lat_clust0))
    x1,y1 = m(np.mean(lon_clust1),np.mean(lat_clust1))
    x2,y2 = m(np.mean(lon_clust2),np.mean(lat_clust2))
    if (percentage(sent0_neg,sent0_neg+sent0_pos)>percentage(sent0_pos,sent0_neg+sent0_pos)):
        m.plot(x0,y0,'ro')
    else:
        m.plot(x0,y0,'go')
    if (percentage(sent1_neg,sent1_neg+sent1_pos)>percentage(sent1_pos,sent1_neg+sent1_pos)):
        m.plot(x1,y1,'ro')
    else:
        m.plot(x1,y1,'go')
    if (percentage(sent2_neg,sent2_neg+sent2_pos)>percentage(sent2_pos,sent2_neg+sent2_pos)):
        m.plot(x2,y2,'ro')
    else:
        m.plot(x2,y2,'go')

    plt.title("Location Clustering and Sentiment Analysis")
    plt.show()


for i in df.index:
    newsId=df['NewsId'][i]
    if(newsId==counter+1):
        counter=counter+1
        draw()
        lat_clust0=[]
        lon_clust0=[]
        lat_clust1=[]
        lon_clust1=[]
        lat_clust2=[]
        lon_clust2=[]
        sent1_pos=0
        sent2_pos=0
        sent0_pos=0
        sent1_neg=0
        sent2_neg=0
        sent0_neg=0
    clust=df['Location_Cluster(k=3)'][i]
    if clust == 0:
        lat_clust0.append(df['lat'][i])
        lon_clust0.append(df['long'][i])
        sent=df['Sen'][i]
        if(sent=='neg'):
            sent0_neg=sent0_neg+1
        else:
            sent0_pos=sent0_pos+1
        
    elif clust ==1:
        lat_clust1.append(df['lat'][i])
        lon_clust1.append(df['long'][i])
        sent=df['Sen'][i]
        if(sent=='neg'):
            sent1_neg=sent1_neg+1
        else:
            sent1_pos=sent1_pos+1
    elif clust ==2:
        lat_clust2.append(df['lat'][i])
        lon_clust2.append(df['long'][i])
        sent=df['Sen'][i]
        if(sent=='neg'):
            sent2_neg=sent2_neg+1
        else:
            sent2_pos=sent2_pos+1
        print sent0_pos,sent0_neg


