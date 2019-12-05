from views import app

if __name__ == "__main__":
    from models import db
    db.create_all()
    app.run(host = "127.0.0.1", port = 8000, use_reloader = True)