from django.conf import settings
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.conf.urls.static import static
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


urlpatterns = [
    path('', include('pages.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/', CreateView.as_view(
        form_class=UserCreationForm,
        success_url=reverse_lazy('pages:homepage'),
        template_name='registration/registration_form.html'
    ),
    name='registration'
    ),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
