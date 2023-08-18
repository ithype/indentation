#!/usr/bin/env python3
from validator.v1 import Validator
from auth import register


def handle_sign_up_form(username, password, email, phone):
    if not Validator.check_email(email):
        return {
            'status': '400',
            'details': 'Invalid email'
        }

    if not Validator.check_phone(phone):
        return {
            'status': '400',
            'details': 'Invalid phone'
        }

    if not Validator.check_username(username):
        return {
            'status': '400',
            'details': 'Invalid or taken username'
        }

    if not Validator.check_password(password):
        return {
            'status': '400',
            'details': 'Invalid or week password'
        }

    register(username, password, email, phone)
    return {
        'status': '200',
        'details': 'Success'
    }
