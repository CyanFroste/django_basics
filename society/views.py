from http import HTTPStatus
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import ValidationError


from society.forms import CreatePostForm, LoginForm, RegisterForm
from society.models import Post, PostLike


def index(request):
    if request.method == "GET":
        create_post_form = CreatePostForm()
        # TODO - PAGINATION
        posts = Post.objects.all()
        buffed_posts = []
        for post in posts:
            buffed_posts.append(
                {"data": post, "like_by_user": post.like_by_user(request.user)}
            )
        return render(
            request,
            "index.html",
            {"create_post_form": create_post_form, "posts": buffed_posts},
        )
    if request.method == "POST":
        create_post_form = CreatePostForm(request.POST)
        if create_post_form.is_valid() and request.user.is_authenticated:
            post = Post(
                user=request.user,
                title=create_post_form.cleaned_data["title"],
                content=create_post_form.cleaned_data["content"],
            )
            post.save()
            return redirect("/")
        return render(request, "index.html", {"create_post_form": create_post_form})


@login_required
def post_likes(req, post_id=None, like_id=None):
    # if req.method == "GET":
    #     if id is None:
    #         return HttpResponse(status=HTTPStatus.BAD_REQUEST)
    #     count = PostLike.objects.filter(post_id=post_id).count()
    #     return JsonResponse({"count": count})
    if req.method == "POST":
        is_liked_by_user = PostLike.objects.filter(
            post_id=post_id, user_id=req.user.id
        ).exists()
        if is_liked_by_user:
            return HttpResponse(status=HTTPStatus.CONFLICT)
        try:
            post = Post.objects.get(id=post_id)
        except:
            return HttpResponse(status=HTTPStatus.NOT_FOUND)
        like = PostLike(user=req.user, post=post)
        like.save()
        return JsonResponse({"id": like.id})
    if req.method == "DELETE":
        try:
            like = PostLike.objects.get(id=like_id)
            like.delete()
            return JsonResponse({"id": like.id})
        except:
            return HttpResponse(status=HTTPStatus.NOT_FOUND)


def register_user(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
            )
            login(request, user)
            return redirect("/")
        return render(request, "register.html", {"form": form})


def logout_user(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")


def login_user(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    if request.method == "POST":
        form = LoginForm(
            data=request.POST  # ANNOYING AF. INCONSISTENCY -> https://stackoverflow.com/questions/8421200/using-authenticationform-in-django
        )
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error("password", ValidationError("user doesn't exist"))
        return render(request, "login.html", {"form": form})
