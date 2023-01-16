from flask import Flask, request, render_template

app = Flask(__name__)

total = ''

@app.route('/', methods = ["GET", "POST"])
def main_page():
    " Функция для возврата числа с цифрами в обратном порядке"
    global total
    if request.method == 'POST':
        number = request.form.get('number')
        if number != '':
            number = list(str(number))
            number.reverse()
            total = ''.join(number)
            return render_template('main_page.html', total = total)
        else:
            total = ' '
    return render_template('main_page.html', total = total)

if __name__ == '__main__':
    app.run()