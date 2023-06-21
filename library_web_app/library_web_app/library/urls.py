from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('booklist/',views.book_list,name='book_list'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('author_list/', views.AuthorListView.as_view(), name='author_list'),

]