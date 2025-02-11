from app import app, db, Project

# Use application context to interact with the database
with app.app_context():
    db.create_all()

    sample_projects = [
        Project(
            title="E-Commerce Website",
            description="A full-stack e-commerce platform with payments.",
            tech_stack="React, Flask, PostgreSQL",
            github="https://github.com/yourusername/ecommerce",
            demo="https://myecommerce.com"
        ),
        Project(
            title="AI Chatbot",
            description="An AI-powered chatbot for customer support.",
            tech_stack="Next.js, Flask, OpenAI API",
            github="https://github.com/yourusername/chatbot",
            demo="https://mychatbot.com"
        )
    ]

    db.session.bulk_save_objects(sample_projects)
    db.session.commit()
    print("Database seeded successfully!")
