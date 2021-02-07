class Config():
    # set FLASK_APP=app
    # set FLASK_ENV=development
    # シークレットキー生成コマンド : python -c "import os; print(os.urandom(16))"
    SECRET_KEY = b"SB\xa5\x9by\xadE\xcf\xcf\xcbu\xdc\xb2\xf9}\x81"
    SQLALCHEMY_DATABASE_URI = ""