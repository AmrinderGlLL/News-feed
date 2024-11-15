from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Endpoint to fetch news
@app.route('/api/news', methods=['GET'])
def get_news():
    query = request.args.get('query', 'technology') 
    api_key = 'api_key'  
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({'error': 'Failed to fetch news'}), 500

if __name__ == '__main__':
    app.run(debug=True)
