from cards import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_card = db.Column(db.String,unique = True)
    description_card = db.Column(db.String,unique = True)
    class_card = db.Column(db.String)
    type_card = db.Column(db.String)
    rare_card = db.Column(db.String)
    attack_card = db.Column(db.String)
    mana_card = db.Column(db.String)
    life_card = db.Column(db.String)
    img = db.Column(db.String)

