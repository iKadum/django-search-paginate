from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def pagination(request, queryset, rpp):  # rpp - results per page
    page_number = request.GET.get("page")  # page number from url (?page=)
    paginator = Paginator(queryset, rpp)

    try:
        new_queryset = paginator.get_page(page_number)

    except PageNotAnInteger:
        new_queryset = paginator.get_page(1)

    except EmptyPage:
        page_number = paginator.num_pages
        new_queryset = paginator.get_page(page_number)

    return new_queryset
