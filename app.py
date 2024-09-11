import os
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

def create_app():
    app = Flask(__name__)

    def create_system_message(preference):
        return f"""You are an expert chef specializing in {preference} dietary modifications. Your task is to transform recipes to meet this dietary preference while maintaining flavor and texture as much as possible. Please follow these guidelines:

    1. Analyze the given recipe thoroughly.
    2. Suggest appropriate substitutions for ingredients that don't meet the {preference} criteria.
    3. Modify cooking techniques if necessary to suit the {preference} diet.
    4. Ensure the transformed recipe is delicious and satisfying.
    5. Format your response using markdown within specific XML tags.

    Use the following XML structure for your response:
    <transformed_recipe>
        <ingredient_list>
        [List modified ingredients here using markdown, preferably as an unordered list]
        </ingredient_list>
        <instructions>
        [Provide step-by-step cooking instructions here using markdown, preferably as an ordered list]
        </instructions>
        <notes>
        [Include any additional notes, tips, or explanations here using markdown formatting. Any changes that were made to the recipe are also catalogued here.]
        </notes>
    </transformed_recipe>

    Remember to use markdown formatting within each XML tag to enhance readability. For example, use `*` for emphasis, `**` for strong emphasis, and `-` or `1.` for lists.

    IMPORTANT: Sometimes, the recipe you are given may be incomplete or ambiguous. In such cases, use your best judgment and creativity to complete the transformation. MAKE SURE TO ADHERE TO THE XML STRUCTURE! <ingredient_list>, <instructions>, and <notes> should ALL BE THERE! Good luck!

    In the case you are given simple or one-word prompts, improvise. still, you should start with <transformed_recipe> and end with </transformed_recipe>. You can include that you are improvising in the notes section."""

    def call_groq_api(recipe, preference):
        system_message = create_system_message(preference)
        user_message = f"Transform this recipe into a {preference} version:\n\n{recipe}"

        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                model="llama-3.1-70b-versatile",
                max_tokens=2048,
                temperature=0.7,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return str(e)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/transform', methods=['POST'])
    def transform():
        recipe = request.form['recipe']
        preference = request.form['preference']
        
        if not recipe or not preference:
            return jsonify({'error': 'Recipe and preference are required'}), 400
        
        transformed_recipe = call_groq_api(recipe, preference)
        
        if transformed_recipe.startswith('Error') or '<transformed_recipe>' not in transformed_recipe:
            return jsonify({'error': 'Failed to transform the recipe. Please try again.'}), 500
        
        return jsonify({
            'original_recipe': recipe,
            'transformed_recipe': transformed_recipe,
            'preference': preference
        })

    return app

# This is the entry point for Vercel
app = create_app()