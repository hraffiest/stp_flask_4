from flask_admin import Admin, BaseView, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from models import *


class DashboardView(AdminIndexView):

    @expose('/')
    def index(self):
        applicants = db.session.query(Applicant).all()
        appl_new = []
        appl_r = []
        for appl in applicants:
            if appl.status == 'распределена в группу':
                appl_r.append(appl)
            if appl.status == 'новая':
                appl_new.append(appl)
        groups = db.session.query(Group).order_by(Group.start_date).all()
        grops_new = []
        for app in appl_new:
            for g in groups:
                if g.g_id == app.group_id and len(grops_new) < 4:
                    grops_new.append(g)
                elif len(grops_new) >= 3:
                    break
                if len(grops_new) >= 3:
                    break
        return self.render('admin/admin_dashboard.html',
                           apps=applicants,
                           r_apps=appl_r,
                           n_apps=appl_new,
                           groups=groups,
                           grops_new=grops_new)


class NewModel(ModelView):
    can_create = True
    can_edit = True
    can_delete = False


admin = Admin(index_view=DashboardView())

admin.add_view(NewModel(User, db.session))
admin.add_view(NewModel(Group, db.session))
admin.add_view(NewModel(Applicant, db.session))
