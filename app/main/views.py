from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
# from .. import db
from ..models import Profile, Coach
# from app import login_manager
from .forms import ProfileForm, CoachForm

@main.route('/')
def index():
    '''
    View page function that creates and returns the post titles on the index page
    '''
    teams = Profile.query.all()
    coaches = Coach.query.all()

    title= 'Coachya'
    return render_template('index.html',title = title,teams = teams,coaches=coaches)

@main.route('/details/<id>')
def details(id):
    '''
    returns the details of the team selected
    '''
    team = Profile.get_profiles(id)
    title = 'Team Details'
    return render_template('details.html', title = title, teams = team)

@main.route('/profile/add',methods = ['GET','POST'])
@login_required
def new_team():
    '''
    View pitch function that returns the pitch page and data
    '''
    form = ProfileForm()

    if form.validate_on_submit():
        teamname = form.teamname.data
        vision = form.vision.data
        mission = form.mission.data
        members = form.members.data
        support = form.support.data
        description = form.description.data
        email = form.email.data
        location = form.location.data

        new_profile = Profile(teamname=teamname,vision=vision,mission=mission,members=members,support = support,email = email,location = location, description = description,user_id=current_user.id)
        new_profile.save_profile()
        flash('Profile has been created!', 'success')
        return redirect(url_for('main.index'))

    return render_template('new_profile.html', profile_form = form)

@main.route('/coach/add',methods = ['GET','POST'])
# @login_required
def new_coach():
    '''
    View pitch function that returns the pitch page and data
    '''
    form = CoachForm()

    if form.validate_on_submit():
        name = form.name.data
        support_to_provide = form.support_to_provide.data
        description = form.description.data


        new_coach = Coach(name=name,support_to_provide=support_to_provide,description = description, user_id=current_user.id)
        new_coach.save_coach()
        flash('Profile has been created!', 'success')
        return redirect(url_for('main.index'))

    return render_template('new_coach.html', coach_form = form)
