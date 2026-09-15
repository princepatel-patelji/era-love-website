from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name="Prince", partner="Era", year=2025, love_messages=["We met...", "Our first date...", "Forever together..."])

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/letter')
def letter():
    return render_template('letter.html')

@app.route('/confession')
def confession():
    return render_template('confession.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/love')
def love():
    return render_template('love.html')

@app.route('/our_story')
def our_story():
    return render_template('our_story.html')

@app.route('/love_card')
def love_card():
    return render_template('love_card.html')

@app.route('/romance')
def romance():
    return render_template('romance.html')
    @app.route('/happy_birthday')
def happy_birthday():
    return render_template('happy_birthday.html')

@app.route('/happy_ji')
def happy_ji():
    return render_template('happy_ji.html')

@app.route('/happy_ji_2')
def happy_ji_2():
    return render_template('happy_ji_2.html')

if __name__ == '__main__':
    app.run(debug=True)
