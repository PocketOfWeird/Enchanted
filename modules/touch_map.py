from typing import List


def touch_map(index: int) -> List: 
    files = {
        0 : ["audio/switch_homestar.ogg","audio/switch_strongbad.ogg"],
        1 : ["audio/hs_heystupid.ogg","audio/hs_canubelieveit.ogg","audio/hs_itsdotcom.ogg","audio/hs_notlookgood.ogg", "audio/hs_email.ogg", "audio/hs_error.ogg"],
        2 : ["audio/sb_dubdeuce.ogg","audio/sb_pizza.ogg","audio/sb_email.ogg"],
        3 : ["audio/bubs_dontutalk.ogg","audio/bubs_ladylike.ogg"],
        4 : ["audio/cz_eatthechort.ogg","audio/cz_jeorghb.ogg"],
        5 : ["audio/ss_frustrating.ogg","audio/ss_sadflying.ogg"],
        6 : ["audio/song_everybody.ogg","audio/song_limit.ogg"]
    }
    return files[index]