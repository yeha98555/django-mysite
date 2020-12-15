from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance, filename):
    return 'course/course_{0}/{1}'.format(instance.title, filename)

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_user')
    title = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    overview = models.TextField()
    video = models.FileField(blank=True, upload_to='videos/')
    attach = models.FileField(blank=True, upload_to=user_directory_path)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
    