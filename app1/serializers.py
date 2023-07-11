from app1.models import Kitap,Yazar
from rest_framework import serializers
class YazarSerializer(serializers.HyperlinkedModelSerializer):#bu yöntem ile modelin ilişkili olduğu diğer yapılar eğer serileştirilecek alanlar arasında yer alıyor ise , ilişkili modellerdeki verilerin bağlantısı geri dönen veri içerisinde yer alır.
    class Meta:
        model=Yazar
        fields=('isim','soyisim')
class KitapSerializer(serializers.ModelSerializer):
    class Meta:
        model=Kitap
        fields=('baslik','created','price','book_detail','book_image')#virgül koymayı sakın unutmayın,anlamadığım bir şekilde DRF ,bu alanının mutlaka bir liste ya da küme tipinde olmasını istiyor. Fields alanına eğer tek bir attribute ekleyeceksiniz mutlaka buna dikkat edin.