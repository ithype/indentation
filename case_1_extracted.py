#!/usr/bin/env python3
from validator.v2 import Validator
from auth import register


def handle_sign_up_form(username, password, email, phone):
    validation_result = Validator.validate((
        { 'value': username, 'type': 'username' },
        { 'value': password, 'type': 'password' },
        { 'value': email, 'type': 'email' },
        { 'value': phone, 'type': 'phone' },
    ))
    if not validation_result['success']:
        return {
            'status': '400',
            'details': {
                'message': 'Validation error',
                'errors': validation_result['error']
            }
        }

    register(username, password, email, phone)
    return {
        'status': '200',
        'details': 'Success'
    }
