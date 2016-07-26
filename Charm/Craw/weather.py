# -*- coding: utf-8 -*-
import urllib2, re, sqlite3, datetime, time


def get_html(url):
    try:
        req_header = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'text/html;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'gzip',
            'Connection': 'close'
        }
        req = urllib2.Request(url, None, req_header)
        resp = urllib2.urlopen(req)
        return resp.read()  # decode('utf-8').encode()  # .decode('gbk').encode(type)
    except IOError:
        return ""


def find_weather(text):
    weather_reg_exp = r'<td width="96"><a .+?>(.+?)</a></td><td.+?>(.+?)</td><td.+?><span>(.+?)</span>' + \
                      r'<span.+?>(.+?)</span></td><td.+?>(.+?)</td><td.+?>(.+?)</td>' + \
                      r'<td.+?><span>(.+?)</span><span.+?>(.+?)</span></td><td.+?>(.+?)</td>'
    reg = re.compile(weather_reg_exp)
    today_reg_exp = r'<li class="selected">今天.+?\((\d+)月(\d+)日\)</li>'
    today_reg = re.compile(today_reg_exp)
    return re.findall(reg, text), re.findall(today_reg, text)


conn = sqlite3.connect('weather.db')
cur = conn.cursor()

try:
    cur.execute(
        'CREATE TABLE weather_day(city_date varchar(19)  PRIMARY KEY,\
        city varchar(8),weather varchar(10),\
        wind varchar (20),HDT varchar(8))'
    )
except:
    print 'TABLE weather_day exists.'
try:
    cur.execute(
        'CREATE TABLE weather_night(city_date varchar(19)  PRIMARY KEY,\
        city varchar(8),weather varchar(10),\
        wind varchar (20),LNT varchar(8))'
    )
except:
    print 'TABLE weather_night exists.'
url = 'http://www.weather.com.cn/textFC/'
area = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn', 'gat']

for a in area:
    weather_data = find_weather(get_html(url + a + '.shtml'))
    month, day = weather_data[1][0]
    month = int(month)
    day = int(day)
    year = datetime.datetime.now().year
    for weather in weather_data[0]:
        city_name, \
        weather_day, wind_day1, wind_day2, temp_day, \
        weather_night, wind_night1, wind_night2, temp_night = weather
        if weather_day != '-':
            try:
                cur.execute(
                    "INSERT INTO weather_day(city_date,city,weather,wind,HDT) \
                    VALUES(%s,%s,%s,%s,%s)" % (
                        "'%s-%d-%d-%d'" % (city_name, year, month, day),
                        "'%s'" % city_name,
                        "'" + weather_day + "'",
                        "'" + wind_day1 + ':' + wind_day2 + "'",
                        "'" + temp_day + "'"))
            except:
                pass
        if weather_night != '-':
            try:
                cur.execute(
                    "INSERT INTO weather_night(city_date,city,weather,wind,LNT) \
                    VALUES(%s,%s,%s,%s,%s)" % (
                        "'%s-%d-%d-%d'" % (city_name, year, month, day),
                        "'%s'" % city_name,
                        "'" + weather_night + "'",
                        "'" + wind_night1 + ':' + wind_night2 + "'",
                        "'" + temp_night + "'"))
            except:
                pass
conn.commit()
cur.execute('select * from weather_day')
result = cur.fetchall()
for r in result:
    for j in r:
        print j,
    print '\n'

cur.execute('select * from weather_night')
result = cur.fetchall()
for r in result:
    for j in r:
        print j,
    print '\n'
cur.close()
conn.close()
