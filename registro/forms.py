from django import forms


SEXO_CHOICE = (
				(0, '-----'),
				(1, 'Hombres'),
				(2, 'Mujeres')
	           )

ANO_CHOICE = (
				(2012, '2012'),
				(2013, '2013'),
				(2014, '2014'),
				(2015, '2015'),
				(2016, '2016'),
				(2017, '2017'),
	           )

class ChatelEdad(forms.Form):
	ano = forms.ChoiceField(choices=ANO_CHOICE)
	sexo = forms.ChoiceField(choices=SEXO_CHOICE)
	edad1 = forms.IntegerField(required=True)
	edad2 = forms.IntegerField(required=True) 