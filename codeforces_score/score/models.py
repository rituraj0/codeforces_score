from django.db import models

# Create your models here.
##insert only accpeted solutions
## contest*100+ index
# date when it was submiited 

class Submission(models.Model): 
    problem_id = models.IntegerField(default=0,unique=True,primary_key=True) 
    pub_date = models.DateTimeField('Question Solved')
	
    def __str__(self): 
        return self.problem_id
