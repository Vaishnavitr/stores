from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask import request
# import sqlite3
from sqlalcourse.models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument('item', type=str, required=True, help='this field item cannot be blank ')
    parser.add_argument('price', type=float, required=True, help='this field price cannot be blank ')

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        # item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404
        """
        for item in items:
            if item['name'] == name:
                return item
        """
        # return {'item': item}, 200 if item else 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists".format(name)}, 400
        """"
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists".format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        """
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occured inserting the item.'}, 500  # internal server error
        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = Item.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': '{} deleted'.format(name)}
        return {'message': '{} not found'.format(name)}

        """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE from items where name =?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'message': '{} deleted'.format(name)}
        
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        if name in items:
            return {'message': '{} deleted'.format(name)}
        else:
            return {'message': '{} not found'.format(name)}
        """

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()  # request.get_json()

        item = ItemModel.find_by_name(name)
        # updated_item = ItemModel(name, data['price'])

        if item is None:
            try:
                # ItemModel.insert()
                item = ItemModel(name, data['price'])
                # updated_item.insert()
                item.save_to_db()

            except:
                return {'message': 'An error occurred while inserting the item'}, 500
        else:
            try:
                item.price = data['price']
                # updated_item.update()
                # updated_item.update()
                item.save_to_db()
            except:
                return {'message': 'An error occured while updating the item'}, 500

        """
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name' : name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        """
        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
        # return {'items': list(map(lambda  x: x.json(), ItemModel.query.all()))}

    """def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * from items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})

        connection.close()
        return {'items': items}"""
