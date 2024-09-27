from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('beauty', 'Beauty & Personal Care'),
        ('home_kitchen', 'Home & Kitchen'),
        ('sports_outdoors', 'Sports & Outdoors'),
        ('books_stationery', 'Books & Stationery'),
        ('toys_baby', 'Toys & Baby Products'),
        ('health_wellness', 'Health & Wellness'),
        ('automotive', 'Automotive'),
        ('groceries', 'Groceries & Gourmet Food'),
        ('jewelry_watches', 'Jewelry & Watches'),
        ('pet_supplies', 'Pet Supplies'),
    ]

    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
        ('white', 'White'),
        ('yellow', 'Yellow'),
        ('pink', 'Pink'),
        ('gray', 'Gray'),
        ('brown', 'Brown'),
        ('purple', 'Purple'),
        ('orange', 'Orange'),
    ]

    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
    ]

    name = models.CharField(max_length=255,blank=True,null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    description = models.TextField()
    material = models.CharField(max_length=100, blank=True, null=True)
    product_image = models.ImageField(upload_to='products/',blank=True,null=True)
    stock_quantity = models.PositiveIntegerField(default=0,blank=True,null=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, blank=True, null=True)
    size = models.CharField(max_length=5, choices=SIZE_CHOICES, blank=True, null=True)
    warranty = models.CharField(max_length=255, blank=True, null=True)  # Warranty period and coverage
    dimensions = models.CharField(max_length=255, blank=True, null=True)  # Product dimensions (size & weight)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Product weight in kg or lbs
    tags = models.CharField(max_length=255, blank=True, null=True)  # SEO-friendly tags or keywords
    def __str__(self):
      return f"{self.name} {self.category} {self.price} {self.description} {self.stock_quantity} {self.size}"


  