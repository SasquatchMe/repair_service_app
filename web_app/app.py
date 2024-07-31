from flask import Flask, request, render_template, redirect, url_for, flash, jsonify, session
from functools import wraps
from loguru import logger
from db.models.tables import db, User, Entity, Order, Object, OrderType, BreakingType

app = Flask(__name__)
app.secret_key = '2a2a2e0d4287aa6c2510dd58748938b7cc7f2e519c5bd760'  # Секретный ключ для сессий

# Пример данных пользователей для демонстрации (позже можно заменить на базу данных)
users = {'praktika_service': 'PraktikA123'}


# Декоратор для проверки авторизации
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Пожалуйста, войдите для доступа к этой странице', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            flash('Вы успешно вошли!', 'success')
            return redirect(url_for('objects_list'))
        else:
            flash('Неправильное имя пользователя или пароль', 'danger')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Вы вышли из системы', 'info')
    return redirect(url_for('login'))


@app.route('/')
@login_required
def objects_list():
    objects = Object.select()
    entities = Entity.select()
    return render_template('objects.html', objects=objects, entities=entities)


# Применяем декоратор ко всем защищенным маршрутам
@app.route('/add_object', methods=['POST'])
@login_required
def add_object():
    data = request.form
    new_object = Object.create(
        login=data['login'],
        address=data['address'],
        phone=data['phone'],
        entity_id=data['entity_id']
    )
    return jsonify({'status': 'success', 'object_id': new_object.id})


@app.route('/update_object/<login>', methods=['GET'])
@login_required
def update_object(login):
    object = Object.get(Object.login == login)
    entities = Entity.select()
    return render_template('update_object.html', object=object, entities=entities)


@app.route('/save_object/<login>', methods=['POST'])
@login_required
def save_object(login):
    object = Object.get(Object.login == login)
    object.login = request.form['login']
    object.address = request.form['address']
    object.entity_id = Entity.get(Entity.id == request.form['entity_id'])
    object.save()
    return redirect(url_for('objects_list'))


@app.route('/orders', methods=['GET'])
@login_required
def orders_list():
    orders = Order.select()
    return render_template('orders.html', orders=orders)


@app.route('/order/<int:order_id>')
@login_required
def order_detail(order_id):
    order = Order.get(Order.id == order_id)
    return render_template('order_detail.html', order=order)


@app.route('/entities', methods=['GET'])
@login_required
def entities_list():
    entities = Entity.select()
    return render_template('entities.html', entities=entities)


@app.route('/add_entity', methods=['POST'])
@login_required
def add_entity():
    entity_name = request.form['entity_name']
    Entity.create(name=entity_name)
    return redirect(url_for('entities_list'))


@app.route('/create_order', methods=['POST'])
@login_required
def create_order():
    data = request.form
    new_order = Order.create(
        order_type_id=data['order_type_id'],
        breaking_type_id=data['breaking_type_id'],
        model_name=data['model_name'],
        desc=data['desc'],
        phone=data['phone'],
        comment=data['comment'],
        object_id=data['object_id']
    )
    return jsonify({'status': 'success', 'order_id': new_order.id})


@app.route('/get_order_types')
@login_required
def get_order_types():
    order_types = OrderType.select()
    return jsonify([{'id': ot.id, 'name': ot.order_type} for ot in order_types])


@app.route('/get_breaking_types')
@login_required
def get_breaking_types():
    breaking_types = BreakingType.select()
    return jsonify([{'id': bt.id, 'name': bt.breaking_type} for bt in breaking_types])


@app.route('/get_objects')
@login_required
def get_objects():
    objects = Object.select()
    return jsonify([{'id': object.id, 'name': object.address} for object in objects])


@app.route('/get_entities')
@login_required
def get_entities():
    entities = Entity.select()
    return jsonify([{'id': entity.id, 'name': entity.name} for entity in entities])


if __name__ == '__main__':
    logger.debug('Start web_app')
    app.run(debug=True)
