from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)

    reviews = relationship("Review", back_populates="game", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Game(id={self.id}, title={self.title}, genre={self.genre})>"

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)

    game = relationship("Game", back_populates="reviews")

    def __repr__(self):
        return f"<Review(id={self.id}, content={self.content}, rating={self.rating}, game_id={self.game_id})>"

# Database setup
engine = create_engine("sqlite:///games.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
