from models.models import UserModel

class UserService:
    def find_user_by_email(self, email):
        user = UserModel.objects.filter(email = email)
        return user or None

    def register_user(self, email, password):
        UserModel.objects.create_user(email = email, username = email, password = password)