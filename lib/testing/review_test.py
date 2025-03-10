import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from lib.models import Base, Game, Review

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def test_create_review(session):
    game = Game(title="Dark Souls", genre="Action RPG")
    session.add(game)
    session.commit()

    review = Review(content="Amazing difficulty!", rating=5, game_id=game.id)
    session.add(review)
    session.commit()

    retrieved_review = session.query(Review).filter_by(game_id=game.id).first()
    assert retrieved_review is not None
    assert retrieved_review.rating == 5
