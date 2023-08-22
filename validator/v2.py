#!/usr/bin/env python3


class Validator:
    VALIDATORS = {
        'email': Validator.check_email,
        'phone': Validator.check_phone,
        'username': Validator.check_username,
        'password': Validator.check_password,
    }

    ERRORS = {
        'email': 'Invalid email',
        'phone': 'Invalid phone',
        'username': 'Invalid or taken username',
        'password': 'Invalid or week password',
    }

    @staticmethod
    def validate(fields: tuple) -> dict:
        errors = []

        for field in fields:
            validator = Validator.VALIDATORS[field_type]
            if validator(field['value'], field['type']):
                continue
            errors.append(Validator.ERRORS[field['type']])

        return {
            'success': len(errors) == 0,
            'errors': errors
        }

    @staticmethod
    def check_username(value: str) -> bool:
        return True

    @staticmethod
    def check_password(value: str) -> bool:
        return True

    @staticmethod
    def check_phone(value: str) -> bool:
        return True

    @staticmethod
    def check_email(value: str) -> bool:
        return True
