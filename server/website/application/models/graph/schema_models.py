from application import db

class EntityClass(db.Model):
    __tablename__ = 'entity_class'

    index = db.Column(db.Integer, primary_key=True)
    prefLabel = db.Column(db.String(64), nullable=False) # 通常英文标签
    label = db.Column(db.String(64), nullable=False) # 通常为中文标签
    subClassOf = db.Column(db.String(64), nullable=False)
    vertical = db.Column(db.String(32), nullable=False)

    comment = db.Column(db.Text, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<EntityClass %r>' % self.prefLabel


class ObjectProperty(db.Model):
    __tablename__ = 'object_property'

    index = db.Column(db.Integer, primary_key=True)
    prefLabel = db.Column(db.String(64), nullable=False)
    label = db.Column(db.String(64), nullable=False)
    comment = db.Column(db.String(256), nullable=True)
    subPropertyOf = db.Column(db.String(64), nullable=True)
    domain = db.Column(db.String(32), nullable=False)
    rangee = db.Column(db.String(32), nullable=False) # range是关键字所以写成rangee
    vertical = db.Column(db.String(32), nullable=False)
    functionalProperty = db.Column(db.Boolean, nullable=False)
    symmetricProperty = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<ObjectProperty %r>' % self.prefLabel


class DataProperty(db.Model):
    __tablename__ = 'data_property'

    index = db.Column(db.Integer, primary_key=True)
    prefLabel = db.Column(db.String(64), nullable=False)
    label = db.Column(db.String(64), nullable=False)
    comment = db.Column(db.String(256), nullable=True)
    subPropertyOf = db.Column(db.String(64), nullable=True)
    domain = db.Column(db.String(32), nullable=False)
    rangee = db.Column(db.String(32), nullable=False) # range是关键字所以写成rangee
    vertical = db.Column(db.String(32), nullable=False)
    functionalProperty = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<ObjectProperty %r>' % self.prefLabel
