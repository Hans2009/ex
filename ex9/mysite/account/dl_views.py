#from __future__ import unicode_literals #from django.shortcuts import render import os,sys
from django.http import HttpResponse
from django.http import StreamingHttpResponse 

# Create your views here.
def download_file(request):  
    if request.method == "POST":
        # do something  
        the_file_name='11.png'             
        filename='media/uploads/11.png'    
        response=StreamingHttpResponse(readFile(filename))  
        response['Content-Type']='application/octet-stream'  
        response['Content-Disposition']='attachment;filename="{0}"'.format(the_file_name)  
        return response  
  
def readFile(filename,chunk_size=512):  
    with open(filename,'rb') as f:  
        while True:  
            c=f.read(chunk_size)  
            if c:  
                yield c  
            else:  
                break  


