from app import db


class Model(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    delete_flag = db.Column(db.Boolean,default=False)
    def save(self):
        session = db.session()
        session.add(self)
        session.commit()

    def delete(self):
        session = db.session()
        session.delete(session)
        session.commit()

class Article(Model):
    title = db.Column(db.String(128))
    author = db.Column(db.String(128))
    description = db.Column(db.Text)
    content = db.Column(db.Text)
    public_time = db.Column(db.DateTime)


