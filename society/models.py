from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # likes = models.ManyToManyField(PostLike)

    def likes(self):
        return PostLike.objects.filter(post_id=self.id).count()

    def like_by_user(self, user):
        try:
            return PostLike.objects.get(post_id=self.id, user_id=user.id)
        except:
            return None


# many to many
class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
