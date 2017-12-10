#!/usr/bin/python
import ssl
import time,sys, os
import json
import requests

api_key = 't2LzCmHjtmkVxo8gV0dyovekWb3Cyut7owS7YIet'

url = 'https://bz.labs.lenovo.com'

print url 

#####################################
## Hans
#####################################
#bug_id = '77579'
bug_id = '122147'
bug_id2 = '114783'
#cmd = '/rest/bug/'+bug_id
#cmd = '/rest/bug?id='+bug_id + ',' + bug_id2
#cmd = '/rest/bug/' + bug_id + '/history'
#cmd = '/rest/bug?bug_severity=Emergency&bug_severity=High&bug_severity=Medium&bug_severity=Low&bug_status=Working&classification=IO_Options&component=Intel_OmniPath&list_id=3265843&product=Intel_OmniPath&query_format=advanced&resolution=---&version=18A_Block'
cmd = 'rest/bug/' + bug_id
#cmd = 'rest/bug/77579/comment'
uri = url + cmd
print uri

r = requests.get(uri, params={'api_key': api_key},verify=False)

print r.text
#print r.status_code
#exit
D = r.json()

#exit(0)

print len(D['bugs'])

