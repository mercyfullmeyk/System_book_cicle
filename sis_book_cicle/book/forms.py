from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta():
        model = Book
        fields = ('name', 'description', 'coins', 'image')

    def clean_subject(self):
        name = self.cleaned_data['Название книги']
        description = self.cleaned_data['Описание книги']
        coins = self.cleaned_data['Литкоины']
        image = self.cleaned_data['Изображение']

        if name and description:
            return name, description, coins, image
        else:
            raise forms.ValidationError(
                'Поле Название книги и Описание книги обязательнs для заполнения!'
            )
