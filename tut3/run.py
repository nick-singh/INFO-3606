from app import app
from app import db

db.create_all()
db.session.commit()

if __name__ == '__main__':
	app.run("0.0.0.0", 5000, debug=True)
