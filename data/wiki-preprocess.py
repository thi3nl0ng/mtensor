import xml.etree.ElementTree as etree
import codecs
import csv
import time
import os

# http://www.ibm.com/developerworks/xml/library/x-hiperfparse/

PATH_WIKI_XML = 'your folder'
FILENAME_WIKI = 'enwiki-20181120-stub-meta-history27.xml'
FILENAME_ARTICLES = 'enwiki27.csv'

ENCODING = "utf-8"
Time_format = '%Y-%m-%d %H:%M:%S'

# Nicely formatted time string
def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)


def strip_tag_name(t):
    t = elem.tag
    idx = k = t.rfind("}")
    if idx != -1:
        t = t[idx + 1:]
    return t


pathWikiXML = os.path.join(PATH_WIKI_XML, FILENAME_WIKI)
pathArticles = os.path.join(PATH_WIKI_XML, FILENAME_ARTICLES)


totalCount = 0

title = None
start_time = time.time()

with codecs.open(pathArticles, "w", ENCODING) as articlesFH:
    articlesWriter = csv.writer(articlesFH, quoting=csv.QUOTE_MINIMAL)
    

    #articlesWriter.writerow(['title', 'user', 'timstamp'])
    

    for event, elem in etree.iterparse(pathWikiXML, events=('start', 'end')):
        tname = strip_tag_name(elem.tag)

        if event == 'start':
            if tname == 'page':

                title = ''
                user = ''
                stamp = ''
                inrevision = False
                incontributor = False
                ns = 0
            elif tname == 'revision':
                inrevision = True
            elif tname == 'contributor' and inrevision:
                incontributor = True
        else:
            #if tname == 'title':
            if tname == 'id' and not inrevision:
                title = elem.text
            elif tname == 'timestamp' and inrevision:
                stamp = elem.text
            #elif (tname == 'username' or tname == 'ip') and incontributor:
            elif (tname == 'id' or tname == 'ip') and incontributor:  
                user = elem.text  
            elif tname == 'revision':
                totalCount += 1
                
                timeinhour = time.mktime(time.strptime(stamp.replace('Z', '').replace('T', ' '), Time_format))
                #articlesWriter.writerow([title, user, int(time.mktime(timeint)), 1])
                #print (time.strftime("%Y%m%d%H", time.gmtime(timeinhour)))
                articlesWriter.writerow([user,title,time.strftime("%Y%m%d%H", time.gmtime(timeinhour))])

                # if totalCount > 100000:
                #  break

                if totalCount > 1 and (totalCount % 100000) == 0:
                    print("{:,}".format(totalCount))

            elem.clear()

elapsed_time = time.time() - start_time

print("Total instances: {:,}".format(totalCount))

print("Elapsed time: {}".format(hms_string(elapsed_time)))
