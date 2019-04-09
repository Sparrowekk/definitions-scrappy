# Trend Micro (Official Pattern Release downloader) script

import requests as rq
import re
import os.path

# url with list of files
url = 'http://downloadcenter.trendmicro.com/index.php?clk=tab_pattern&clkval=1&regs=NABU&lang_loc=1'

# store url with get function
resp = rq.get(url)

# searching filename
filename = re.findall(r'lpt[^zip]*zip', resp.text)

# remove duplicates
filename = set(filename)
filepath = 'C:\\Users\\lwrobel\\Desktop\\Wirusy\\Trend'

for file in filename:
    # check for duplicate (if file exsist just ignore)
    if os.path.isfile(file):
        print(f"{file} exsist!")
        continue

    # download the zip
    new_url = 'http://www.trendmicro.com/ftp/products/aupattern/ent95/' + file #+ '?_ga=2.138497651.1323185747.1554710355-1754265805.1553599272'
    new_resp = rq.get(new_url)

    # write zip to disk
    with open(filepath, 'wb') as file_obj:
        file_obj.write(file)
        print(f"Succesfully retrieved {file}!")
