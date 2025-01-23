from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta():
        model = Book
        fields = ('name', 'description', 'coins', 'image')

    def clean_subject(self):
        name = self.cleaned_data['name']
        description = self.cleaned_data['description']
        coins = self.cleaned_data['coins']
        image = self.cleaned_data['image']

        if name and description:
            return name, description, coins, image
        else:
            raise forms.ValidationError(
                'Поле name и description обязательно для заполнения!'
            )
