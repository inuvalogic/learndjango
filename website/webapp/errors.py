from django.http import HttpResponseNotFound, Http404
from django.views.defaults import page_not_found, server_error, permission_denied, bad_request
from django.core.exceptions import PermissionDenied, SuspiciousOperation, ValidationError

def custom_404(request, exception):
    # return HttpResponseNotFound("<h1>Page not found</h1>")
    # raise Http404("Page does not exist")
    return page_not_found(request, exception='')
    
def custom_500(request):
    return server_error(request)

def custom_403(request, exception):
    return permission_denied(request, exception='')

def custom_400(request, exception):
    return bad_request(request, exception='')

def raise403(request):
    raise PermissionDenied

def raise400(request):
    raise SuspiciousOperation("Bad Request")

def raise500(request):
    raise ValidationError("Error Message")