import os
import requests
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "shopping_app_secret_key"  # Required for flash messages

# API server URL - configurable via environment variable
API_URL = os.environ.get('API_SERVER_URL', 'http://localhost:3000')

# Routes
@app.route('/')
def index():
    """Home page - display all shopping items"""
    try:
        response = requests.get(f"{API_URL}/items")
        if response.status_code == 200:
            items = response.json()
            return render_template('shopping.html', items=items, page='index')
        else:
            flash(f"Error fetching items: {response.status_code}", "error")
            return render_template('shopping.html', items=[], page='index')
    except requests.exceptions.RequestException as e:
        flash(f"Connection error: {str(e)}", "error")
        return render_template('shopping.html', items=[], page='index')

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    """Add a new item"""
    if request.method == 'POST':
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        
        if not name or not quantity:
            flash("Both name and quantity are required", "error")
            return redirect(url_for('add_item'))
        
        try:
            quantity = int(quantity)
        except ValueError:
            flash("Quantity must be a number", "error")
            return redirect(url_for('add_item'))
        
        try:
            response = requests.post(
                f"{API_URL}/items", 
                json={"name": name, "quantity": quantity}
            )
            
            if response.status_code in [200, 201]:
                item = response.json()
                flash(f"Item {'updated' if response.status_code == 200 else 'added'} successfully", "success")
                return redirect(url_for('index'))
            else:
                flash(f"Error adding item: {response.status_code}", "error")
        except requests.exceptions.RequestException as e:
            flash(f"Connection error: {str(e)}", "error")
        
    return render_template('shopping.html', page='add')

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    """Edit an existing item"""
    if request.method == 'POST':
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        
        if not name or not quantity:
            flash("Both name and quantity are required", "error")
            return redirect(url_for('edit_item', item_id=item_id))
        
        try:
            quantity = int(quantity)
        except ValueError:
            flash("Quantity must be a number", "error")
            return redirect(url_for('edit_item', item_id=item_id))
        
        try:
            response = requests.put(
                f"{API_URL}/items/{item_id}", 
                json={"name": name, "quantity": quantity}
            )
            
            if response.status_code == 200:
                flash("Item updated successfully", "success")
                return redirect(url_for('index'))
            elif response.status_code == 404:
                flash("Item not found", "error")
                return redirect(url_for('index'))
            else:
                flash(f"Error updating item: {response.status_code}", "error")
        except requests.exceptions.RequestException as e:
            flash(f"Connection error: {str(e)}", "error")
    else:
        # GET request - fetch current item data
        try:
            response = requests.get(f"{API_URL}/items/{item_id}")
            if response.status_code == 200:
                item = response.json()
                return render_template('shopping.html', item=item, page='edit')
            elif response.status_code == 404:
                flash("Item not found", "error")
                return redirect(url_for('index'))
            else:
                flash(f"Error fetching item: {response.status_code}", "error")
                return redirect(url_for('index'))
        except requests.exceptions.RequestException as e:
            flash(f"Connection error: {str(e)}", "error")
            return redirect(url_for('index'))
    
    return render_template('shopping.html', page='edit')

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    """Delete an item"""
    try:
        response = requests.delete(f"{API_URL}/items/{item_id}")
        
        if response.status_code == 204:
            flash("Item deleted successfully", "success")
        elif response.status_code == 404:
            flash("Item not found", "error")
        else:
            flash(f"Error deleting item: {response.status_code}", "error")
    except requests.exceptions.RequestException as e:
        flash(f"Connection error: {str(e)}", "error")
    
    return redirect(url_for('index'))

# Create templates directory if it doesn't exist
if not os.path.exists('templates'):
    os.makedirs('templates')

# Create the single HTML template file
with open('templates/shopping.html', 'w') as f:
    f.write('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopping List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            border-bottom: 1px solid #ccc;
            padding-bottom: 10px;
        }
        h1 {
            margin: 0;
            color: #333;
        }
        .btn {
            display: inline-block;
            padding: 8px 16px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            border: none;
            cursor: pointer;
            font-size: 14px;
        }
        .btn:hover {
            background-color: #45a049;
        }
        .btn-danger {
            background-color: #f44336;
        }
        .btn-danger:hover {
            background-color: #d32f2f;
        }
        .btn-secondary {
            background-color: #2196F3;
        }
        .btn-secondary:hover {
            background-color: #0b7dda;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #f5f5f5;
        }
        .flash-messages {
            padding: 0;
            margin-bottom: 20px;
        }
        .flash-message {
            padding: 10px;
            margin: 5px 0;
            border-radius: 4px;
            list-style: none;
        }
        .flash-success {
            background-color: #dff0d8;
            color: #3c763d;
            border: 1px solid #d6e9c6;
        }
        .flash-error {
            background-color: #f2dede;
            color: #a94442;
            border: 1px solid #ebccd1;
        }
        form div {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="number"] {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .actions {
            white-space: nowrap;
        }
        .api-status {
            font-size: 12px;
            margin-top: 10px;
            color: #666;
        }
    </style>
</head>
<body>
    <header>
        <h1>Shopping List</h1>
        <nav>
            <a href="/" class="btn btn-secondary">Home</a>
            <a href="/add" class="btn">Add Item</a>
        </nav>
    </header>
    
    {% if get_flashed_messages() %}
    <ul class="flash-messages">
        {% for category, message in get_flashed_messages(with_categories=true) %}
        <li class="flash-message flash-{{ category }}">{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    
    <main>
        {% if page == 'index' %}
            <h2>My Items</h2>
            
            {% if items %}
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Quantity</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {% for item in items %}
                    <tr>
                        <td>{{ item.id }}</td>
                        <td>{{ item.name }}</td>
                        <td>{{ item.quantity }}</td>
                        <td class="actions">
                            <a href="/edit/{{ item.id }}" class="btn btn-secondary">Edit</a>
                            <a href="/delete/{{ item.id }}" class="btn btn-danger" onclick="return confirm('Are you sure you want to delete this item?')">Delete</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
            {% else %}
            <p>No items found. Click "Add Item" to create your first item.</p>
            {% endif %}
        {% elif page == 'add' %}
            <h2>Add New Item</h2>
            
            <form method="post">
                <div>
                    <label for="name">Item Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div>
                    <label for="quantity">Quantity:</label>
                    <input type="number" id="quantity" name="quantity" min="1" required>
                </div>
                <div>
                    <button type="submit" class="btn">Add Item</button>
                    <a href="/" class="btn btn-secondary">Cancel</a>
                </div>
            </form>
        {% elif page == 'edit' %}
            <h2>Edit Item</h2>
            
            <form method="post">
                <div>
                    <label for="name">Item Name:</label>
                    <input type="text" id="name" name="name" value="{{ item.name }}" required>
                </div>
                <div>
                    <label for="quantity">Quantity:</label>
                    <input type="number" id="quantity" name="quantity" value="{{ item.quantity }}" min="1" required>
                </div>
                <div>
                    <button type="submit" class="btn">Update Item</button>
                    <a href="/" class="btn btn-secondary">Cancel</a>
                </div>
            </form>
        {% endif %}
    </main>
    
    <footer>
        <div class="api-status">
            API Server: {{ api_server_url }}
        </div>
    </footer>
</body>
</html>
    ''')

if __name__ == '__main__':
    # Use environment variable for port or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Set debug mode based on environment variable
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    # Print configuration information
    print(f"API Server URL: {API_URL}")
    print(f"Frontend running on port: {port}")
    print(f"Debug mode: {debug}")
    
    # Add API URL to template context
    @app.context_processor
    def inject_api_url():
        return dict(api_server_url=API_URL)
    
    app.run(host='0.0.0.0', port=port, debug=debug)