import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from django.contrib import messages
from django.views.generic import (
    CreateView, 
    UpdateView, 
    DetailView, 
    TemplateView, 
    View, 
    ListView
)
from django.urls import reverse
from django.template.loader import render_to_string
from django.db.models import Q

from registrar.models import (
    RequirementsModel,
    RequirementsTransfereeModel,
    CourseModel
)
from registrar.forms import (
    RequirementsForm,
    RequirementsTransfereeForm,
    CourseForm
) 

""" Requirements Views """
class RequirementsListView(TemplateView):
    
    template_name = 'stud_requirements/student_requirements_list.html'
            
    def get_context_data(self, **kwargs):
        context = super(RequirementsListView, self).get_context_data(**kwargs)
        context['requirements_list'] = RequirementsModel.objects.all()
        context['requirements_transferee_list'] = RequirementsTransfereeModel.objects.all()
        return context
''' --------------------------------REQUIREMENTS TRANSFEREE  -------------------------------------------------------- '''
class RrequirementsTransCreateView(CreateView):
    model = RequirementsTransfereeModel
    form_class = RequirementsTransfereeForm
    template_name = 'stud_requirements/student_requirements_list.html'
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            requirements_trans_obj = form.save(commit=False)
            requirements_trans_obj.save()
            
            return self.form_valid(form)
        return self.form_invalid(form)
    
    def form_valid(self, form):
        requirements_obj = form.save(commit=False)

        current_site = get_current_site(self.request)

        if self.request.is_ajax():
            return JsonResponse(
                {
                    'error': False,
                }
            )

        if self.request.POST.get('savenewform'):
            return redirect('registrar:add_requirements')
        return redirect('registrar:requirements_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(
                {
                    'error': True,
                    'requirements_trans_errors': form.errors
                }
            )
        return self.render_to_response(
            self.get_context_data(form=form)
        )

    def get_context_data(self, **kwargs):
        context = super(RrequirementsTransCreateView,self).get_context_data(**kwargs)
        context['requirements_trans_form'] = context['form']
        return context
    
class RequirementsTransUpdateView(UpdateView):
    models = RequirementsTransfereeModel
    form_class = RequirementsTransfereeForm
    template_name = 'stud_requirements/create_requirements_trans.html'
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            requirements_trans_obj = form.save(commit=False)
            requirements_trans_obj.save()

            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        requirements_trans_obj = form.save(commit=False)
        current_site = get_current_site(self.request)

        if self.request.is_ajax():
            return JsonResponse(
                {
                    'error': False,
                }
            )
        return redirect('#')
    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(
                {
                    'error': True
                }
            )

        return self.render_to_response(
            self.get_context_data(form=form)
        )

    def get_context_data(self, **kwargs):
        context = super(RequirementsUpdateView,
                        self).get_context_data(**kwargs)
        context['requirements_trans_obj'] = self.object
        context['requirements_trans_form'] = context['form']
        return context
    
    
    
class RequirementsTransDetailView(DetailView):
    model = RequirementsTransfereeModel
    context_object_name = 'requirements_trans_record'
    template_name = 'stud_requirements/trans_detail.html'
    queryset = RequirementsTransfereeModel.objects.all()
    
    
class RequirementsDetailView(DetailView):
    model = RequirementsModel
    context_object_name = 'requirements_record'
    template_name = 'requirements/requirements_detail.html'
    queryset = RequirementsModel.objects.all()



''' -------------------------- REQUIREMENTS ------------------------------------------------------------------- '''
class RequirementsCreateView(CreateView):
    model = RequirementsModel
    form_class = RequirementsForm
    template_name = 'stud_requirements/create_student_requirements.html'
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            requirements_obj = form.save(commit=False)
            requirements_obj.save()
            
            return self.form_valid(form)
        return self.form_invalid(form)
    
    
    def form_valid(self, form):
        requirements_obj = form.save(commit=False)
        
        current_site = get_current_site(self.request)
        
        if self.request.is_ajax():
            return JsonResponse(
                {
                    'error': False,
                }
            )
        
        if self.request.POST.get('savenewform'):
            return redirect('registrar:add_requirements')
        return redirect('registrar:requirements_list')
    
    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(
                {
                    'error': True,
                    'requirements_errors': form.errors
                }
            )
        return self.render_to_response(
            self.get_context_data(form=form)
        )
    
    def get_context_data(self, **kwargs):
        context = super(RequirementsCreateView, self).get_context_data(**kwargs)
        context['requirements_form'] = context['form']
        
        return context
    
    

class RequirementsDetailView(DetailView):
    model = RequirementsModel
    context_object_name = 'requirements_record'
    template_name = 'requirements/requirements_detail.html'
    
    def get_queryset(self):
        queryset = self.models.all()
        queryset = super(RequirementsDetailView, self).get_queryset()
        return queryset.select_related('requirements_name')
    
    
    def get_context_data(self, **kwargs):
        context = super(RequirementsDetailView, self).get_context_data(**kwargs)
        context['requirements_record'] = self.context_object_name
        
        return context
    
    

class RequirementsUpdateView(UpdateView):
    model = RequirementsModel
    form_class = RequirementsForm
    template_name = 'requirements/create_requirements.html'
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            requirements_obj = form.save(commit=False)
            requirements_obj.save()
            
            return self.form_valid(form)
        return self.form_invalid(form)
    
    
    
    def form_valid(self, form):
        requirements_obj = form.save(commit=False)
        current_site = get_current_site(self.request)
        
        if self.request.is_ajax():
            return JsonResponse(
                {
                    'error':False,
                }
            )
    
    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(
                {
                    'error':True
                }
            )

        return self.render_to_response(
            self.get_context_data(form=form)
        )
        
    def get_context_data(self, **kwargs):
        context = super(RequirementsUpdateView, self).get_context_data(**kwargs)
        context['requirements_obj'] = self.object
        context['requirements_form'] = context['form']
        
        return context
        
        
""" Available Course Views """

class CourseListView(ListView):
    model = CourseModel
    context_object_name = 'course_obj_list'
    template_name = 'available_course/course_list.html'
    
    def get_queryset(self):
        queryset = self.model.objects.all()
        
        request_post = self.request.POST
        if request_post:
            if request_post.GET('course_name'):
                queryset = queryset.filter(
                    course_name__icontains=request.post.get('course_name')
                )
        
        return queryset.distinct()
    
    
    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['course_obj_list'] = self.get_queryset()
        context['per_page'] = self.request.POST.get('per_page')
        
        search = False
        if(
            self.request.POST.get('course_name')
        ):
            search = True
        context['search'] = search
        return context
    
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
    


class CourseCreateView(CreateView):
    model = CourseModel
    form_class = CourseForm
    template_name = 'available_course/create_course.html'
    success_url = '/registrar/create/course/'
    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     form = self.get_form()
    #     if form.is_valid():
    #         course_obj = form.save(commit=False)
    #         course_obj.save()
            
    #         return self.form_valid(form)
    #     return self.form_invalid(form)
    
    # def form_valid(self, form):
    #     course_obj = form.save(commit=False)
    #     current_site = get_current_site(self.request)
        
    #     if self.request.is_ajax():
    #         return JsonResponse(
    #             {
    #                 'error': False,
    #             }
    #         )
        
    #     if self.request.POST.get('savenewform'):
    #         return redirect('registrar:add_requirements')
    #     return redirect('registrar:course_list')
    

    # def form_invalid(self, form):
    #     if self.request.is_ajax():
    #         return JsonResponse(
    #             {
    #                 'error':True,
    #                 'course_errors': form.errors
    #             }
    #         )
    
    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['course_form'] = context['form']
        
        return context
    
    

class CourseDetailView(DetailView):
    model = CourseForm
    context_object_name = 'course_record'
    template_name = 'course/course_detail.html'
    
    def get_queryset(self):
        queryset = super(CourseDetailView, self).get_queryset()
        return queryset.select_related('course_name')
    
    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['course_record'] = self.object 
        
        return context
    

class CourseUpdateView(UpdateView):
    model = CourseModel
    form_class = CourseForm
    template_name = 'course/create_course.html'
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            course_obj = form.save(commit=False)
            course_obj.save()
            
            return self.form_valid(form)
        return self.form_invalid(form)
    
    
    
    def form_valid(self, form):
        course_obj = form.save(commit=False)
        current_site = get_current_site(self.request)
        
        if self.request.is_ajax():
            return JsonResponse(
                {
                    'error': False,
                }
            )
        return redirect('registrar:course_list')
    
    
    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(
                {
                    'error':True,
                    'course_errors': form.errors
                }
            )
        
        return self.render_to_response(
            self.get_context_data(form=form)
        )
    
    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['course_obj'] = self.object 
        context['course_form'] = context['form']
    
        return context
    
    
    
