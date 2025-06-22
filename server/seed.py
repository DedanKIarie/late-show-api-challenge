from config import app, db
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from models.user import User

with app.app_context():
    db.drop_all()
    db.create_all()

    print("Seeding database...")

    # Seed Guests
    guest1 = Guest(name='Bill Burr', occupation='Comedian')
    guest2 = Guest(name='Viola Davis', occupation='Actress')
    guest3 = Guest(name='Neil deGrasse Tyson', occupation='Astrophysicist')

    db.session.add_all([guest1, guest2, guest3])
    db.session.commit()

    # Seed Episodes
    episode1 = Episode(date='2024-10-26', number=1520)
    episode2 = Episode(date='2024-10-27', number=1521)

    db.session.add_all([episode1, episode2])
    db.session.commit()

    # Seed Appearances
    appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode1.id)
    appearance3 = Appearance(rating=5, guest_id=guest3.id, episode_id=episode2.id)

    db.session.add_all([appearance1, appearance2, appearance3])
    db.session.commit()
    
    # Seed a default user for testing
    user1 = User(username='testuser')
    user1.set_password('password')
    db.session.add(user1)
    db.session.commit()


    print("Database seeded!")
