from rosters import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^$',
        RedirectView.as_view(
            url='/cutthecheck/audit',
            permanent=True,
        ),
    ),
    url(
        r'^cutthecheck/audit/$',
        views.AuditView.as_view(),
        name="league-audit"
    ),
    url(
        r'^cutthecheck/bible/$',
        views.BibleView.as_view(),
        name='salary-bible'
    ),
    url(
        r'^cutthecheck/detail/(?P<slug>[-_\w]+)/$',
        views.ProfileView.as_view(),
        name="profile-page",
    )
)
