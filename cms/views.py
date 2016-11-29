from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView

from cms.models import Paper, Report
from cms.forms import PaperForm, ReportForm
import datetime


def gakunen_subtraction(today,prev):
    if today.month < 4:
        today_year = today.year - 1
    else:
        today_year = today.year
    if prev.month < 4:
        prev_year = prev.year - 1
    else:
        prev_year = prev.year
    return today_year - prev_year
    

def paper_list(request):
    url = request.build_absolute_uri()
    if '?' in url:
        params_list = [x.split('=') for x in url.split('?')[-1].split('&')]
    else:
        params_list = []
    params = {}
    for param in params_list:
        params[param[0]]=param[1]
    if "sort_by" in params:
        sort_by=params['sort_by']
    else:
        sort_by=None
    if 'order' in params:
        order = params['order']
    else:
        order = None
    if sort_by == 'num_of_pages':
        papers = Paper.objects.all().order_by("id")
    else:
        if order == "descending":
            papers = Paper.objects.all().order_by("-"+sort_by)
        elif order == "ascending":
            papers = Paper.objects.all().order_by(sort_by)
        else:
            papers = Paper.objects.all().order_by('id')
    if 'num_of_pages' == sort_by:
        for i,paper in enumerate(papers):
            try:
                page_idx = [int(x) for x in paper.pages.split('-')]
            except ValueError:
                pass
            if len(page_idx)==2:
                page_start = page_idx[0]
                page_end = page_idx[1]
                paper.num_of_pages = page_end - page_start + 1
            else:
                paper.num_of_pages=-1
        if order == 'descending' and not paper.num_of_pages==-1:
            papers = sorted([p for p in papers],key = lambda x:x.num_of_pages)
        elif not paper.num_of_pages==-1:
            papers =sorted([p for p in papers], key = lambda x:x.num_of_pages, reverse=True)
    for paper in papers:
        paper.color = '#FFFFFF'
        reports = paper.reports.all().order_by('id')
        paper.num_of_reports = len(reports)
        for report in reports:
            today = datetime.datetime.today()
            tdatetime = datetime.datetime.strptime(report.date, "%Y-%m-%d")
            if gakunen_subtraction(today,tdatetime) <= 3:
                paper.color="#FFBB69"
        if (not paper.reading=="") and paper.color !="#FFBB69":
            paper.color = '#FFFFCC'
        if not paper.note == '': #noteに文字列が存在する場合
            paper.color = "D3EDFB" #行を水色に設定
        try:
            page_idx = [int(x) for x in paper.pages.split("-")]
        except ValueError:
            page_idx = []
        if len(page_idx)==2:
            page_start = page_idx[0]
            page_end = page_idx[1]
            paper.num_of_pages = page_end - page_start + 1
        else:
            paper.num_of_pages=-1
    return render(request,
                  'cms/paper_list.html',
                  {'papers':papers})


def paper_edit(request, paper_id=None):
    if paper_id:
        paper = get_object_or_404(Paper, pk=paper_id)
    else:
        paper = Paper()

    if request.method == 'POST':
        form = PaperForm(request.POST, instance=paper)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.save()
            return redirect('cms:paper_list')
    else:
        form = PaperForm(instance=paper)
    return render(request, 'cms/paper_edit.html', dict(form=form, paper_id=paper_id))


def admin_message(request, paper_id=None):
    papers = Paper.objects.all().order_by('id')
    return render(request,
                  'cms/admin_message.html',
                  {'papers':papers})

def paper_del(request, paper_id):
    paper = get_object_or_404(Paper, pk=paper_id)
    paper.delete()
    return redirect('cms:paper_list')



class ReportList(ListView):
    context_object_name = 'reports'
    template_name = 'cms/reports_list.html'
    paginate_by = 6
    def get(self, request, *args, **kwargs):
        paper = get_object_or_404(Paper, pk = kwargs['paper_id'])
        reports = paper.reports.all().order_by('id')
        self.object_list = reports

        context = self.get_context_data(object_list=self.object_list, paper=paper)
        return self.render_to_response(context)


def report_edit(request, paper_id, report_id=None):
    paper = get_object_or_404(Paper, pk=paper_id)
    if report_id:
        report = get_object_or_404(Report, pk=report_id)
    else:
        report = Report()

    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            report = form.save(commit=False)
            report.paper = paper
            report.save()
            return redirect('cms:report_list', paper_id=paper_id)
    else:
        form = ReportForm(instance=report)

    return render(request,
                  'cms/report_edit.html',
                  dict(form=form, paper_id=paper_id, report_id=report_id))

def report_del(request, paper_id, report_id):
    """感想の削除"""
    report = get_object_or_404(Report, pk=report_id)
    report.delete()
    return redirect('cms:report_list', paper_id=paper_id)
