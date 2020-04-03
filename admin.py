from flask_admin import Admin, BaseView, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from models import *


class NewModel(ModelView):
    can_create = True
    can_edit = True
    can_delete = False


class MailerView(BaseView):
    @expose('/')
    def mails(self):
        return self.render('admin/mailer/index.html')


class StatsView(BaseView):
    @expose('/')
    def stats(self):
        part = len(db.session.query(Participant).all())
        regs = len(db.session.query(Enrollment).all())
        return self.render('admin/stats/index.html', parts=part, regs=regs)


# class ParticipantView(BaseView):
#     @expose('/<e_id>')
#     def event_stats(self, e_id):
#         event = db.session.query(Event).get(e_id)
#         enroll = db.session.query(Enrollment).filter(Enrollment.event_id == e_id).all()
#
#         if not enroll or len(enroll) > event.seats:
#             seats = f'Осталось {len(enroll) - event.seats}'
#         else:
#             seats = 'Мест нет'
#         return self.render('admin/events/index.html', event=event, seats=seats)


class DashboardView(AdminIndexView):

    @expose('/')
    def index(self):
        return self.render('admin/dashboard_index.html')


admin = Admin(index_view=DashboardView())
#
# admin.add_view(ParticipantView(name='ИНфа об эвентах', endpoint='events'))
admin.add_view(StatsView(name='Статистика', endpoint='stats'))
admin.add_view(MailerView(name='Рассылки', endpoint='mailer'))
admin.add_view(NewModel(Location, db.session))
admin.add_view(NewModel(Enrollment, db.session))
admin.add_view(NewModel(Participant, db.session))
admin.add_view(NewModel(Event, db.session))
