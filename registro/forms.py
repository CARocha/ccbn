from django import forms


SEXO_CHOICE = (
				(0, '-----'),
				(1, 'Hombres'),
				(2, 'Mujeres')
	           )

class ChatelEdad(forms.Form):
	sexo = forms.ChoiceField(choices=SEXO_CHOICE)
	edad1 = forms.IntegerField(required=True)
	edad2 = forms.IntegerField(required=True) 