from django.db import models

# Create your models here.

class Cv(models.Model):
    """Model definition for cv."""

    # TODO: Define fields here
    username = models.CharField(max_length = 150)
    fullname = models.CharField(max_length = 150)
    address = models.CharField(max_length = 250)
    phone_number = models.CharField(max_length = 150)
    job_title = models.CharField(max_length = 150)
    linkedin = models.CharField(max_length = 150)
    github = models.CharField(max_length = 150,blank=True,null=True)
    

    class Meta:
        """Meta definition for cv."""

        verbose_name = 'cv'
        verbose_name_plural = 'cvs'

    def __str__(self):
        """Unicode representation of cv."""
        return self.fullname
    
    
class section(models.Model):
    """Model definition for section."""

    # TODO: Define fields here
    models.ForeignKey(Cv, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    
    

    class Meta:
        """Meta definition for section."""

        verbose_name = 'section'
        verbose_name_plural = 'sections'

    def __str__(self):
        """Unicode representation of section."""
        pass

