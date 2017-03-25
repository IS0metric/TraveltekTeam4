from flask import Flask, render_template, url_for
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
    print(etree.tostring(root))
    for element in root.iterfind("results/cruise"):
        name = element.get("name")
        price = element.get("price")
        ships = element.iterdescendants("ship")
        imageurl = None
        for ship in ships:
            imageurl = ship.get("imageurl")
        print("{0} is {1}".format(name, price))
        print(imageurl)
        all_cruises.append({"name": name, "price": price, "imageurl": imageurl, })
    context["all_cruises"] = all_cruises
    return render_template('Index.html', context=context)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
