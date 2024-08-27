from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Project, Blog
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Process the form data, e.g., send an email
        send_mail(
            subject=f'Contact Form Submission from {name}',
            message=message,
            from_email=email,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )

        messages.success(request, 'Thank you for your message. We will get back to you shortly.')
        return redirect('home')
    return render(request, 'home.html')