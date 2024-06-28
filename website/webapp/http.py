from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse

def request(request):
    # response = HttpRequest.scheme
    # response = HttpRequest.body
    # response = HttpRequest.method

    # response = HttpRequest.get_host(self=request)
    response = HttpRequest.is_secure(self=request)

    return HttpResponse(response)

def response(request):
    # response = HttpResponse("Here's the text of the web page.")
    # response = HttpResponse("Text only, please.", content_type="text/plain")
    # response = HttpResponse(b"Bytestrings are also accepted.")
    # response = HttpResponse(memoryview(b"Memoryview as well."))

    # response = HttpResponse()
    # response.write("<p>Here's the text of the web page.</p>")
    # response.write("<p>Here's another paragraph.</p>")

    response = HttpResponse("<h1>created</h1>", status=201)

    return response

def redirect(request):
    return HttpResponseRedirect("/redirected/")

def json(request):
    response = JsonResponse({"foo": "bar"})
    return response