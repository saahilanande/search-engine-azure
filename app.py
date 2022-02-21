import re
from flask import Flask, render_template, request,redirect,url_for



app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
            if request.form.get("fbutton"):
                searchword = request.form['txt1']
                if len(searchword)!=0:
                    final = alice(searchword)
                    final.append(wonder(searchword))
                    final.append(candide(searchword))
                    final.append(doDonQuijoten(searchword))
                    final.append(Shakespeare(searchword))
                    return render_template('home.html',heading="SEARCH RESULTS",display=final)
                else:
                    final = ['PLEASE ENTER SOME VALUE TO SEARCH']
                    return render_template('home.html',heading="SEARCH RESULTS",display=final)

            else:
                return render_template('home.html')
    else:
        return render_template('home.html')

results=[]

def alice(word):
    stop = addstopwords()
    count = 0
    foundcount = 0
    file = open(r'AliceCleaner.txt', encoding="utf-8")
    lines = file.readlines()
    for data in lines:
        data = data.lower()
        data = data.replace(".","")
        data = data.replace(",","")
        data = data.replace(":","")
        data = data.replace("\"","")
        data = data.replace("!","")
        data = data.replace("'","")
        data = data.replace("â€˜","")
        data = data.replace("*","")
        data = data.replace("|","")
        data = data.replace("#","")
        data = data.replace("'","")
        data = data.replace("’","")
        data = data.replace("?","")
        data = data.replace('“',"")
        data = data.replace('”',"")
        data = data.replace('_',"")
        for x in stop:
            data = data.replace("\\b"+x+"\\b","")
        normalstring = str(data)
        index = normalstring.find(""+word+"")
        count = count + 1
        if index != -1:
            item1 = "FOUND IN FILE: AliceCleaner.TXT"
            item2 = "LINE NO:"+str(count)+""
            item3 = "CHARACTER NO IN LINE:"+str(index)+""
            item4 = normalstring
            results.extend([item1,item2,item3,item4])
            foundcount = foundcount + 1

    if foundcount == 0:
        fail = 'NO SEARCH FOUND IN AliceCleaner.txt'
        results.append(fail)
        return results
    else:
        return results


def wonder(word):
    stop = addstopwords()
    count = 0
    foundcount = 0
    file = open(r'AliceInWonderland.txt', encoding="utf-8")
    lines = file.readlines()
    for data in lines:
        data = data.lower()
        data = data.replace(".","")
        data = data.replace(",","")
        data = data.replace(":","")
        data = data.replace("\"","")
        data = data.replace("!","")
        data = data.replace("'","")
        data = data.replace("â€˜","")
        data = data.replace("*","")
        data = data.replace("|","")
        data = data.replace("#","")
        data = data.replace("'","")
        data = data.replace("’","")
        data = data.replace("?","")
        data = data.replace('“',"")
        data = data.replace('”',"")
        data = data.replace('_',"")
        for x in stop:
            data = data.replace("\\b"+x+"\\b","")
        normalstring = str(data)
        index = normalstring.find(""+word+"")
        count = count + 1
        if index != -1:
            item1 = "FOUND IN FILE: AliceInWonderland.TXT"
            item2 = "LINE NO:"+str(count)+""
            item3 = "CHARACTER NO IN LINE:"+str(index)+""
            item4 = normalstring
            results.extend([item1,item2,item3,item4])
            foundcount = foundcount + 1

    if foundcount == 0:
        fail = 'NO SEARCH FOUND IN AliceInWonderland.txt'
        results.append(fail)
        return results
    else:
        return results

def candide(word):
    stop = addstopwords()
    count = 0
    foundcount = 0
    file = open(r'CandideEn.txt', encoding="utf-8")
    lines = file.readlines()
    for data in lines:
        data = data.lower()
        data = data.replace(".","")
        data = data.replace(",","")
        data = data.replace(":","")
        data = data.replace("\"","")
        data = data.replace("!","")
        data = data.replace("'","")
        data = data.replace("â€˜","")
        data = data.replace("*","")
        data = data.replace("|","")
        data = data.replace("#","")
        data = data.replace("'","")
        data = data.replace("’","")
        data = data.replace("?","")
        data = data.replace('“',"")
        data = data.replace('”',"")
        data = data.replace('_',"")
        for x in stop:
            data = data.replace("\\b"+x+"\\b","")
        normalstring = str(data)
        index = normalstring.find(""+word+"")
        count = count + 1
        if index != -1:
            item1 = "FOUND IN FILE: CandideEn.TXT"
            item2 = "LINE NO:"+str(count)+""
            item3 = "CHARACTER NO IN LINE:"+str(index)+""
            item4 = normalstring
            results.extend([item1,item2,item3,item4])
            foundcount = foundcount + 1

    if foundcount == 0:
        fail = 'NO SEARCH FOUND IN CandideEn.txt'
        results.append(fail)
        return results
    else:
        return results
    
def doDonQuijoten(word):
    stop = addstopwords()
    count = 0
    foundcount = 0
    file = open(r'DonQuijote.txt', encoding="utf-8")
    lines = file.readlines()
    for data in lines:
        data = data.lower()
        data = data.replace(".","")
        data = data.replace(",","")
        data = data.replace(":","")
        data = data.replace("\"","")
        data = data.replace("!","")
        data = data.replace("'","")
        data = data.replace("â€˜","")
        data = data.replace("*","")
        data = data.replace("|","")
        data = data.replace("#","")
        data = data.replace("'","")
        data = data.replace("’","")
        data = data.replace("?","")
        data = data.replace('“',"")
        data = data.replace('”',"")
        data = data.replace('_',"")
        for x in stop:
            data = data.replace("\\b"+x+"\\b","")
        normalstring = str(data)
        index = normalstring.find(""+word+"")
        count = count + 1
        if index != -1:
            item1 = "FOUND IN FILE: DonQuijote.TXT"
            item2 = "LINE NO:"+str(count)+""
            item3 = "CHARACTER NO IN LINE:"+str(index)+""
            item4 = normalstring
            results.extend([item1,item2,item3,item4])
            foundcount = foundcount + 1

    if foundcount == 0:
        fail = 'NO SEARCH FOUND IN DonQuijote.txt'
        results.append(fail)
        return results
    else:
        return results

    
def Shakespeare(word):
    stop = addstopwords()
    count = 0
    foundcount = 0
    file = open(r'Shakespeare.txt', encoding="utf-8")
    lines = file.readlines()
    for data in lines:
        data = data.lower()
        data = data.replace(".","")
        data = data.replace(",","")
        data = data.replace(":","")
        data = data.replace("\"","")
        data = data.replace("!","")
        data = data.replace("'","")
        data = data.replace("â€˜","")
        data = data.replace("*","")
        data = data.replace("|","")
        data = data.replace("#","")
        data = data.replace("'","")
        data = data.replace("’","")
        data = data.replace("?","")
        data = data.replace('“',"")
        data = data.replace('”',"")
        data = data.replace('_',"")
        for x in stop:
            data = data.replace("\\b"+x+"\\b","")
        normalstring = str(data)
        index = normalstring.find(""+word+"")
        count = count + 1
        if index != -1:
            item1 = "FOUND IN FILE: Shakespeare.TXT"
            item2 = "LINE NO:"+str(count)+""
            item3 = "CHARACTER NO IN LINE:"+str(index)+""
            item4 = normalstring
            results.extend([item1,item2,item3,item4])
            foundcount = foundcount + 1

    if foundcount == 0:
        fail = 'NO SEARCH FOUND IN Shakespeare.txt'
        results.append(fail)
        return results
    else:
        return results

    

"""def filesearchnltk():
    file = open(r'AliceCleaner.txt', encoding="utf-8")
    file_read = file.read()
    regex = nltk.RegexpTokenizer(r"\w+")
    
    stopdata = addstopwords()
    stpwrd = nltk.corpus.stopwords.words('english')
    stpwrd.extend(stopdata)
    
    
    removepunc = regex.tokenize(file_read)
    removestop = [words for words in removepunc if not words in stpwrd]
    normalstring = nltk.Text(removestop)

    return normalstring"""
    
    

def addstopwords():
    stopfile = open('stopwords.txt', encoding="utf-8")
    read = stopfile.read()
    morestop=[]
    for rem in read.lower().split():
        rem = rem.replace("\"","")
        morestop.append(rem)
    return morestop


if __name__ == '__main__':
    app.run(debug =True,host='0.0.0.0')