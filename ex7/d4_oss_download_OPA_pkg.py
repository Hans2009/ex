import urllib.request
import urllib.parse
import http.cookiejar

url = "http://rsl-ossweb20.labs.lenovo.com:9084/OssWeb/RedLogon.do"

postdata = urllib.parse.urlencode({
    "userId":"lishuai6@lenovo.com",
    "password":"ssss"
}).encode('utf-8')

req = urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')
#create cookie object
cjar = http.cookiejar.CookieJar()
#Create cookie processor
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
#Set opener as global parameter
urllib.request.install_opener(opener)
file = opener.open(req)
data = file.read()
file = open("/hans/study/ex/ex7/2.html","wb")
file.write(data)
file.close()



#url2= "http://rsl-ossweb20.labs.lenovo.com:9084/OssWeb/DisplayOssForm.do?formId=88905"
url2 = "http://rsl-ossweb20.labs.lenovo.com:9084/OssWeb/DisplayOssForm.do?formId=87437"
data2 = urllib.request.urlopen(url2).read()
fhandle = open("/hans/study/ex/ex7/3.html","wb")
fhandle.write(data2)
fhandle.close()


#url3 =  "http://rsl-ossweb20.labs.lenovo.com:9084/OssWeb/DownloadRepositoryFile.do?filename=intc_sw_nic_10.6.0.0.134_linux_x86_64.txt"
url4 =  "http://rsl-ossweb20.labs.lenovo.com:9084/OssWeb/DownloadRepositoryFile.do?filename=IntelOPA-IFS.RHEL74-x86_64.10.6.0.0.112.tgz"

#urllib.request.urlretrieve(url3,filename='oss_readme.txt')
urllib.request.urlretrieve(url4,filename='IFS-RHEL74-10.6.0.0.0.112.tgz')

######################################


