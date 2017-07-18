from django.forms import ModelForm
from artworks.models import Checkin, CheckinImage


class CheckinForm(ModelForm):
    class Meta:
        model = Checkin
        fields = ('condition', 'damaged', 'damaged_description')


class CheckinImageForm(ModelForm):
    class Meta:
        model = CheckinImage
        fields = ('image', )
