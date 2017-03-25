from flask import Flask
import requests
from lxml import etree

app = Flask(__name__)
app.config["DEBUG"] = True

API_USERNAME = 'hackathon'
API_PASSWORD = 'pr38ns48'
testreq = '''<?xml version="1.0"?>
<request>
    <auth username="hackathon" password="pr38ns48" />
    <method action="simplesearch" sitename="cruisedemo.traveltek.net"
        status="Live" type="cruise">
        <searchdetail type="cruise" startdate="2017-04-01" enddate="2017-04-30"
            adults="2" children="0" sid="30115" resultkey="default">
        </searchdetail>
    </method>
</request>'''

@app.route('/')
def index():
    context = {}
    r = requests.post('https://fusionapi.traveltek.net/0.9/interface.pl',
    data={"xml": testreq})
    root = etree.fromstring(r.text)
    all_cruises = []
    for element in root.find("results/cruise"):
        name = element.get("name")
        price = element.get("price")
        print("{0} is {1}".format(name, price))
        all_cruises.append({"name": name, "price": price})
    context["all_cruises"] = all_cruises
    return render_template('index.html', context=context)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
