from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def generate_form_errors(form):
    message = ""
    for field in form:
        if field.errors:
            message += field.errors
    for err in form.non_field_errors():
        message += str(err)

    return message


def pagination(request, events, per_page):

    paginator_instance = Paginator(events, per_page)
    page_number = request.GET.get('page', 1)

    try:
        paginator_instance = paginator_instance.page(page_number)
    except PageNotAnInteger:
        paginator_instance = paginator_instance.page(1)
    except EmptyPage:
        paginator_instance = paginator_instance.page(paginator_instance.num_pages)

    return paginator_instance