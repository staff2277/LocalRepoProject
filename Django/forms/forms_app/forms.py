from django import forms # type: ignore

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)

    def sendEmail(self):
        print(f"Sending email from {self.cleaned_data ["email"]} with {self.cleaned_data ["message"]}")