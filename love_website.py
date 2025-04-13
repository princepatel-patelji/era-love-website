from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Mock data for timeline and gallery
relationship_timeline = [
    {"date": "2023-06-15", "event": "Our first date at the aapne mujhe purpose kiya partner What the Day That Is My Baby !", "description": "Prince and Era shared a magical evening with coffee and laughter."},
    {"date": "2025-02-21", "event": "Our First Hug and Kiss", "description": "We exchanged gifts and you kiss me on my chiks hug me in the moonlight."},
    {"date": "2000-09-21", "event": "Your Birthday My Dear Wife ", "description": "A romantic getaway to celebrate our love the day when god made you for me and for my love my Dear Honey !"},
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
    love_messages = [
        "You are the melody of my heart, Era! ❤️",
        "Every raindrop reminds me of our love story. 🌧️",
        "You’re my forever, my cute baby! 🍼💞",
        "Hand in hand, we’ll dance through life. 🤝",
        "Your hug is my safe haven, my love! 🤗",
        "Every kiss from you lights up my world. 💋",
        "Together, we’re a beautiful dream come true. 🌸"
    ]
    return render_template('index.html', name="Era Pandey", partner="Prince Patel", year=current_year, love_messages=love_messages)

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
        {"title": "Tum Hi Ho", "artist": "Arijit Singh", "url": "https://www.youtube.com/watch?v=UkzXh3Q8O6w"},
        {"title": "Channa Mereya", "artist": "Arijit Singh", "url": "https://www.youtube.com/watch?v=0yq6qK0vgh0"},
    ]
    return render_template('music.html', songs=songs)

@app.route('/our_story')
def our_story():
    return render_template('our_story.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))  # Render uses PORT environment variable
    app.run(host='0.0.0.0', port=port, debug=False)  # Debug=False for production
