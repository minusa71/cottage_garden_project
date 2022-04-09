from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.deconstruct import deconstructible
from django.contrib.auth import get_user_model
from cloudinary import models as cloudinary_models



from Cottage_garden_project.accounts.models import Profile

FIRST_NAME_MAX_LEN = 10
FIRST_NAME_MIN_LEN = 2
LAST_NAME_MAX_LEN = 20
IMAGE_MAX_SIZE_VALIDATOR = 5
IMAGE_UPLOAD_DIR = 'gardens/'
PLANT_PROT_NAME_MAX_LEN=10

User_Model = get_user_model()


@deconstructible
class MaxFileSizeInMBValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_message(self):
        return f'Max file size is {self.max_size:.2f} MB '


# class Profiles(models.Model):
#     NAME_MAX_LENGTH = 10
#     first_name = models.CharField(
#         max_length=NAME_MAX_LENGTH,
#     )
#
#     last_name = models.CharField(
#         max_length=NAME_MAX_LENGTH,
#     )
#
#     email = models.EmailField(
#         null=True,
#         blank=True,
#     )


class Garden(models.Model):

    PERENNIAL_PLANTS = 'Perennial plants'
    ANNUAL_PLANTS = 'Annual plants'
    HOME_PLANTS = 'Home plants'
    GARDEN_NAME_MAX_LEN = 20
    ADDRESS_MAX_LEN=40

    TYPES = [(x,x) for x in (PERENNIAL_PLANTS, ANNUAL_PLANTS, HOME_PLANTS)]

    name = models.CharField(
        max_length=GARDEN_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
        )
    )

    type = models.CharField(
        max_length=max(len(x) for (x,_) in TYPES),
        choices=TYPES,

    )

    address = models.CharField(
        max_length=ADDRESS_MAX_LEN,
    )

    image = cloudinary_models.CloudinaryField(
        'image',
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        User_Model,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('user', 'name')


class PlantProtection(models.Model):
    PLANT_DESC_MAX_LEN=30
    product_name = models.CharField(
        max_length=PLANT_PROT_NAME_MAX_LEN,
    )
    description = models.CharField(
        max_length=PLANT_DESC_MAX_LEN,
    )
    price = models.FloatField()

    def __str__(self):
        return self.product_name


class Plant(models.Model):
    FRUIT_TREE = 'Fruit tree'
    EVERGREEN_TREE = 'Evergreen tree'
    BUSH = 'Bush'
    CLIMBING_PLANT = 'Climbing plants'
    VEGETABLE = 'Vegetable'
    FLOWER = 'Flower'
    OTHER = 'Other'
    TYPES = [(x,x) for x in (FRUIT_TREE, EVERGREEN_TREE, BUSH, CLIMBING_PLANT, VEGETABLE, FLOWER, OTHER)]
    PLANT_NAME_MAX_LEN=15
    TYPE_NAME_MAX_LEN=15
    SORT_NAME_MAX_LEN=15
    PLANT_NAME_MIN_LEN=2
    TYPE_NAME_MIN_LEN=2
    SORT_NAME_MIN_LEN=2

    name = models.CharField(
        max_length=PLANT_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(PLANT_NAME_MIN_LEN),
        )
    )

    type = models.CharField(
        max_length=max(len(x) for (x,_) in TYPES),
        choices=TYPES,
        validators=(
            MinLengthValidator(TYPE_NAME_MIN_LEN),
        )
    )

    sort = models.CharField(
        max_length=SORT_NAME_MAX_LEN,
        null=True,
        blank=True,
        validators=(
            MinLengthValidator(SORT_NAME_MIN_LEN),

        )
    )

    image = cloudinary_models.CloudinaryField(
        'image',
        null=True,
        blank=True,
    )

    year = models.DateField(

    )

    plant_protections = models.CharField(
        max_length=PLANT_PROT_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    harvest_quantity = models.FloatField(

    )

    # plant_protection = models.ManyToManyField(
    #     PlantProtection,
    # )

    garden = models.ForeignKey(
        Garden,
        on_delete=models.CASCADE,
    )


# class PlantPhoto(models.Model):
#     photo = cloudinary_models.CloudinaryField('image')
#
#     description = models.TextField(
#         null=True,
#         blank=True,
#     )
#
#     publication_date = models.DateTimeField(
#         auto_now_add=True,
#     )
#
#     likes = models.IntegerField(
#         default=0,
#     )
#
#     tagged_pets = models.ManyToManyField(
#         Plant,
#         # validate at least 1 pet
#     )
#
#     user = models.ForeignKey(
#         UserModel,
#         on_delete=models.CASCADE,
#     )




class UseFullTips(models.Model):
    PLANT_NAME_TEXT_MAX_LEN=50
    plant_name = models.CharField(
        max_length=PLANT_PROT_NAME_MAX_LEN,
    )
    text_field = models.CharField(
        max_length=PLANT_NAME_TEXT_MAX_LEN,
    )

    plants = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE,
    )


