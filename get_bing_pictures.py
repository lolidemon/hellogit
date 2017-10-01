import urllib
import urllib2
import sys
import os
import json

def save_pic(pic_url, local_path=sys.path[0] + '\\back_pic'):
    pic_name = pic_url[pic_url.rfind('/') + 1:]
    if not os.path.exists(local_path):
        os.mkdir(local_path)
    urllib.urlretrieve(pic_url, local_path + '\\' + pic_name)


def get_pic(json_url='http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&nc=1506734678595&FORM=HYLH&video=1'):
    site_url = 'http://cn.bing.com'

    request = urllib2.Request(url=json_url)
    response = urllib2.urlopen(request)
    page = response.read().decode('utf8')

    pics_json = json.loads(page)
    for pic_json in pics_json['images']:
        save_pic(site_url + pic_json['url'])

# getPic()
get_pic()
