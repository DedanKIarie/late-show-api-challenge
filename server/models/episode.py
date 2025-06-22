from config import db

class Episode(db.Model):
    __tablename__ ='episodes'
    
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)
    
    appearances = db.relationship('Appearance', back_populates= 'episode', cascade = 'all, delete-orphan')
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number,
            'appearances': [appearance.to_dict_with_guest() for appearance in self.appearances]
        }