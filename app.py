from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        print(f"Username: {username}, Email: {email}")
        return render_template('success.html', username=username, email=email)
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')

#commands to run: Docker build -t simple-flask-app .
#                 Docker run -p 5000:5000 simple-flask-app
#this is changed