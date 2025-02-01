from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST

from .forms import TodoForm
from .models import Todo


@login_required
def index(request):
    context = {"todos": Todo.objects.filter(user=request.user), "form": TodoForm()}
    return render(request, "todo/index.html", context)


@login_required
@require_POST
def submit_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()

        messages.success(request, "Todo added!")
        # return HTMX partial
        context = {"todo": todo}
        return render(request, "todo/partials/todo_item.html", context)
    return render(request, "")


@login_required
@require_POST
def complete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.is_completed = True
    todo.save()
    messages.info(request, "Todo completed!")
    context = {"todo": todo}
    return render(request, "todo/partials/todo_item.html", context)


@login_required
@require_http_methods(["DELETE"])
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    response = HttpResponse(status=204)
    response["HX-Trigger"] = "delete-todo"
    return response
