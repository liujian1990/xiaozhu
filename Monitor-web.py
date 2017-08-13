
import httplib
import urlparse
import logging

#tenantid  and p_obj2id is talk userid
#luid is room id

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='xiaozhu.log',
                filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def request(url, cookie=''):
    ret = urlparse.urlparse(url)  # Parse input URL
    if ret.scheme == 'http':
        conn = httplib.HTTPConnection(ret.netloc)
    elif ret.scheme == 'https':
        conn = httplib.HTTPSConnection(ret.netloc)

    url = ret.path
    if ret.query: url += '?' + ret.query
    if ret.fragment: url += '#' + ret.fragment
    if not url: url = '/'

    conn.request(method='GET', url=url, headers={'Cookie': cookie})
    return conn.getresponse()

def getmsg():
    isNewmsg=False;
    cookie_str="newcheckcode=fb17e4a244256449ed19e3c9a7ed012e " \
               "gr_user_id=4cc643c4-3132-45a1-a02f-370f37cc358a " \
               "gr_session_id_59a81cc7d8c04307ba183d331c373ef6=15178fdd-cb0b-4442-bb88-6891b52b8992 " \
               "gr_cs1_93b793ea-a3f3-4124-88de-52388092c7df=user_id:10828045659 " \
               "gr_cs1_15178fdd-cb0b-4442-bb88-6891b52b8992=user_id:3570009229"
    url="http://imserver.xiaozhu.com:8080/webim/pushlet.srv?p_id=aaf0a0cbede2d5929fb8e5026f392d68&p_event=refresh" \
        "&p_from=3570009229&p_from_client=h5-fk" \
        "&sessid=801fae17767afed6c819dfba3a7c1702" \
        "&jsoncallback=jQuery21105148322051926567_1502052263375&_="
    tm = 1502052263388
    while True:
        tm = tm + 1
        urlf = url + str(tm)
        html_doc = request(urlf, cookie_str).read()
        info = html_doc[130:-256]
        print "-tm--"
        print html_doc
        print "info",info
        if len(info) > 10 :
            if  not isNewmsg:
                #logging.info(info)
                isNewmsg=True
            else:
                isNewmsg=False #ensure towice info not saved

def getlist():
    cookie_str=""
    url="https://wirelesspub.xiaozhu.com/app/xzfk/html5/500/im/talklist?jsonp=msglist_callback&offset=1&step=10" \
        "&userid=3570009229&sessid=801fae17767afed6c819dfba3a7c1702&userId=3570009229" \
        "&sessId=801fae17767afed6c819dfba3a7c1702&jsonp=msglist_callback&timestamp=1502052268483&_=" \
        "1502052263380"
print "______START________"
getmsg()



