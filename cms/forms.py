from django.forms import ModelForm
from cms.models import Paper, Report


class PaperForm(ModelForm):
    class Meta:
        model = Paper
        fields = ('title','authors','references', 'pages','year','URL','abstract','reading','note',)

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ('reporter','grade','date','motivations','contributions','questions', )

'''
class ToggleForm(ModelForm):
    class Meta:
        model = Paper
        fields = ('recommended',)
'''
