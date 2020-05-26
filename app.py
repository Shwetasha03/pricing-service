from flask import Flasks
from views.items import item_blueprint

app = Flask(__name__)
app.register_blueprint(item_blueprint, url_prefix="/items")

if __name__ == '__main__':
    app.run(debug=True)

#url = "https://www.johnlewis.com/2018-apple-ipad-pro-12-9-inch-a12x-bionic-ios-wi-fi-512gb/space-grey/p3834538"
#tag_name = "p"
#query = {"class": "price price--large"}

#ipad = Item(url, tag_name, query)
#ipad.save_to_mongo()

#items_loaded = Item.all()
#print(items_loaded)
#print(items_loaded[0].load_price())
