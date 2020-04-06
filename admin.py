from flask_admin import Admin, BaseView, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from models import *


class DashboardView(AdminIndexView):

    @expose('/')
    def index(self):
        # order by a_id because we dont have date column in applicant model
        applicants = db.session.query(Applicant).order_by(Applicant.a_id.desc()).all()
        appl_new = []
        appl_r = []
        for appl in applicants:
            if appl.status == 'распределена в группу':
                appl_r.append(appl)
            if appl.status == 'новая':
                appl_new.append(appl)
        groups = db.session.query(Group).order_by(Group.start_date.desc()).all()
        # dict for free seats in groups
        dict_for_d = dict()
        for group in groups[:4]:
            dict_for_d[group.g_id] = len(db.session.query(Applicant).filter(Applicant.group_id == group.g_id).all())
        return self.render('admin/admin_dashboard.html',
                           apps=applicants,
                           r_apps=appl_r,
                           n_apps=appl_new,
                           groups=groups,
                           dict_for_d=dict_for_d)


class NewModel(ModelView):
    can_create = True
    can_edit = True
    can_delete = False


admin = Admin(index_view=DashboardView())

admin.add_view(NewModel(User, db.session))
admin.add_view(NewModel(Group, db.session))
admin.add_view(NewModel(Applicant, db.session))
