import pytest
import GoogleApi as API
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\111\Desktop\project2\Final\grand-bank-330020-d28baa368690.json"
def test_sentiment():
    ###x = 'text      : I like doing project 3 of EC601 in BU \nscore     : 90.0% \nmagnitude : 90.0%\n'
    x = 'text      : I like doing project 3 of EC601 in BU\nscore     : 90.0%\nmagnitude : 90.0%\n'
    y = API.analyze_text_sentiment('I like doing project 3 of EC601 in BU')
    assert x == y

def test_entities():
    x = "================================================================================\nname           : project\ntype           : OTHER\nsalience       : 66.3%\nwikipedia_url  : -\nmid            : -\n================================================================================\nname           : BU\ntype           : ORGANIZATION\nsalience       : 20.7%\nwikipedia_url  : https://en.wikipedia.org/wiki/Boston_University\nmid            : /m/0gl5_\n================================================================================\nname           : EC601\ntype           : ORGANIZATION\nsalience       : 13.1%\nwikipedia_url  : -\nmid            : -\n================================================================================\nname           : 3\ntype           : NUMBER\nsalience       : 0.0%\nwikipedia_url  : -\nmid            : -\n"
    y = API.analyze_text_entities('I like doing project 3 of EC601 in BU')
    assert x == y

def test_syntax():
    x = "sentences : 1\ntokens    : 9\nPRON      : I\nVERB      : like\nVERB      : doing\nNOUN      : project\nNUM       : 3\nADP       : of\nNOUN      : EC601\nADP       : in\nNOUN      : BU\n"
    y = API.analyze_text_syntax('I like doing project 3 of EC601 in BU') 
    assert x == y

def test_classify():
    x = '================================================================================\ncategory  : /Jobs & Education/Education\nconfidence: 51%\n'
    y = API.classify_text('I like doing project 3 of EC601 in BU. I am a graduate student in BU. My favourite dining hall is Warren Towers. I arrived in Boston two months ago and it is my fitst time for me to visit US.')
    print("x=", x)
    print("y=", y)
    assert x == y