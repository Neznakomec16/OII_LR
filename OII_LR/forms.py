from django import forms


class RequestForm(forms.Form):
    experience = forms.ChoiceField(widget=forms.Select, choices=[('small', 'Небольшой'), ('middle', 'Средний'), ('big', 'Большой')])
    age = forms.ChoiceField(widget=forms.Select, choices=[('small', 'Молодой'), ('middle', 'Средний'), ('big', 'Старше среднего')])

    experience.widget.attrs.update({'class': 'form-select form-select-lg mb-3'})
    age.widget.attrs.update({'class': 'form-select form-select-lg mb-3'})


class CreatePersonForm(forms.Form):
    experience = forms.FloatField(max_value=1488, min_value=0)
    age = forms.FloatField(max_value=1488, min_value=0)

    experience.widget.attrs.update({'class': 'form-select form-select-lg mb-3'})
    age.widget.attrs.update({'class': 'form-select form-select-lg mb-3'})


class ReactorForm(forms.Form):
    Temperature = forms.FloatField(min_value=-1, max_value=150, initial=85)
    Consumption = forms.FloatField(min_value=-1, max_value=8, initial=3.5)
    Pressure = forms.FloatField(min_value=-1, max_value=100, initial=-1)
