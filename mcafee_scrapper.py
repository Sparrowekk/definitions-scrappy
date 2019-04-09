# McAfee (VirusScan Dat downloader) script

import requests as rq
import re
import os.path
 
# url with list of files
url = 'http://update.nai.com/Products/commonupdater/'
 
# store url with get function
resp = rq.get(url)
 
 
# searching filename
filename = re.findall(r'avvdat[^zip]*zip', resp.text)
 
# remove duplicates
filename = set(filename)
 
for file in filename:
    # check for duplicate (if file exsist just ignore)
    if os.path.isfile(file):
        print(f"{file} exsist!")
        continue
 
    # download the zip
    new_url = 'http://update.nai.com/Products/commonupdater/' + file
    new_resp = rq.get(new_url)
 
    # write zip to disk
    with open(file, 'wb') as file:
        file.write(new_resp.content)
        print(f"Succesfully retrieved {file}!")