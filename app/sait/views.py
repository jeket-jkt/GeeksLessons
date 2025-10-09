from django.shortcuts import render, redirect
from app.sait.models import Settings, Statics, Imgaes, Comment
from .forms import CommentForm
def index(request):
    settings_all = Settings.objects.all()
    statistic_all = Statics.objects.all()
    image_all = Imgaes.objects.all()
    return render(request, "index.html", locals())

def index(request):
    comments = Comment.objects.order_by('-created_at')
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'index.html', {'form': form, 'comments': comments})