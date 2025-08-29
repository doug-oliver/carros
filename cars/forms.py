from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is not None and value < 0:
            raise forms.ValidationError("O valor do carro não pode ser negativo.")
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year and factory_year < 1975:  # O primeiro carro foi inventado em 1886
            raise forms.ValidationError("O ano de fabricação não pode ser anterior a 1975.")    
        elif factory_year and factory_year > 2025:  # Considerando que estamos em 2023
            raise forms.ValidationError("O ano de fabricação não pode ser posterior a 2025.")
        return factory_year