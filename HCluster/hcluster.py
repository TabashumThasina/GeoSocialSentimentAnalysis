import re
import clusters
post={}
wordcounts={}
apcount={}
newsByLine = [ line for line in open("TranslatedToEnglish.txt")]
def createDictionaryNewsById():
    i=1
    newss=""
    
    post.setdefault(str("i"),"")
    for news in newsByLine:
        list_of_output=[]
        print i
        if (news.rfind(str(i+1)))>-1:
           post[str(i)]="".join(str(x)for x in newss)
           newss=""
           i=i+1
           post.setdefault(str(i),"")
        newss= newss+news
def getwordcounts():
    for (key,val) in post.items():
        txt = val
        wc={}
        try:
            words= re.compile(r'[^A-Z^a-z]+').split(txt)
            for word in words:
                wc.setdefault(word,0)
                wc[word]+=1
            wordcounts[key]=wc
            for(word,count) in wc.items():
                apcount.setdefault(word,0)
                if count > 1:
                    apcount[word]+=1
        except TypeError,e:
            continue 
    #print apcount
        
        #print wc
        #print wordcounts[key]
       
createDictionaryNewsById()
getwordcounts()
wordlist = []
for (w, bc) in apcount.items():
    wordlist.append(w)
out = open('blogdata2.txt', 'w')
#out.write('Blog')
for word in wordlist:
    out.write('\t%s' % word)
out.write('\n')
for (blog, wc) in wordcounts.items():
    #print (blog)
    out.write(blog)
    for word in wordlist:
        if word in wc:
            out.write('\t%d' % wc[word])
        else:
            out.write('\t0')
    out.write('\n')
out.close()

