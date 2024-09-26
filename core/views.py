# inport statement
from django.shortcuts import render  , get_object_or_404  , redirect 
from datetime import datetime
from taggit.models import Tag
from django.db.models import Avg
from django.http import JsonResponse
from core.models import PaymentRequest, Category , Vendor , Product , ProductImages ,Cart,CartItem , Order , ProductReview , WishList , Address ,BaylingAddress
from core.form import ProductReviewForm , BaylingAddressForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from django.db import transaction
from core import support
from .payment_service import BkashService

# object statement
# bkash_service = BkashService()

def home(request):
    
    products = Product.objects.all().order_by('-id')
    
    # Calculate the average rating for each product
    products_with_ratings = []
    for product in products:
        avg_rating = ProductReview.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
        products_with_ratings.append({
            'product': product,
            'avg_rating': avg_rating,
        })
    
    context = {
        "products": products_with_ratings,
    }
    
    return render(request, 'core/home.html', context)

                  ####################  Catagory ########################

def account(request):
    orders_with_details = []
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
        for order in orders:
            bayling = BaylingAddress.objects.filter(order=order).first()
            payment_req = PaymentRequest.objects.filter(order=order).first()
            orders_with_details.append({
                'order': order,
                'bayling': bayling,
                'payment_req': payment_req,
            })

    context = {
        'orders_with_details': orders_with_details,
    }
    return render(request, 'user/account.html', context)


def catagory_item_view(request , name):
    products = Product.objects.filter(catagori=name)
    
    products_with_ratings = []
    for product in products:
        avg_rating = ProductReview.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
        products_with_ratings.append({
            'product': product,
            'avg_rating': avg_rating,
        })
    
    context = {
        "products": products_with_ratings,
    }
    
    return render(request, 'core/home.html', context)

def category_view(request):
    data = Category.objects.all().values()
    data_list = list(data)  # Converting the queryset to a list

    return JsonResponse(data_list, safe=False)

                  ############# vendor ######################

def vendor_view(request):
    data = Vendor.objects.all()
    
    context = {
        "vendors":data,
    }
    return render(request, 'core/vendor.html', context)

def vendor_API(request):
    vendor = Vendor.objects.all()
    
    vendor_json = serializers.serialize('json', vendor)
    
    return JsonResponse( vendor_json , safe=False)

def vendor_details(request , vid):
    data = Vendor.objects.filter(vid=vid)
    context = {
        "vendors":data,
    }
    return render(request, 'core/vendor-details.html', context)

                ################# products #####################

def product_details(request, pid):
    product = get_object_or_404(Product, pid=pid)
    
    review =  ProductReview.objects.filter(product=product)
    # avgeage rating
    avg_rating =  ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    
    reviewForm = ProductReviewForm()
    context = {
        "product_details": product,
        'review':review,
        'avg_rating':avg_rating,
        'R_form':reviewForm,
    }
    return render(request, 'core/product-details.html', context)

def tags(request,tag_slug=None):
    
    products = Product.objects.filter(product_status='published').order_by('-id')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag , slug=tag_slug)
        products = products.filter(tags__in=[tag])
    
    products_with_ratings = []
    for product in products:
        avg_rating = ProductReview.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
        products_with_ratings.append({
            'product': product,
            'avg_rating': avg_rating,
        })
    
    context = {
        "products": products_with_ratings,
        "tag":tag,
    }
    return render(request, 'core/home.html', context)

def add_review(request,pid):
    try:
        product = Product.objects.get(pid=pid)
    except Product.DoesNotExist:
        return JsonResponse({'bool': False, 'message': 'Product not found'}, status=404)
    
    if not request.user.is_authenticated:
        return JsonResponse({'bool': False, 'message': 'Login first'})
    user = request.user
    review = request.POST['review']
    rating = request.POST['rating']
    
    ProductReview.objects.create(
        user=user,
        product=product,
        review = review,
        rating = rating,
    )
    contex = {
        'user':user.username,
        'review':review,
        'rating':rating,
    }
    Avg_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    
    return JsonResponse({
        'bool':True,
        "contex":contex,
        'avg_rating':Avg_rating,
    })

def sharch_view(request):
    query = request.GET.get('q')
    
    products = Product.objects.filter(title__icontains=query).order_by('-date')
    try:
    
     if query.startswith('#'):
        tag = get_object_or_404(Tag , slug=support.remove_first_character(query))
        products = Product.objects.filter(tags__in=[tag])
    except Exception as e:
        print(e)
    products_with_ratings = []
    for product in products:
        avg_rating = ProductReview.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
        products_with_ratings.append({
            'product': product,
            'avg_rating': avg_rating,
        })
    
    context = {
        "products": products_with_ratings,
        'query':query,
    }
    
    return render(request, 'core/sharch.html', context)

def filter_view(request):
    
    item_value = request.GET.getlist('item')
    if item_value:
        products=Product.objects.filter(vendor__in=item_value)
    else:
        products = Product.objects.all()
    
    min_price = request.GET.get('min_p')
    max_price = request.GET.get('max_p')
    if min_price and int(min_price) > 1:
        products = products.filter(price__gte=min_price, price__lte=max_price)
        
        
    products_with_ratings = []
    for product in products:
        avg_rating = ProductReview.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
        products_with_ratings.append({
            'product': product,
            'avg_rating': avg_rating,
        })
    
    context = {
        "products": products_with_ratings,
    }
    
    return render(request, 'core/home.html', context)

def add_chart(request):
    item_value = request.GET.getlist('item')
    order_no = request.GET.get('orderNo')

    products = Product.objects.filter(pid__in=item_value)

    products_with_ratings = []
    for product in products:
        avg_rating = ProductReview.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
        print(f'Product: {product}, Avg Rating: {avg_rating}')  # Debugging
        products_with_ratings.append({
            'product': product,
            'avg_rating': avg_rating,
        })

    context = {
        "products": products_with_ratings,
        "OrderNo":order_no,
    }
    
    return render(request, 'core/cart.html', context)

@csrf_exempt  # Use csrf_exempt if you're not sending the CSRF token
@transaction.atomic  # Ensure that the order creation and cart item addition are atomic
def order(request):
    if request.method == 'POST':
        try:
            bool = False
            cart_item = None
            if not request.user.is_authenticated:
               return JsonResponse({'message':'login-require'})
            user = request.user
            data = json.loads(request.body)  # Parse the JSON data
            total_price = 0  # Initialize total price
            cart_items = []  # Store CartItem instances

            for item in data:
                unique_number = item.get('item')
                quantity = int(item.get('quantity', 1))

                # Filter the product by its unique number
                try:
                    product = Product.objects.get(pid=unique_number)
                    total_price += product.price * quantity  # Multiply price by quantity

                    # Create and save the CartItem
                    cart_item = CartItem.objects.create(user=user, product=product, quantity=quantity)
                    cart_items.append(cart_item)
                except Product.DoesNotExist:
                    return JsonResponse({"error": f"Product with unique number {unique_number} not found"}, status=404)
            if(cart_item != None):
                bool = True
                # Create the Order instance
                order = Order.objects.create(user=user, total_price=total_price)

                # Add the CartItem instances to the Order
                order.items.add(*cart_items)

            # Return the total price
            return JsonResponse({"total_price": total_price ,'bool':bool })

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    # Handle other request methods if necessary
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def update_order(request,oid):
    if request.method == 'POST':
        try:
            bool = False
            cart_item = None
            if not request.user.is_authenticated:
               return JsonResponse({'message':'login-require'})
            user = request.user
            data = json.loads(request.body)  # Parse the JSON data
            total_price = 0  # Initialize total price
            cart_items = []  # Store CartItem instances

            for item in data:
                unique_number = item.get('item')
                quantity = int(item.get('quantity', 1))

                # Filter the product by its unique number
                try:
                    product = Product.objects.get(pid=unique_number)
                    total_price += product.price * quantity  # Multiply price by quantity

                    # Create and save the CartItem
                    cart_item = CartItem.objects.create(user=user, product=product, quantity=quantity)
                    cart_items.append(cart_item)
                except Product.DoesNotExist:
                    return JsonResponse({"error": f"Product with unique number {unique_number} not found"}, status=404)
            if(cart_item != None):
                bool = True
                # Create the Order instance
                order = Order.objects.get(oid=oid)
                if order.payment_status:
                    return JsonResponse({'message':'After accepting order you can not update order'})
                old_cart_items = order.items.all()
                for i in old_cart_items:
                   for_delete = CartItem.objects.get(id=i.id)
                   for_delete.delete()    # delete cart item
                
                # Add the CartItem instances to the Order
                order.items.add(*cart_items)
                order.total_price = total_price
                order.save()

            # Return the total price
            return JsonResponse({"total_price": total_price ,'bool':bool })

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    # Handle other request methods if necessary
    return JsonResponse({"error": "Invalid request method"}, status=405)

def cancle_order(request,oid):
    try:
        success = False
        
        order = Order.objects.get(oid=oid)
        if order.payment_status:
            return JsonResponse({'message':'Please contact our help line'})
        
        cart_items = order.items.all()
        for i in cart_items:
            for_delete = CartItem.objects.get(id=i.id)
            for_delete.delete()    # delete cart item
        bayling = BaylingAddress.objects.get(order = order)
        if bayling:
           bayling.delete()
        order.delete() # delete order

        success = True
        
        return JsonResponse({'success': success})

    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)
    except Exception as e:
        print(e)
        return JsonResponse({"error": str(e)}, status=400)

def baylingAdd(request , oid): 
    order = Order.objects.get(oid=oid)
    if order.payment_status:
        return render(request , 'error/error.html',{'message':' after payment you can not change your bayling address . If you need any help , you will contact or chat with us'})
    elif request.method == 'POST':
        data = request.POST
        
        # Getting or creating a BaylingAddress object using the order
        bayling, created = BaylingAddress.objects.get_or_create(
            order=order,
        )
        
        # Updating fields after object creation or retrieval
        bayling.your_name = data['your_name']
        bayling.email = data['email']
        bayling.phone_number = data['phone_number']
        bayling.division = data['division']
        bayling.district = data['district']
        bayling.home_address = data['home_address']
        
        # Save the updated object
        bayling.save()
        
        # Redirect to the payment page (pass the correct view name or URL pattern)
        return render(request,'payment/payment.html', {'order_oid':oid})
    
    return render(request, "payment/bayling.html")

def paymentAdd(request , oid):
    return render(request,'payment/payment.html', {'order_oid':oid})

def payment_request(request):
    if request.method == 'POST':
        data = request.POST
        print(data)  # Debugging
        
        order = Order.objects.get(oid=data['order_oid'])
        if not order:
            return render(request, 'error/error.html', {'message': 'Order not found'})
        
        try:
            if order.payment_status:
                return render(request, 'error/error.html', {'message': 'After payment, you cannot change your billing address. If you need any help, please contact or chat with us.'})
            
            p_request, created = PaymentRequest.objects.get_or_create(order=order)
            p_request.your_name = data['name']
            p_request.phone_number = data['phone']
            p_request.transaction = data['transaction_id']
            
            # The date string should already be in 'YYYY-MM-DD' format, so this should work without issues
            p_request.tr_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
            
            p_request.payment_method = data['payment_method']
            
            # Save the object
            p_request.save()
            
            return render(request, 'error/error.html', {'message': 'Success in making payment request. We will accept your request in a few hours and then deliver your product.'})
        
        except Exception as e:
            print(e)
            return render(request, 'error/error.html', {'message': 'Failed to make a payment request. Please provide valid data.'})
    
    return redirect('/')


"""

@csrf_exempt
def initiate_payment(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return JsonResponse({"success": False, "message": "Order not found."})

        amount = order.total_price

        # Check if token is present and valid
        if not bkash_service.token or datetime.now() >= bkash_service.token_expiry:
            bkash_service.get_access_token()
        else:
            try:
                # Optional: Add a lightweight token validation request if necessary
                pass
            except Exception:
                bkash_service.refresh_access_token()

        # Create the payment
        payment_response = bkash_service.create_payment(amount, invoice_number=order_id)
        payment_id = payment_response.get("paymentID")

        if payment_id:
            # Store paymentID in the Order for tracking
            order.payment_id = payment_id
            order.save()

            # Execute the payment
            execution_response = bkash_service.execute_payment(payment_id)

            if execution_response.get("transactionStatus") == "Completed":
                # Update order status to completed
                order.payment_status = True
                order.save()

                return JsonResponse({
                    "success": True,
                    "message": "Payment completed successfully.",
                    "transaction_id": execution_response.get("trxID")
                })
            else:
                return JsonResponse({
                    "success": False,
                    "message": "Failed to complete payment."
                })
    else:
        form = BaylingAddressForm()
            
    return render(request, "payment/bayling.html" , {'form':form})

@csrf_exempt
def refund_payment(request):
    if request.method == "POST":
        payment_id = request.POST.get("payment_id")
        amount = request.POST.get("amount")
        trx_id = request.POST.get("trx_id")
        reason = request.POST.get("reason", "Product Return")

        # Refund the payment
        refund_response = bkash_service.refund_payment(payment_id, amount, trx_id, reason)

        if refund_response.get("statusCode") == "0000":  # Assuming 0000 is a success code
            return JsonResponse({
                "success": True,
                "message": "Refund processed successfully.",
                "refund_trxID": refund_response.get("refundTrxID")
            })
        else:
            return JsonResponse({
                "success": False,
                "message": "Failed to process refund."
            })

    return render(request, "refund_payment.html")
"""
