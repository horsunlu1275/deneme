from django import forms


class PersonelForm(forms.Form):
    p_name = forms.CharField(label='Personelin Adı', max_length=20)
    p_surname = forms.CharField(label='Personelin Soyadı', max_length=20)
    rutbe = forms.CharField(label='Personelin Rütbesi', max_length=30)
    age = forms.IntegerField(label='Personelin Yaşı')
