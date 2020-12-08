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


class TraficLightForm(forms.Form):
    flux_destiny = forms.FloatField(min_value=0, max_value=1)