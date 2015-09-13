import re


text_file = open("file.xml", "r")
msg = text_file.read()
print len(msg)

regex = r'(?s)<app>(?:.*?)<appid>((.*?)?)</appid>(?:.*?)<name>(.*?)?</name>(?:.*?)</app>'


person = re.findall(regex, msg)
#print(person)

hello2 = [[x[0], x[1] ,x[2].strip(' ')]for x in person]

persdonsorte = sorted(hello2, key=lambda k: k[2].upper()) 

import urllib2
with open("filesorted.xml", "a") as myfile:
    myfile.write("<applist><apps>")
    for x in persdonsorte:

        myfile.write("<app><appid>"+x[1]+"</appid><name>"+x[2]+"</name></app>")

    myfile.write("</apps></applist>")
