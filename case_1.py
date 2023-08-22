#!/usr/bin/env python3
from validator.v1 import Validator
from auth import register


def handle_sign_up_form(username, password, email, phone):
    if Validator.check_email(email):
        if Validator.check_phone(phone):
            if Validator.check_username(username):
                if Validator.check_password(password):
                    register(username, password, email, phone)
                    return {
                        'status': '200',
                        'details': 'Success'
                    }
                else:
                    return {
                        'status': '400',
                        # This code is so hard to read, that I made a mistake in error message
                        'details': 'Invalid or taken username'
                    }
            else:
                return {
                    'status': '400',
                    'details': 'Invalid or taken username'
                }
        else:
            return {
                'status': '400',
                'details': 'Invalid phone'
            }
    else:
        return {
            'status': '400',
            'details': 'Invalid email'
        }
