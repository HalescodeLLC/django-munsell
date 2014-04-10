
from django.db import models


# Create your models here.
class MunsellColor(models.Model):
    hue_a = models.CharField(max_length=4)
    hue_b = models.CharField(max_length=4)
    value = models.CharField(max_length=4)
    chroma = models.CharField(max_length=4)
    nice_name = models.CharField(max_length=64)
    munsell_name = models.CharField(max_length=16)
    sortable_name = models.CharField(max_length=16)
    n_r = models.CharField(max_length=8)
    n_g = models.CharField(max_length=8)
    n_b = models.CharField(max_length=8)
    s_r = models.CharField(max_length=4)
    s_g = models.CharField(max_length=4)
    s_b = models.CharField(max_length=4)
    hexval = models.CharField(max_length=8)

    class Meta:
        ordering = ['sortable_name']

    def convert_to_normalized_rgb(self):
        return [self.n_r, self.n_g, self.n_b]

    def convert_to_normalized_rgb_single_string(self):
        return '%s %s %s' % (self.n_r, self.n_g, self.n_b)

    def convert_to_standard_rgb(self):
        return [self.s_r, self.s_g, self.s_b]

    def convert_to_standard_rgb_single_string(self):
        return '%s %s %s' % (self.s_r, self.s_g, self.s_b)

    def __str__(self):
        return self.munsell_name
