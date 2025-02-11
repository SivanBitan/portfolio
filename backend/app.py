from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

# SQLite Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)  # Allow frontend requests

# Database Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    tech_stack = db.Column(db.Text, nullable=False)
    github = db.Column(db.String(200))
    demo = db.Column(db.String(200))

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Create tables before first run
with app.app_context():
    db.create_all()

# API Routes
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    project_list = [{
        "id": p.id,
        "title": p.title,
        "description": p.description,
        "tech_stack": p.tech_stack.split(','),
        "github": p.github,
        "demo": p.demo
    } for p in projects]
    return jsonify({"projects": project_list})

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    new_message = ContactMessage(
        name=data['name'],
        email=data['email'],
        message=data['message']
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify({"message": "Message sent successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
