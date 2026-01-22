from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.

# See ALL listed items (for sale or sold regardless)
def post_list(request):
    posts = Post.objects.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
 )