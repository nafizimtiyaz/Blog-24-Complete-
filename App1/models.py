from django.db import models

class artical(models.Model):
    title=models.CharField(max_length=150)
    slug=models.CharField(max_length=100,unique=True)
    body=models.CharField(max_length=20000)
    views =models.IntegerField(default=0)
    date=models.DateTimeField(auto_now=False,auto_now_add=True)
    image=models.ImageField(default='abc.png',upload_to='Artical')


    def __str__(self):
        return self.title

class bookreview(models.Model):
    title=models.CharField(max_length=150)
    slug=models.CharField(max_length=100)
    body=models.CharField(max_length=20000)
    views = models.IntegerField(default=0)
    date=models.DateTimeField(auto_now=False,auto_now_add=True)
    image=models.ImageField(default='abc.png',upload_to='bookreview')


    def __str__(self):
        return self.title


class somajsongsker(models.Model):
    title=models.CharField(max_length=150)
    slug=models.CharField(max_length=100)
    body=models.CharField(max_length=20000)
    views = models.IntegerField(default=0)
    date=models.DateTimeField(auto_now=False,auto_now_add=True)
    image=models.ImageField(default='abc.png',upload_to='somajsongsker')


    def __str__(self):
        return self.title

class songbad(models.Model):
    title=models.CharField(max_length=1500)
    slug=models.CharField(max_length=1000)
    body=models.CharField(max_length=20000)
    views = models.IntegerField(default=0)
    date=models.DateTimeField(auto_now=False,auto_now_add=True)
    image=models.ImageField(default='abc.png',upload_to='songbad')


    def __str__(self):
        return self.title

class itihash(models.Model):
    title=models.CharField(max_length=1500)
    slug=models.CharField(max_length=1000)
    body=models.CharField(max_length=20000)
    views = models.IntegerField(default=0)
    date=models.DateTimeField(auto_now=False,auto_now_add=True)
    image=models.ImageField(default='abc.png',upload_to='itihash')


    def __str__(self):
        return self.title


class law(models.Model):
    title=models.CharField(max_length=150)
    slug=models.CharField(max_length=100)
    body=models.CharField(max_length=20000)
    views = models.IntegerField(default=0)
    date=models.DateTimeField(auto_now=False,auto_now_add=True)
    image=models.ImageField(default='abc.png',upload_to='law')


    def __str__(self):
        return self.title



class politics(models.Model):
    title=models.CharField(max_length=150)
    slug=models.CharField(max_length=100)
    body=models.CharField(max_length=20000)
    views = models.IntegerField(default=0)
    date=models.DateTimeField(auto_now=False,auto_now_add=True)
    image=models.ImageField(default='abc.png',upload_to='politics')


    def __str__(self):
        return self.title


class interview(models.Model):
    title=models.CharField(max_length=150)
    slug=models.CharField(max_length=100)
    body=models.CharField(max_length=20000)
    views = models.IntegerField(default=0)
    date=models.DateTimeField(auto_now=False,auto_now_add=True)
    image=models.ImageField(default='abc.png',upload_to='interview')


    def __str__(self):
        return self.title


class Personality(models.Model):
    title=models.CharField(max_length=150)
    slug=models.CharField(max_length=100)
    body=models.CharField(max_length=20000)
    views = models.IntegerField(default=0)
    date=models.DateTimeField(auto_now=False,auto_now_add=True)
    image=models.ImageField(default='abc.png',upload_to='Personality')


    def __str__(self):
        return self.title


class Islamic(models.Model):
    title=models.CharField(max_length=150)
    slug=models.CharField(max_length=100)
    body=models.CharField(max_length=20000)
    views = models.IntegerField(default=0)
    date=models.DateTimeField(auto_now=False,auto_now_add=True)
    image=models.ImageField(default='abc.png',upload_to='Islamic')


    def __str__(self):
        return self.title


class Bibidh(models.Model):
    title=models.CharField(max_length=150)
    slug=models.CharField(max_length=100)
    body=models.CharField(max_length=20000)
    views = models.IntegerField(default=0)
    date=models.DateTimeField(auto_now=False,auto_now_add=True)
    image=models.ImageField(default='abc.png',upload_to='Bibidh')


    def __str__(self):
        return self.title


class blog(models.Model):
    title=models.CharField(max_length=150)
    slug=models.CharField(max_length=100)
    body=models.CharField(max_length=20000)
    views = models.IntegerField(default=0)
    date=models.DateTimeField(auto_now=False,auto_now_add=True)
    image=models.ImageField(default='abc.png',upload_to='Blog')


    def __str__(self):
        return self.title


class Recentworld(models.Model):
    title=models.CharField(max_length=150)
    slug=models.CharField(max_length=100)
    body=models.CharField(max_length=20000)
    views = models.IntegerField(default=0)
    date=models.DateTimeField(auto_now=False,auto_now_add=True)
    image=models.ImageField(default='abc.png',upload_to='recentworld')


    def __str__(self):
        return self.title

class ElectedPost(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=100)
    body = models.CharField(max_length=20000)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField(default='abc.png', upload_to='ElectedPost')

    def __str__(self):
        return self.title

class BrakingNews(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=100)
    body = models.CharField(max_length=20000)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField(default='abc.png', upload_to='BrakingNews')

    def __str__(self):
        return self.title