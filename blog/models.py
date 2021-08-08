from django.db import models

class PostCategory(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=50)
	category = models.ForeignKey(PostCategory, null=True, blank=True, on_delete=models.DO_NOTHING)
	published = models.BooleanField(default=False)
	text = models.TextField(blank=True)
	creation_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	STATUS_VISIBLE = 'visible'
	STATUS_HIDDEN = 'hidden'
	STATUS_MODERATED = 'moderated'

	STATUS_CHOICES = (
        (STATUS_VISIBLE, 'visible'),
        (STATUS_HIDDEN, 'hidden'),
        (STATUS_MODERATED, 'moderated'),
	)

	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	author = models.CharField(max_length=50)
	status = models.CharField(max_length=20, default=STATUS_VISIBLE, choices=STATUS_CHOICES)
	moderation_text = models.CharField(max_length=200, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{} - {} - (status={})'.format(self.author, self.text[:20], self.status)