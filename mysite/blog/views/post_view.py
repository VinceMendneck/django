from django.http import HttpResponse
from django.views.generic import View

class PostView(View):
    """
    A view que lida com a exibição de um post de blog.
    """
    def get(self, request, *args, **kwargs):
        # Lógica para recuperar e exibir o post de blog
        return HttpResponse("Blog Post")