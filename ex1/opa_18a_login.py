#!/usr/bin/python
import ssl
import time,sys, os
import cmd, commands
#import urllib3
import json
from dateutil.relativedelta import *
from dateutil.tz import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *

import logging
from cmd import Cmd
logging.captureWarnings(True)
now = parse(commands.getoutput("date"))
today = now.date()
time = now.time()

print str(today)[:4] + "/" + str(today)[5:7] + "/" + str(today)[8:10] + "/" + str(time)[:2] + str(time)[3:5] + "/"


file_directory = "/var/www/html/" + str(today)[:4] + "/" + str(today)[5:7] + "/" + str(today)[8:10] + "/" + str(time)[:2] + str(time)[3:5] + "/"
os.makedirs(file_directory)
os.makedirs(file_directory + "action")
file_name = file_directory + "collection.csv"
dump_file = open(file_name, "w+")


os.environ["PYTHONWARNINGS"] = "ignore:Unverified HTTPS request"
import requests


#import urllib3
#urllib3.disable_warnings()

os.environ["PYTHONWARNINGS"] = "ignore:Unverified HTTPS request"
#print "Python Warnings:", os.environ["PYTHONWARNINGS"]

#print "Request Version:", requests.__version__

#this would be in the env variables.

restHOST = 'bz.labs.lenovo.com'
#restHOST = 'bz-test.labs.lenovo.com'

#here are the api keys.
#bz-test api key for scripts@lenovo.com
#api_key = ''

api_key = 'LzPsQjTED2zQS2SDrFZWBU6R383LZgEGp0bkSAu0'

#bz api key for scripts@lenovo.com
#api_key = 'sQlgUDZlLlfZASz6whVRoO74A4D7aWVWHzneGWCp'

restPROTOCOL = 'https'
restPORT = '443'

url = restPROTOCOL+'://'+restHOST

#print
#print "system info"
#print restHOST
#print

#cmd = '/rest/bug??bug_status=Open&bug_status=Working&bug_status=Rejected&bug_status=Fixed&bug_status=Verify&classification=IO_Options&classification=Internal_Storage&classification=Storage_Controllers&f1=version&f3=OP&f4=priority&f5=bug_severity&f6=CP&f7=cf_tagging&j3=OR&list_id=1738927&n7=1&o1=anywordssubstr&o4=equals&o5=equals&o7=equals&query_format=advanced&v1=Purley_MS%20Purley_Value%20Purley_Ventura%20Purley_Electron%20Purley_Stark%20imm3.cable%20imm3.cyborg%20imm3.carnage%20imm3.constantine%20imm3.electron%20imm3.stark%20imm3.ventura%2017A_Block%2017A_Mobile%20scom_mp_7.1%20scvmm_addin_3.1.0%20Purley_Proton%20%20Purley_Winterfell%20%20Purley_Odin%20%20imm3.proton%20%20imm3.winterfell%20%20imm3.odin%20%20imm3.dunbar%20%20purley_ga%20%20Purley_LXCA%20%20OneCli-Purley&v4=1&v5=Emergency&v7=P1%20Purley%20and%2017A%20FV%20Defects'


#cmd = '/buglist.cgi?bug_status=Open&bug_status=Working&bug_status=Fixed&bug_status=Verify&classification=IO_Options&component=Intel_OmniPath&list_id=3247878&product=Intel_OmniPath&query_format=advanced&resolution=---&version=18A_Block'

cmd = '/rest/bug??bug_status=Open&bug_status=Working&bug_status=Fixed&bug_status=Verify&classification=IO_Options&component=Intel_OmniPath&list_id=3247878&product=Intel_OmniPath&query_format=advanced&resolution=---&version=18A_Block&ctype=csv&human=1'


uri = url + cmd

print uri

r = requests.get(uri, params={'api_key': api_key},verify=False)

#print r.text
#print r.status_code
#exit
D = r.json()

#exit(0)

#print len(D['bugs'])

############################


for defect in D['bugs']:
    print json.dumps(defect, sort_keys=True, indent=2, separators=(',', ': '))
    bug_id = defect['id']
    headline = defect['summary']
    product = defect['product']
    component = defect['component']
    state = defect['status']
    action = defect['whiteboard']
    sev = defect['severity']
    answer = defect['cf_answer']
    submitter = defect['creator']
    limitation = defect['cf_limitation_status']
    tip_status = defect['cf_tip_status']
    tip_number = defect['cf_tip_pointer']
    owner = defect['assigned_to']
    open_date_parts = defect['creation_time']
    open_date_parse = parse(open_date_parts)
    open_date = open_date_parse.date()
    days_active  = (today - open_date).days
    change_date_parts = defect['last_change_time']
    change_date_parse = parse(change_date_parts)
    change_date = change_date_parse.date()
    days_inactive  = (today - change_date).days
    release = defect['version']
    fix_date = defect['deadline']
    risk_level = defect['cf_risk_level']
    # Collect History

    urlH = restPROTOCOL+'://'+restHOST
    cmdH = '/rest/bug'
    cmdH = cmdH + '/'+ str(bug_id)
    cmdH = cmdH + '/history' 

    uriH = urlH + cmdH

    rH = requests.get(uriH, params={'api_key': api_key},verify=False)

    H = rH.json()

    # print len(H['bugs'])
    state_change = False
    action_file_name = file_directory + "/action/action_" + str(bug_id) + ".output"
    action_file = open(action_file_name, "w+")     
    action_file.write ("Date-Time\tAction\n" + open_date_parts + "\tDefect Opened")

    ############################

    for defect in H['bugs']:
        for history in defect['history']:
    #        print ("History entry (date/time): " + history['when'])
            for change in history['changes']:
    #            print ("\tChange Field: " + change['field_name'])
                if change['field_name'] == "status":
                    state_change = True
                    new_state = change['added']
                    old_state = change['removed']
                    state_change_date = history['when']
                if change['field_name'] == "whiteboard":
                    action_file.write (
                        "\n" + history['when'] +
                        "\t" + str(change['added'].replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "'").replace(u"\u201d", "'").replace(u"\u3001", "'").replace(u"\uff08", "'").replace(u"\uff0c", "'").replace(u"\uff1a", "'").replace(u"\uff09", "'").replace(u"\u2013", "'"))
                    )
                if change['field_name'] == "deadline":
                    action_file.write (
                        "\n" + history['when'] +
                        "\t" + "Target Date Change From: " +
                        str(change['removed'].replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "'").replace(u"\u201d", "'").replace(u"\u3001", "'").replace(u"\uff08", "'").replace(u"\uff0c", "'").replace(u"\uff1a", "'").replace(u"\uff09", "'").replace(u"\u2013", "'")) +
                        "To: " +
                        str(change['added'].replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "'").replace(u"\u201d", "'").replace(u"\u3001", "'").replace(u"\uff08", "'").replace(u"\uff0c", "'").replace(u"\uff1a", "'").replace(u"\uff09", "'").replace(u"\u2013", "'"))
                    )
                if change['field_name'] == "product":
                    action_file.write (
                        "\n" + history['when'] +
                        "\t" + "Defect Product Change From: " +
                        str(change['removed'].replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "'").replace(u"\u201d", "'").replace(u"\u3001", "'").replace(u"\uff08", "'").replace(u"\uff0c", "'").replace(u"\uff1a", "'").replace(u"\uff09", "'").replace(u"\u2013", "'")) +
                        " To: " +
                        str(change['added'].replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "'").replace(u"\u201d", "'").replace(u"\u3001", "'").replace(u"\uff08", "'").replace(u"\uff0c", "'").replace(u"\uff1a", "'").replace(u"\uff09", "'").replace(u"\u2013", "'"))
                    )
                if change['field_name'] == "status":
                    action_file.write (
                        "\n" + history['when'] +
                        "\t" + "Defect State Change From: " +
                        str(change['removed'].replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "'").replace(u"\u201d", "'").replace(u"\u3001", "'").replace(u"\uff08", "'").replace(u"\uff0c", "'").replace(u"\uff1a", "'").replace(u"\uff09", "'").replace(u"\u2013", "'")) +
                        " To: " +
                        str(change['added'].replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "'").replace(u"\u201d", "'").replace(u"\u3001", "'").replace(u"\uff08", "'").replace(u"\uff0c", "'").replace(u"\uff1a", "'").replace(u"\uff09", "'").replace(u"\u2013", "'"))
                    )                 


    if state_change == True:
        state_change_date_parse = parse(state_change_date)
        state_change_date = state_change_date_parse.date()
        state_days_age = (today - state_change_date).days
    #    print ("Last State Change:  From: " + old_state + " To: " + new_state + " " + str(state_days_age) + " day(s) ago")
    else:
        new_state = "Never"
        old_state = "Never"
        state_days_age = 0
    #    print ("State Never Changed")

     
    dump_file.write (
        str(bug_id) +
        "\t" + str(product) +
        "\t" + str(component) +
        "\t" + str(limitation) +
        "\t" + str(action.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "'").replace(u"\u201d", "'").replace(u"\u3001", "'").replace(u"\uff08", "'").replace(u"\uff0c", "'").replace(u"\uff1a", "'").replace(u"\uff09", "'").replace(u"\u2013", "'")) +
        "\t" + str(sev) +
        "\t" + str(submitter) +
        "\t" + str(owner) +
        "\t" + str(state) +
        "\t" + str(answer) +
        "\t" + str(headline.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "'").replace(u"\u201d", "'").replace(u"\u3001", "'").replace(u"\uff08", "'").replace(u"\uff0c", "'").replace(u"\uff1a", "'").replace(u"\uff09", "'").replace(u"\u2013", "'")) +
        "\t" + str(open_date_parts) +
        "\t" + str(days_active) +
        "\t" + str(release) +
        "\t" + str(fix_date) +
        "\t" + str(days_inactive) +
        "\t" + str(state_days_age) +
        "\t" + str(old_state) +
        "\t" + str(new_state) +
        "\t" + str(risk_level) +
        "\n"  
        )



exit(0)

