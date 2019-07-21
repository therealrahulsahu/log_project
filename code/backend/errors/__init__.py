class BackToFeatureError(Exception):
    def __init__(self):
        pass


class notFoundError(Exception):
    def __init__(self):
        pass


class NotFoundError(Exception):
    def __init__(self):
        pass


class WrongDetailsError(Exception):
    def __init__(self):
        pass


class WrongPasswordError(Exception):
    def __init__(self):
        pass


class AlreadyExistsError(Exception):
    def __init__(self, mess=""):
        self.mess = mess

    def __str__(self):
        return '{}'.format(self.mess)


class WrongUsernameError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Wrong Username"


class WrongEmailError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Wrong Email or Recovery Hint"
