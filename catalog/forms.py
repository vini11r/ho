from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        fields = "__all__"

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
