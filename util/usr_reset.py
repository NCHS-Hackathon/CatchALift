import os, sys, django
sys.path.append('/home/jackson/Projects/CatchALift/cal')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cal.settings'
django.setup()
from django.contrib.auth.models import User, Group
import json

user_json = open('usr.json', 'r')
user_list = json.load(user_json)
group_list = ['CALadmin', 'User', 'Coach']

for group in group_list:
    if len(Group.objects.filter(name=group)) == 0:
        Group.objects.create(name=group)

for user in user_list:
    if len(User.objects.filter(username=user['username'])) == 0:
        new_user = User.objects.create_user(username=user['username'],password=user['password'],first_name=user['fname'], last_name=user['lname'])
        Group.objects.get(name=user['group']).user_set.add(new_user)
        print('Added ' + user['username'])
