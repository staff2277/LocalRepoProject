from django import forms

class contactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.Textarea()

    def sendMessage(self):
        return f"\nName = {self.cleaned_data ["name"]} \n Email = {self.cleaned_data ["email"]} \n Message = {self.cleaned_data ["message"]} \n"