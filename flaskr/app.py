from flaskr import create_app
from .modelos import db, Registro
import datetime

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    r = Registro(id="8269ce8b-5f68-4fc8-99ed-2a1751842c77", instancia="1", fecha=datetime.datetime.now(), payload= '{"example":"EXAMPLE"}')
    Registro.query.filter_by(id="8269ce8b-5f68-4fc8-99ed-2a1751842c77").delete()
    db.session.add(r)
    db.session.commit()
    print(Registro.query.all())
    Registro.query.filter_by(id="8269ce8b-5f68-4fc8-99ed-2a1751842c77").delete()