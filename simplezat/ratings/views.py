from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView


class RatingView(TemplateView):
    template = 'ratings.html'

    def get(self, request):
        return render(request, self.template)


class CommentView(TemplateView):
    template = 'comments.html'

    def get(self, request, rating):
        return render(request, self.template, context={'rating': rating})

    def post(self, request, rating):
        return redirect(reverse('thanks'))


class ThankView(TemplateView):
    template = 'thanks.html'

    def get(self, request):
        return render(request, self.template)
