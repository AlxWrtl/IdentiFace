from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.orm import declarative_base, sessionmaker
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLITE_PATH = os.path.join(BASE_DIR, "faces.db")
DATABASE_URL = f"sqlite:///{SQLITE_PATH}"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()


class Face(Base):
    __tablename__ = "faces"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    encoding = Column(LargeBinary, nullable=False)


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

print("DB created")


def save_encoding(name, encoding):
    encoded_blob = pickle.dumps(encoding)
    new_face = Face(name=name, encoding=encoded_blob)
    session.add(new_face)
    session.commit()
    print(f"-- Encoding for {name} saved --")


def load_encoding():
    encodings, names = [], []

    for face in session.query(Face).all():

        encodings.append(pickle.loads(face.encoding))
        names.append(face.name)

    print(f"-- {len(encodings)} faces loaded --")

    return encodings, names
