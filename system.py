import os

versiyon = "0.5.0"

# veri dizinleri
data = [("0","0","0","0","0","0","0","0","0","0"),
("0","0","0","0","0","0","0","0","0","0"),
("0","0","0","0","0","0","0","0","0","0"),
("0","0","0","0","0","0","0","0","0","0"),
("0","0","0","0","0","0","0","0","0","0")]
soru = [
(
# normal sorular
"bu nesne canlı mı?",
"bu nesne elmadan küçük mü?",
"bu nesne bir canlının parçası mı?",
"bu nesne yenilebilir mi?",
"bu nesne parayla satılabilir mi?",
"kesmek veya kısaltmak mümkün mü?",
"bu nesne önemli ve değerli mi?",
"bu nesne ışık yayıyor mu?",
"bu nesne ısı yayabiliyor mu?",
"bu nesne katı mı?"
),
# evet cevabı için alternatif sorular
(
"bu şey nefes alıyor mu?",
"bu şey iğne ucundan daha mı büyük?",
"bu şey canlının en önemli parçalarından biri mi?",
"bu şey tatlı mı?",
"bu şey ucuz mu?",
"bu şey sıklıkla kısaltılır mı?",
"bu şey genelde zenginlerde mi oluyor?",
"bu şey parlak mı?",
"bu şey insanları ısıtır mı?",
"bu şey sert mi?"
),
# bazen cevabı için alternatif sorular
(
"bu şey tek hücreli canlı mı?",
"bu şey uzuyor mu?",
"bu şey insanlarda bulunabilir mi?",
"bu şey acı mı?",
"bu şeyin ticareti yasadışı mı?",
"bu şey kısaltılmalı mı?",
"bu şey enflasyonda sürekli düşüyor mu?",
"bu şey bir odayı aydınlatır mı?",
"bu şey bir odayı ısıtabilir mi?",
"bu şey bir kas gibi kasılıp gevşiyor mu?"
),
# nadiren cevabı için alternatif sorular
(
"bu şey bir hastalık mı?",
"bu şey bir insan elinin boyunu geçebilir mi?",
"bu şey canlılardan alınıyor veya canlılara ekleniyor mu?",
"bu şey zehirli mi?",
"bu şey nadir mi bulunuyor?",
"bu şeyi kısaltmak zararlı mı?",
"bu şey her insanda bulunabiliyor mu?",
"bu nesne her evde olmalı mı?",
"bu nesne ateş yakabilir mi?",
"bu şey genelde sıvı veya gaz mı?"
),
# sıklıkla cevabı için alternatif sorular
(
"bu nesne bir insan bedeninde bulunabilir mi?",
"bu nesne genelde insan eliyle mi büyür?",
"bu nesne ameliyat ile alınır mı?",
"tatlı mı?",
"bu nesne pahalı mı?",
"kesmek veya kısaltmak için herhangi bir ders gerekir mi?",
"bu nesne takı gibi birşey mi?",
"bu şey ışık için mi kullanılır?",
"bu şey ısı için mi kullanılır?",
"bu şey eriyebilir mi?"
)]

# soru sıraları (10-20)
soru_sırası = [0,0,0,0,0]

########################
# ./system/cevap_list.dg --> sorulara uygun öğrenilmiş cevap kelimelerini kapsar
# ./system/data_list.dg --> sorular sayesinde öğrenilmiş kelimeleri kapsar
def sistemkontrol():
	try:
		os.mkdir("system")
		print("system yeni oluşturulduğu için hiçbir nesne bulunmamaktadır.")
	except: print("(...)")
	open("system/data_list.dg", "a")
	print("bilinen kelimeler listesini güncellemek için https://nopen.com web sitesini inceleyiniz!")
	open("system/cevap_list.dg","a")
	bb = open("system/cevap_list.dg", "r")
	DATA = bb.read()
	if DATA == "" or DATA == "e 1|h 0|b 2|n 3|s 4|":
		cevap_zekasi = open("system/cevap_list.dg", "w")
		cevap_zekasi.write("e 1|h 0|b 2|n 3|s 4|")
		cevap_zekasi.close()
		print("tek bildiğim (cevap verebileceğin) kelimeler 'e' (evet), 'h' (hayır), b (bazen), n (nadiren) ve s'dir (sıklıkladır); kelime dosyasını indirebilirsin.")
	else:
		cevap_zekasi = open("system/cevap_list.dg", "r")
		DATA =[]
		for x in cevap_zekasi.read().split("|"):
			DATA.append(x.split(" ")[0])
		cevap_zekasi.close()
		print("ben biraz cevap biliyorum, bana bunlarla da cevap verebilirsin!")
		print(" ".join(DATA))
	print("system hazır!")


########################
# cevap verilen kelimeyi kontrol eder
# in --> str {0-1-2-3-4}
# out --> str num ("-1") 0-1-2-3-4
def kelimekontrol(veri):
	oku = open("system/cevap_list.dg", "r")
	a = "0"
	for x in oku.read().split("|"):
		if x != "":
			if x.split(" ")[0] == veri:
				a = "1"
				return x.split(" ")[1]
	if a == "0": return yenikelime(veri)
	
########################
# yeni cevap verilebilir kelime öğrenimi
# in --> str {0-1-2-3-4}
# out --> str num ("-1") 0-1-2-3-4
def yenikelime(veri):
	global data
	global soru_sırası
	global kelime_var_mı
	print("abi ben " + str(veri) + " ne bilmiyorum! bu kelimeyi öğrenmemi ister misin?\n(...)")
	cevap = input()
	cevap = kelimekontrol(cevap)
	if cevap == "1":
		print(" " + veri + " ne anlamına gelmektedir?")
		cevap = input("(...)\n")
		cevap = kelimekontrol(cevap)
		okudayi = open("system/cevap_list.dg", "r")
		icerik = okudayi.read()
		okudayi.close()
		yazdayi = open("system/cevap_list.dg", "w")
		yazdayi.write(icerik + str(veri) + " " + str(cevap) + "|")
		print("yeni bir kelime öğrendim! (" + veri + ")")
		return cevap

########################
# soruları sorar ve cevapları kaydeder
# in(0-5) --> aynı soru sırası (e-s)
def sorucevap(veri):
	global soru_sırası
	global data
	if soru_sırası[veri] < 10:
		def sor():
			print("...")
			print(soru[veri][soru_sırası[veri]])
			print("...")
			cevap = input()
			cevap = kelimekontrol(cevap)
			if cevap != None:
				data[veri][soru_sırası[veri]] = cevap
				soru_sırası[veri] += 1
		if veri == 0: sor()
		else:
			print(data[0][soru_sırası[veri]])
			if data[0][soru_sırası[veri]] == str(veri): sor()
			else: soru_sırası[veri] += 1
		sorucevap(veri)


########################
# data_list yani öğrenilmiş nesneler dosyasını okur ve sonuç üretir, yeni kelimeyi kaydeder
def dosyaoku():
	buldunmugereksiz = False
	oku = open("system/data_list.dg", "r")
	for x in oku.read().split("|"):
		if x != "":
			if x.split(" ")[1] == ("".join(data[0])+"".join(data[1])+"".join(data[2])+"".join(data[3])+"".join(data[4])):
				print("BULDUM BULDUM!!! bu nesne " + x.split(" ")[0] + ", değil mi?\n...")
				abi_buldum_mu = input()
				abi_buldum_mu = kelimekontrol(abi_buldum_mu)
				if abi_buldum_mu == "1": buldunmugereksiz = True
				elif abi_buldum_mu == "0": buldunmugereksiz = False
				else:
					print("hey, ben ne dediğini anlayamadım. lütfen e (evet) veya h (hayır) yaz, büyük harf girme çünkü anlam değişebilir bilmiyorum.")
					dosyaoku()
	if buldunmugereksiz == False:
		print("bulamadım, o nesne neydi?")
		object_name = input()
		oku = open("system/data_list.dg", "r")
		yedekle_abe = oku.read()
		yaz = open("system/data_list.dg", "w")
		yaz.write(yedekle_abe + object_name + " " + ("".join(data[0])+"".join(data[1])+"".join(data[2])+"".join(data[3])+"".join(data[4])) + "|")


########################
# launcher
def başlat():
	global soru_sırası
	x = 0
	soru_sırası = [0,0,0,0,0]
	while x < 5:
		sorucevap(x)
		x += 1
	dosyaoku()
	cevap = input("tekrar oynamak ister misin?\n")
	cevap = kelimekontrol(cevap)
	if cevap == "1":
		print("tekrar oynadığın için teşekkür ederim!!!")
		başlat()


########################
# çalıştırma
sistemkontrol()
başlat()