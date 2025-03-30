from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ObituaryForm
from .models import Obituary

def submit_obituary(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Obituary submitted successfully!')
            return redirect('submit_obituary')
    else:
        form = ObituaryForm()
    
    return render(request, 'obituaries/obituary_form.html', {'form': form})
from django.core.paginator import Paginator
from .models import Obituary

def view_obituaries(request):
    obituaries_list = Obituary.objects.all().order_by('-submission_date')
    paginator = Paginator(obituaries_list, 10)  # Show 10 obituaries per page
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'obituaries/view_obituaries.html', {'page_obj': page_obj})

from django.shortcuts import get_object_or_404

def obituary_detail(request, slug):
    obituary = get_object_or_404(Obituary, slug=slug)
    return render(request, 'obituaries/obituary_detail.html', {'obituary': obituary})