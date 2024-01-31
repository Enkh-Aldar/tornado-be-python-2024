from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Language

def language_view(request):
    # Assuming YourModel is the model you want to paginate
    queryset = Language.objects.all()

    # Number of items to display per page
    items_per_page = 2

    # Create a Paginator object
    paginator = Paginator(queryset, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        current_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        current_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        current_page = paginator.page(paginator.num_pages)

    # Now you can pass the current_page object to your template
    return render(request, 'language.html', {'current_page': current_page})