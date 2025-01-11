from django.shortcuts import render, get_object_or_404
from django.views import generic 
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm #UserChangeForm
#PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

# PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm,PasswordChangingForm, ProfilePageForm, ListView, Homeview, Comment
from theblog.models import Profile, Post, Comment
from django import forms

class ProfilePageForm(forms.ModelForm):
		class Meta:
			model  = Profile
			fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url')

			widgets ={
					'bio': forms.TextInput(attrs={'class': 'form-control'}),
					#'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
					'website_url': forms.TextInput(attrs={'class': 'form-control'}),
					'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
					'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
			}



class SignUpForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailField)
	first_name = forms.CharField


class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	cats = Category.objects.all()
	ordering = ['-post_date']
	#ordering =['-id']

	def get_context_data(self,*args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context
	
def CategoryListView(request):	
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html',{'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
	#category_posts= Post.objects.filter(category=cats)
	cat_menu_list = Category.objects.all()
	category_posts = Post.objects.filter(category=cats.replace('-', ' '))
	return render(request, 'categories.html',{'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})

class CreateProfilePageView(CreateView):
		model = Profile
		form_class = ProfilePageForm
		template_name = "registration/create_user_profile_page.html"
		#fields = '__all__'
		
		def form_valid(self, form):
			form.instance.user = self.request.user
			return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
	model = Profile
	template_name = 'registration/edit_profile_page.html'
	fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url']
	success_url = reverse_lazy('home')

class ShowProfilePageView(DetailView):
		model = Profile
		template_name = 'registration/user_profile.html'


		def get_context_data(self,*args,** kwargs):
			# users = Profile.objects.all()
			context = super(ShowProfilePageView, self).get_context_data(self,*args,** kwargs)
			page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
			context['page_user'] = page_user
			return context


class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	#form_class = PasswordChangeForm
	success_url = reverse_lazy('password_success')
# success_url = reverse_lasy('home')
def password_success(request):
	return render(request, 'registration/password_success.html',{})

class UserRegisterView(generic.CreateView):
	form_class= SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

	
class UserEditView(generic.UpdateView):
	form_class= EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user