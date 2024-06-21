import os
from flask import Flask, request, jsonify, send_from_directory, render_template, session
from groq import Groq
from flask_session import Session
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


# Initialize GOOGLE API
GOOGLE_API_KEY = api_key=os.environ.get("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = api_key=os.environ.get("SEARCH_ENGINE_ID")

app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
app.config['SECRET_KEY'] = 'supersecretkey'  # Replace with a strong secret key
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

def serve():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/<path:path>')
def static_serve(path):
    return send_from_directory(app.static_folder, path)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('input')
        google_search = request.json.get('google_search')
        youtube_search = request.json.get('youtube_search')
        wikipedia_search = request.json.get('wikipedia_search')

        # Debug: Print received input
        print(f"Received input: {user_input}")
        print(f"Google search: {google_search}")
        print(f"YouTube search: {youtube_search}")
        print(f"Wikipedia search: {wikipedia_search}")

        # Call Groq LLM
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama3-8b-8192",
        )
        llm_response = chat_completion.choices[0].message.content.strip()

        # Debug: Print LLM response
        print(f"LLM response: {llm_response}")

        # Extract keywords from LLM response (mocked for this example)
        keywords = extract_keywords(user_input)
        print(f"Extracted keywords: {keywords}")

        search_results = {
            "google": [],
            "youtube": [],
            "wikipedia": []
        }

        if google_search:
            try:
                search_results["google"] = search_google(keywords)
                print(f"Google search results: {search_results['google']}")
            except Exception as e:
                print(f"Error during Google search: {e}")
                search_results["google"] = []
            '''
        if youtube_search:
            search_results["youtube"] = search_youtube(keywords)
        if wikipedia_search:
            search_results["wikipedia"] = search_wikipedia(keywords)'''

        response_data = {"response": llm_response, "search_results": search_results}
        print(f"Response data: {response_data}")
        return jsonify(response_data)
    except Exception as e:
        print(f"Error in /chat endpoint: {e}")
        return jsonify({"error": str(e)}), 500

    

def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    keywords = [word for word in words if word.isalnum() and word.lower() not in stop_words]
    return keywords


def search_google(keywords):
    api_key = GOOGLE_API_KEY
    search_engine_id = SEARCH_ENGINE_ID
    query = ''.join(keywords)
    url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}'
    print(f"Google search URL: {url}") 
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get('items', [])
        formatted_results = [{'title': item['title'], 'link': item['link']} for item in results]
        print(f"Formatted Google search results: {formatted_results}")
        return formatted_results
    elif response.status_code == 403:
        print(f"Rate limit exceeded: {response.json()}")
        return [{'title': 'Rate limit exceeded', 'link': 'https://developers.google.com/custom-search/v1/overview#quota'}]
    else:
        print(f"Error response from Google API: {response.status_code} - {response.text}")
        return []

def search_wikipedia(keywords):
    query = ' '.join(keywords)
    url = f'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json'
    print(f"Wikipedia search URL: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get('query', {}).get('search', [])
        formatted_results = [{'title': item['title'], 'link': f"https://en.wikipedia.org/wiki/{item['title'].replace(' ', '_')}"} for item in results]
        print(f"Formatted Wikipedia search results: {formatted_results}")
        return formatted_results
    else:
        print(f"Error response from Wikipedia API: {response.status_code} - {response.text}")
        return []


@app.route('/')
def serve_index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)




