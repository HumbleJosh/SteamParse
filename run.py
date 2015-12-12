_author_ = "bernardo"

import re


text_file = open("v2.xml", "r")
msg = text_file.read()
print len(msg)

regex = r'(?s)<app>(?:.*?)<appid>((.*?)?)</appid>(?:.*?)<name>(.*?)?</name>(?:.*?)</app>'


person = re.findall(regex, msg)
#print(person)


import urllib2
with open("file.xml", "a") as myfile:
    myfile.write("<applist><apps>")
    for x in person:
        app = x[1]
        request = urllib2.Request('https://steamdb.info/app/'+str(app)+'/', headers={"User-Agent": "Mozilla/4.0 (compatible; MSIE 4.01; Windows NT)"})
        contents = urllib2.urlopen(request).read()


        if "<table class=\"table table-fixed table-prices table-hover table-sortable" in contents:
            myfile.write("<app><appid>"+x[1]+"</appid><name>"+x[2]+"</name></app>")
            print "ok " + x[2]
        else:
            print "not " + x[2]
    myfile.write("</applist></apps>")
