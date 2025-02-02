import os
import json
from googletrans.constants import LANGUAGES

MAX_RETRY = 5
MAX_FTB_QUEST_FILES = 200
MAX_MODPACK_NAME_LEN = 15

MESSAGES = dict()
for filename in os.listdir("lang"):
    base, ext = os.path.splitext(filename)
    if ext == ".json":
        MESSAGES[base] = json.load(open(f"lang/{filename}", "r", encoding="utf-8-sig"))

MINECRAFT_LOCALES = [
    "af_za",
    "ar_sa",
    "ast_es",
    "az_az",
    "ba_ru",
    "bar",
    "be_by",
    "bg_bg",
    "br_fr",
    "brb",
    "bs_ba",
    "ca_es",
    "cs_cz",
    "cy_gb",
    "da_dk",
    "de_at",
    "de_ch",
    "de_de",
    "el_gr",
    "en_au",
    "en_ca",
    "en_gb",
    "en_nz",
    "en_pt",
    "en_ud",
    "en_us",
    "enp",
    "enws",
    "eo_uy",
    "es_ar",
    "es_cl",
    "es_ec",
    "es_es",
    "es_mx",
    "es_uy",
    "es_ve",
    "esan",
    "et_ee",
    "eu_es",
    "fa_ir",
    "fi_fi",
    "fil_ph",
    "fo_fo",
    "fr_ca",
    "fr_fr",
    "fra_de",
    "fur_it",
    "fy_nl",
    "ga_ie",
    "gd_gb",
    "gl_es",
    "haw_us",
    "he_il",
    "hi_in",
    "hr_hr",
    "hu_hu",
    "hy_am",
    "id_id",
    "ig_ng",
    "io_en",
    "is_is",
    "isv",
    "it_it",
    "ja_jp",
    "jbo_en",
    "ka_ge",
    "kk_kz",
    "kn_in",
    "ko_kr",
    "ksh",
    "kw_gb",
    "la_la",
    "lb_lu",
    "li_li",
    "lmo",
    "lo_la",
    "lol_us",
    "lt_lt",
    "lv_lv",
    "lzh",
    "mk_mk",
    "mn_mn",
    "ms_my",
    "mt_mt",
    "nah",
    "nds_de",
    "nl_be",
    "nl_nl",
    "nn_no",
    "no_no",
    "oc_fr",
    "ovd",
    "pl_pl",
    "pt_br",
    "pt_pt",
    "qya_aa",
    "ro_ro",
    "rpr",
    "ru_ru",
    "ry_ua",
    "sah_sah",
    "se_no",
    "sk_sk",
    "sl_si",
    "so_so",
    "sq_al",
    "sr_cs",
    "sr_sp",
    "sv_se",
    "sxu",
    "szl",
    "ta_in",
    "th_th",
    "tl_ph",
    "tlh_aa",
    "tok",
    "tr_tr",
    "tt_ru",
    "uk_ua",
    "val_es",
    "vec_it",
    "vi_vn",
    "yi_de",
    "yo_ng",
    "zh_cn",
    "zh_hk",
    "zh_tw",
    "zlm_arab"
]

MINECRAFT_LANGUAGES = {
    "af_za": "Afrikaans",
    "ar_sa": "Arabic",
    "az_az": "Azerbaijani",
    "be_by": "Belarusian",
    "bg_bg": "Bulgarian",
    "bs_ba": "Bosnian",
    "ca_es": "Catalan",
    "cs_cz": "Czech",
    "cy_gb": "Welsh",
    "da_dk": "Danish",
    "de_at": "German",
    "de_ch": "German",
    "de_de": "German",
    "el_gr": "Greek",
    "en_au": "English",
    "en_ca": "English",
    "en_gb": "English",
    "en_nz": "English",
    "en_pt": "English",
    "en_ud": "English",
    "en_us": "English",
    "eo_uy": "Esperanto",
    "es_ar": "Spanish",
    "es_cl": "Spanish",
    "es_ec": "Spanish",
    "es_es": "Spanish",
    "es_mx": "Spanish",
    "es_uy": "Spanish",
    "es_ve": "Spanish",
    "et_ee": "Estonian",
    "eu_es": "Basque",
    "fa_ir": "Persian",
    "fi_fi": "Finnish",
    "fr_ca": "French",
    "fr_fr": "French",
    "fy_nl": "Frisian",
    "ga_ie": "Irish",
    "gd_gb": "Scots Gaelic",
    "gl_es": "Galician",
    "haw_us": "Hawaiian",
    "he_il": "Hebrew",
    "hi_in": "Hindi",
    "hr_hr": "Croatian",
    "hu_hu": "Hungarian",
    "hy_am": "Armenian",
    "id_id": "Indonesian",
    "ig_ng": "Igbo",
    "is_is": "Icelandic",
    "it_it": "Italian",
    "ja_jp": "Japanese",
    "ka_ge": "Georgian",
    "kk_kz": "Kazakh",
    "kn_in": "Kannada",
    "ko_kr": "Korean",
    "la_la": "Latin",
    "lb_lu": "Luxembourgish",
    "lo_la": "Lao",
    "lt_lt": "Lithuanian",
    "lv_lv": "Latvian",
    "mk_mk": "Macedonian",
    "mn_mn": "Mongolian",
    "ms_my": "Malay",
    "mt_mt": "Maltese",
    "nl_be": "Dutch",
    "nl_nl": "Dutch",
    "no_no": "Norwegian",
    "pl_pl": "Polish",
    "pt_br": "Portuguese",
    "pt_pt": "Portuguese",
    "ro_ro": "Romanian",
    "ru_ru": "Russian",
    "sk_sk": "Slovak",
    "sl_si": "Slovenian",
    "so_so": "Somali",
    "sq_al": "Albanian",
    "sr_cs": "Serbian",
    "sr_sp": "Serbian",
    "sv_se": "Swedish",
    "ta_in": "Tamil",
    "th_th": "Thai",
    "tl_ph": "Filipino",
    "tr_tr": "Turkish",
    "uk_ua": "Ukrainian",
    "vi_vn": "Vietnamese",
    "yi_de": "Yiddish",
    "yo_ng": "Yoruba",
    "zh_cn": "Chinese (Simplified)",
    "zh_tw": "Chinese (Traditional)"
}

MINECRAFT_TO_GOOGLE = {
    "af_za": "af",
    "ar_sa": "ar",
    "az_az": "az",
    "be_by": "be",
    "bg_bg": "bg",
    "bs_ba": "bs",
    "ca_es": "ca",
    "cs_cz": "cs",
    "cy_gb": "cy",
    "da_dk": "da",
    "de_at": "de",
    "de_ch": "de",
    "de_de": "de",
    "el_gr": "el",
    "en_au": "en",
    "en_ca": "en",
    "en_gb": "en",
    "en_nz": "en",
    "en_pt": "en",
    "en_ud": "en",
    "en_us": "en",
    "eo_uy": "eo",
    "es_ar": "es",
    "es_cl": "es",
    "es_ec": "es",
    "es_es": "es",
    "es_mx": "es",
    "es_uy": "es",
    "es_ve": "es",
    "et_ee": "et",
    "eu_es": "eu",
    "fa_ir": "fa",
    "fi_fi": "fi",
    "fr_ca": "fr",
    "fr_fr": "fr",
    "fy_nl": "fy",
    "ga_ie": "ga",
    "gd_gb": "gd",
    "gl_es": "gl",
    "haw_us": "haw",
    "he_il": "he",
    "hi_in": "hi",
    "hr_hr": "hr",
    "hu_hu": "hu",
    "hy_am": "hy",
    "id_id": "id",
    "ig_ng": "ig",
    "is_is": "is",
    "it_it": "it",
    "ja_jp": "ja",
    "ka_ge": "ka",
    "kk_kz": "kk",
    "kn_in": "kn",
    "ko_kr": "ko",
    "la_la": "la",
    "lb_lu": "lb",
    "lo_la": "lo",
    "lt_lt": "lt",
    "lv_lv": "lv",
    "mk_mk": "mk",
    "mn_mn": "mn",
    "ms_my": "ms",
    "mt_mt": "mt",
    "nl_be": "nl",
    "nl_nl": "nl",
    "no_no": "no",
    "pl_pl": "pl",
    "pt_br": "pt",
    "pt_pt": "pt",
    "ro_ro": "ro",
    "ru_ru": "ru",
    "sk_sk": "sk",
    "sl_si": "sl",
    "so_so": "so",
    "sq_al": "sq",
    "sr_cs": "sr",
    "sr_sp": "sr",
    "sv_se": "sv",
    "ta_in": "ta",
    "th_th": "th",
    "tl_ph": "tl",
    "tr_tr": "tr",
    "uk_ua": "uk",
    "vi_vn": "vi",
    "yi_de": "yi",
    "yo_ng": "yo",
    "zh_cn": "zh-cn",
    "zh_tw": "zh-tw"
}

MINECRAFT_TO_DEEPL = {
    "ar_sa": "AR",
    "bg_bg": "BG",
    "cs_cz": "CS",
    "da_dk": "DA",
    "de_at": "DE",
    "de_ch": "DE",
    "de_de": "DE",
    "el_gr": "EL",
    "en_au": "EN-GB",
    "en_ca": "EN-US",
    "en_gb": "EN-GB",
    "en_nz": "EN-GB",
    "en_pt": "EN-US",
    "en_ud": "EN-US",
    "en_us": "EN-US",
    "es_ar": "ES",
    "es_cl": "ES",
    "es_ec": "ES",
    "es_es": "ES",
    "es_mx": "ES",
    "es_uy": "ES",
    "es_ve": "ES",
    "et_ee": "ET",
    "fi_fi": "FI",
    "fr_ca": "FR",
    "fr_fr": "FR",
    "hu_hu": "HU",
    "id_id": "ID",
    "it_it": "IT",
    "ja_jp": "JA",
    "ko_kr": "KO",
    "lt_lt": "LT",
    "lv_lv": "LV",
    "nl_nl": "NL",
    "no_no": "NB",
    "pl_pl": "PL",
    "pt_br": "PT-BR",
    "pt_pt": "PT-PT",
    "ro_ro": "RO",
    "ru_ru": "RU",
    "sk_sk": "SK",
    "sl_si": "SL",
    "sv_se": "SV",
    "tr_tr": "TR",
    "uk_ua": "UK",
    "zh_cn": "ZH"
}

if __name__ == "__main__":
    MINECRAFT_LANGUAGES = dict()
    MINECRAFT_TO_GOOGLE = dict()
    for lang in MINECRAFT_LOCALES:
        _lang = lang.replace("_", "-")
        if LANGUAGES.get(_lang):
            MINECRAFT_LANGUAGES[lang] = LANGUAGES[_lang].title()
            MINECRAFT_TO_GOOGLE[lang] = _lang
            continue
        _lang = _lang.split("-")[0]
        if LANGUAGES.get(_lang):
            MINECRAFT_LANGUAGES[lang] = LANGUAGES[_lang].title()
            MINECRAFT_TO_GOOGLE[lang] = _lang
            continue