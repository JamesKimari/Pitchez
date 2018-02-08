from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Pitch, Comment
from .forms import PitchForm, UpdateProfile, CommentsForm
from flask_login import login_required, current_user
from .. import db, photos

@main.route('/')
@login_required
def index():
    """
    View root page function that returns the index page and its data
    """
    title = 'Pitches'
    general = Pitch.query.all()
    product_pitch = Pitch.query.filter_by(category = 'Product Pitch').all()
    pickup_lines = Pitch.query.filter_by(category = 'Pickup Lines').all()
    interview_pitch = Pitch.query.filter_by(category = 'Interview Pitch').all()
    promotion_pitch = Pitch.query.filter_by(category = 'Promotion Pitch').all()

    return render_template('index.html', title = title, general = general, product_pitch = product_pitch, pickup_lines = pickup_lines, interview_pitch = interview_pitch, promotion_pitch = promotion_pitch)

@main.route('/user/<uname>')
@login_required
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
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile', uname = uname))

@main.route('/pitch/new_pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()    

    if pitch_form.validate_on_submit():
        pitch = Pitch(title = pitch_form.title.data, category = pitch_form.category.data, pitch_content = pitch_form.pitch_content.data, author = pitch_form.author.data)

        db.session.add(pitch)
        db.session.commit() 
        
        return redirect(url_for('main.index'))
    
    return render_template('new_pitch.html', pitch_form = pitch_form)   

@main.route('/pitch/comments', methods = ['GET', 'POST'])
@login_required
def comments():    
    comments_form = CommentsForm() 
    comments = Comment.query.all()    

    if comments_form.validate_on_submit():       

        # Updated comment instance
        new_comment = Comment(body = comments_form.body.data)

        # Save review method
        new_comment.save_comment()

        return redirect(url_for('main.comments'))
    
    return render_template('comments.html', comments_form = comments_form, comments = comments)
