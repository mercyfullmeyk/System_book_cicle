from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta():
        model = Book
        fields = ('name', 'description', 'image')

    def clean_subject(self):
        name = self.cleaned_data['name']
        description = self.cleaned_data['description']
        image = self.cleaned_data['image']

        if name and description:
            return name, description, image
        else:
            raise forms.ValidationError(
                'Поле name и description обязательнs для заполнения!'
            )
