from classes import Line, Station

A = Line("A", "Green")
B = Line("B", "Yellow")
C = Line("C", "Red")

lineA = []
lineA.extend([
    Station("Nemocnice_Motol", A),
    Station("Petriny", A),
    Station("Nadrazi_Veleslavin", A),
    Station("Borislavka", A),
    Station("Dejvicka", A),
    Station("Hradcanska", A),
    Station("Malostranska", A),
    Station("Staromestska", A),
    Station("Mustek", A),
    Station("Muzeum", A),
    Station("Namesti Miru", A),
    Station("Jiriho z Podebrad", A),
    Station("Flora", A),
    Station("Zelivskeho", A),
    Station("Strasnicka", A),
    Station("Skalka", A),
    Station("Depo Hostivar", A)])

lineB = []
lineB.extend([
    Station("Zlicin", B),
    Station("Stodulky", B),
    Station("Luka", B),
    Station("Luziny", B),
    Station("Hurka", B),
    Station("Nove Butovice", B),
    Station("Jinonice", B),
    Station("Radlicka", B),
    Station("Smichovske nadrazi", B),
    Station("Andel", B),
    Station("Karlovo namesti", B),
    Station("Narodni Trida", B),
    Station("Mustek", B),
    Station("Namesti Republiky", B),
    Station("Florenc", B),
    Station("Krizikova", B),
    Station("Invalidovna", B),
    Station("Palmovka", B),
    Station("Ceskomoravska", B),
    Station("Vysocanska", B),
    Station("Kolbenova", B),
    Station("Hloubetin", B),
    Station("Rajska Zahrada", B),
    Station("Cerny most", B)])

lineC = []
lineC.extend([
    Station("Haje", C),
    Station("Opatov", C),
    Station("Chodov", C),
    Station("Roztyly", C),
    Station("Kacerov", C),
    Station("Budejovicka", C),
    Station("Pankrac", C),
    Station("Prazskeho povstani", C),
    Station("Vysehrad", C),
    Station("I.P.Pavlova", C),
    Station("Muzeum", C),
    Station("Hlavni Nadrazi", C),
    Station("Florenc", C),
    Station("Vltavska", C),
    Station("Nadrazi Holesovice", C),
    Station("Kobylisy", C),
    Station("Ladvi", C),
    Station("Strizkov", C),
    Station("Prosek", C),
    Station("Letnany", C)])

metro = []
metro.extend([*lineA, *lineB, *lineC])
