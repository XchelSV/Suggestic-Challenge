from django.db import models
import json

# Create your models here.
class Sequence(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=200)
    
    def set_value(self, x):
        self.value = json.dumps(x)

    def get_value(self):
        return json.loads(self.value)