from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import ShortURL
from .utils import generate_short_code
from .qr import generate_qr_code
from django.contrib.auth.forms import UserCreationForm

@login_required
def dashboard(request):
    urls = ShortURL.objects.filter(user=request.user)
    for u in urls:
        # Generate QR code if it doesn't exist
        if not u.qr_code:
            qr_path = generate_qr_code(request.build_absolute_uri(f'/{u.short_code}'))
            u.qr_code = qr_path
            u.save()
    return render(request, 'shortener/dashboard.html', {'urls': urls})


@login_required
def create_url(request):
    if request.method == "POST":
        original_url = request.POST.get("original_url")
        custom_code = request.POST.get("custom_code")
        expires_at = request.POST.get("expires_at")

        # Handle custom short code
        if custom_code:
            if ShortURL.objects.filter(short_code=custom_code).exists():
                return render(request, "shortener/create.html", {"error": "Custom short URL already exists"})
            short_code = custom_code
        else:
            short_code = generate_short_code()
            while ShortURL.objects.filter(short_code=short_code).exists():
                short_code = generate_short_code()

        # Create the ShortURL instance
        url = ShortURL.objects.create(
            user=request.user,
            original_url=original_url,
            short_code=short_code,
            expires_at=expires_at if expires_at else None
        )

        # Generate QR code for the short URL
        qr_path = generate_qr_code(request.build_absolute_uri(f'/{url.short_code}'))
        url.qr_code = qr_path
        url.save()

        return redirect("dashboard")

    return render(request, "shortener/create.html")


@login_required
def edit_url(request, id):
    url = get_object_or_404(ShortURL, id=id, user=request.user)
    if request.method == 'POST':
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
    url.click_count += 1
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
