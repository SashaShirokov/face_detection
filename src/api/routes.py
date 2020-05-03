from api import generator, db
from api.forms import Forms
from api.models import interview_data, User

from flask import Flask, render_template, Response, Blueprint, url_for, flash, redirect

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/')
def home():
    return render_template('home.html', interview_data=interview_data)


@api_bp.route('/about')
def about():
    return render_template('about.html')


@api_bp.route('/forms', methods=['GET', 'POST'])
def forms():
    form = Forms()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Info from {form.username.data} has been successfully received!', 'success')
        return redirect(url_for('api_bp.forms'))
    return render_template('forms.html', title='Forms', form=form)


@api_bp.route('/video_feed')
def video_feed():
    known_faces = []
    known_names = []
    return Response(generator.gen(known_faces, known_names),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
