# 🔹 Klíčová slova pro filtrování článků
KEYWORDS = [
    "armáda české republiky", "armáda", "armády", "armádní", "armádních",
    "vojáci", "vojáků", "vojákům", "voják",
    "AČR", "obrana", "ministerstvo obrany", "vojenské", "vojenská", "vojenští",
    "vojenské cvičení", "armadní cvičení",

    "česká armáda", "czech army", "generální štáb", "gš ačr",
    "náčelník generálního štábu", "mo čr", "ministerstvo obrany čr",
    "vojenská policie", "vojenské zpravodajství", "vojenské správy",
    "vojenský útvar", "vojenská akademie",

    "vojenská technika", "vojenské vozidlo", "vojenské letadlo",
    "tanky", "dělostřelectvo", "pěchota", "speciální síly",
    "výsadkáři", "prapor", "pluk", "brigáda",
    "generál ", "vojenský pilot", "vojenský lékař",

    "bojová vozidla", "stíhačky", "vrtulníky",
    "pandur", "leopard", "gripen", "bvp", "dana", "t-72",
    "modernizace armády", "nákup techniky", "akvizice armády",

    "nato", "severoatlantická aliance",
    "zahraniční operace", "operace v zahraničí", "spojenecké síly", 
    "mezinárodní cvičení", "obranná spolupráce", "vojenská pomoc",

    "mobilizace", "odvod", "záložníci", "aktivní záloha",
    "vojenská služba", "branná povinnost", "vojenský rozpočet",
    "obranná strategie", "obranný průmysl", "letectvo",
    "pozemní síly", "chemici", "ženisté", "spojaři", "logistika armády",
    "vojenský výcvik", "vojenské školy", "vojenské stipendium",
    "vojenský lékař"
]

def contains_keywords(text):
    """Ověří, zda text obsahuje některé z klíčových slov"""
    return any(keyword.lower() in text.lower() for keyword in KEYWORDS)