from django.http import HttpResponseNotFound, Http404
from django.views.defaults import page_not_found, server_error, permission_denied, bad_request
from django.core.exceptions import PermissionDenied, SuspiciousOperation, ValidationError

def custom_404(request):
    # return HttpResponseNotFound("<h1>Page not found</h1>")
    # raise Http404("Page does not exist")
    return page_not_found(request, exception='')

def custom_500(request):
    raise ValidationError("Error Message")
    # return server_error(request)

def custom_403(request):
    # raise PermissionDenied
    return permission_denied(request, exception='')

def custom_400(request):
    raise SuspiciousOperation('Bad request')
    # return bad_request(request, exception='')