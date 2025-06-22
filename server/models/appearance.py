from config import db
from sqlalchemy.orm import validates

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))

    guest = db.relationship('Guest', back_populates='appearances')
    episode = db.relationship('Episode', back_populates='appearances')

    @validates('rating')
    def validate_rating(self, key, rating):
        if not (isinstance(rating, int) and 1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        return rating

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'guest_id': self.guest_id,
            'episode_id': self.episode_id
        }

    def to_dict_with_guest(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'guest': self.guest.to_dict()
        }
