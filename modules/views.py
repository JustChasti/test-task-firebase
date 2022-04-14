import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from flask import Blueprint
from flask import render_template, redirect, url_for
from modules import forms


bp = Blueprint('views', __name__)
database_url = 'https://test-project-ceef3-default-rtdb.firebaseio.com/'

cred = credentials.Certificate("dbkey.json")
firebase_admin.initialize_app(
    cred,
    {'databaseURL': database_url}
)


class DuplicateError(Exception):
    def __init__(self, name):
        self.message = f'Cтрана {name} уже есть в списке'
        super().__init__(self.message)

@bp.route("/test")
def test():
    return 'hello world'


@bp.route("/")
@bp.route("/home")
def home():
    return render_template('home.html', title='home')


@bp.route("/countries_get", methods=['GET', 'POST'])
def get():
    ref = db.reference("/countries/")
    countries = ref.get()
    return render_template('get.html', data=countries)


@bp.route("/countries_add", methods=['GET', 'POST'])
def add():
    form = forms.AddForm()
    ermessage = ''
    if form.validate_on_submit():
        try:
            print(form.name.data)
            ref = db.reference("/countries/")
            countries = ref.get()
            if form.name.data in countries:
                raise DuplicateError(form.name.data)
            countries.append(form.name.data)
            ref = db.reference("/")
            ref.update({"countries":countries})
            return redirect('/countries_get')
        
        except DuplicateError as e:
            ermessage = str(e)
        except Exception as e:
            print(e)
            ermessage = 'Ошибка - попытайтесь снова'
    return render_template('add.html', form=form, error=ermessage)