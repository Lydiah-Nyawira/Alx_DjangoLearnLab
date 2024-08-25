from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']  # List fields you want in the form

    # Optional: Add custom validation or form logic here
    def clean_publication_year(self):
        publication_year = self.cleaned_data.get('publication_year')
        if publication_year < 0:
            raise forms.ValidationError('Publication year cannot be negative.')
        return publication_year