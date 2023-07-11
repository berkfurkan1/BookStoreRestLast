from django.db import models



# Create your models here.


class Yazar(models.Model):
    isim=models.CharField(max_length=30)
    soyisim=models.CharField(max_length=30)
    created= models.DateTimeField('date created',null=True)
    #kitaplar=models.ManyToManyField(Kitap)
    def __str__(self):
       return '%s %s'%(self.isim,self.soyisim)

class Kitap(models.Model):
    baslik=models.CharField(max_length=70)
    #Many-to-one relationships:(models.ForeignKey)
    yazar = models.ForeignKey(Yazar,on_delete=models.CASCADE,null=True)
    #models.CASCADE -> bir yazar silindiğinde yazara ait kitapları siler.
    created=models.DateTimeField('date created',null=True)
    price=models.DecimalField(decimal_places=2,max_digits=4,null=True)
    book_detail = models.TextField(null=True)
    book_image = models.ImageField(upload_to='images/',null=True,blank=True)
   

    class Meta:
         verbose_name ='Kitap'
         verbose_name_plural='Kitaplar'
         ordering=['-created']# created zamanlarına göre sıralanıyor.
    def __str__(self):
       return self.baslik 