
# Import Flask and other necessary libraries
from flask import Flask, render_template, request

# Create a Flask application
app = Flask(__name__)

# Define the route for the landing page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for the North Indian recipes page
@app.route('/north_indian_recipes')
def north_indian_recipes():
    return render_template('north_indian_recipes.html')

# Define the route for the South Indian recipes page
@app.route('/south_indian_recipes')
def south_indian_recipes():
    return render_template('south_indian_recipes.html')

# Define the route for the recipe detail page
@app.route('/recipe_detail/<recipe_id>')
def recipe_detail(recipe_id):
    return render_template('recipe_detail.html', recipe_id=recipe_id)

# Define the route for the search page
@app.route('/search')
def search():
    query = request.args.get('query')  # Get the search query from the request parameters
    # Filter the recipes based on the search query and display the results
    return render_template('search.html', query=query)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
