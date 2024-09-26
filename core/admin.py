from django.contrib import admin
from core.models import PaymentRequest, Category , Vendor , Product , ProductImages ,Cart,CartItem , Order , ProductReview , WishList , Address , BaylingAddress

class ProductImageAdmin(admin.TabularInline):
    model = ProductImages
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['user','title','featured','product_image','price','product_status','catagori']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','category_image']
    
class VendorAdmin(admin.ModelAdmin):
    list_display = ['title','vendor_image']
    
class CartOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cart._meta.fields]
    
class CartItemsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CartItem._meta.fields]
    
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user','review','rating']
    
class WishListAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WishList._meta.fields]
    
class AddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Address._meta.fields]
    
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    
class BaylingAdmin(admin.ModelAdmin):
    list_display = ['your_name','email','home_address']
    
class PaymentRequestAdmin(admin.ModelAdmin):
    list_display = ['your_name','transaction','payment_method','tr_date']
    
    
    
##################     now register all models ##########################

admin.site.register(Product , ProductAdmin)
admin.site.register(Category , CategoryAdmin)
admin.site.register(Vendor , VendorAdmin)
admin.site.register(Cart , CartOrderAdmin)
admin.site.register(CartItem, CartItemsAdmin)
admin.site.register(ProductReview , ProductReviewAdmin)
admin.site.register(WishList ,WishListAdmin)
admin.site.register(Address , AddressAdmin)
admin.site.register(Order ,OrderAdmin)
admin.site.register(BaylingAddress,BaylingAdmin)
admin.site.register(PaymentRequest , PaymentRequestAdmin)