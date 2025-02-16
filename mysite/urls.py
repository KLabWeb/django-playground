from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),      # path expect 2+ args: route & view
    path("pollsrestapi/", include("pollsrestapi.urls")),
    path("admin/", admin.site.urls),            # include appends /polls paths to polls/
]                                               # allows easy sub-domains by folder