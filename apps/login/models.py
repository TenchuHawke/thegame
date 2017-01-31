from __future__ import unicode_literals
from django.db import models
import bcrypt, re

EMAIL_REGEX = re.compile(r'^[a-z0-9.+_-]+@[a-z0-9._-]+\.[a-z]+$')


class UserManager(models.Manager):
    def add_user(self, postData):
        errors = []
        # TODO change validations
        if not len(postData['first_name']):
            errors.append('First name can not be blank.')
        if not len(postData['last_name']):
            errors.append('Last name can not be blank.')
        if not len(postData['password']):
            errors.append('Password can not be blank.')
        if len(postData['password'])<8:
            errors.append('Password must be 8 characters long.')
        if not len(postData['confirm_password']):
            errors.append('Password confirmation can not be blank.')
        if not postData['password'] == postData['confirm_password']:
            errors.append("Passwords do not match")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Must use a valid email, all lowercase please')

        user = Users.objects.filter(email=postData['email'])

        if user:
            errors.append('E-mail already exists')

        modelResponse = {}
        # if failed validation, send response to views.py
        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        #Passed validation, save user
        else:
            hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            Users.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=hashed_password)
            user=Users.objects.filter(email= postData['email'])
            modelResponse['status']=True
            modelResponse['user']=user

        return modelResponse

    def check_user(self, postData):

        errors = []
        modelResponse={}
        if not postData['lemail']:
            errors.append("E-mail can't be blank.")
        else:
            print postData
            user = Users.objects.filter(email = postData['lemail'])
            if user:
                # check passwords
                if not bcrypt.checkpw(postData['lpassword'].encode(), user[0].password.encode()):
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


class Users(models.Model):
    email = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=60, unique=True)
    userlevel = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
