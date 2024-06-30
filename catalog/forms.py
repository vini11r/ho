from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, VersionProduct


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_name(self):
        name = self.cleaned_data["name"]
        for word in self.forbidden_words:
            if word in name.lower():
                raise ValidationError("Нельзя использовать запрещенные слова")
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        for word in self.forbidden_words:
            if word in description.lower():
                raise ValidationError("Нельзя использовать запрещенные слова")
        return description


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = VersionProduct
        fields = "__all__"
