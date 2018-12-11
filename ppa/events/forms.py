from django import forms
from .models import Event, Region
from django.contrib.admin.widgets import AdminDateWidget


class NewEventForm(forms.ModelForm):
    #test= forms.DateTimeField()
    name = forms.CharField(widget=forms.Textarea(), max_length=200)
    region = forms.ModelChoiceField(queryset=Region.objects.all())
    event_name = forms.CharField(widget=forms.Textarea(), max_length=200)
    location = forms.CharField(widget=forms.Textarea(), max_length=200)
    #event_date = forms.DateTimeField(widget=forms.DateTimeInput(format=['%d/%m/%Y']),help_text='%d/%m/%Y')  #TODO: maybe cits widgets
    event_date = forms.DateTimeField(widget=forms.DateTimeInput(format=['%d/%m/%Y']),
                                     help_text='%d/%m/%Y')  # TODO: maybe cits widgets
    #start_time = forms.TimeField(widget=forms.TimeInput)
    #end_time = forms.TimeField(widget=forms.TimeInput)
    description = forms.CharField(widget=forms.Textarea(), max_length=200)
    guest_count= forms.IntegerField()
    #host_count = forms.IntegerField(widget=forms.NumberInput)
    dangerous_equipment = forms.CharField(widget=forms.Textarea(), max_length=200)

    class Meta:
        model = Event
        fields = ['name','region', 'event_name', 'location','event_date','description',
                  'guest_count','dangerous_equipment']

        # name = models.CharField(max_length=200)
        # event_name = models.CharField(max_length=200)
        # event_date = models.DateTimeField('date published')
        # location = models.CharField(max_length=200)
        # start_time = models.TimeField
        # end_time = models.TimeField
        # event_desr = models.CharField(max_length=200)
        # event_guest_count = models.IntegerField
        # event_host_count = models.IntegerField
        # event_dangerous_equipment = models.CharField(max_length=200)
        # created_date = models.DateTimeField(default=timezone.now)
        # region = models.ForeignKey(Region, related_name='region', on_delete=models.CASCADE)
        # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)