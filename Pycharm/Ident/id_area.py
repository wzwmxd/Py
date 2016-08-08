# -*- coding: utf-8 -*-
import re, urllib2, sqlite3

conn = sqlite3.connect('ident_local.db')
cur = conn.cursor()
try:
    cur.execute('CREATE TABLE ident(id varchar(6) PRIMARY KEY,\
                local varchar(32),prov_id varchar(6),prov varchar(32));')
except:
    print 'TABLE "ident" EXISTS.'

url = 'http://www.qucha.net/shenfenzheng/city.htm'
text = urllib2.urlopen(url).read().decode('gb2312').replace(', ', '')
id_exp_head = ur'(110000 .+?)<br />[\r\n\t ]+'
id_exp_body = ur'<br />[\r\n\t ]+(.+?)<br />[\r\n\t ]+'
id_reg = re.compile(id_exp_head + id_exp_body * 64)
id_list = id_reg.findall(text)[0]
for i in range(31):
    prov = id_list[2 * i]
    local = id_list[2 * i + 1]
    prov_num, prov_name = prov.split(' ')
    local_list = local.split(' ')
    i = 0
    while i < len(local_list):
        local_num = local_list[i]
        local_name = local_list[i + 1]
        print local_num, local_name, prov_num, prov_name
        cur.execute("INSERT INTO ident(id,\
                local,prov_id ,prov) VALUES('%s','%s','%s','%s')" % (
            local_num, local_name, prov_num, prov_name
        ))
        i += 2
conn.commit()
cur.close()
conn.close()
