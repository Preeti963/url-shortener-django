from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import ShortURL
from .utils import generate_short_code
from django.contrib.auth.forms import UserCreationForm

@login_required
def dashboard(request):
    urls = ShortURL.objects.filter(user=request.user)
    return render (request, 'shortener/dashboard.html', {'urls':urls})

@login_required
def create_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')

        short_code = generate_short_code()
        while ShortURL.objects.filter(short_code=short_code).exists():
            short_code = generate_short_code()

        ShortURL.objects.create(
            user=request.user,
            original_url=original_url,
            short_code=short_code
        )
        return redirect('dashboard')
 
    return render(request, 'shortener/create.html')

@login_required
def edit_url(request, id):
    url =get_object_or_404(ShortURL, id=id, user=request.user)

    if request.method =='POST':
        url.original_url = request.POST.get('original_url')
        url.save()
        return redirect('dashboard')
    
    return render(request, 'shortener/edit.html', {'url': url})

@login_required
def delete_url(request, id):
    url = get_object_or_404(ShortURL, id=id, user=request.user)
    url.delete()
    return redirect('dashboard')

def redirect_url(request, code):
    url = get_object_or_404(ShortURL, short_code=code)

    if url.expires_at and timezone.now() > url.expires_at:
        return render(request, 'shortener/expired.html')
    
    url.click_count +=1
    url.save()
    return redirect(url.original_url)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})