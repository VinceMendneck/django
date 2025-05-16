from django.views.generic import ListView, DetailView
from blog.models import Post

class PostView(ListView):
    """
    A view que lida com a exibição de um post de blog.
    """
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(DetailView):
    """
    A view que lida com a exibição de um post de blog.
    """
    model = Post
    template_name = 'post_detail.html'