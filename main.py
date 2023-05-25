from translate import Translator

translator_EnTr = Translator(from_lang="english", to_lang="turkish")
translator_TrEn = Translator(from_lang="turkish", to_lang="english")


def trslt_e_t():
    word = input("İngilizce Kelime Giriniz: ")
    translation = translator_EnTr.translate(word)
    print(translation)


def trslt_t_e():
    word = input("Türkçe Kelime Giriniz: ")
    translation = translator_TrEn.translate(word)
    print(translation)


while True:
    try:
        select_translate = input("1- İngilizce > Türkçe\n2- Türkçe > İngilizce\nSeçin Yapınız 1 veya 2: ")

        if select_translate == "1":
            trslt_e_t()

        elif select_translate == "2":
            trslt_t_e()

    except ValueError:
        print("Yanlış Seçim Yaptınız..")