from flask import Flask, url_for, render_template, request
from werkzeug.exceptions import InternalServerError 

from app.config import Config
from app import index
from app.utils.error_handler import handle_error
from app.utils.utility import context_processor

def create_app():
    app = Flask(__name__)

    #設定
    app.config.from_object(Config)
    
    #コントローラ
    app.register_blueprint(index.bp)

    #エラーハンドラ
    app.register_error_handler(InternalServerError, handle_error)

    #ユーティリティ
    app.context_processor(context_processor)

    return app


