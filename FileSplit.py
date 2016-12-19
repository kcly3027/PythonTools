#encoding=gb2312
import os
import re

def splitfile(filepath,partialLine=10000*10):
    filedir,name = os.path.split(filepath)
    name,ext = os.path.splitext(name)
    filedir = os.path.join(filedir,name)
    if not os.path.exists(filedir):
        os.mkdir(filedir)
    partno = 0
    stream = open(filepath,'rb')
    while True:
        partfilename = os.path.join(filedir,name + '_' + str(partno) + ext)
        print 'write start %s' % partfilename
        part_stream = open(partfilename,'wb')
        read_count = 0
        read_count_once = 0
        while read_count < partialLine:
            read_content = stream.readline()
            read_count_once = len(read_content)
            if read_count_once > 0:
                result, number = re.subn('( {2,})', ',', read_content) 
                part_stream.write(result)
            else: 
                break
            read_count += 1
        part_stream.close()
        if read_count_once == 0:
            break;
        partno += 1
    print 'done'
splitfile(r'F:\20161216-50M-A.csv',100000)