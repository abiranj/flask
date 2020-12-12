from flask import Flask, jsonify, request, render_template
stores = [
    {
        'name' : 'myStore',
        'items' : [
            {
                'name' : 'my item',
                'price' : '35'


            }
        ]
    }
]

app = Flask (__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return render_template('index.html')


#post/store data: {name}
@app.route('/store', methods=['post'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store1(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
        return jsonify({'message' : 'store not find'})

#to get
@app.route('/store')
def get_store():
    return jsonify({'stores': stores})

#

@app.route('/store/<string:name>/item', methods=['post'])
def create_item_in_store(name):
    print('aa')
    request_data = request.get_json()
  #  storeName = request_data['store']
    #for store in stores:
        #if store['name'] == name:
    new_item = {
                 'name' : request_data['name'],
                 'price' : request_data ['price']
            }
    stores.append(new_item)
    return jsonify(stores)
    print(stores)

        #return jsonify({'message' : 'store not find'})


@app.route('/store/<string:name>/item', methods=['delete'])
def delete_item_in_store(name):
    print('bb')
    request_data = request.get_json()
  
    del stores[request_data]
    print(stores)


    return jsonify(stores)



app.run(port=5001)