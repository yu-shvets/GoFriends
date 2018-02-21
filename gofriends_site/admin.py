from django.contrib import admin
from .models import CaseStudies, Services, Technologies, Industries, About, Contacts, Customers, MetaTags
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


admin.site.register(CaseStudies)
admin.site.register(Services)
admin.site.register(Technologies)
admin.site.register(Industries)
admin.site.register(About)
admin.site.register(Contacts)
admin.site.register(Customers)
admin.site.register(MetaTags)










