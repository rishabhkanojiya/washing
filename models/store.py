from db import db


class StoreModel(db.Model):

    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    token = db.Column(db.Integer)
    rfid_code = db.Column(db.String(50))
    water_usage = db.Column(db.Float(precision=2))

    def __init__(self, name, token, rfid_code, water_usage):
        self.name = name
        self.token = token
        self.rfid_code = rfid_code
        self.water_usage = water_usage

    def json(self):
        return {'name': self.name, 'token': self.token, 'rfid_code': self.rfid_code,
                'water_usage': self.water_usage}

    @classmethod
    def find_by_rf(cls, rfid_code):
        return cls.query.filter_by(rfid_code=rfid_code).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
