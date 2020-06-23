class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{passwd}@{host}/{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
