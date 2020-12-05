from django.forms import ModelForm
from django import forms

# Models
from .models import Visitor, Survey


class VisitorAttendanceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["gender"].widget.attrs.update({"class": "form-control"})
        self.fields["category"].widget.attrs.update({"class": "form-control"})

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
    }

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "required": False,
            }
        )
    )
    province = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "pattern": "[A-Za-z ]+",
                "required": True,
                "title": "Invalid Province.",
            }
        )
    )
    age = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "required": True,
            }
        )
    )
    gender = forms.ChoiceField(
        choices=GENDER_OPTION,
    )
    institution = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "required": True,
            }
        )
    )
    category = forms.ChoiceField(
        choices=CATEGORY_OPTION,
    )

    class Meta:
        model = Visitor
        fields = [
            "province",
            "age",
            "gender",
            "institution",
            "category",
        ]


class SurveyForm(ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "required": True,
            }
        )
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "required": True,
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "required": True,
            }
        )
    )
    province = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "required": True,
            }
        )
    )
    question = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "required": True,
                "maxlength": 100,
            }
        )
    )

    class Meta:
        model = Survey
        fields = [
            "name",
            "phone_number",
            "email",
            "province",
            "question",
        ]
