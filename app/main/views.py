from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
# from .. import db
from ..models import Profile
# from app import login_manager
from .forms import ProfileForm

@main.route('/')
def index():
    '''
    View page function that creates and returns the post titles on the index page
    '''

    form = ProfileForm()

    # if form.validate_on_submit():
    #     new_team = Team(actual_post=form.post.data, user_id=current_user.id)
    #     # new_team.save_post()
    #     # flash('Team has been created successfully')
    #     return redirect(url_for('.index'))
    # # team = Team.query.all()
    title= 'Coachya'
    return render_template('index.html',title = title)





@main.route('/profile/add',methods = ['GET','POST'])
# @login_required
def new_profile():
    '''
    View pitch function that returns the pitch page and data
    '''
    form = ProfileForm()

    if form.validate_on_submit():
        teamname = form.teamname.data
        vision = form.vision.data
        mission = form.mission.data
        members = form.members.data

        new_profile = Profile(teamname=teamname,vision=vision,mision=mission,members=members,user_id=current_user.id)
        new_profile.save_profile()
        flash('Profile has been created!', 'success')
        return redirect(url_for('main.home'))

    return render_template('new_profile.html', profile_form = form)