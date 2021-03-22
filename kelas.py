class Kalkulator:
    """contoh kelas kalkulator sederhana"""
 
    def __init__(self, i=12345):
        self.i = i  # i adalah variabel pada constructor, self.i adalah variabel dari class
 
    def f(self):
        return 'hello world'
    
    @classmethod
    def tambah_angka(cls, angka1, angka2):
        return '{} + {} = {}'.format(angka1, angka2, angka1 + angka2)


k = Kalkulator(i=1024)  # melakukan instantiation sekaligus mengisi atribut i jadi 1024
print(k.i)              # mencetak atribut i dari objek k dengan keluaran nilai 1024
print(k.tambah_angka(1, 2)) # tanpa perlu memberikan masukan untuk argumen cls

# run on https://ideone.com/OheNfF
