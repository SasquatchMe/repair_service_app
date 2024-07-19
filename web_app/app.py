from db.models.tables import db, User, Entity
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    users = User.select()
    entities = Entity.select()
    return render_template('index.html', users=users, entities=entities)


# Обработка формы добавления пользователя
@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['login']
    address = request.form['address']
    entity_id = request.form['entity_id']
    print(entity_id)
    User.create(login=username, address=address, entity_id=entity_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
