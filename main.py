import tkinter

window = tkinter.Tk()
window.title("Not Hesaplama 1.1")
window.config(pady=30, padx=80)

def not_hesaplama():
    vize = vize_notu.get()
    final = final_notu.get()
    vize_yüzdesi = 40
    final_yüzdesi = 60
    if vize == "" or final == "":
        not_bilgisi.config(text="Vize ve final notunu giriniz!")
    else:
        try:
            not_ortalanması = float(vize) * vize_yüzdesi / 100 + float(final) * final_yüzdesi / 100
            if not_ortalanması < 45:
                not_bilgisi.config(text=derece_düzeyi(not_ortalanması)+Bütünleme(final_yüzdesi, vize_yüzdesi, final, vize, not_ortalanması))
            else:
                not_bilgisii = derece_düzeyi(not_ortalanması)
                not_bilgisi.config(text=not_bilgisii)
        except ValueError:
            not_bilgisi.config(text="Bir sayı giriniz!")

def silme_button():
    vize_notu.delete(first=0, last=tkinter.END)
    final_notu.delete(0, tkinter.END)

def Bütünleme(final_yüzdesi, vize_yüzdesi, final, vize, not_ortalanması):
    while True:
        not_ortalanması = float(vize) * vize_yüzdesi / 100 + float(final) * final_yüzdesi / 100
        not_ortalanması=int(not_ortalanması)
        if not_ortalanması > 44:
            not_bilgisi = f" Bütünlemeden {final} almanız lazım"
            break
        else:
            final = int(final)
            final += 1
    return not_bilgisi
vize_notu_başlık = tkinter.Label(text="Vize Notunu Girin")
vize_notu_başlık.pack()
vize_notu = tkinter.Entry(width=12)
vize_notu.pack()
final_notu_başlık = tkinter.Label(text="Final Notunu Girin")
final_notu_başlık.pack()
final_notu = tkinter.Entry(width=12)
final_notu.pack()
Hesaplama_button = tkinter.Button(text="Hesapla", command=not_hesaplama)
Hesaplama_button.pack()
silme_button = tkinter.Button(width=9, text="Sil", command=silme_button)
silme_button.pack()
not_bilgisi = tkinter.Label()
not_bilgisi.pack()

def derece_düzeyi(not_ortalanması):
    #not_ortalanması = int(not_ortalanması)
    not_bilgisii = f"Senin not ortalaman {not_ortalanması}.  Senin harf notun"
    if 90 < not_ortalanması <= 100:
        not_bilgisii += " AA"
    elif 85 < not_ortalanması <= 90:
        not_bilgisii += " BA"
    elif 80 < not_ortalanması <= 85:
        not_bilgisii += " BB"
    elif 70 < not_ortalanması <= 80:
        not_bilgisii += " CB"
    elif 60 < not_ortalanması <= 70:
        not_bilgisii += " CC"
    elif 50 < not_ortalanması <= 60:
        not_bilgisii += " DC"
    elif 45 < not_ortalanması <= 50:
        not_bilgisii += " DD"
    else:
        not_bilgisii += " FF (kaldın)"
    return not_bilgisii

window.mainloop()