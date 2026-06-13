from django.db import models
import bcrypt

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=23)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"USER NAME: {self.first_name} {self.last_name} ---- ID: {self.id}"


    @property
    def username(self):
        return f"{self.first_name} {self.last_name}"


    # def get_user(self, id, email):
    #     users = User.objects.filter(first_name="Олесь").all()
    #     for user in users:
    #         user.first_name
    #     user = User.objects.filter(id=id)
    #     user = User.objects.filter(id=id).first()
    #     user = User.objects.get(id=id)

    @classmethod
    def get_user_by_id(cls, id):
        return cls.objects.get(id=id)

    def password_hash(self, password: str) -> str:
        salt = bcrypt.gensalt()
        password = password.encode("utf-8")
        password_hash = bcrypt.hashpw(password, salt)
        decod_password = password_hash.decode("utf-8")
        return decod_password

    def check_password(self, password: str) -> str:
        password = password.encode("utf-8")
        password_hash = self.password.encode("utf-8")
        return bcrypt.checkpw(password=password, hashed_password=password_hash)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )

    tags = models.ManyToManyField(
        'Tag',
        blank=True
    )

    is_featured = models.BooleanField(default=False)

    views = models.PositiveIntegerField(default=0)

    likes = models.PositiveIntegerField(default=0)

    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0, null=False)
    price = models.FloatField(default=0.0, null=False)
    is_active = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        product_active = "🚫"
        if self.is_active:
            product_active = "✅"

        return f"Product ID: {self.id} Name: {self.name} ACIVE: {product_active}"

    def save(self, *args, **kwargs):
        if self.stock == 0:
            self.is_active = False
        else:
            self.is_active = True
        super().save(*args, **kwargs)





