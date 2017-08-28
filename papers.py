import re
import requests

with open('README.md', 'r') as f:
    for l in f.readlines():
        if "pdf" in l:
            url   = re.findall('http[s]?://.*.pdf', l)[0]
            title = re.findall('\[.*\]', l)[0]
            title = title.strip('[').strip(']').lower()
            title = re.sub(' ', '_', title)
            title = re.sub('[,:-?\'\.]', '', title)
            title = title + '.pdf'
            print(title)
            with open(title, 'wb') as o:
                response = requests.get(url)
                o.write(response.content)
