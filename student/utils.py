from .models import Student

def user_has_associated_student(user):
    has_student = False
    try:
        has_student = (user.student is not None)
    except Student.DoesNotExist:
        pass
    return has_student and (user.student is not None)
