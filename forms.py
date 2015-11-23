from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'tag', 'image', 'views']

    def add_post(request):
        context = RequestContext(request)
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():  # is the form valid?
                form.save(commit=True)  # yes?
                return redirect(index)
            else:
                print(form.errors)  # no? display errors to end user
        else:
            form = PostForm()
        return render_to_response('blog/add_post.html', {'form': form}, context)
