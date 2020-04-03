from flask_admin import Admin, BaseView, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from models import *


class NewModel(ModelView):
    can_create = True
    can_edit = True
    can_delete = False


class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats/index.html')


class DashboardView(AdminIndexView):

    @expose('/')
    def index(self):
        return self.render('admin/dashboard_index.html')


admin = Admin(index_view=DashboardView())

admin.add_view(StatsView(name='Статистика', endpoint='stats'))
admin.add_view(NewModel(Location, db.session))
admin.add_view(NewModel(Enrollment, db.session))
admin.add_view(NewModel(Participant, db.session))
admin.add_view(NewModel(Event, db.session))
