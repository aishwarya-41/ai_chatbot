from . import db

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_message = db.Column(db.Text) 
    bot_response = db.Column(db.Text) 
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
