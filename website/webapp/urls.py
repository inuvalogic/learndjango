from django.urls import path, re_path, register_converter, include

from . import views, converters, user, http, errors, posts

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("", views.index, name="index"),

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
    path("http/json", http.json),
    path("http/redirect", http.redirect),

    # Error
    path("http/403", errors.raise403),
    path("http/403", errors.raise403),
    path("http/400", errors.raise400),
    path("http/500", errors.raise500),
    path("http/403", errors.raise403),

    # Template
    path("posts/", include("webapp.posts_urls")),
    # path("posts/", include("webapp.posts_generic_urls")),

]