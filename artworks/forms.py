from django import forms
from django.forms import ModelForm
from artworks.models import Checkin, CheckinImage, CheckinDamage


class CheckinForm(ModelForm):
    condition = forms.ChoiceField(
      widget=forms.RadioSelect,
      choices=[
        ('G', 'Good Condition'),
        ('D', 'Damaged')],
      label='What\'s the current condition of the artwork?'
    )
    damage = forms.ModelMultipleChoiceField(
      widget=forms.CheckboxSelectMultiple,
      queryset=CheckinDamage.objects.all(),
      required=True,
      label=''
    )
    damaged_description = forms.CharField(
      widget=forms.Textarea,
      required=False,
      label='What kind of damage do you see?'
    )

    class Meta:
        model = Checkin
        fields = ('condition', 'damage', 'damaged_description')


class CheckinImageForm(ModelForm):
    class Meta:
        model = CheckinImage
        fields = ('image', )
