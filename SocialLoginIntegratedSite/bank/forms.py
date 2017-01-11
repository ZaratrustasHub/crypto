from django import forms
from bank.models import TransactionHistory, customer
from captcha.fields import CaptchaField



class TransactionForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter your full name.")
    accnumberfrom = forms.CharField(max_length=26, help_text="Please enter your acc number")
    accnumberto = forms.CharField(max_length=26, help_text="Please enter recipent acc number.")
    cash = forms.FloatField(help_text="Please enter value of transaction")  

    captcha = CaptchaField()

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = TransactionHistory
        fields = ('name', 'accnumberfrom', 'accnumberto', 'cash',)


class CustomerForm(forms.ModelForm):
     
    name = forms.CharField(max_length=128, help_text="Please enter your full name")
    accnumber = forms.CharField(max_length=26, help_text="Please enter your unique account number")
    saldo = forms.FloatField(required=True)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = customer

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('transactions',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

