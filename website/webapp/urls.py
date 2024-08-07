from django.urls import path, re_path, register_converter, include

from . import views, converters, user, http, errors

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),

    # URLconf
    path("blogs/category-name/", views.list_by_category),
    path("blogs/<int:year>/", views.list_by_year),
    path("blogs/<int:year>/<int:month>/", views.list_by_month),
    path("blogs/<int:year>/<int:month>/<slug:slug>/", views.post_detail),

    # Path converters
    path("str/<str:param_str>", views.path_converter_string),
    path("int/<int:param_int>", views.path_converter_number),
    path("slug/<slug:param_slug>", views.path_converter_slug),
    path("uuid/<uuid:param_uuid>", views.path_converter_uuid),
    path("path/<path:param_path>", views.path_converter_path),

    # Regular expression
    re_path(r"^comments/(?:page-(?P<page_number>[0-9]+)/)?$", views.regex),

    # Custom path converters
    path("custom/<yyyy:year>/", views.list_custom),

    # Naming URL patterns
    path("articles/", views.articles, name="article-list"),

    # Set Default value
    path("blog/", views.page),
    path("blog/<int:num>/", views.page),

    # Include other URLconf
    path("other/", include("webapp.other_urls")),
    path("user/", include([
        path("profile", user.profile),
        path("password", user.password),
        path("setting", user.setting),
    ])),

    # Namespace
    path("news/", include("webapp.news_urls")),

    # HTTP Methods
    path("http/request", http.request),
    path("http/response", http.response),
    path("http/redirect", http.redirect),
    path("http/json", http.json),

    # Error
    path("error/404", errors.custom_404),
    path("error/500", errors.custom_500),
    path("error/403", errors.custom_403),
    path("error/400", errors.custom_400),

    # Template
    # path("posts/", include("webapp.posts_urls")),
    path("posts/", include("webapp.posts_generic_urls")),
]