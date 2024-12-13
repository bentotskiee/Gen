from fuzzywuzzy import process

# Expanded dictionary for Gen Z words translation in both English and Tagalog
GEN_Z_TRANSLATIONS = {
    "salty": {"en": "annoyed or upset", "tl": "naiinis o nagagalit"},
    "lit": {"en": "amazing or exciting", "tl": "kamangha-mangha o kapana-panabik"},
    "ghosted": {"en": "ignored or avoided", "tl": "iniiwasan o binabalewala"},
    "slay": {"en": "perform exceptionally well", "tl": "gumanap ng napakahusay"},
    "yeet": {"en": "to throw something with force", "tl": "ihagis nang malakas"},
    "savage": {"en": "bold and unfiltered", "tl": "matapang at walang preno"},
    "no cap": {"en": "no lie, or seriously", "tl": "seryoso, walang biro"},
    "bop": {"en": "a really good song", "tl": "isang magandang kanta"},
    "drip": {"en": "stylish or fashionable", "tl": "astig o fashionable"},
    "fam": {"en": "close friends or family", "tl": "malalapit na kaibigan o pamilya"},
    "W": {"en": "shorthand for win", "tl": "panalo"},
    "L": {"en": "shorthand for loss/losing", "tl": "pagkatalo"},
    "L+ratio": {"en": "bad internet response", "tl": "masamang tugon sa internet"},
    "dank": {"en": "excellent or very high quality", "tl": "napakahusay o mataas ang kalidad"},
    "cheugy": {"en": "outdated or uncool", "tl": "luma o hindi uso"},
    "lodi": {"en": "idol", "tl": "iniidolo"},
    "petmalu": {"en": "amazing", "tl": "kahanga-hanga"},
    "werpa": {"en": "power", "tl": "lakas"},
    "rush": {"en": "in a hurry", "tl": "nagmamadali"},
    "ormoc": {"en": "completely okay", "tl": "ayos na ayos"},
    "shook": {"en": "shocked", "tl": "nagulat"},
    "sus": {"en": "suspicious", "tl": "kahina-hinala"},
    "clout": {"en": "influence", "tl": "impluwensya"},
    "vibe": {"en": "feeling", "tl": "pakiramdam"},
    "bet": {"en": "agreement", "tl": "sang-ayon"},
    "slaps": {"en": "awesome", "tl": "malupit"},
    "simp": {"en": "overly attentive", "tl": "sobrang magbigay"},
    "fomo": {"en": "fear of missing out", "tl": "takot na mawalan ng pagkakataon"},
    "stan": {"en": "superfan", "tl": "masugid na tagahanga"},
    "flex": {"en": "show off", "tl": "ipakita"},
    "cap": {"en": "lie", "tl": "kasinungalingan"},
    "lowkey": {"en": "subtle", "tl": "tahimik"},
    "highkey": {"en": "obvious", "tl": "hayag"},
    "mood": {"en": "current feeling", "tl": "pakiramdam"},
    "canceled": {"en": "rejected", "tl": "itinakwil"},
    "cringe": {"en": "awkward", "tl": "nakakahiya"},
    "hype": {"en": "excitement", "tl": "kasiyahan"},
    "bussin": {"en": "delicious", "tl": "masarap"},
    "glow up": {"en": "improve appearance", "tl": "paganda"},
    "tea": {"en": "gossip", "tl": "tsismis"},
    "squad": {"en": "friend group", "tl": "barkada"},
    "bae": {"en": "significant other", "tl": "karelasyon"},
    "vibe check": {"en": "assess energy", "tl": "suriin ang vibe"},
    "jelly": {"en": "jealous", "tl": "selos"},
    "TMI": {"en": "too much info", "tl": "sobrang impormasyon"},
    "throw shade": {"en": "insult", "tl": "manlait"},
    "on fleek": {"en": "perfectly done", "tl": "perpekto"},
    "stay woke": {"en": "be aware", "tl": "maging alerto"},
    "turnt": {"en": "excited", "tl": "masaya"},
    "yasss": {"en": "yes with excitement", "tl": "oo ng masaya"},
    "catch feelings": {"en": "develop emotions", "tl": "magka-feelings"},
    "ship": {"en": "support a relationship", "tl": "suportahan ang relasyon"},
    "zaddy": {"en": "stylish man", "tl": "astig na lalaki"},
    "tbh": {"en": "to be honest", "tl": "sa totoo lang"},
    "finesse": {"en": "skillfully handle", "tl": "gamitin ang galing"},
    "deadass": {"en": "seriously", "tl": "seryoso"},
    "vibe out": {"en": "chill with the mood", "tl": "sumabay sa vibe"},
    "boss": {"en": "leader", "tl": "lider"},
    "periodt": {"en": "end of statement", "tl": "tapos na"},
    "big mood": {"en": "relatable feeling", "tl": "pakiramdam na relatable"},
    "hundo p": {"en": "100% sure", "tl": "siguradong-sigurado"},
    "awit": {"en": "disappointment", "tl": "dismaya"},
    "charot": {"en": "just kidding", "tl": "biro lang"},
    "sanaol": {"en": "wish everyone", "tl": "sana lahat"},
    "beshie": {"en": "best friend", "tl": "matalik na kaibigan"},
    "walwal": {"en": "drunk", "tl": "lasing"},
    "banas": {"en": "irritated", "tl": "naiinis"},
    "chika": {"en": "talk", "tl": "kwento"},
    "push": {"en": "go ahead", "tl": "ituloy"},
    "momshie": {"en": "endearing friend term", "tl": "tawag sa kaibigan"},
    "lowbat": {"en": "exhausted", "tl": "pagod"},
    "pagod si lodi": {"en": "admired but tired", "tl": "hinihangaang pagod"},
    "boom panis": {"en": "success", "tl": "tagumpay"},
    "tropa": {"en": "group of friends", "tl": "barkada"},
    "astig": {"en": "cool", "tl": "maangas"},
    "hanash": {"en": "complaint or issue", "tl": "reklamo"},
    "laglag pants": {"en": "epic fail", "tl": "palpak"},
    "englot": {"en": "confused", "tl": "nalilito"},
    "dasurv": {"en": "deserved", "tl": "nararapat"},
}


def translate_genz_word(word, lang="en"):
    """
    Translates a Gen Z word into either English or Tagalog.
    :param word: The Gen Z word to translate.
    :param lang: The language for the translation (either 'en' or 'tl').
    :return: The translated word or an error message if not found.
    """
    translation = GEN_Z_TRANSLATIONS.get(word.lower())
    if translation:
        return translation.get(lang, "Translation not available in this language.")
    return "Translation not found."

def suggest_closest_word(word):
    """
    Suggests the closest matching Gen Z word using FuzzyWuzzy.
    :param word: The input word.
    :return: The closest matching word or an empty string if none is found.
    """
    gen_z_words = list(GEN_Z_TRANSLATIONS.keys())
    closest_match, score = process.extractOne(word.lower(), gen_z_words)
    return closest_match if score >= 70 else ""
