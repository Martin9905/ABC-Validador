from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Registro(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    instancia = db.Column(db.String(64))
    fecha = db.Column(db.DateTime)
    payload = db.Column(db.String(4000))

    def __repr__(self):
        return "{} {} {} {}".format(self.id, self.instancia, self.fecha, self.payload)
