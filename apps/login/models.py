from __future__ import unicode_literals
from django.db import models
import bcrypt, re

EMAIL_REGEX = re.compile(r'^[a-z0-9.+_-]+@[a-z0-9._-]+\.[a-z]+$')


class UserManager(models.Manager):
    def add_user(self, postData):
        errors = []
        # TODO change validations
        if not postData['password2']:
            errors.append('Password can not be blank.')
        if len(postData['password2'])<8:
            errors.append('Password must be 8 characters long.')
        if not len(postData['confirm']):
            errors.append('Password confirmation can not be blank.')
        if not postData['password2'] == postData['confirm']:
            errors.append("Passwords do not match")
        if not EMAIL_REGEX.match(postData['email_add']):
            errors.append('Must use a valid email, all lowercase please')

        user = Users.objects.filter(email=postData['email_add'])

        if user:
            errors.append('E-mail already exists')

        modelResponse = {}
        # if failed validation, send response to views.py
        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        #Passed validation, save user
        else:
            hashed_password = bcrypt.hashpw(postData['password2'].encode(), bcrypt.gensalt())
            Users.objects.create(email=postData['email_add'], username=postData['add_username'], password=hashed_password)
            user=Users.objects.filter(email= postData['email_add'])
            modelResponse['status']=True
            modelResponse['user']=user

        return modelResponse

    def check_user(self, postData):
        # TODO ('lowercase username')
        errors = []
        modelResponse={}
        if not postData['username']:
            errors.append("Username can't be blank.")
        else:
            user = Users.objects.filter(username = postData['username'])
            if user:
                # check passwords
                if not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                    errors.append('Invalid E-mail, password combination, try again')
                else:
                    modelResponse['status']=True
                    modelResponse['user']=user
            else:
                errors.append('User not found, try another email or register a new account.')
        if errors:
            modelResponse['status']=False
            modelResponse['errors']=errors
        return modelResponse

    def update_user(self, postData):
        errors = []
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Must use a valid email, all lowercase please')
        if len(postData['username'])<3:
            errors.append('Must enter valid username')
        user = Users.objects.filter(username=postData['username']).exclude(id=postData['id'])

        if user:
            errors.append('Username already exists')

        user = Users.objects.filter(email=postData['email']).exclude(id=postData['id'])

        if user:
            errors.append('Email already exists')

        modelResponse={}

        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors

        else:
            user = Users.objects.get(id=postData['id'])
            user.username = postData['username']
            user.email = postData['email']
            user.userlevel = postData['userlevel']
            user.save()
            modelResponse['status'] = True
        return modelResponse



class Users(models.Model):
    email = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=60, unique=True)
    userlevel = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
