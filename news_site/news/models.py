from django.db import models

class Article(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)   # Specifies the max length of each article title
    timestamp = models.DateTimeField()   # Specifies the ublication time of each article
    text = models.TextField('Article text')  # Stores the actual article text
    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    """
    This establishes as relationship between articles and comments; ForeignKey establishes 1 article / comment; on_delete param is specified when instantiating 
    ForeignKey in case the foreign key is deleted from the database. models.CASCADE makes sure that comments will be also deleted if an article is deleted.
    """
    objects = models.Manager()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=70)   # stores the name of the visitor commenting
    text = models.TextField('Comment text')   # stores the comment text
    def __str__(self):
        return "{} says '{}'".format(self.author, self.text)