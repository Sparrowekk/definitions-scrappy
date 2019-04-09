# Sophos (IDE parser) script

import bs4 as bs
import urllib.request
import json

def ide_parser(source):
    """IDE definition parser"""
    source = urllib.request.urlopen(f"{source}").read()
    content = bs.BeautifulSoup(source, 'lxml')

    return content

ide = ide_parser('https://downloads.sophos.com/downloads/info/latest_IDE.xml')
content = ide.body

publish_date = ''

for i in content.published:
    publish_date += i


def write_to_file(filename):
    """JSON dump sophos_files"""
    filename = filename
    with open(filename, 'w') as f_obj:
        json.dump(f"{content}", f_obj)
        print(f"File info:\n")
        for c in content:
            print(f"{c}")
        print("The file has been saved!")

write_to_file(f'C:\\Users\\lwrobel\\Desktop\\Wirusy\\Sophos\\IDE\\{publish_date[:10]}.json')