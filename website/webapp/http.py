from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse, Http404

def request(request):
    response = HttpRequest.scheme
    response = HttpRequest.body
    response = HttpRequest.method

    response = HttpRequest.get_host()
    response = HttpRequest.is_secure()

    return HttpResponse(response)

def response(request):
    response = HttpResponse("Here's the text of the web page.")
    response = HttpResponse("Text only, please.", content_type="text/plain")
    response = HttpResponse(b"Bytestrings are also accepted.")
    response = HttpResponse(memoryview(b"Memoryview as well."))

    response = HttpResponse()
    response.write("<p>Here's the text of the web page.</p>")
    response.write("<p>Here's another paragraph.</p>")

    response = HttpResponse("<h1>created</h1>", status=201)

    return response

def redirect(request):
    return HttpResponseRedirect("/redirected/")

def json(request):
    response = JsonResponse({"foo": "bar"})
    return response