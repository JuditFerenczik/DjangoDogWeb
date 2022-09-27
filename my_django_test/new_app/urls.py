from django.urls import path
from . import views


app_name = 'new_app'
urlpatterns = [
    path('', views.sample_view, name='example'),
    path('variable/', views.variable_view, name='variable'),
    path('<int:num_page>', views.num_page_view),
    path('<str:topic>', views.news_view, name='topic_page')

]
