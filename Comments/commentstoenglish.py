# -*- coding: utf8 -*-
from googletrans import Translator
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from xlwt import Workbook
translator = Translator()

# Bangla to english translation using googletrans within 1000 char from file name
# 'in.txt'

wb=Workbook()
sheet1=wb.add_sheet('comments')
sheet1.col(0).width=1000
sheet1.col(1).width=10000
xl =pd.ExcelFile('allCommentsDatasetWithNewsID.xlsx')
df = xl.parse("ALLCommentsDATA")
for i in df.index:
    id=df['news_id'][i]
    sheet1.write(i,0,id)
    try:
        inputText= df['message'][i]
        if(len(inputText) > 1000):
                continue
        tranText = translator.translate(inputText, dest='en')
        sheet1.write(i,1,tranText.text)
        
    except:
        sheet1.write(i,1,'unicode error')
        continue

wb.save('commentsinenglish.xls')
