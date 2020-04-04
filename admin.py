from flask_admin import Admin, BaseView, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from models import *


class DashboardView(AdminIndexView):

    @expose('/')
    def index(self):
        applicants = db.session.query(Applicant).all()
        return self.render('admin/admin_dashboard.html', apps=applicants)


class NewModel(ModelView):
    can_create = True
    can_edit = True
    can_delete = False


admin = Admin(index_view=DashboardView())

admin.add_view(NewModel(User, db.session))
admin.add_view(NewModel(Group, db.session))
admin.add_view(NewModel(Applicant, db.session))
