from flask import Flask, render_template, request, flash, redirect, url_for
import config, uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4())

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if request.form['submitBtn'] == "Add":

            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            if config.add_user(firstname, lastname, email):
                return render_template('index.html', data=config.get_data())
            else:
                flash('Error Adding User!')
                return render_template('index.html', data=config.get_data())
        elif request.form['submitBtn'] == "Save":
            id_ = request.form['editid']
            firstname = request.form['editfirstname']
            lastname = request.form['editlastname']
            email = request.form['editemail']
            if config.edit_user(id_, firstname, lastname, email):
                return render_template('index.html', data=config.get_data())
            else:
                flash('Error Editing User Data!')
                return render_template('index.html', data=config.get_data())
    else:
        return render_template('index.html', data=config.get_data()) # add jinja2 data

@app.route('/delete/<id_>')
def delete(id_):
    if config.delete_user(id_):
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index')) # did not delete user

if __name__ == '__main__':
    config.init()
    app.run(debug=True)