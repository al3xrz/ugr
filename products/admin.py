from django.contrib import admin
from products.models import ProductGroup
from products.models import Product
from supply.models import Supplier
from supply.models import Feedback
from supply.models import Point
from geo.models import Locality
from geo.models import Municipality
from geo.models import Position




admin.site.register(ProductGroup)
admin.site.register(Product)

admin.site.register(Supplier)
admin.site.register(Feedback)
admin.site.register(Point)


admin.site.register(Municipality)
admin.site.register(Locality)
admin.site.register(Position)


