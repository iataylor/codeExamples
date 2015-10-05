from django.conf.urls import url
from . import views

"""URLs used by the views in main_site."""
urlpatterns = [
    url(r'^doctors/(?P<user>[0-9]+)/', views.doctorDetail, name='doctorDetail'),
    url(r'^patients/(?P<user>[0-9]+)/', views.patientDetail, name='patientDetail'),
    url(r'^nurses/(?P<user>[0-9]+)/', views.nurseDetail, name='nurseDetail'),
    url(r'^hospitalAdmins/(?P<user>[0-9]+)/', views.hospitalAdminDetail, name='hospitalAdminDetail'),
    url(r'^doctors-other/(?P<user>[0-9]+)/', views.doctorDetail_other, name='doctorDetail_other'),
    url(r'^patients-other/(?P<user>[0-9]+)/', views.patientDetail_other, name='patientDetail_other'),
    url(r'^patients-admin/(?P<user>[0-9]+)/(?P<id>[0-9]+)/', views.patientDetail_admin, name='patientDetail_admin'),
    url(r'^nurses-other/(?P<user>[0-9]+)/', views.nurseDetail_other, name='nurseDetail_other'),
    url(r'^hospitalAdmins-other/(?P<user>[0-9]+)/', views.hospitalAdminDetail_other, name='hospitalAdminDetail_other'),
    url(r'^patients-doctor/(?P<user>[0-9]+)/(?P<id>[0-9]+)/', views.patientDetail_doctor, name='patientDetail_doctor'),
    url(r'^patients-nurse/(?P<user>[0-9]+)/(?P<id>[0-9]+)/', views.patientDetail_nurse, name='patientDetail_nurse'),
    url(r'^doctor-updates-patient/(?P<user>[0-9]+)/(?P<id>[0-9]+)/', views.doctor_update_patient, name='doctor_update_patient'),
    url(r'^admin-updates-patient/(?P<user>[0-9]+)/(?P<id>[0-9]+)/', views.admin_update_patient, name='admin_update_patient'),
    url(r'^nurse-updates-patient/(?P<user>[0-9]+)/(?P<id>[0-9]+)/', views.nurse_update_patient, name='doctor_update_patient'),
    url(r'^inbox/(?P<user>[0-9]+)/', views.inbox, name='inbox'),
    url(r'^outbox/(?P<user>[0-9]+)/', views.outbox, name='outbox'),
    url(r'^message/(?P<user>[0-9]+)/', views.newMessage, name='newMessage'),
    url(r'^view-message/(?P<user>[0-9]+)/', views.view_message, name='view_message'),
    url(r'^view-log/', views.view_activity_log, name='view_activity_log'),
    url(r'^login/$', views.login_page, name='Login'),
    url(r'^registration/$', views.registration_page, name='Registration'),
    url(r'^register-doctor/$', views.register_doctor, name='register_doctor'),
    url(r'^register-hospitalAdmin/$', views.register_hospitalAdmin, name='register_hospitalAdmin'),
    url(r'^register-nurse/$', views.register_nurse, name='register_nurse'),
    url(r'^patient-update/(?P<user>[0-9]+)/', views.patient_update, name='patient_update'),
    url(r'^doctor-update/(?P<user>[0-9]+)/', views.doctor_update, name='doctor_update'),
    url(r'^nurse-update/(?P<user>[0-9]+)/', views.nurse_update, name='nurse_update'),
    url(r'^hospitalAdmin-update/(?P<user>[0-9]+)/', views.hospitalAdmin_update, name='hospitalAdmin_update'),
    url(r'^calendar-doctor/(?P<user>[0-9]+)/(?P<id>[0-9]+)/', views.get_calendar_doctor, name='get_calendar_doctor'),
    url(r'^calendar-patient/(?P<user>[0-9]+)/(?P<id>[0-9]+)/', views.get_calendar_patient, name='get_calendar_patient'),
    url(r'^appointmentDoctor/(?P<user>[0-9]+)/(?P<id>[0-9]+)/', views.get_appointment_doctor, name='get_Appointment_doctor'),
    url(r'^appointmentPatient/(?P<user>[0-9]+)/(?P<id>[0-9]+)/', views.get_appointment_patient, name='get_Appointment_patient'),
    url(r'^create-appointment/(?P<user>[0-9]+)/(?P<id>[0-9]+)/', views.newAppointment, name='newAppointment'),
    #url(r'^cancel-appointment/(?P<user>[0-9]+)/(?P<id>[0-9]+)/', views.cancelAppointment, name='cancelAppointment'),
    url(r'^logout/$', views.logout_page, name="Logout"),
    url(r'^', views.default_page, name="default_page"),
]