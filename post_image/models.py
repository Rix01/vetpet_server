from django.db import models
from post.models import Post

class PostImage(models.Model):
    post_img_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    post_img_url = models.URLField(null=True)

    def __str__(self):
        return str(self.post_img_id)