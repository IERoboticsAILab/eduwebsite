from django.db import models
from django.db.models import Q

class IntroText(models.Model):
    text = models.TextField()
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    scholar_url = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cyphy_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.text

class SiteSettings(models.Model):
    title = models.CharField(('Site Title'), max_length=200, default='Eduardo Castello')
    subtitle = models.CharField(('Subtitle'), max_length=200, default='Postdoctoral research fellow at MIT')
    banner_image = models.ImageField(('Banner Image'), upload_to='banners/', blank=True, null=True)

    class Meta:
        verbose_name = ('Site Settings')
        verbose_name_plural = ('Site Settings')

    def __str__(self):
        return 'Site Settings'

    @classmethod
    def get_settings(cls):
        return cls.objects.first() or cls.objects.create()

class Keyword(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Publication(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=500)
    image = models.ImageField(upload_to='publications/', blank=True)
    publication_date = models.DateField()
    journal = models.CharField(max_length=200)
    doi = models.CharField(max_length=200, blank=True)
    archivelink = models.URLField(blank=True)
    abstract = models.TextField()
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    keywords = models.ManyToManyField(Keyword, blank=True, related_name='publications')

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    video_url = models.URLField(blank=True)
    date = models.DateField()
    github_link = models.URLField(blank=True)
    publications = models.ManyToManyField(Publication, blank=True, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='project_gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} - Image {self.order}"

class ExperienceDescription(models.Model):
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Experience Description"

    def save(self, *args, **kwargs):
        if not self.pk and ExperienceDescription.objects.exists():
            return ExperienceDescription.objects.first()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Experience Description"

class EducationItem(models.Model):
    title = models.CharField(max_length=200)
    date_range = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.institution}"

class WorkItem(models.Model):
    title = models.CharField(max_length=200)
    date_range = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.institution}"

class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField(help_text="Enter the YouTube embed URL (e.g., https://www.youtube.com/embed/VIDEO_ID)")
    date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    language = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class ResearchLine(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='research_lines/', blank=True)
    video_url = models.URLField(blank=True)
    date = models.DateField(blank=True, null=True)
    projects = models.ManyToManyField('Project', blank=True, related_name='research_lines')
    publications = models.ManyToManyField('Publication', blank=True, related_name='research_lines')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def all_publications(self):
        """
        Get all publications including those from related projects
        """
        return Publication.objects.filter(
            Q(research_lines=self) |  # Direct publications
            Q(projects__research_lines=self)  # Publications from related projects
        ).distinct()

class OpenPositions(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    instructions = models.TextField()
    contact_email = models.EmailField()
    deadline = models.TextField()

    class Meta:
        verbose_name_plural = "Open Positions"

    def __str__(self):
        return self.title
