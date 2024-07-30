from db.models.tables import db, User, Entity, Order
from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)


@app.route('/')
def users_list():
    users = User.select()
    entities = Entity.select()
    return render_template('users.html', users=users, entities=entities)


# Обработка формы добавления пользователя
@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['login']
    address = request.form['address']
    entity_id = request.form['entity_id']
    print(entity_id)
    User.create(login=username, address=address, entity_id=entity_id)
    return redirect(url_for('users_list'))


@app.route('/update_user/<login>', methods=['GET'])
def update_user(login):
    user = User.get(User.login == login)
    entities = Entity.select()
    return render_template('update_user.html', user=user, entities=entities)


@app.route('/save_user/<login>', methods=['POST'])
def save_user(login):
    user = User.get(User.login == login)
    user.login = request.form['login']
    user.address = request.form['address']
    user.entity_id = Entity.get(Entity.id == request.form['entity_id'])
    user.save()
    return redirect(url_for('users_list'))


@app.route('/orders', methods=['GET'])
def orders_list():
    orders = Order.select()
    return render_template('orders.html', orders=orders)


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
