from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.timezone import now
from django.utils.text import slugify
from django.utils import timezone
from languages.fields import LanguageField
from django.urls import reverse
#utils
from choices import SKILL_LEVEL, RATING_CHOICES

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        #ordering = ('category_name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
            return self.name

class Link(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    class Meta:
        #ordering = ('category_name',)
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
            return self.name

class Instructor(models.Model):
    name = models.CharField(max_length=200, default='')
    about = models.CharField(max_length=500, default='')
    specialization = models.CharField(max_length=200, default='')
    phone_number = PhoneNumberField()
    link = models.ManyToManyField(Link, default='#')
    image = models.ImageField(upload_to='images/instructor')
    image_thumbnail = ImageSpecField(source='image',
        processors=[ResizeToFill(350, 200)],
        format='JPEG',
        options={'quality': 60})

    class Meta:
        #ordering = ('category_name',)
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'

    def __str__(self):
            return self.name

class Course(models.Model):
    title = models.CharField(max_length=200, db_index=True, default='')
    slug = models.SlugField(max_length=200, db_index=True, default='')
    description = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to='images/courses')
    image_thumbnail = ImageSpecField(source='image',processors=[ResizeToFill(350, 200)], format='JPEG',
        options={'quality': 60})
    year = models.DateField()
    #course_link = models.CharField(max_length=500, default="")
    year = models.DateField()
    price = models.FloatField()
    publish = models.DateTimeField(default=timezone.now)
    demo = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="course_category")
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name="course_instructor")
    language = LanguageField(default='', blank=False)
    skill_level = models.CharField(choices=SKILL_LEVEL, max_length=50)

    class Meta:
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("Course_detail", kwargs={"pk": self.pk})

#Add duration to module
class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True, default='')


    class Meta:
        verbose_name ='Module'
        verbose_name_plural = 'Modules'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("course:module", args=[self.id, self.slug])

    def __str__(self):
        return self.title

#Add duration to lesson
class Lesson(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='module', default='')
    slug = models.SlugField(max_length=200, db_index=True, default='')
    video_url = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    class Meta:
        verbose_name ='Lesson'
        verbose_name_plural = 'Lessons'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("course:lesson", args=[self.id, self.slug])

    def __str__(self):
        return self.title
