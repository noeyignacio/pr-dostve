from django.db import models
from django.core.validators import RegexValidator


class Visitor(models.Model):

    GENDER_OPTION = {
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
        ("PREFER NOT TO SAY", "PREFER NOT TO SAY"),
        ("OTHERS", "OTHERS"),
    }

    CATEGORY_OPTION = {
        ("SME", "SME"),
        ("Academe", "Academe"),
        ("LGU", "LGU"),
        ("Student", "Student"),
        ("General Public", "General Public"),
        ("PWD", "PWD"),
        ("RNV", "RNV"),
        ("JCM", "JCM"),
    }

    name = models.CharField(
        default="Anonymous",
        max_length=50,
    )
    province = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
    )
    gender = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        choices=GENDER_OPTION,
    )
    institution = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )
    category = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        choices=CATEGORY_OPTION,
    )

    date_create = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name + " - " + self.category


class Survey(models.Model):

    name = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )
    phone_regex = RegexValidator(regex=r"^(09|\+639)\d{9}$")
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=12,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        max_length=250,
        null=False,
        blank=False,
    )
    province = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )
    question = models.TextField(
        max_length=500,
        null=False,
        blank=False,
    )

    date_create = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name + " - " + self.phone_number + " - " + self.email
