from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name='home'),
    path("about/", views.aboutPage, name='about'),
    path('blog/<str:url>', views.postsPage, name="blogs"),
    path('category/<slug:url>', views.categoriesPage, name='categories'),
]
