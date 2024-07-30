from db.models.tables import db, User, Entity, Order, Object
from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)


@app.route('/')
def objects_list():
    objects = Object.select()
    entities = Entity.select()
    return render_template('objects.html', objects=objects, entities=entities)


# Обработка формы добавления пользователя
@app.route('/add_object', methods=['POST'])
def add_object():
    login = request.form['login']
    address = request.form['address']
    entity_id = request.form['entity_id']
    Object.create(login=login, address=address, entity_id=entity_id)
    return redirect(url_for('objects_list'))


@app.route('/update_object/<login>', methods=['GET'])
def update_object(login):
    object = Object.get(Object.login == login)
    entities = Entity.select()
    return render_template('update_object.html', object=object, entities=entities)


@app.route('/save_object/<login>', methods=['POST'])
def save_object(login):
    object = Object.get(Object.login == login)
    object.login = request.form['login']
    object.address = request.form['address']
    object.entity_id = Entity.get(Entity.id == request.form['entity_id'])
    object.save()
    return redirect(url_for('objects_list'))


@app.route('/orders', methods=['GET'])
def orders_list():
    orders = Order.select()
    return render_template('orders.html', orders=orders)


@app.route('/order/<int:order_id>')
def order_detail(order_id):
    order = Order.get(Order.id == order_id)
    return render_template('order_detail.html', order=order)


@app.route('/entities', methods=['GET'])
def entities_list():
    entities = Entity.select()
    return render_template('entities.html', entities=entities)


@app.route('/add_entity', methods=['POST'])
def add_entity():
    entity_name = request.form['entity_name']
    Entity.create(name=entity_name)
    return redirect(url_for('entities_list'))


if __name__ == '__main__':
    app.run(debug=True)
