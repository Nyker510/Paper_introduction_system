from django.forms import ModelForm
from cms.models import Paper, Report
from datetimewidget.widgets import DateWidget

class PaperForm(ModelForm):
    class Meta:
        model = Paper
        fields = ('title', 'authors', 'references', 'pages',
                  'year', 'URL', 'abstract', 'reading', 'note',)


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ('reporter', 'grade', 'date', 'motivations',
                  'contributions', 'questions', )
        widgets = {
            'date': DateWidget(usel10n=True)
        }


'''
class ToggleForm(ModelForm):
    class Meta:
        model = Paper
        fields = ('recommended',)
'''
