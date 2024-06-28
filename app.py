from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User is {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'User have posted {post_id}'


@app.route('/password/<name>', methods=['GET', 'POST'])
def index(name):
    if request.method == 'POST':
        num_upper = int(request.form.get('upper', 0))
        num_lower = int(request.form.get('lower', 0))
        num_digits = int(request.form.get('digits', 0))
        num_special = int(request.form.get('special', 0))

        if num_upper + num_lower + num_digits + num_special == 0:
            error = "Please specify at least one character type."
            return render_template('index.html', error=error)

        upper_chars = random.choices(string.ascii_uppercase, k=num_upper)
        lower_chars = random.choices(string.ascii_lowercase, k=num_lower)
        digit_chars = random.choices(string.digits, k=num_digits)
        special_chars = random.choices(string.punctuation, k=num_special)

        password_list = upper_chars + lower_chars + digit_chars + special_chars
        random.shuffle(password_list)

        password = ''.join(password_list)
        return render_template('index.html', password=password)
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
