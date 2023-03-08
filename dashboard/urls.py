from django.conf import Settings, settings
from django.conf.urls.static import static
from django.urls import path
from.import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('delete_note/<int:pk>',views.delete_note, name='delete-note'),
    path('notes_detail/<int:pk>',views.NotesDetailView.as_view(),name="notes-detail"),
    path('index',views.index,name="index"),
    path('upload',views.upload, name="upload"),
    path('assignment/',views.assig_list, name="assignment"),
    path('assignment/upload/', views.upload_assig, name="upload_assig"),
    path('assignment/<int:pk>/', views.delete_assign, name="delete_assign"),
    path('notes_adder',views.notes_adder, name="notesadder"),
    path('experiment',views.experiment, name="experiments"),
    path('exp/',views.exp_list,name="experiment"),
    path('exp/upload/', views.upload_exp, name="upload_exp"),
    path('exp/<int:pk>/', views.delete_exp, name="delete_exp"),
    path('upload exx',views.upload_experiment, name="upload exx"),
    path('register', views.register, name="register"),
    path('assg_page',views.assg_page,name="assg_page"),
    path('exp1',views.exp1,name="exp1"),
    # path('log in/', views.log_in, name="login")
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


