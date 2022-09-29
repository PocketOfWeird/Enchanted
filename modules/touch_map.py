from typing import List


def touch_map(index: int) -> List: 
    files = {
        0 : ["audio/switch_homestar.mp3","audio/switch_strongbad.mp3"],
        1 : ["audio/hs_heystupid.mp3","audio/hs_canubelieveit.mp3","audio/hs_itsdotcom.mp3","audio/hs_notlookgood.mp3", "audio/hs_email.mp3", "audio/hs_error.mp3"],
        2 : ["audio/sb_dubdeuce.mp3","audio/sb_system.mp3","audio/sb_pizza.mp3","audio/sb_email.mp3"],
        3 : ["audio/bubs_dontutalk.mp3","audio/bubs_ladylike.mp3"],
        4 : ["audio/cz_eatthechort.mp3","audio/cz_jeorghb.mp3"],
        5 : ["audio/ss_frustrating.mp3","audio/ss_sadflying.mp3"],
        6 : ["audio/song_everybody.mp3","audio/song_limit.mp3"]
    }
    return files[index]