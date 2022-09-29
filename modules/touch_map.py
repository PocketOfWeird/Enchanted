from typing import List


def touch_map(index: int) -> List: 
    files = {
        0 : ["~/Documents/GitHub/Enchanted/audio/switch_homestar.mp3","~/Documents/GitHub/Enchanted/audio/switch_strongbad.mp3"],
        1 : ["~/Documents/GitHub/Enchanted/audio/hs_heystupid.mp3","~/Documents/GitHub/Enchanted/audio/hs_canubelieveit.mp3","~/Documents/GitHub/Enchanted/audio/hs_itsdotcom.mp3","~/Documents/GitHub/Enchanted/audio/hs_notlookgood.mp3", "hs_email.mp3", "hs_error.mp3"],
        2 : ["~/Documents/GitHub/Enchanted/audio/sb_dubdeuce.mp3","~/Documents/GitHub/Enchanted/audio/sb_system.mp3","~/Documents/GitHub/Enchanted/audio/sb_pizza.mp3","sb_email.mp3"],
        3 : ["~/Documents/GitHub/Enchanted/audio/bubs_dontutalk.mp3","~/Documents/GitHub/Enchanted/audio/bubs_ladylike.mp3"],
        4 : ["~/Documents/GitHub/Enchanted/audio/cz_eatthechort.mp3","~/Documents/GitHub/Enchanted/audio/cz_jeorghb.mp3"],
        5 : ["~/Documents/GitHub/Enchanted/audio/ss_frustrating.mp3","~/Documents/GitHub/Enchanted/audio/ss_sadflying.mp3"],
        6 : ["~/Documents/GitHub/Enchanted/audio/song_everybody.mp3","~/Documents/GitHub/Enchanted/audio/song_limit.mp3"]
    }
    return files[index]