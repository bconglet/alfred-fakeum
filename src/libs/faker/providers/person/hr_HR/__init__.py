# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = ['{{first_name}} {{last_name}}']

    first_names_male = [
        "Aldo", "Alen", "Andrija", "Ante", "Anto", "Anton", "Antonio",
        "Antun", "Boris", "Božo", "Branko", "Bruno", "Dalibor", "Damir",
        "Danijel", "Dario", "Darko", "David", "Davor", "Dejan", "Denis",
        "Dino", "Domagoj", "Dominik", "Dragan", "Dragutin", "Dražen",
        "Duje", "Dušan", "Elvis", "Erik", "Filip", "Fran", "Franjo",
        "Goran", "Hrvoje", "Igor", "Ilija", "Ivan", "Ivica", "Ivo",
        "Jakov", "Janko", "Josip", "Joso", "Jozo", "Joško", "Juraj",
        "Jure", "Karlo", "Kristijan", "Leon", "Lovre", "Lovro", "Luka",
        "Marijan", "Marin", "Mario", "Marko", "Martin", "Mate", "Matej",
        "Mateo", "Matija", "Mato", "Mihael", "Mijo", "Milan", "Mile",
        "Mirko", "Miroslav", "Mislav", "Mladen", "Nenad", "Niko",
        "Nikola", "Nikša", "Patrik", "Pavao", "Pero", "Petar", "Robert",
        "Roko", "Romano", "Rudolf", "Saša", "Siniša", "Slavko", "Stjepan",
        "Tomislav", "Tomo", "Toni", "Valter", "Vedran", "Viktor",
        "Vjekoslav", "Vladimir", "Vlado", "Zdravko", "Zlatko", "Zoran",
        "Zvonko", "Đuro", "Šime", "Željko",
    ]

    first_names_female = [
        "Albina", "Ana", "Andrea", "Ane", "Anica", "Anita", "Anka",
        "Ankica", "Antonija", "Anđa", "Anđela", "Bara", "Barbara",
        "Barica", "Biljana", "Biserka", "Božena", "Božica", "Branka",
        "Danica", "Danijela", "Dora", "Draga", "Dragica", "Elizabeta",
        "Ema", "Eva", "Franciska", "Fuma", "Gordana", "Hana", "Ika",
        "Iva", "Ivana", "Ivanka", "Ivka", "Jadranka", "Jana", "Janja",
        "Jasminka", "Jasna", "Jele", "Jelena", "Josipa", "Julijana",
        "Karla", "Kata", "Katarina", "Kate", "Katica", "Kristina", "Lana",
        "Lara", "Laura", "Lea", "Lidija", "Ljiljana", "Ljubica", "Lorena",
        "Lucija", "Maja", "Manda", "Mara", "Mare", "Maria", "Marica",
        "Marija", "Marijana", "Marina", "Marta", "Martina", "Matea",
        "Mateja", "Matija", "Mia", "Milena", "Milica", "Milka", "Mira",
        "Mirjana", "Nada", "Nataša", "Nevenka", "Nika", "Nikolina",
        "Nina", "Petra", "Renata", "Rozalija", "Ruža", "Ružica",
        "Sandra", "Sanja", "Sara", "Slavica", "Snježana", "Stana",
        "Suzana", "Tatjana", "Tea", "Terezija", "Valentina", "Vera",
        "Veronika", "Vesna", "Zdenka", "Zora", "Zorka", "Đurđica",
        "Štefanija", "Štefica", "Željka",
    ]

    first_names = first_names_female + first_names_male
    last_names = [
        "Abičić", "Abramović", "Adžijević", "Akmačić", "Alković",
        "Amanović", "Amidžić", "Andrašek", "Andrijašević", "Andrijević",
        "Aničić", "Antić", "Antolković", "Antonić", "Babić", "Bajan",
        "Baksa", "Balatinac", "Balinčić", "Balić", "Baljak", "Ban",
        "Baničević", "Banko", "Banovac", "Barac", "Barać", "Barbieri",
        "Barbir", "Barbić", "Barešić", "Barić", "Baričević", "Barišić",
        "Barković", "Barnaba", "Barušić", "Batrac", "Batrnek", "Bazjak",
        "Bačak", "Bačić", "Bašić", "Bašnec", "Bebić", "Begonja", "Beletić",
        "Belošević", "Benić", "Benčić", "Beraković", "Bernardić", "Bertoša",
        "Bezić", "Bijelić", "Bingula", "Birkić", "Birtić", "Bićanić",
        "Bičak", "Bičanić", "Bjeliš", "Blagaić", "Blažek", "Blažević",
        "Blažičko", "Boban", "Bobanović", "Bogadi", "Bogdan", "Bogović",
        "Bojanić", "Boljkovac", "Bolčević", "Borak", "Borojević", "Borošak",
        "Bosilj", "Botica", "Botić", "Bošnjak", "Bošnjaković", "Božanić",
        "Božanović", "Božiković", "Božić", "Božičević", "Božičković",
        "Bradić", "Brajković", "Bralić", "Brandić", "Branković", "Bračun",
        "Brcko", "Brezjan", "Britvec", "Brlas", "Brlek", "Brletić", "Bukvić",
        "Buljan", "Bungić", "Bunić", "Bunčić", "Burić", "Burčul", "Buršić",
        "Butković", "Buzov", "Bučanac", "Bučar", "Bušljeta", "Cafuk", "Car",
        "Carić", "Cestarić", "Ciganović", "Cik", "Cindrić", "Colić", "Crevar",
        "Crneković", "Crnković", "Cukon", "Culi", "Cvenić", "Cvetković",
        "Cvetnić", "Cvitan", "Cvrtila", "Dabo", "Damijanić", "Damjanović",
        "Darojković", "Dautanec", "Dautović", "Debelić", "Derežić", "Deže",
        "Didović", "Dizdar", "Dobrić", "Dolinar", "Dolić", "Dominiković",
        "Dominković", "Dončević", "Dragičević", "Dragobratović", "Dragojević",
        "Drakulić", "Drandić", "Dražić", "Dretvić", "Dubovečak", "Dujmović",
        "Dukić", "Duvančić", "Dvojak", "Džapo", "Erceg", "Ercegović",
        "Ergotić", "Eršek", "Eterović", "Fabijanić", "Ferenac", "Filar",
        "Filipović", "Filipčić", "Flego", "Forjan", "Franić", "Franičević",
        "Franjić", "Franušić", "Friščić", "Frketić", "Fuček", "Gabud",
        "Galešić", "Galić", "Galović", "Gegić", "Gelemanović", "Glasnović",
        "Glavan", "Glavor", "Gligora", "Godinić", "Golubić", "Gotić",
        "Govorčinović", "Gracin", "Grba", "Grbac", "Gredičak", "Gregov",
        "Grgić", "Grgurević", "Grgurić", "Grgurovac", "Grubišić", "Gržetić",
        "Gržinčić", "Guberović", "Gudelj", "Gulan", "Guštin", "Hadrović",
        "Hadžić", "Halambek", "Halapir", "Hanžek", "Harapin", "Hardi",
        "Herceg", "Herout", "Hećimović", "Hinić", "Hodak", "Horak", "Horvat",
        "Horvatek", "Horvatinec", "Horvatić", "Hrabar", "Hranić", "Hranj",
        "Hrastinski", "Hren", "Hrvojić", "Hršak", "Hrženjak", "Huljev",
        "Husnjak", "Ignac", "Ilijić", "Ilinović", "Ilić", "Ivandić",
        "Ivanović", "Ivančan", "Ivšić", "Jagarinec", "Jagečić", "Jakopec",
        "Jakopović", "Jakovac", "Jaković", "Jakovljević", "Jakupić", "Jakuš",
        "Jasprica", "Jelavić", "Jelić", "Jemrić", "Jerković", "Jonjić",
        "Josipović", "Jovanovac", "Jovanović", "Jović", "Jozić", "Jugovac",
        "Jukić", "Juretić", "Jureško", "Jurić", "Jurišić", "Jurjević",
        "Jurković", "Jurlina", "Jurčić", "Kadija", "Kahlina", "Kalanjoš",
        "Kalazić", "Kaniški", "Karagić", "Karamarko", "Karlović", "Karmelić",
        "Karuza", "Katić", "Kauzlarić", "Keleković", "Kelečić", "Kelić",
        "Kereković", "Kevo", "Kinkela", "Kirinčić", "Klanac", "Klarin",
        "Klarić", "Klasić", "Kligl", "Knezović", "Knežević", "Kocijančić",
        "Kokanović", "Kokorić", "Kolarec", "Kolega", "Kolić", "Komar",
        "Komljenović", "Kopjar", "Kos", "Kosanović", "Kosić", "Kostanić",
        "Kostelac", "Kovač", "Kovaček", "Kovačević", "Kovačić", "Koški",
        "Koščević", "Krajcar", "Kralj", "Kraljević", "Kraljić", "Kramarić",
        "Kresonja", "Križan", "Krpan", "Krznarić", "Krčelić", "Kršanac",
        "Krželj", "Kujundžić", "Kukučka", "Kunac", "Kupsjak", "Kurtoić",
        "Kuveždić", "Kuzmić", "Kučić", "Kuščević", "Labaš", "Labinjan",
        "Ladavac", "Lakošeljac", "Lasić", "Lazar", "Legović", "Lelas",
        "Lenić", "Lešić", "Lešković", "Leščić", "Liber", "Licul", "Liović",
        "Lisica", "Ljubetić", "Ljubić", "Ljubičić", "Lojen", "Lorencin",
        "Lovrić", "Lucić", "Lukinić", "Lukić", "Lukša", "Lukšić", "Lučić",
        "Macan", "Madunić", "Magić", "Mahnet", "Majdenić", "Majstorović",
        "Makovac", "Maletić", "Malnar", "Maloča", "Mamić", "Mamula", "Maras",
        "Marasović", "Maraš", "Mardešić", "Maretić", "Marijanović", "Marin",
        "Marinković", "Marinović", "Marić", "Maričević", "Marjanović",
        "Markanjević", "Markovac", "Marković", "Markuš", "Martinić",
        "Martinović", "Martinčević", "Martić", "Marušić", "Maršić", "Maržić",
        "Matahlija", "Matana", "Matas", "Mateša", "Matijaš", "Matijević",
        "Matić", "Matko", "Matković", "Matokanović", "Matovina", "Matošević",
        "Matulin", "Matulić", "Mavra", "Maćešić", "Medač", "Medić", "Medved",
        "Meić", "Merkaš", "Mesarić", "Mesić", "Mihalić", "Mihaljević",
        "Mihelčić", "Mihić", "Mikić", "Miklečić", "Mikulandra", "Mikulec",
        "Mikulčić", "Milas", "Milatić", "Miletić", "Milevoj", "Milina",
        "Miličić", "Miloslavić", "Milotić", "Milovac", "Mimica", "Miočić",
        "Mirosavljević", "Mirt", "Mičetić", "Mišak", "Miše", "Mišković",
        "Modrić", "Mofardin", "Morić", "Moscarda", "Moslavac", "Močibob",
        "Mraović", "Mudri", "Mudronja", "Mustapić", "Mustač", "Mušćet",
        "Mužina", "Mužić", "Nakić", "Načinović", "Nedić", "Nikolić", "Nimac",
        "Nišević", "Nižetić", "Norac", "Novak", "Novosel", "Obradović",
        "Obratov", "Odobašić", "Orbanić", "Orešković", "Orlić", "Orlović",
        "Oršolić", "Oršoš", "Oršulić", "Ozimec", "Pajur", "Palić", "Pamić",
        "Pandurić", "Papak", "Paparić", "Paradi", "Pavelić", "Pavin", "Pavić",
        "Pavičić", "Pavković", "Pavlović", "Pecotić", "Pedišić", "Peharda",
        "Penić", "Perak", "Perić", "Perišić", "Perkov", "Perković", "Peroš",
        "Peruško", "Perčić", "Petek", "Peterlik", "Petrić", "Petričević",
        "Petrović", "Pečur", "Peša", "Pešić", "Pikec", "Piljek", "Pintarić",
        "Plantak", "Plantek", "Plažanin", "Pleše", "Pokas", "Pokos", "Polić",
        "Poljak", "Polonijo", "Polović", "Pongrac", "Popović", "Poropat",
        "Poslon", "Pozder", "Požega", "Predovan", "Prelec", "Preočanin",
        "Pribanić", "Priselac", "Prpić", "Prskalo", "Prtenjača", "Puharić",
        "Puljiz", "Putinja", "Puškarić", "Radelić", "Radin", "Radinović",
        "Radić", "Radman", "Radojković", "Radolović", "Radović", "Radočaj",
        "Radošević", "Raguž", "Rahija", "Rajn", "Rajčić", "Rakela", "Rakuljić",
        "Raljević", "Raspor", "Rastija", "Rađenović", "Rašeta", "Rašić",
        "Ražov", "Rebić", "Rendulić", "Resanović", "Ribarić", "Ribić",
        "Ribičić", "Rijetković", "Risek", "Ritoša", "Ričko", "Roca", "Roce",
        "Rogošić", "Rojnić", "Roso", "Rubeša", "Rubinić", "Rukavina", "Rumora",
        "Sabljak", "Sabol", "Sakač", "Salopek", "Sardelić", "Sedlar",
        "Semialjac", "Seničić", "Seršić", "Sever", "Sikirić", "Simić",
        "Sinožić", "Sirotić", "Skupnjak", "Sladonja", "Slavica", "Smoković",
        "Smolić", "Sobota", "Sokač", "Sokić", "Sokol", "Soldo", "Solomun",
        "Sorić", "Sošić", "Sršen", "Stanić", "Staničić", "Stančin",
        "Starčević", "Stipanović", "Stiperski", "Stojanov", "Stojnić",
        "Stojčević", "Stolnik", "Stošić", "Stražičić", "Strinavić", "Stupalo",
        "Surać", "Svetličić", "Tepeš", "Terlević", "Terzić", "Tešija",
        "Tisaj", "Toić", "Tolj", "Tomić", "Tomičić", "Tomljanović", "Tonc",
        "Topić", "Totić", "Trbović", "Trgovčić", "Triplat", "Trnski",
        "Trutanić", "Tudić", "Tudor", "Tuksar", "Turina", "Turk", "Turudić",
        "Turčinov", "Tuđa", "Tušek", "Tuškan", "Ugrinić", "Ukić", "Urlić",
        "Ušić", "Vaci", "Valentić", "Valjetić", "Varga", "Veić", "Vela",
        "Vidaković", "Vidas", "Vidov", "Vidović", "Viljevac", "Vincetić",
        "Vitasović", "Vižintin", "Vladislavić", "Vlašić", "Vojković",
        "Volarević", "Volarić", "Vorkapić", "Vozila", "Vrabelj", "Vranić",
        "Vrban", "Vretenar", "Vrhovec", "Vugdelija", "Vugec", "Vuk",
        "Vukman", "Vukobratović", "Vuković", "Vukušić", "Vuljak", "Vučetić",
        "Vučin", "Vučković", "Zakinja", "Zanoški", "Zeba", "Zebec", "Zelić",
        "Zgorelec", "Zmaić", "Zrilić", "Zrinski", "Zubčić", "Ćorić", "Ćosić",
        "Ćurić", "Čagalj", "Čargonja", "Čizmić", "Čiš", "Čižmešija", "Čop",
        "Čotić", "Čović", "Čubrić", "Čudić", "Čukman", "Čulina", "Čuljak",
        "Čupić", "Čuček", "Đurašević", "Đurinić", "Šalić", "Šantić", "Šargač",
        "Šarić", "Šarlija", "Šegović", "Šelendić", "Šeparović", "Šestak",
        "Šestan", "Šibalić", "Šimara", "Šimić", "Šimičić", "Šimunić",
        "Šimunović", "Šinković", "Šipek", "Šipić", "Šitum", "Škara", "Škoda",
        "Škrlin", "Škrnički", "Škrtić", "Škugor", "Škunca", "Šokčević",
        "Šošić", "Šoštarić", "Špika", "Špišić", "Špoljarić", "Špralja",
        "Štefanec", "Štefović", "Štifanić", "Štimac", "Štrbac", "Štrljić",
        "Šturlan", "Šunjić", "Šupraha", "Šuran", "Šurbek", "Šurina", "Šverko",
        "Žabjačan", "Žagar", "Žerjav", "Žeželić", "Žic", "Žiković", "Živić",
        "Živković", "Žufika", "Žugec", "Žunec", "Županić", "Žuvela", "Žužić",
    ]
