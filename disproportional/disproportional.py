import requests

xml = """<?xml version="1.0"?>
<methodCall>
    <methodName>phone</methodName>
    <params>
        <param>
            <value><string>Bert</string></value>
        </param>
    </params>
</methodCall>
"""
headers = {'Content-Type': 'text/xml'}
r = requests.post('http://www.pythonchallenge.com/pc/phonebook.php', data=xml, headers=headers)

print(r.text)