from django.http import HttpResponse

response = HttpResponse()

response.set_cookie(key,  value,  max_age)