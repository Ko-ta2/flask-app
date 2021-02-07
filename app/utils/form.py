from flask import session
from wtforms import Form, StringField, IntegerField, RadioField, SelectField, BooleanField, DateField
from wtforms.validators import InputRequired, Length, Optional, NumberRange, AnyOf
from wtforms.csrf.session import SessionCSRF

choices = [("値1", "ラベル1"), ("値2", "ラベル2"), ("値3", "ラベル3")]
selects = [("値1", "ラベル1"), ("値2", "ラベル2"), ("値3", "ラベル3")]

class BaseForm(Form):
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = b"+o\xc1\xd7n\xe5\xe3{\x9f\xbd\xf6\x17jF\xc4\xce"
        locales = ["ja"]

        @property
        def csrf_context(self):
            return session

class ContentForm(BaseForm):
    title = StringField("文字列", [InputRequired(), Length(max=50)])
    price = IntegerField("数値", [NumberRange(min=1, max=100)], default=10)
    favorite = RadioField("ラジオボタン", [InputRequired(), AnyOf([value for value, label in choices])], \
        choices=choices, default="値1")
    country = SelectField("セレクトボックス", [Optional(), AnyOf([value for value, label in selects])], \
        choices=selects)
    checked = BooleanField("チェックボックス", default="checked")
    switch = BooleanField("スイッチ")
    date = StringField("日付")
    time = StringField("時間")
    

