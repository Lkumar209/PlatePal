import requests
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

GROQ_API_KEY = 'GROQ_API_KEY'
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'

def call_groq_api(recipe, preference):
    messages = [
        {"role": "system", "content": "You are an expert chef. You will transform recipes based on dietary preferences, such as vegan, gluten-free, or low-carb."},
        {"role": "user", "content": f"Please convert this recipe to a {preference} version, making sure to replace non-{preference} ingredients with appropriate alternatives: {recipe}"}
    ]
    
    headers = {
        'Authorization': f'Bearer {GROQ_API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": "mixtral-8x7b-32768",  
        "messages": messages,
        "max_tokens": 500,  # Adjust token limit based on expected output size
        "temperature": 0.7  #  adjusted to control randomness
    }

    # Make the API request to Groq
    response = requests.post(GROQ_API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return f"Error: Could not transform the recipe (status code: {response.status_code})."


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transform', methods=['POST'])
def transform():
    recipe = request.form['recipe']
    preference = request.form['preference']

    transformed_recipe = call_groq_api(recipe, preference)

    return render_template('index.html', original_recipe=recipe, transformed_recipe=transformed_recipe, preference=preference)

if __name__ == '__main__':
    app.run(debug=True)
