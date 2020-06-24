class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{passwd}@{ip}/{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
