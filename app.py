from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
cou = {'count': 0}


@app.route('/')
def home():
    return render_template('index.html', title="Flask", name="Hello Flask",
                           countt=cou['count'])


@app.route('/in', methods=['POST'])
def incre():
    # getA = request.form.get('action')
    getA = request.form['action']
    if getA == 'increase':
        cou['count'] += 1
    elif getA == 'decrease':
        cou['count'] -= 1
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
