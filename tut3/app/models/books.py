from app import db



class Book(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    title = db.Column(db.String(80))

    def __repr__(self):
        return "<Title: {}>".format(self.title)

    def toJSON(self):
        return {
            "id":self.id,
            "title":self.title
        }
