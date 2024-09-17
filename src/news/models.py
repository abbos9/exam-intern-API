from django.db import models
from users.models import User
from general_dj.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.TextField(max_length=65)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    file = models.FileField(upload_to='posts/files', null=True, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


class PostImage(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Post Image"
        verbose_name_plural = "Post Images"
    def __str__(self):
        return self.post.title



class PostComment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        verbose_name = "Post Comment"
        verbose_name_plural = "Post Comments"


    def __str__(self):
        return f'{self.user} on {self.comment}'


class PostLike(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')
        verbose_name = "Post Like"
        verbose_name_plural = "Post Likes"

    
    def __str__(self):
        return self.user.username


class PostSave(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')
        verbose_name = "Post Save"
        verbose_name_plural = "Post Saves"


    def __str__(self):
        return self.user