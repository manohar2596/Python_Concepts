from flask import Flask, render_template
from urllib.parse import urlencode

app = Flask(__name__)

# Set the template folder explicitly
app.template_folder = 'templates'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search_results')
def search_results():
    crafting_scissors = [
        {'id': 'crafting-scissors-1', 'name': 'Crafting Scissors 1', 'description': 'Designed for precision in crafting projects.', 'image': 'crafting-scissors-1.jpg'},
        {'id': 'crafting-scissors-2', 'name': 'Crafting Scissors 2', 'description': 'Another crafting scissor description.', 'image': 'crafting-scissors-2.jpg'},
        {'id': 'crafting-scissors-3', 'name': 'Crafting Scissors 3', 'description': 'Yet another crafting scissor description.', 'image': 'crafting-scissors-3.jpg'},
        {'id': 'crafting-scissors-4', 'name': 'Crafting Scissors 4', 'description': 'Crafting scissor description.', 'image': 'crafting-scissors-4.jpg'},
        {'id': 'crafting-scissors-5', 'name': 'Crafting Scissors 5', 'description': 'Crafting scissor description.', 'image': 'crafting-scissors-5.jpg'},
        {'id': 'crafting-scissors-6', 'name': 'Crafting Scissors 6', 'description': 'Crafting scissor description.', 'image': 'crafting-scissors-6.jpg'},
        {'id': 'crafting-scissors-7', 'name': 'Crafting Scissors 7', 'description': 'Crafting scissor description.', 'image': 'crafting-scissors-7.jpg'},
        {'id': 'crafting-scissors-8', 'name': 'Crafting Scissors 8', 'description': 'Crafting scissor description.', 'image': 'crafting-scissors-8.jpg'},
        {'id': 'crafting-scissors-9', 'name': 'Crafting Scissors 9', 'description': 'Crafting scissor description.', 'image': 'crafting-scissors-9.jpg'},
        {'id': 'crafting-scissors-10', 'name': 'Crafting Scissors 10', 'description': 'Crafting scissor description.', 'image': 'crafting-scissors-10.jpg'},
    ]
    return render_template('search_results.html', crafting_scissors=crafting_scissors)

@app.route('/scissors/<path:scissor_id>')
def scissor_detail(scissor_id):
    try:
        # URL-encode the scissor_id
        encoded_scissor_id = urlencode({'path': scissor_id})
        # Render the individual scissor page based on the encoded scissor_id
        return render_template('scissor_detail.html', scissor_id=encoded_scissor_id)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
