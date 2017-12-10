#!/usr/bin/python
import ssl
import time,sys, os
import json
import requests


#api_key = 'LzPsQjTED2zQS2SDrFZWBU6R383LZgEGp0bkSAu0'
api_key = 't2LzCmHjtmkVxo8gV0dyovekWb3Cyut7owS7YIet'

url = 'https://bz.labs.lenovo.com'

print url 

cmd = '/rest/bug??bug_status=Open&bug_status=Working&bug_status=Rejected&bug_status=Fixed&bug_status=Verify&classification=IO_Options&classification=Internal_Storage&classification=Storage_Controllers&f1=version&f3=OP&f4=priority&f5=bug_severity&f6=CP&f7=cf_tagging&j3=OR&list_id=1738927&n7=1&o1=anywordssubstr&o4=equals&o5=equals&o7=equals&query_format=advanced&v1=Purley_MS%20Purley_Value%20Purley_Ventura%20Purley_Electron%20Purley_Stark%20imm3.cable%20imm3.cyborg%20imm3.carnage%20imm3.constantine%20imm3.electron%20imm3.stark%20imm3.ventura%2017A_Block%2017A_Mobile%20scom_mp_7.1%20scvmm_addin_3.1.0%20Purley_Proton%20%20Purley_Winterfell%20%20Purley_Odin%20%20imm3.proton%20%20imm3.winterfell%20%20imm3.odin%20%20imm3.dunbar%20%20purley_ga%20%20Purley_LXCA%20%20OneCli-Purley&v4=1&v5=Emergency&v7=P1%20Purley%20and%2017A%20FV%20Defects'
#cmd = '/rest/bug??f1=keywords&f2=OP&f3=keywords&f4=reporter&f5=CP&list_id=714210&o1=substring&o3=substring&o4=substring&query_format=advanced&v1=DeferClone&v3=DeferClone&v4=bugzilla_automation'
#cmd = '/rest/bug??f1=bug_status&f2=OP&f3=bug_status&f4=cf_limitation_status&f5=blocked&f6=cf_target_release&f7=CP&o1=equals&o3=equals&o4=substring&o5=isempty&o6=notequals&order=bug_id&query_format=advanced&v1=Limitation&v3=Limitation&v4=Temporary&v6=n%2Fa%20-%20Legacy%20defect'
#cmd = '/rest/product?type=accessible'
#cmd = '/rest/group?names=Lenovo'
#cmd = '/editproducts.cgi?action=editgroupcontrols&product=Ridgeis_Istanbul'
#cmd = '/rest/bug??f1=cf_dup_id&f2=OP&f3=cf_dup_id&limit=0&list_id=1048444&o1=isnotempty&o3=isnotempty&order=cf_answer%2Cbug_id%20DESC&query_format=advanced'

#bug_id = 73649
#bug_id = str(sys.argv[1])
#cmd = '/rest/bug'
uri = url + cmd

#print 
print uri

r = requests.get(uri, params={'api_key': api_key},verify=False)

print r.text
#print r.status_code
#exit
D = r.json()

#exit(0)

print len(D['bugs'])

