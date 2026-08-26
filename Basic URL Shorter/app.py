import string
import random
from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

# Simple in-memory storage for shortend URLs
url_db = {}

def generate_short_url(length=6):
    # Generates a random 6-character string for the short URL
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    # Takes a long url from request JSON and returns a short code.
    data = request.get_json()
    long_url = data.get('long_url')

    if not long_url:
        return jsonify({'error': 'No long URL provided'}), 400

    # Generate a unique short URL code
    short_code = generate_short_url()
    url_db[short_code] = long_url

    return jsonify({
        "short_code": short_code,
        "short_url": f"https://yourdomain.com/{short_code}"
    })

@app.route('/<short_code>', methods=['GET'])
def redirect_to_long_url(short_code):
    # Finds the long URL by code and redirects to it.

    long_url = url_db.get(short_code)
    if long_url:
        # 302 Redirect tells the browser to go to the new URL 
        return redirect(long_url)
    else:
        return jsonify({'error': 'Short URL not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)