from application import db


class Entity2Label(db.Model):
    __tablename__ = 'entity2label'

    text_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=True)
    text = db.Column(db.Text, nullable=False)
    label = db.Column(db.Text, nullable=False)
    mark = db.Column(db.Integer, nullable=False)
    origin = db.Column(db.String(256), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Entity2Label %r>' % self.origin


class Relation2Label(db.Model):
    __tablename__ = 'relation2label'

    sentence_id = db.Column(db.Integer, primary_key=True)
    sentence = db.Column(db.Text, nullable=False)
    head = db.Column(db.String(64), nullable=False)
    tail = db.Column(db.String(64), nullable=False)
    head_type = db.Column(db.Integer, nullable=False)
    tail_type = db.Column(db.Integer, nullable=False)
    relation_type = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    mark = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Relation2Label %r>' % self.relation_type
