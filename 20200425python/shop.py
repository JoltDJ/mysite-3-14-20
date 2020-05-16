from flask import Flask, render_template
from flask import request, redirect

products = {
  "sku01": { 
      "id": "sku01", 
      "name": "Pen", 
      "price": 15, 
      "desc": 'Sorry! My dog bit it.', 
      'src': 'https://previews.123rf.com/images/photoman/photoman1005/photoman100500128/7034662-broken-pencil-with-white-background.jpg' 
      },
  "sku02": { 
      "id": "sku02", 
      "name": "Cup", 
      "price": 80, 
      "desc": 'Just cracked...but still works? ', 
      'src': 'data:image/jpeg;base64,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'
      },
  "sku03": { 
      "id": "sku03", 
      "name": "Notebook", 
      "price": 550, 
      "desc": 'Found it in the dump.', 
      'src': 'https://endhack.com/wp-content/uploads/2018/07/broken-laptop.jpg'
      },
  "sku04": { 
      "id": "sku04", 
      "name": "Paper", 
      "price": 5, 
      "desc": 'For every piece of paper, one tree is planted.', 
      'src': 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTWfRWE88I5Ds9sFSfpbOcrJuVDEBp4KRkwjxBk3n45c1x2-Ttu&usqp=CAU'
      }
}

app = Flask(__name__)

@app.route("/")
def hello():
    title = 'Shop Website'

    return render_template('shop.html', title=title, products=products)

@app.route("/product/<id>")
def product(id):
    pd = products[id]
    return render_template('product.html', product = pd)