from random import choice

d = [
    ("Glava pred roko", "Tomo Omahna"),
    ("S katere hoste pa si ti pršu?", "Tomo Omahna"),
    ("Dej odpri okn! Zard zvoka!", "Tomo Omahna"),
    ("Za kok si kupil suknjič? Po dobavni ceni.", "Tomo Omahna"),
    ("Ubi se", "Tomo Omahna"),
    ("Za vsako rit palca raste", "Tomo Omahna"),
    ("Ena bl resna plučnca me je zagrabla, pa so me napumpal", "Tomo Omahna"),
    ("Kvas lesen", "Tomo Omahna"),
    ("Naročil sem vam da mi prepleskate fasado, vi mi pa rože zalivate, in pričakujete plačilo", "Tomo Omahna"),
    ("Jao", "Tomo Omahna"),
    ("Fantje, nismo kupil BMW-ja da bomo na bencinu šparal", "Tomo Omahna"),
    ("Če pogledaš ekipo camerona so vsi črni pa če pogledate na tribuno so tud vsi črni pa če pogledaš trenerja je tud on črn. Zakaj je tako? Ker so pojedl vse bele.", "Tomo Omahna"),
    ("Rusov je 140 miljonov, američanov pa 300 miljonov. Zakaj je tko? Ker američani štejejo črnce kt ljudi", "Tomo Omahna"),
    ("Zanimivo", "Lidija Gorišek"),
    ("A ste slišali za tiste viruse ki nič ne delajo? To so uni albanski virusi", "Dušan Sitar"),
    ("Orehova torta ... njam", "Janja Žlebnik"),
    ("Ecka pecka pošto pelja, pošta se zvrne, ecka pecka prdne", "Marko Kastelic"),
    ("Naši južni bratje", "Marko Kastelic"),
    ("Pardon, samo da majnika ubijem", "Marko Kastelic"),
    ("Tiho fantje", "Matjaž Majnik"),
    ("Športna smola", "Marko Kastelic"),
    ("Eeeh kako se že temu reče", "Marko Kastelic"),
    ("Rečmo da hočeš petko pa prideš do mene s sekirco pa mi rečeš, da hočeš petko. Jaz te uprašam, zakaj bi ti to petko dal, nato pa ti pokažeš sekirco. A bi ti poj dal petko? Ne, js bi še večjo sekirco potegnu!", "Marko Kastelic"),
    ("Šlebič tebe je itak težko ne opazit", "Matjaž Majnik"),
    ("BENJAMIN", "Katja Lasbaher"),
    ("Gospod, če imate težave z želodcem, prosim če lahko trpite v tišini", "Karin Kastelic"),
    ("V osnovni šoli smo delali IQ test, imela sm VČASIH okol 120, ampak ko ženska rodi otroka baje da odmre 20% možganskih celic. Jaz imam 3 otroke.", "Karin Kastelic"),
    ("Ja a je to dobr? Ja verjetn je dobr", "Miki"),
    ("Fantje zdej pa se umirite da premislimo, kaj bomo dali v GROUP BY stavek", "Matjaž Majnik"),
]

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'ok':
        return f'```fix\nNe ni ok\n ~ Katja Lasbaher ~```'

    if p_message == 'ane':
        return f'```fix\nAne\n ~ Dušan Sitar ~```'    

    if p_message == '/wisdom':
        izbran = choice(d)
        return f'```fix\n{izbran[0]}\n ~ {izbran[1]} ~```'

    return 'Uporab: /wisdom'


