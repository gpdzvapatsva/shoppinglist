from flask import *
app = Flask(__name__)
@app.route('/')
def shopping():
    return render_template('shoppinglist.html')
@app.route('/showitems', methods=['POST', 'GET'])
def showitems():
    if request.method == 'POST':
        result = request.form
        return render_template('showitems.html', result=result)
if __name__ == '__main__':
    app.debug = True
    app.run()
