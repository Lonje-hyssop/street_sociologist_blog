from django.db import models
from django.conf import settings
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = MarkdownxField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    post_Image = models.ImageField(upload_to= "images/", blank=True, null=True)
    
    def formatted_markdown(self):
        """Convert Markdown content to HTML for display."""
        return markdownify(self.text)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
