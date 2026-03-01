from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# A simple list of hardcoded suggestions (could be from a database)
SUGGESTIONS = [
    "Apple", "Avocado", "Apricot",
    "Banana", "Blueberry", "Blackberry",
    "Cherry", "Cranberry", "Coconut",
    "Date", "Dragonfruit",
    "Elderberry",
    "Fig",
    "Grape", "Grapefruit", "Guava",
    "Honeydew",
    "Kiwi", "Kumquat",
    "Lemon", "Lime", "Lychee",
    "Mango", "Melon", "Mandarin",
    "Nectarine",
    "Orange", "Olive",
    "Peach", "Pear", "Plum", "Pineapple", "Papaya", "Pomegranate",
    "Raspberry",
    "Strawberry",
    "Tangerine", "Tomato",
    "Watermelon"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest', methods=['GET'])
def suggest():
    query = request.args.get('q', '').lower()
    
    if not query:
        return jsonify([])
        
    # Filter the list based on whether the suggestion starts with the query
    filtered_suggestions = [
        item for item in SUGGESTIONS if item.lower().startswith(query)
    ]
    
    # Return at most 10 suggestions
    return jsonify(filtered_suggestions[:10])

if __name__ == '__main__':
    app.run(port=5001, debug=True)
