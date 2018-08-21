import django_tables2 as tables
from student.models import DefenseSession

class SessionTable(tables.Table):
    class Meta:
        model = DefenseSession
        template_name = 'public/anon2.html'