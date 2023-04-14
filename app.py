from flask import Flask, render_template, redirect, request
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    connection = sqlite3.connect('databese.db')
    connection.row_factory = sqlite3.Row  # connessione al DB sara organizzata in righe
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', parametro = posts)

@app.route('/<int:idx>/delete', methods = ("POST",)) 
def delete(idx):
    connection = sqlite3.connect('databese.db')
    connection.row_factory = sqlite3.Row
    connection.execute('DELETE FROM posts WHERE id= ?', (idx,))
    connection.commit()
    connection.close()
    return redirect('/')


@app.route('/create', methods = ("GET","POST")) 
def create():
    if request.method == 'POST':
        titolo = request.form['titolo']
        info = request.form['info']
        connection = sqlite3.connect('databese.db')
        connection.row_factory = sqlite3.Row 
        connection.execute('INSERT INTO posts (titolo, info) VALUES (?, ?)', (titolo, info))
        connection.commit()
        connection.close()
        return redirect('/')
    return render_template('create.html')
    


if __name__ == '__main__':
    app.run(debug=True)
