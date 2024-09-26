from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

# choices statemet
STATUS_CHOICE = (
    ("proccess","Proccess"),
    ("shipped","Shipped"),
    ("delivered","Delivered"),
)

STATUS = (
    ("draft","Draft"),
    ("disabled","Disabled"),
    ("rejected","Rejected"),
    ("in_review","In Review"),
    ("published","Published"),
)

RATING = (
    (1,"⭐ ☆ ☆ ☆ ☆"),
    (2,"⭐⭐ ☆ ☆ ☆"),
    (3,"⭐⭐⭐ ☆ ☆"),
    (4,"⭐⭐⭐⭐ ☆"),
    (5,"⭐⭐⭐⭐⭐"),
)

MODE = (
    ('cod','Cash on delivery'),
    ('pp','Pre-paid'),
    ('pop','Post paid'),
)

DIVISION = (
    ('dhaka', 'DHAKA'),
    ('chattogram', 'CHATTOGRAM'),
    ('rajshahi', 'RAJSHAHI'),
    ('khulna', 'KHULNA'),
    ('barishal', 'BARISHAL'),
    ('sylhet', 'SYLHET'),
    ('rangpur', 'RANGPUR'),
    ('mymensingh', 'MYMENSINGH')
)

DISTRICT = (
    ('bagerhat', 'BAGERHAT'),
    ('bandarban', 'BANDARBAN'),
    ('barguna', 'BARGUNA'),
    ('barishal', 'BARISHAL'),
    ('bhola', 'BHOLA'),
    ('bogura', 'BOGURA'),
    ('brahmanbaria', 'BRAHMANBARIA'),
    ('chapainawabganj', 'CHAPAINAWABGANJ'),
    ('chandpur', 'CHANDPUR'),
    ('chattogram', 'CHATTOGRAM'),
    ('chuadanga', 'CHUADANGA'),
    ('cumilla', 'CUMILLA'),
    ('coxsbazar', 'COXSBAZAR'),
    ('dinajpur', 'DINAJPUR'),
    ('dhaka', 'DHAKA'),
    ('faridpur', 'FARIDPUR'),
    ('feni', 'FENI'),
    ('gaibandha', 'GAIBANDHA'),
    ('gazipur', 'GAZIPUR'),
    ('gopalganj', 'GOPALGANJ'),
    ('habiganj', 'HABIGANJ'),
    ('jamalpur', 'JAMALPUR'),
    ('jashore', 'JASHORE'),
    ('jhalokathi', 'JHALOKATHI'),
    ('jhenaidah', 'JHENAIDAH'),
    ('joypurhat', 'JOYPURHAT'),
    ('khagrachari', 'KHAGRACHARI'),
    ('kishoreganj', 'KISHOREGANJ'),
    ('khulna', 'KHULNA'),
    ('kurigram', 'KURIGRAM'),
    ('kushtia', 'KUSHTIA'),
    ('lakshmipur', 'LAKSHMIPUR'),
    ('lalmonirhat', 'LALMONIRHAT'),
    ('madaripur', 'MADARIPUR'),
    ('magura', 'MAGURA'),
    ('manikganj', 'MANIKGANJ'),
    ('meherpur', 'MEHERPUR'),
    ('moulvibazar', 'MOULVIBAZAR'),
    ('munshiganj', 'MUNSHIGANJ'),
    ('mymensingh', 'MYMENSINGH'),
    ('narail', 'NARAIL'),
    ('narayanganj', 'NARAYANGANJ'),
    ('narsingdi', 'NARSINGDI'),
    ('natore', 'NATORE'),
    ('netrokona', 'NETROKONA'),
    ('nilphamari', 'NILPHAMARI'),
    ('noakhali', 'NOAKHALI'),
    ('pabna', 'PABNA'),
    ('panchagarh', 'PANCHAGARH'),
    ('patuakhali', 'PATUAKHALI'),
    ('pirojpur', 'PIROJPUR'),
    ('rajbari', 'RAJBARI'),
    ('rajshahi', 'RAJSHAHI'),
    ('rangamati', 'RANGAMATI'),
    ('rangpur', 'RANGPUR'),
    ('satkhira', 'SATKHIRA'),
    ('shariatpur', 'SHARIATPUR'),
    ('sherpur', 'SHERPUR'),
    ('sirajganj', 'SIRAJGANJ'),
    ('sunamganj', 'SUNAMGANJ'),
    ('sylhet', 'SYLHET'),
    ('tangail', 'TANGAIL'),
    ('thakurgaon', 'THAKURGAON')
)



def user_dictory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True,length=10, max_length=20,prefix='cat',alphabet = 'abcdefgh12345')
    title = models.CharField(max_length=100,default="Food")
    image = models.ImageField(upload_to='catagorie' , default="catagori.jpg")
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' %(self.image.url))
    
    def __str__(self):
        return self.title
    
    
class Vendor(models.Model):
    vid = ShortUUIDField(unique=True,length=10, max_length=20,prefix='ven',alphabet = 'abcdefgh12345')
    
    title = models.CharField(max_length=100 ,default='vendor')
    image = models.ImageField(upload_to=user_dictory_path , default='vendor.jpg')
    description = RichTextField(null=True, blank=True, default="i am Amazing vendor.")
    
    address = models.CharField(max_length=100, default="123 london main street.")
    contact = models.CharField(max_length=100, default="+123 (456) 789")
    chat_resp_time = models.CharField(max_length=100, default='100')
    shipping_on_time = models.CharField(max_length=100,default="100")
    authentic_rating = models.CharField(max_length=100,default="100")
    days_return = models.CharField(max_length=100,default="100")
    warranty_preiods = models.CharField(max_length=100,default="100")
    
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name_plural = 'Vendors'
        
    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' %(self.image.url))
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    pid = ShortUUIDField(unique=True,length=10, max_length=20,alphabet = 'abcdefgh12345')
    
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    catagori = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL, null=True , related_name='product')
    
    title = models.CharField(max_length=100 , default="fresh pree")
    image = models.ImageField(upload_to=user_dictory_path , default='product.jpg')
    description = RichTextField(null=True, blank=True , default="this is the product.")
    
    price = models.DecimalField(max_digits=999999999 , decimal_places=2 , default="1.99")
    old_price = models.DecimalField(max_digits=999999999 , decimal_places=2 , default="2.99")
    specifications = RichTextField(null=True,blank=True)
    tags = TaggableManager(blank=True)
    
    product_status = models.CharField(choices=STATUS,max_length=10 , default="in_review")
    status = models.BooleanField(default=True)
    in_stoke = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    
    sku = ShortUUIDField(unique=True,length=4, max_length=10, prefix="sku", alphabet = '12345678')
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(null=True,blank=True)
    
    class Meta:
        verbose_name_plural = 'Products'
        
    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' %(self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price
    
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images",default="product.jpg")
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True , related_name='product')
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Products Images'
        

################### Cart , Order , OrderItems, Addresss ####################          
        
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"
    
    class Meta:
        verbose_name_plural = 'Cart Order'
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"

    def get_total_price(self):
        return self.product.price * self.quantity
    
    class Meta:
        verbose_name_plural = 'Cart Oreder Items'
        

class Order(models.Model):
    oid = ShortUUIDField(unique=True,length=10, max_length=20,alphabet = 'abcdefgh123456789')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(choices=MODE , default='cod', max_length=20)
    payment_status = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=200 , null=True , blank=True , default="P_IDxxxxx")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}" 

###############  payment model ###################

class BaylingAddress(models.Model):
    b_id = ShortUUIDField(unique=True,length=10,max_length=15 , alphabet = 'abcdefghij12345')
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    your_name= models.CharField(default="your name" , max_length=30)
    phone_number = models.CharField(max_length=15 , blank=True)
    email = models.EmailField(blank=True)
    division = models.CharField(max_length=25, choices=DIVISION , default='dhaka')
    district = models.CharField(max_length=30 , choices=DISTRICT , default='dhaka' )
    home_address = models.CharField(max_length=300 , default='N/A' )
    
    def __str__(self):
        return self.your_name
    
class PaymentRequest(models.Model):
    pr_id = ShortUUIDField(unique=True, length=10, max_length=15, alphabet='accdefghij12345')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    is_accept = models.BooleanField(default=False)
    your_name = models.CharField(default="your name", blank=True, max_length=30)
    phone_number = models.CharField(max_length=15, blank=True)
    transaction = models.CharField(max_length=100, blank=True, default='txid_xxx')
    payment_method = models.CharField(max_length=20, blank=True, default="") 
    tr_date = models.DateField(blank=True , null=True)
    
    def __str__(self):
        return self.your_name

    
##################     product review  ratting ##############################

class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='reviews')
    review = RichTextField()
    rating = models.IntegerField(choices=RATING , default=None)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Product Reviews'
    
    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    
    
class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Wishlists'
    
    def __str__(self):
        return self.product.title
    
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100 , null=True)
    status = models.BooleanField(default=False)
