# PlatePal - Culinary Transformation

PlatePal is a web application that transforms recipes to meet specific dietary preferences using AI-powered recommendations. Whether you're looking for vegan, gluten-free, or low-carb alternatives, PlatePal has got you covered!

## Features

- Transform recipes to vegan, gluten-free, or low-carb versions
- AI-powered recipe modifications using Groq API
- User-friendly web interface
- Responsive design for various devices

## Technologies Used

- Python
- Flask
- Groq API
- HTML/CSS/JavaScript
- Vercel (for deployment)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- A Groq API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/platepal.git
   cd platepal
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Local Development

To run the application locally:

1. Ensure you're in the project directory and your virtual environment is activated.

2. Run the Flask application:
   ```
   python app.py
   ```

3. Open a web browser and navigate to `http://localhost:5000`.

## Deployment to Vercel

To deploy PlatePal to Vercel:

1. Install the Vercel CLI:
   ```
   npm install -g vercel
   ```

2. Log in to your Vercel account:
   ```
   vercel login
   ```

3. Deploy the application:
   ```
   vercel
   ```

4. Follow the prompts to configure your deployment.

5. Set up the environment variable (GROQ_API_KEY) in the Vercel dashboard.

## Usage

1. Enter your recipe in the text area provided.
2. Select your desired dietary preference (Vegan, Gluten-Free, or Low-Carb).
3. Click the "Transform" button.
4. View the transformed recipe with ingredient substitutions and modified instructions.
5. Use the "Copy Recipe" button to copy the transformed recipe to your clipboard.
6. Click "Start Anew" to transform another recipe.

## Contributing

Contributions to PlatePal are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.