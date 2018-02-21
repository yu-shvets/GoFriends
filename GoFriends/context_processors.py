from gofriends_site.models import MetaTags


def project_variables(request):
    index_tags = MetaTags.objects.filter(page__iexact='index').first()
    return {'index': index_tags}
