from django import forms
# from django.forms import Form, ModelForm

class FormProduct(forms.Form):
    name_class = "card-product-input"
    sub_price_class_name = "price" + " " + name_class
    name = forms.CharField(
        label="name",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            "type": "text",
            "placeholder": "Імя продукта",
            "class": name_class
        })
    )

    description = forms.CharField(
        label="description",
        widget=forms.TextInput(attrs={
            "type": "text",
            "placeholder": "Опис",
            "class": name_class
        })
    )

    stock = forms.IntegerField(
        label="stock",
        max_value=10000,
        min_value=1,
        widget=forms.TextInput(attrs={
            "placeholder": "Кількість на кладі",
            "class": name_class
        })
    )

    price = forms.FloatField(
        label="price",
        required=True,
        max_value=10000.0,
        min_value=1.0,
        widget=forms.TextInput(attrs={
            "type": "number",
            "placeholder": "Ціна",
            "class": f"{name_class} {sub_price_class_name}"
            # "class": sub_price_class_name
        })
    )




