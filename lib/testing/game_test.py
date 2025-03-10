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

def test_create_game(session):
    game = Game(title="Elden Ring", genre="RPG")
    session.add(game)
    session.commit()

    retrieved_game = session.query(Game).filter_by(title="Elden Ring").first()
    assert retrieved_game is not None
    assert retrieved_game.genre == "RPG"
