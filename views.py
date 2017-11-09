from settings import *
from models import *
import command
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template


@app.route('/')
def test():
    command.Orgs.create("Chinese Corner", "2017", "No des")
    command.Activities.create("Chinese Corner First Activity", "asjdkfl")
    command.Members.create("Hankel", "20160401", "arche")
    command.Orgs.add_activity("Chinese Corner", "Chinese Corner First Activity", "asdjfkl")
    command.Orgs.add_member("Chinese Corner", "Hankel", "Leader")
    command.Activities.add_org("Chinese Corner First Activity", "Chinese Corner")
    command.Activities.add_member("Chinese Corner First Activity", "Hankel", "Leader")
    command.Members.add_org("Hankel", "Chinese Corner")
    command.Members.add_activity("Hankel", "Chinese Corner First Activity", "ajsdkfl")
    command.Members.add_activity()
    return render_template('test.html')
