import urllib.request
import urllib.parse
url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LBuCC"
postdata = urllib.parse.urlencode({
    "username":"Hans_Li",
    "password":"Wonder2017"
}).encode('utf-8')

req = urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')
data = urllib.request.urlopen(req).read()

fhandle = open("/hans/study/ex/ex3/2.html","wb")
fhandle.write(data)
fhandle.close()


