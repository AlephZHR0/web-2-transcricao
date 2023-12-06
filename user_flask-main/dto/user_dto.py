class UserDTO:
    def __init__(self, user_id, username, ra, birthdate, email, password):
        self.user_id = user_id
        self.username = username
        self.ra = ra
        self.birthdate = birthdate
        self.email = email
        self.password = password

    @staticmethod
    def from_model(model):
        return UserDTO(user_id=model.user_id, username=model.username, ra=model.ra, birthdate=model.birthdate, email=model.email, password=model.password)
