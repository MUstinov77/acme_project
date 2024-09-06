# birthday/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


def birthday(request, pk=None):
    instance = None
    if pk:
        instance = get_object_or_404(Birthday, pk=pk)
    form = BirthdayForm(
        request.POST or None,
        files=request.FILES or None,
        instance=instance
    )
    context = {'form': form}
    if form.is_valid():
        form.save()
        birthday_countdown = calculate_birthday_countdown(
            form.cleaned_data['birthday']
        )
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birthday/birthday.html', context)

def birthday_list(request):
    birthdays = Birthday.objects.order_by('id')
    paginator = Paginator(birthdays, 10)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {'page_object': page_object}
    return render(request, 'birthday/birthday_list.html', context)

def delete_birthday(request, pk):
    instance = get_object_or_404(Birthday, pk=pk)
    form = BirthdayForm(instance=instance)
    if request.method == 'POST':
        instance.delete()
        return redirect('birthday:list')
    context = {'form': form}
    return render(request, 'birthday/birthday.html', context)