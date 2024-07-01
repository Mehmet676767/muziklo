HELP_1 = """<b><u>admin komutlar :</b></u>

Kanal için kullanmak üzere komutların başına /c eklemeniz yeterlidir.


/duruklat : Çalan akışı duraklatır.

/devam : Duraklatılmış akışı devam ettirir.

/atla : Şu anda çalan akışı atlar ve sıradaki parçayı çalmaya başlar.

/son veya /stop : Kuyruğu temizler ve şu anda çalan akışı sonlandırır.

/player : Etkileşimli bir çalıcı paneli alırsınız.

/queue : Kuyrukta bekleyen parçaların listesini gösterir.
"""

HELP_2 = """
<b><u>yetkili komutlar :</b></u>

Yetkili kullanıcılar, sohbette yönetici hakları olmadan botu kullanabilirler.

/auth [kullanıcı adı/kullanıcı ID] : Botun yetkilendirme listesine bir kullanıcı ekler.

/unauth [kullanıcı adı/kullanıcı ID] : Bir kullanıcıyı yetkilendirme listesinden kaldırır.

/authusers : Grubun yetkili kullanıcılarının listesini gösterir.
"""

HELP_3 = """
<u><b>reklam.Komutlar</b></u> [ sadece yöneticiler ] :


/reklam [mesaj veya bir mesaja cevap] : Botun sunucu sohbetlerine bir mesajı yayınlamasını sağlar.

BROADCASTING MODES:
-pin : Yayınlanan mesajlarınızı sunucu sohbetlerinde sabitler.
-pinloud : Yayınlanan mesajınızı sunucu sohbetlerinde sabitler ve üyelere bildirim gönderir.
-user : Mesajı botunuzu başlatan kullanıcılara yayınlar.
-assistant : Mesajınızı botun asistan hesabından yayınlar.
-nobot : Botun mesajı yayınlamamasını zorlar.

ÖRNEK: /reklam -user -assistant -pin test ediliyor yayını
"""

HELP_4 = """<u><b>GRUP BLOKE  :</b></u> [ SADECE YÖNETİCİLER ]

𝖱𝖾𝗌𝗍𝗋𝗂𝖼𝗍 𝖲𝗁𝗂𝗍 𝖢𝗁𝖺𝗍𝗌 𝖳𝗈 𝖴𝗎𝖾 𝖮𝗎𝗋 𝖯𝗋𝖾𝖼𝗂𝗈𝗎𝗌 𝖡𝗈𝗍 .

/blacklistchat [ 𝖢𝗁𝖺𝗍 𝖨𝖣 ] : 𝖡𝗅𝖺𝖼𝗄𝗅𝗂𝗌𝗍 𝖠 𝖢𝗁𝖺𝗍 𝖥𝗋𝗈𝗆 𝖴𝗌𝗂𝗇𝗀 𝖳𝗁𝖾 𝖡𝗈𝗍 .
/whitelistchat [ 𝖢𝗁𝖺𝗍 𝖨𝖣 ] : 𝖶𝗁𝗂𝗍𝖾𝗅𝗂𝗌𝗍 𝖳𝗁𝖾 𝖡𝗅𝖺𝖼𝗄𝗅𝗂𝗌𝗍𝖾𝖽 𝖢𝗁𝖺𝗍 .
/blacklistedchat : 𝖲𝗁𝗈𝗐𝗌 𝖳𝗁𝖾 𝖫𝗂𝗌𝗍 𝖮𝖿 𝖡𝗅𝖺𝖼𝗄𝗅𝗂𝗌𝗍𝖾𝖽 𝖢𝗁𝖺𝗍𝗌 .
"""

HELP_5 = """
<u><b>kullanıcı bloke :</b></u> [ sadece yöneticiler ]

Değerli botumuzu kullanarak saçma sohbetleri sınırlayın.

/blacklistchat [sohbet ID] : Bot kullanarak bir sohbeti engeller.
/whitelistchat [sohbet ID] : Engellenen sohbeti beyaz listeye alır.
/blacklistedchat : Engellenen sohbetlerin listesini gösterir.
"""

HELP_6 = """
<u><b>kanal oynatma komutlar :</b></u>

Kanalda ses/video akışı yapabilirsiniz.

/cplay : Kanalın video sohbetinde istenen ses parçasını çalmaya başlar.
/cvplay : Kanalın video sohbetinde istenen video parçasını çalmaya başlar.
/cplayforce veya /cvplayforce : Devam eden akışı durdurur ve istenen parçayı çalmaya başlar.

/channelplay [sohbet kullanıcı adı veya ID] veya [disable] : Kanalı bir gruba bağlar ve grup tarafından gönderilen komutlarla parçaları çalmaya başlar.
"""

HELP_7 = """
<u><b>GLOBAL BAN KOMUTLAR</b></u> [ SADECE YONETİCİLER ] :

/gban [kullanıcı adı veya bir kullanıcıya cevap] : Küfürbazı tüm sunucu sohbetlerinden ve botu kullanarak onu engeller.
/ungban [kullanıcı adı veya bir kullanıcıya cevap] : Küfürbazın global olarak engelini kaldırır.
/gbannedusers : Global olarak engellenen kullanıcıların listesini gösterir.
"""

HELP_8 = """
<b><u>DONGU KOMUTLAR :</b></u>

<b>Aktif parçayı/şarkıyı veya yayını döngüde başlatır</b> 

/dongu [enable/disable] : Devam eden akışı döngüye alır/devre dışı bırakır.
/loop [1, 2, 3, ...] : Belirtilen değer için döngüyü etkinleştirir
"""

HELP_9 = """
<u><b>BAKIM.MODU</b></u> [ SADECE YÖNETİCİLER ] :

/logs : Botun günlüklerini alır.

/logger [enable/disable] : Botun etkinliklerini günlüğe kaydetmeye başlar/devre dışı bırakır.

/maintenance [enable/disable] : Botun bakım modunu etkinleştirir/devre dışı bırakır.
"""

HELP_10 = """
<b><u>PİNG VE STAT :</b></u>

/start : Müzik botunu başlatır.
/help : Komutların açıklamalarıyla bir yardım menüsü alırsınız.

/ping : Botun pingini ve sistem istatistiklerini gösterir.

/stats : Botun genel istatistiklerini gösterir.
"""

HELP_11 = """
<u><b>OYNAT KOMUTLAR :</b></u>

<b>v :</b> video sarki açmak için .
<b>force :</b> 𝖲zorla oynatmak için .

v : Video oynatma için kullanılır.
force : Zorla oynatma için kullanılır.

/oynat veya /voynat : Video sohbetinde istenen parçayı çalmaya başlar.

/playforce veya /vplayforce : Devam eden akışı durdurur ve istenen parçayı çalmaya başlar.
"""

HELP_12 = """
<b><u>AKIŞI KARIŞTIR :</b></u>

/shuffle : Kuyruğu karıştırır.
/queue : Karıştırılmış kuyruğu gösterir.
"""

HELP_13 = """
<b><u>İLERİ SAR :</b></u>

/ilerisar [saniye cinsinden süre] : Akışı verilen süreye ileri sarmak için kullanılır.
/gerisar [saniye cinsinden süre] : Akışı verilen süreye geri sarmak için kullanılır.
"""

HELP_14 = """
<b><u>ŞARKI İNDİRME</b></u>

/bul [şarkı adı/yt url] : YouTube'dan herhangi bir parçayı MP3 veya MP4 formatında indirir.
"""

HELP_15 = """
<b><u>HIZ KOMUTLARI :</b></u>

Devam eden akışın oynatma hızını kontrol edebilirsiniz. [Yalnızca yöneticiler için]

/speed veya /playback : Grubun sesli oynatma hızını ayarlamak için.
/cspeed veya /cplayback : Kanalın sesli oynatma hızını ayarlamak için.
"""
