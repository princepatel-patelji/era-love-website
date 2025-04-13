from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Mock data for timeline and gallery
relationship_timeline = [
    {"date": "2023-06-15", "event": "Our first date at the cozy café!", "description": "Prince and Era shared a magical evening with coffee and laughter."},
    {"date": "2023-12-25", "event": "Christmas under the stars", "description": "We exchanged gifts and danced in the moonlight."},
    {"date": "2024-07-01", "event": "One-year anniversary", "description": "A romantic getaway to celebrate our love!"},
]

gallery_images = [
    {"url": "https://source.unsplash.com/300x200/?couple", "caption": "Us smiling together"},
    {"url": "https://source.unsplash.com/300x200/?love", "caption": "Holding hands forever"},
    {"url": "https://source.unsplash.com/300x200/?romance", "caption": "Our favorite sunset"},
]

confessions = []

@app.route('/')
def home():
    current_year = datetime.now().year
    return render_template('index.html', name="Era Pandey", partner="Prince Patel", year=current_year)

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', timeline=relationship_timeline)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', images=gallery_images)

@app.route('/letter')
def letter():
    return render_template('letter.html')

@app.route('/confession', methods=['GET', 'POST'])
def confession():
    if request.method == 'POST':
        message = request.form.get('message')
        if message:
            confessions.append({
                'message': message,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
        return jsonify({'status': 'success'})
    return render_template('confession.html', confessions=confessions)

@app.route('/music')
def music():
    songs = [
        {"title": "Perfect", "artist": "Ed Sheeran", "url": "https://www.kozco.com/tech/piano2-Audacity1.2.5.mp3"},
        {"title": "Love Story", "artist": "Taylor Swift", "url": "https://www.kozco.com/tech/LRMonoPhase4.mp3"},
    ]
    return render_template('music.html', songs=songs)

if __name__ == '__main__':
    app.run(debug=True)