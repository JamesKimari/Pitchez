from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Pitch
from .forms import PitchForm, UpdateProfile
from flask_login import login_required, current_user
from .. import db, photos

@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    title = 'Pitchez'
    pitches = Pitch.query.all()

    return render_template('index.html', title = title, pitches = pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))

    return render_template('profile/update.html', form = form)

@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile', uname = uname))

@main.route('/login/pitch/new_pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()
    title = 'New Pitch'

    if pitch_form.validate_on_submit():
        pitch = Pitch(title = pitch_form.title.data, category = pitch_form.category.data, pitch_content = pitch_form.pitch_content.data)
        

        db.session.add(pitch)
        db.session.commit() 
        
        return redirect(url_for('main.index'))

    
    return render_template('new_pitch.html', title = title, pitch_form = pitch_form)    
