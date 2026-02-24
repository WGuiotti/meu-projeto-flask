# Import necessary modules from Flask
from flask import Flask, render_template
import os

# Initialize the Flask application
app = Flask(__name__)

# Professional Configuration: Define path to database
app.config['DATABASE'] = os.path.join(app.root_path, 'database', 'site.db')

# Define the route for the root URL ('/')
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# Example route for a sub-page in the 'pages' folder
@app.route('/about')
def about():
    return render_template('pages/about.html')

# Run the application if executed as the main script
if __name__ == '__main__':
    # Run in debug mode for development
    app.run(debug=True)