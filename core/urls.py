from django.urls import path
from core import views

urlpatterns = [
    path('',views.home , name='home'),
    
    #catagory
    path('catagori/', views.category_view , name='catagori'),
    path('catagory/<slug:name>/', views.catagory_item_view , name='catagori-item'),
    
    # Account
    path('account/',views.account , name='account'),
    
    #vendor
    path('vendor/', views.vendor_view , name='vendor'),
    path('vendor/<slug:vid>/', views.vendor_details , name='vendor-details'),
    path('vendor-api/', views.vendor_API , name='vendor-api'),
    
    #product
    path('product/<slug:pid>/', views.product_details , name='product-details'),
    
    #tags
    path('product/tag/<slug:tag_slug>/',views.tags , name='tags-product'),
    
    #add review 
    path('add-review/<slug:pid>/',views.add_review , name='add-review'),
    
    #Sharching 
    path('sharch/',views.sharch_view , name='sharch'),
    path('filter/',views.filter_view , name='filter'),
    
    # add Cart....
    path('cart/',views.add_chart , name='cart'),
    
    # order , update order , cancle order
    path('order/',views.order , name='your-view'),
    path('uporder/<slug:oid>/',views.update_order , name='update-order'),
    path('cancle-order/<slug:oid>/',views.cancle_order , name='cancle_order'),
    path('bayling/<slug:oid>/',views.baylingAdd , name='bayling-add'),
    path('payment-request/',views.payment_request , name='payment-request'),
    path('add-pay/<slug:oid>/',views.paymentAdd , name='payment-add'),
    
    # bkash payment
    # path('initiate-payment/', views.initiate_payment, name='initiate_payment'),

]
