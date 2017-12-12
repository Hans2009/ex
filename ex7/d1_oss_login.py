import urllib.request
import urllib.parse
#url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LBuCC"
#url = "http://rsl-ossweb20.labs.lenovo.com:9084/OssWeb/OneStopShopRedLogin.do"
#url = "http://rsl-ossweb20.labs.lenovo.com:9084/OssWeb/html/SecureLogon.html"
#url = "http://rsl-ossweb20.labs.lenovo.com:9084/OssWeb/j_security_check"
url = "http://rsl-ossweb20.labs.lenovo.com:9084/OssWeb/RedLogon.do"

postdata = urllib.parse.urlencode({
    "userId":"lishuai6@lenovo.com",
    "password":"ssss"
}).encode('utf-8')

req = urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')
data = urllib.request.urlopen(req).read()

fhandle = open("/hans/study/ex/ex7/1.html","wb")
fhandle.write(data)
fhandle.close()




