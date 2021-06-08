"""This module contains the general information for TopSystem ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class TopSystemConsts:
    MODE_CLUSTER = "cluster"
    MODE_STAND_ALONE = "stand-alone"
    MODE_UNSPECIFIED = "unspecified"
    TIME_ZONE_AFRICA_ABIDJAN = "Africa/Abidjan"
    TIME_ZONE_AFRICA_ACCRA = "Africa/Accra"
    TIME_ZONE_AFRICA_ADDIS_ABABA = "Africa/Addis Ababa"
    TIME_ZONE_AFRICA_ALGIERS = "Africa/Algiers"
    TIME_ZONE_AFRICA_ASMARA = "Africa/Asmara"
    TIME_ZONE_AFRICA_BAMAKO = "Africa/Bamako"
    TIME_ZONE_AFRICA_BANGUI = "Africa/Bangui"
    TIME_ZONE_AFRICA_BANJUL = "Africa/Banjul"
    TIME_ZONE_AFRICA_BISSAU = "Africa/Bissau"
    TIME_ZONE_AFRICA_BLANTYRE = "Africa/Blantyre"
    TIME_ZONE_AFRICA_BRAZZAVILLE = "Africa/Brazzaville"
    TIME_ZONE_AFRICA_BUJUMBURA = "Africa/Bujumbura"
    TIME_ZONE_AFRICA_CAIRO = "Africa/Cairo"
    TIME_ZONE_AFRICA_CASABLANCA = "Africa/Casablanca"
    TIME_ZONE_AFRICA_CEUTA = "Africa/Ceuta"
    TIME_ZONE_AFRICA_CONAKRY = "Africa/Conakry"
    TIME_ZONE_AFRICA_DAKAR = "Africa/Dakar"
    TIME_ZONE_AFRICA_DAR_ES_SALAAM = "Africa/Dar es Salaam"
    TIME_ZONE_AFRICA_DJIBOUTI = "Africa/Djibouti"
    TIME_ZONE_AFRICA_DOUALA = "Africa/Douala"
    TIME_ZONE_AFRICA_EL_AAIUN = "Africa/El Aaiun"
    TIME_ZONE_AFRICA_FREETOWN = "Africa/Freetown"
    TIME_ZONE_AFRICA_GABORONE = "Africa/Gaborone"
    TIME_ZONE_AFRICA_HARARE = "Africa/Harare"
    TIME_ZONE_AFRICA_JOHANNESBURG = "Africa/Johannesburg"
    TIME_ZONE_AFRICA_JUBA = "Africa/Juba"
    TIME_ZONE_AFRICA_KAMPALA = "Africa/Kampala"
    TIME_ZONE_AFRICA_KHARTOUM = "Africa/Khartoum"
    TIME_ZONE_AFRICA_KIGALI = "Africa/Kigali"
    TIME_ZONE_AFRICA_KINSHASA = "Africa/Kinshasa"
    TIME_ZONE_AFRICA_LAGOS = "Africa/Lagos"
    TIME_ZONE_AFRICA_LIBREVILLE = "Africa/Libreville"
    TIME_ZONE_AFRICA_LOME = "Africa/Lome"
    TIME_ZONE_AFRICA_LUANDA = "Africa/Luanda"
    TIME_ZONE_AFRICA_LUBUMBASHI = "Africa/Lubumbashi"
    TIME_ZONE_AFRICA_LUSAKA = "Africa/Lusaka"
    TIME_ZONE_AFRICA_MALABO = "Africa/Malabo"
    TIME_ZONE_AFRICA_MAPUTO = "Africa/Maputo"
    TIME_ZONE_AFRICA_MASERU = "Africa/Maseru"
    TIME_ZONE_AFRICA_MBABANE = "Africa/Mbabane"
    TIME_ZONE_AFRICA_MOGADISHU = "Africa/Mogadishu"
    TIME_ZONE_AFRICA_MONROVIA = "Africa/Monrovia"
    TIME_ZONE_AFRICA_NAIROBI = "Africa/Nairobi"
    TIME_ZONE_AFRICA_NDJAMENA = "Africa/Ndjamena"
    TIME_ZONE_AFRICA_NIAMEY = "Africa/Niamey"
    TIME_ZONE_AFRICA_NOUAKCHOTT = "Africa/Nouakchott"
    TIME_ZONE_AFRICA_OUAGADOUGOU = "Africa/Ouagadougou"
    TIME_ZONE_AFRICA_PORTO_NOVO = "Africa/Porto-Novo"
    TIME_ZONE_AFRICA_SAO_TOME = "Africa/Sao Tome"
    TIME_ZONE_AFRICA_TRIPOLI = "Africa/Tripoli"
    TIME_ZONE_AFRICA_TUNIS = "Africa/Tunis"
    TIME_ZONE_AFRICA_WINDHOEK = "Africa/Windhoek"
    TIME_ZONE_AMERICA_ADAK = "America/Adak"
    TIME_ZONE_AMERICA_ANCHORAGE = "America/Anchorage"
    TIME_ZONE_AMERICA_ANGUILLA = "America/Anguilla"
    TIME_ZONE_AMERICA_ANTIGUA = "America/Antigua"
    TIME_ZONE_AMERICA_ARAGUAINA = "America/Araguaina"
    TIME_ZONE_AMERICA_ARGENTINA_BUENOS_AIRES = "America/Argentina/Buenos Aires"
    TIME_ZONE_AMERICA_ARGENTINA_CATAMARCA = "America/Argentina/Catamarca"
    TIME_ZONE_AMERICA_ARGENTINA_CORDOBA = "America/Argentina/Cordoba"
    TIME_ZONE_AMERICA_ARGENTINA_JUJUY = "America/Argentina/Jujuy"
    TIME_ZONE_AMERICA_ARGENTINA_LA_RIOJA = "America/Argentina/La Rioja"
    TIME_ZONE_AMERICA_ARGENTINA_MENDOZA = "America/Argentina/Mendoza"
    TIME_ZONE_AMERICA_ARGENTINA_RIO_GALLEGOS = "America/Argentina/Rio Gallegos"
    TIME_ZONE_AMERICA_ARGENTINA_SALTA = "America/Argentina/Salta"
    TIME_ZONE_AMERICA_ARGENTINA_SAN_JUAN = "America/Argentina/San Juan"
    TIME_ZONE_AMERICA_ARGENTINA_SAN_LUIS = "America/Argentina/San Luis"
    TIME_ZONE_AMERICA_ARGENTINA_TUCUMAN = "America/Argentina/Tucuman"
    TIME_ZONE_AMERICA_ARGENTINA_USHUAIA = "America/Argentina/Ushuaia"
    TIME_ZONE_AMERICA_ARUBA = "America/Aruba"
    TIME_ZONE_AMERICA_ASUNCION = "America/Asuncion"
    TIME_ZONE_AMERICA_ATIKOKAN = "America/Atikokan"
    TIME_ZONE_AMERICA_BAHIA = "America/Bahia"
    TIME_ZONE_AMERICA_BAHIA_BANDERAS = "America/Bahia Banderas"
    TIME_ZONE_AMERICA_BARBADOS = "America/Barbados"
    TIME_ZONE_AMERICA_BELEM = "America/Belem"
    TIME_ZONE_AMERICA_BELIZE = "America/Belize"
    TIME_ZONE_AMERICA_BLANC_SABLON = "America/Blanc-Sablon"
    TIME_ZONE_AMERICA_BOA_VISTA = "America/Boa Vista"
    TIME_ZONE_AMERICA_BOGOTA = "America/Bogota"
    TIME_ZONE_AMERICA_BOISE = "America/Boise"
    TIME_ZONE_AMERICA_CAMBRIDGE_BAY = "America/Cambridge Bay"
    TIME_ZONE_AMERICA_CAMPO_GRANDE = "America/Campo Grande"
    TIME_ZONE_AMERICA_CANCUN = "America/Cancun"
    TIME_ZONE_AMERICA_CARACAS = "America/Caracas"
    TIME_ZONE_AMERICA_CAYENNE = "America/Cayenne"
    TIME_ZONE_AMERICA_CAYMAN = "America/Cayman"
    TIME_ZONE_AMERICA_CHICAGO = "America/Chicago"
    TIME_ZONE_AMERICA_CHIHUAHUA = "America/Chihuahua"
    TIME_ZONE_AMERICA_COSTA_RICA = "America/Costa Rica"
    TIME_ZONE_AMERICA_CRESTON = "America/Creston"
    TIME_ZONE_AMERICA_CUIABA = "America/Cuiaba"
    TIME_ZONE_AMERICA_CURACAO = "America/Curacao"
    TIME_ZONE_AMERICA_DANMARKSHAVN = "America/Danmarkshavn"
    TIME_ZONE_AMERICA_DAWSON = "America/Dawson"
    TIME_ZONE_AMERICA_DAWSON_CREEK = "America/Dawson Creek"
    TIME_ZONE_AMERICA_DENVER = "America/Denver"
    TIME_ZONE_AMERICA_DETROIT = "America/Detroit"
    TIME_ZONE_AMERICA_DOMINICA = "America/Dominica"
    TIME_ZONE_AMERICA_EDMONTON = "America/Edmonton"
    TIME_ZONE_AMERICA_EIRUNEPE = "America/Eirunepe"
    TIME_ZONE_AMERICA_EL_SALVADOR = "America/El Salvador"
    TIME_ZONE_AMERICA_FORTALEZA = "America/Fortaleza"
    TIME_ZONE_AMERICA_GLACE_BAY = "America/Glace Bay"
    TIME_ZONE_AMERICA_GODTHAB = "America/Godthab"
    TIME_ZONE_AMERICA_GOOSE_BAY = "America/Goose Bay"
    TIME_ZONE_AMERICA_GRAND_TURK = "America/Grand Turk"
    TIME_ZONE_AMERICA_GRENADA = "America/Grenada"
    TIME_ZONE_AMERICA_GUADELOUPE = "America/Guadeloupe"
    TIME_ZONE_AMERICA_GUATEMALA = "America/Guatemala"
    TIME_ZONE_AMERICA_GUAYAQUIL = "America/Guayaquil"
    TIME_ZONE_AMERICA_GUYANA = "America/Guyana"
    TIME_ZONE_AMERICA_HALIFAX = "America/Halifax"
    TIME_ZONE_AMERICA_HAVANA = "America/Havana"
    TIME_ZONE_AMERICA_HERMOSILLO = "America/Hermosillo"
    TIME_ZONE_AMERICA_INDIANA_INDIANAPOLIS = "America/Indiana/Indianapolis"
    TIME_ZONE_AMERICA_INDIANA_KNOX = "America/Indiana/Knox"
    TIME_ZONE_AMERICA_INDIANA_MARENGO = "America/Indiana/Marengo"
    TIME_ZONE_AMERICA_INDIANA_PETERSBURG = "America/Indiana/Petersburg"
    TIME_ZONE_AMERICA_INDIANA_TELL_CITY = "America/Indiana/Tell City"
    TIME_ZONE_AMERICA_INDIANA_VEVAY = "America/Indiana/Vevay"
    TIME_ZONE_AMERICA_INDIANA_VINCENNES = "America/Indiana/Vincennes"
    TIME_ZONE_AMERICA_INDIANA_WINAMAC = "America/Indiana/Winamac"
    TIME_ZONE_AMERICA_INUVIK = "America/Inuvik"
    TIME_ZONE_AMERICA_IQALUIT = "America/Iqaluit"
    TIME_ZONE_AMERICA_JAMAICA = "America/Jamaica"
    TIME_ZONE_AMERICA_JUNEAU = "America/Juneau"
    TIME_ZONE_AMERICA_KENTUCKY_LOUISVILLE = "America/Kentucky/Louisville"
    TIME_ZONE_AMERICA_KENTUCKY_MONTICELLO = "America/Kentucky/Monticello"
    TIME_ZONE_AMERICA_KRALENDIJK = "America/Kralendijk"
    TIME_ZONE_AMERICA_LA_PAZ = "America/La Paz"
    TIME_ZONE_AMERICA_LIMA = "America/Lima"
    TIME_ZONE_AMERICA_LOS_ANGELES = "America/Los Angeles"
    TIME_ZONE_AMERICA_LOWER_PRINCES = "America/Lower Princes"
    TIME_ZONE_AMERICA_MACEIO = "America/Maceio"
    TIME_ZONE_AMERICA_MANAGUA = "America/Managua"
    TIME_ZONE_AMERICA_MANAUS = "America/Manaus"
    TIME_ZONE_AMERICA_MARIGOT = "America/Marigot"
    TIME_ZONE_AMERICA_MARTINIQUE = "America/Martinique"
    TIME_ZONE_AMERICA_MATAMOROS = "America/Matamoros"
    TIME_ZONE_AMERICA_MAZATLAN = "America/Mazatlan"
    TIME_ZONE_AMERICA_MENOMINEE = "America/Menominee"
    TIME_ZONE_AMERICA_MERIDA = "America/Merida"
    TIME_ZONE_AMERICA_METLAKATLA = "America/Metlakatla"
    TIME_ZONE_AMERICA_MEXICO_CITY = "America/Mexico City"
    TIME_ZONE_AMERICA_MIQUELON = "America/Miquelon"
    TIME_ZONE_AMERICA_MONCTON = "America/Moncton"
    TIME_ZONE_AMERICA_MONTERREY = "America/Monterrey"
    TIME_ZONE_AMERICA_MONTEVIDEO = "America/Montevideo"
    TIME_ZONE_AMERICA_MONTREAL = "America/Montreal"
    TIME_ZONE_AMERICA_MONTSERRAT = "America/Montserrat"
    TIME_ZONE_AMERICA_NASSAU = "America/Nassau"
    TIME_ZONE_AMERICA_NEW_YORK = "America/New York"
    TIME_ZONE_AMERICA_NIPIGON = "America/Nipigon"
    TIME_ZONE_AMERICA_NOME = "America/Nome"
    TIME_ZONE_AMERICA_NORONHA = "America/Noronha"
    TIME_ZONE_AMERICA_NORTH_DAKOTA_BEULAH = "America/North Dakota/Beulah"
    TIME_ZONE_AMERICA_NORTH_DAKOTA_CENTER = "America/North Dakota/Center"
    TIME_ZONE_AMERICA_NORTH_DAKOTA_NEW_SALEM = "America/North Dakota/New Salem"
    TIME_ZONE_AMERICA_OJINAGA = "America/Ojinaga"
    TIME_ZONE_AMERICA_PANAMA = "America/Panama"
    TIME_ZONE_AMERICA_PANGNIRTUNG = "America/Pangnirtung"
    TIME_ZONE_AMERICA_PARAMARIBO = "America/Paramaribo"
    TIME_ZONE_AMERICA_PHOENIX = "America/Phoenix"
    TIME_ZONE_AMERICA_PORT_OF_SPAIN = "America/Port of Spain"
    TIME_ZONE_AMERICA_PORT_AU_PRINCE = "America/Port-au-Prince"
    TIME_ZONE_AMERICA_PORTO_VELHO = "America/Porto Velho"
    TIME_ZONE_AMERICA_PUERTO_RICO = "America/Puerto Rico"
    TIME_ZONE_AMERICA_RAINY_RIVER = "America/Rainy River"
    TIME_ZONE_AMERICA_RANKIN_INLET = "America/Rankin Inlet"
    TIME_ZONE_AMERICA_RECIFE = "America/Recife"
    TIME_ZONE_AMERICA_REGINA = "America/Regina"
    TIME_ZONE_AMERICA_RESOLUTE = "America/Resolute"
    TIME_ZONE_AMERICA_RIO_BRANCO = "America/Rio Branco"
    TIME_ZONE_AMERICA_SANTA_ISABEL = "America/Santa Isabel"
    TIME_ZONE_AMERICA_SANTAREM = "America/Santarem"
    TIME_ZONE_AMERICA_SANTIAGO = "America/Santiago"
    TIME_ZONE_AMERICA_SANTO_DOMINGO = "America/Santo Domingo"
    TIME_ZONE_AMERICA_SAO_PAULO = "America/Sao Paulo"
    TIME_ZONE_AMERICA_SCORESBYSUND = "America/Scoresbysund"
    TIME_ZONE_AMERICA_SHIPROCK = "America/Shiprock"
    TIME_ZONE_AMERICA_SITKA = "America/Sitka"
    TIME_ZONE_AMERICA_ST_BARTHELEMY = "America/St Barthelemy"
    TIME_ZONE_AMERICA_ST_JOHNS = "America/St Johns"
    TIME_ZONE_AMERICA_ST_KITTS = "America/St Kitts"
    TIME_ZONE_AMERICA_ST_LUCIA = "America/St Lucia"
    TIME_ZONE_AMERICA_ST_THOMAS = "America/St Thomas"
    TIME_ZONE_AMERICA_ST_VINCENT = "America/St Vincent"
    TIME_ZONE_AMERICA_SWIFT_CURRENT = "America/Swift Current"
    TIME_ZONE_AMERICA_TEGUCIGALPA = "America/Tegucigalpa"
    TIME_ZONE_AMERICA_THULE = "America/Thule"
    TIME_ZONE_AMERICA_THUNDER_BAY = "America/Thunder Bay"
    TIME_ZONE_AMERICA_TIJUANA = "America/Tijuana"
    TIME_ZONE_AMERICA_TORONTO = "America/Toronto"
    TIME_ZONE_AMERICA_TORTOLA = "America/Tortola"
    TIME_ZONE_AMERICA_VANCOUVER = "America/Vancouver"
    TIME_ZONE_AMERICA_WHITEHORSE = "America/Whitehorse"
    TIME_ZONE_AMERICA_WINNIPEG = "America/Winnipeg"
    TIME_ZONE_AMERICA_YAKUTAT = "America/Yakutat"
    TIME_ZONE_AMERICA_YELLOWKNIFE = "America/Yellowknife"
    TIME_ZONE_ANTARCTICA_CASEY = "Antarctica/Casey"
    TIME_ZONE_ANTARCTICA_DAVIS = "Antarctica/Davis"
    TIME_ZONE_ANTARCTICA_DUMONT_DURVILLE = "Antarctica/DumontDUrville"
    TIME_ZONE_ANTARCTICA_MACQUARIE = "Antarctica/Macquarie"
    TIME_ZONE_ANTARCTICA_MAWSON = "Antarctica/Mawson"
    TIME_ZONE_ANTARCTICA_MC_MURDO = "Antarctica/McMurdo"
    TIME_ZONE_ANTARCTICA_PALMER = "Antarctica/Palmer"
    TIME_ZONE_ANTARCTICA_ROTHERA = "Antarctica/Rothera"
    TIME_ZONE_ANTARCTICA_SOUTH_POLE = "Antarctica/South Pole"
    TIME_ZONE_ANTARCTICA_SYOWA = "Antarctica/Syowa"
    TIME_ZONE_ANTARCTICA_TROLL = "Antarctica/Troll"
    TIME_ZONE_ANTARCTICA_VOSTOK = "Antarctica/Vostok"
    TIME_ZONE_ARCTIC_LONGYEARBYEN = "Arctic/Longyearbyen"
    TIME_ZONE_ASIA_ADEN = "Asia/Aden"
    TIME_ZONE_ASIA_ALMATY = "Asia/Almaty"
    TIME_ZONE_ASIA_AMMAN = "Asia/Amman"
    TIME_ZONE_ASIA_ANADYR = "Asia/Anadyr"
    TIME_ZONE_ASIA_AQTAU = "Asia/Aqtau"
    TIME_ZONE_ASIA_AQTOBE = "Asia/Aqtobe"
    TIME_ZONE_ASIA_ASHGABAT = "Asia/Ashgabat"
    TIME_ZONE_ASIA_BAGHDAD = "Asia/Baghdad"
    TIME_ZONE_ASIA_BAHRAIN = "Asia/Bahrain"
    TIME_ZONE_ASIA_BAKU = "Asia/Baku"
    TIME_ZONE_ASIA_BANGKOK = "Asia/Bangkok"
    TIME_ZONE_ASIA_BEIRUT = "Asia/Beirut"
    TIME_ZONE_ASIA_BISHKEK = "Asia/Bishkek"
    TIME_ZONE_ASIA_BRUNEI = "Asia/Brunei"
    TIME_ZONE_ASIA_CHOIBALSAN = "Asia/Choibalsan"
    TIME_ZONE_ASIA_CHONGQING = "Asia/Chongqing"
    TIME_ZONE_ASIA_COLOMBO = "Asia/Colombo"
    TIME_ZONE_ASIA_DAMASCUS = "Asia/Damascus"
    TIME_ZONE_ASIA_DHAKA = "Asia/Dhaka"
    TIME_ZONE_ASIA_DILI = "Asia/Dili"
    TIME_ZONE_ASIA_DUBAI = "Asia/Dubai"
    TIME_ZONE_ASIA_DUSHANBE = "Asia/Dushanbe"
    TIME_ZONE_ASIA_GAZA = "Asia/Gaza"
    TIME_ZONE_ASIA_HARBIN = "Asia/Harbin"
    TIME_ZONE_ASIA_HEBRON = "Asia/Hebron"
    TIME_ZONE_ASIA_HO_CHI_MINH = "Asia/Ho Chi Minh"
    TIME_ZONE_ASIA_HONG_KONG = "Asia/Hong Kong"
    TIME_ZONE_ASIA_HOVD = "Asia/Hovd"
    TIME_ZONE_ASIA_IRKUTSK = "Asia/Irkutsk"
    TIME_ZONE_ASIA_JAKARTA = "Asia/Jakarta"
    TIME_ZONE_ASIA_JAYAPURA = "Asia/Jayapura"
    TIME_ZONE_ASIA_JERUSALEM = "Asia/Jerusalem"
    TIME_ZONE_ASIA_KABUL = "Asia/Kabul"
    TIME_ZONE_ASIA_KAMCHATKA = "Asia/Kamchatka"
    TIME_ZONE_ASIA_KARACHI = "Asia/Karachi"
    TIME_ZONE_ASIA_KASHGAR = "Asia/Kashgar"
    TIME_ZONE_ASIA_KATHMANDU = "Asia/Kathmandu"
    TIME_ZONE_ASIA_KHANDYGA = "Asia/Khandyga"
    TIME_ZONE_ASIA_KOLKATA = "Asia/Kolkata"
    TIME_ZONE_ASIA_KRASNOYARSK = "Asia/Krasnoyarsk"
    TIME_ZONE_ASIA_KUALA_LUMPUR = "Asia/Kuala Lumpur"
    TIME_ZONE_ASIA_KUCHING = "Asia/Kuching"
    TIME_ZONE_ASIA_KUWAIT = "Asia/Kuwait"
    TIME_ZONE_ASIA_MACAU = "Asia/Macau"
    TIME_ZONE_ASIA_MAGADAN = "Asia/Magadan"
    TIME_ZONE_ASIA_MAKASSAR = "Asia/Makassar"
    TIME_ZONE_ASIA_MANILA = "Asia/Manila"
    TIME_ZONE_ASIA_MUSCAT = "Asia/Muscat"
    TIME_ZONE_ASIA_NICOSIA = "Asia/Nicosia"
    TIME_ZONE_ASIA_NOVOKUZNETSK = "Asia/Novokuznetsk"
    TIME_ZONE_ASIA_NOVOSIBIRSK = "Asia/Novosibirsk"
    TIME_ZONE_ASIA_OMSK = "Asia/Omsk"
    TIME_ZONE_ASIA_ORAL = "Asia/Oral"
    TIME_ZONE_ASIA_PHNOM_PENH = "Asia/Phnom Penh"
    TIME_ZONE_ASIA_PONTIANAK = "Asia/Pontianak"
    TIME_ZONE_ASIA_PYONGYANG = "Asia/Pyongyang"
    TIME_ZONE_ASIA_QATAR = "Asia/Qatar"
    TIME_ZONE_ASIA_QYZYLORDA = "Asia/Qyzylorda"
    TIME_ZONE_ASIA_RANGOON = "Asia/Rangoon"
    TIME_ZONE_ASIA_RIYADH = "Asia/Riyadh"
    TIME_ZONE_ASIA_SAKHALIN = "Asia/Sakhalin"
    TIME_ZONE_ASIA_SAMARKAND = "Asia/Samarkand"
    TIME_ZONE_ASIA_SEOUL = "Asia/Seoul"
    TIME_ZONE_ASIA_SHANGHAI = "Asia/Shanghai"
    TIME_ZONE_ASIA_SINGAPORE = "Asia/Singapore"
    TIME_ZONE_ASIA_TAIPEI = "Asia/Taipei"
    TIME_ZONE_ASIA_TASHKENT = "Asia/Tashkent"
    TIME_ZONE_ASIA_TBILISI = "Asia/Tbilisi"
    TIME_ZONE_ASIA_TEHRAN = "Asia/Tehran"
    TIME_ZONE_ASIA_THIMPHU = "Asia/Thimphu"
    TIME_ZONE_ASIA_TOKYO = "Asia/Tokyo"
    TIME_ZONE_ASIA_ULAANBAATAR = "Asia/Ulaanbaatar"
    TIME_ZONE_ASIA_URUMQI = "Asia/Urumqi"
    TIME_ZONE_ASIA_UST_NERA = "Asia/Ust-Nera"
    TIME_ZONE_ASIA_VIENTIANE = "Asia/Vientiane"
    TIME_ZONE_ASIA_VLADIVOSTOK = "Asia/Vladivostok"
    TIME_ZONE_ASIA_YAKUTSK = "Asia/Yakutsk"
    TIME_ZONE_ASIA_YEKATERINBURG = "Asia/Yekaterinburg"
    TIME_ZONE_ASIA_YEREVAN = "Asia/Yerevan"
    TIME_ZONE_ATLANTIC_AZORES = "Atlantic/Azores"
    TIME_ZONE_ATLANTIC_BERMUDA = "Atlantic/Bermuda"
    TIME_ZONE_ATLANTIC_CANARY = "Atlantic/Canary"
    TIME_ZONE_ATLANTIC_CAPE_VERDE = "Atlantic/Cape Verde"
    TIME_ZONE_ATLANTIC_FAROE = "Atlantic/Faroe"
    TIME_ZONE_ATLANTIC_MADEIRA = "Atlantic/Madeira"
    TIME_ZONE_ATLANTIC_REYKJAVIK = "Atlantic/Reykjavik"
    TIME_ZONE_ATLANTIC_SOUTH_GEORGIA = "Atlantic/South Georgia"
    TIME_ZONE_ATLANTIC_ST_HELENA = "Atlantic/St Helena"
    TIME_ZONE_ATLANTIC_STANLEY = "Atlantic/Stanley"
    TIME_ZONE_AUSTRALIA_ADELAIDE = "Australia/Adelaide"
    TIME_ZONE_AUSTRALIA_BRISBANE = "Australia/Brisbane"
    TIME_ZONE_AUSTRALIA_BROKEN_HILL = "Australia/Broken Hill"
    TIME_ZONE_AUSTRALIA_CURRIE = "Australia/Currie"
    TIME_ZONE_AUSTRALIA_DARWIN = "Australia/Darwin"
    TIME_ZONE_AUSTRALIA_EUCLA = "Australia/Eucla"
    TIME_ZONE_AUSTRALIA_HOBART = "Australia/Hobart"
    TIME_ZONE_AUSTRALIA_LINDEMAN = "Australia/Lindeman"
    TIME_ZONE_AUSTRALIA_LORD_HOWE = "Australia/Lord Howe"
    TIME_ZONE_AUSTRALIA_MELBOURNE = "Australia/Melbourne"
    TIME_ZONE_AUSTRALIA_PERTH = "Australia/Perth"
    TIME_ZONE_AUSTRALIA_SYDNEY = "Australia/Sydney"
    TIME_ZONE_EUROPE_AMSTERDAM = "Europe/Amsterdam"
    TIME_ZONE_EUROPE_ANDORRA = "Europe/Andorra"
    TIME_ZONE_EUROPE_ATHENS = "Europe/Athens"
    TIME_ZONE_EUROPE_BELGRADE = "Europe/Belgrade"
    TIME_ZONE_EUROPE_BERLIN = "Europe/Berlin"
    TIME_ZONE_EUROPE_BRATISLAVA = "Europe/Bratislava"
    TIME_ZONE_EUROPE_BRUSSELS = "Europe/Brussels"
    TIME_ZONE_EUROPE_BUCHAREST = "Europe/Bucharest"
    TIME_ZONE_EUROPE_BUDAPEST = "Europe/Budapest"
    TIME_ZONE_EUROPE_BUSINGEN = "Europe/Busingen"
    TIME_ZONE_EUROPE_CHISINAU = "Europe/Chisinau"
    TIME_ZONE_EUROPE_COPENHAGEN = "Europe/Copenhagen"
    TIME_ZONE_EUROPE_DUBLIN = "Europe/Dublin"
    TIME_ZONE_EUROPE_GIBRALTAR = "Europe/Gibraltar"
    TIME_ZONE_EUROPE_GUERNSEY = "Europe/Guernsey"
    TIME_ZONE_EUROPE_HELSINKI = "Europe/Helsinki"
    TIME_ZONE_EUROPE_ISLE_OF_MAN = "Europe/Isle of Man"
    TIME_ZONE_EUROPE_ISTANBUL = "Europe/Istanbul"
    TIME_ZONE_EUROPE_JERSEY = "Europe/Jersey"
    TIME_ZONE_EUROPE_KALININGRAD = "Europe/Kaliningrad"
    TIME_ZONE_EUROPE_KIEV = "Europe/Kiev"
    TIME_ZONE_EUROPE_LISBON = "Europe/Lisbon"
    TIME_ZONE_EUROPE_LJUBLJANA = "Europe/Ljubljana"
    TIME_ZONE_EUROPE_LONDON = "Europe/London"
    TIME_ZONE_EUROPE_LUXEMBOURG = "Europe/Luxembourg"
    TIME_ZONE_EUROPE_MADRID = "Europe/Madrid"
    TIME_ZONE_EUROPE_MALTA = "Europe/Malta"
    TIME_ZONE_EUROPE_MARIEHAMN = "Europe/Mariehamn"
    TIME_ZONE_EUROPE_MINSK = "Europe/Minsk"
    TIME_ZONE_EUROPE_MONACO = "Europe/Monaco"
    TIME_ZONE_EUROPE_MOSCOW = "Europe/Moscow"
    TIME_ZONE_EUROPE_OSLO = "Europe/Oslo"
    TIME_ZONE_EUROPE_PARIS = "Europe/Paris"
    TIME_ZONE_EUROPE_PODGORICA = "Europe/Podgorica"
    TIME_ZONE_EUROPE_PRAGUE = "Europe/Prague"
    TIME_ZONE_EUROPE_RIGA = "Europe/Riga"
    TIME_ZONE_EUROPE_ROME = "Europe/Rome"
    TIME_ZONE_EUROPE_SAMARA = "Europe/Samara"
    TIME_ZONE_EUROPE_SAN_MARINO = "Europe/San Marino"
    TIME_ZONE_EUROPE_SARAJEVO = "Europe/Sarajevo"
    TIME_ZONE_EUROPE_SIMFEROPOL = "Europe/Simferopol"
    TIME_ZONE_EUROPE_SKOPJE = "Europe/Skopje"
    TIME_ZONE_EUROPE_SOFIA = "Europe/Sofia"
    TIME_ZONE_EUROPE_STOCKHOLM = "Europe/Stockholm"
    TIME_ZONE_EUROPE_TALLINN = "Europe/Tallinn"
    TIME_ZONE_EUROPE_TIRANE = "Europe/Tirane"
    TIME_ZONE_EUROPE_UZHGOROD = "Europe/Uzhgorod"
    TIME_ZONE_EUROPE_VADUZ = "Europe/Vaduz"
    TIME_ZONE_EUROPE_VATICAN = "Europe/Vatican"
    TIME_ZONE_EUROPE_VIENNA = "Europe/Vienna"
    TIME_ZONE_EUROPE_VILNIUS = "Europe/Vilnius"
    TIME_ZONE_EUROPE_VOLGOGRAD = "Europe/Volgograd"
    TIME_ZONE_EUROPE_WARSAW = "Europe/Warsaw"
    TIME_ZONE_EUROPE_ZAGREB = "Europe/Zagreb"
    TIME_ZONE_EUROPE_ZAPOROZHYE = "Europe/Zaporozhye"
    TIME_ZONE_EUROPE_ZURICH = "Europe/Zurich"
    TIME_ZONE_INDIAN_ANTANANARIVO = "Indian/Antananarivo"
    TIME_ZONE_INDIAN_CHAGOS = "Indian/Chagos"
    TIME_ZONE_INDIAN_CHRISTMAS = "Indian/Christmas"
    TIME_ZONE_INDIAN_COCOS = "Indian/Cocos"
    TIME_ZONE_INDIAN_COMORO = "Indian/Comoro"
    TIME_ZONE_INDIAN_KERGUELEN = "Indian/Kerguelen"
    TIME_ZONE_INDIAN_MAHE = "Indian/Mahe"
    TIME_ZONE_INDIAN_MALDIVES = "Indian/Maldives"
    TIME_ZONE_INDIAN_MAURITIUS = "Indian/Mauritius"
    TIME_ZONE_INDIAN_MAYOTTE = "Indian/Mayotte"
    TIME_ZONE_INDIAN_REUNION = "Indian/Reunion"
    TIME_ZONE_PACIFIC_APIA = "Pacific/Apia"
    TIME_ZONE_PACIFIC_AUCKLAND = "Pacific/Auckland"
    TIME_ZONE_PACIFIC_CHATHAM = "Pacific/Chatham"
    TIME_ZONE_PACIFIC_CHUUK = "Pacific/Chuuk"
    TIME_ZONE_PACIFIC_EASTER = "Pacific/Easter"
    TIME_ZONE_PACIFIC_EFATE = "Pacific/Efate"
    TIME_ZONE_PACIFIC_ENDERBURY = "Pacific/Enderbury"
    TIME_ZONE_PACIFIC_FAKAOFO = "Pacific/Fakaofo"
    TIME_ZONE_PACIFIC_FIJI = "Pacific/Fiji"
    TIME_ZONE_PACIFIC_FUNAFUTI = "Pacific/Funafuti"
    TIME_ZONE_PACIFIC_GALAPAGOS = "Pacific/Galapagos"
    TIME_ZONE_PACIFIC_GAMBIER = "Pacific/Gambier"
    TIME_ZONE_PACIFIC_GUADALCANAL = "Pacific/Guadalcanal"
    TIME_ZONE_PACIFIC_GUAM = "Pacific/Guam"
    TIME_ZONE_PACIFIC_HONOLULU = "Pacific/Honolulu"
    TIME_ZONE_PACIFIC_JOHNSTON = "Pacific/Johnston"
    TIME_ZONE_PACIFIC_KIRITIMATI = "Pacific/Kiritimati"
    TIME_ZONE_PACIFIC_KOSRAE = "Pacific/Kosrae"
    TIME_ZONE_PACIFIC_KWAJALEIN = "Pacific/Kwajalein"
    TIME_ZONE_PACIFIC_MAJURO = "Pacific/Majuro"
    TIME_ZONE_PACIFIC_MARQUESAS = "Pacific/Marquesas"
    TIME_ZONE_PACIFIC_MIDWAY = "Pacific/Midway"
    TIME_ZONE_PACIFIC_NAURU = "Pacific/Nauru"
    TIME_ZONE_PACIFIC_NIUE = "Pacific/Niue"
    TIME_ZONE_PACIFIC_NORFOLK = "Pacific/Norfolk"
    TIME_ZONE_PACIFIC_NOUMEA = "Pacific/Noumea"
    TIME_ZONE_PACIFIC_PAGO_PAGO = "Pacific/Pago Pago"
    TIME_ZONE_PACIFIC_PALAU = "Pacific/Palau"
    TIME_ZONE_PACIFIC_PITCAIRN = "Pacific/Pitcairn"
    TIME_ZONE_PACIFIC_POHNPEI = "Pacific/Pohnpei"
    TIME_ZONE_PACIFIC_PORT_MORESBY = "Pacific/Port Moresby"
    TIME_ZONE_PACIFIC_RAROTONGA = "Pacific/Rarotonga"
    TIME_ZONE_PACIFIC_SAIPAN = "Pacific/Saipan"
    TIME_ZONE_PACIFIC_TAHITI = "Pacific/Tahiti"
    TIME_ZONE_PACIFIC_TARAWA = "Pacific/Tarawa"
    TIME_ZONE_PACIFIC_TONGATAPU = "Pacific/Tongatapu"
    TIME_ZONE_PACIFIC_WAKE = "Pacific/Wake"
    TIME_ZONE_PACIFIC_WALLIS = "Pacific/Wallis"
    TIME_ZONE_UTC = "UTC"
    CMC1_IS_ACTIVE_ABSENT = "absent"
    CMC1_IS_ACTIVE_ACTIVE = "active"
    CMC1_IS_ACTIVE_STANDBY = "standby"
    CMC2_IS_ACTIVE_ABSENT = "absent"
    CMC2_IS_ACTIVE_ACTIVE = "active"
    CMC2_IS_ACTIVE_STANDBY = "standby"


class TopSystem(ManagedObject):
    """This is TopSystem class."""

    consts = TopSystemConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("TopSystem", "topSystem", "sys", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['topRoot'], ['aaaLdap', 'aaaTacacsPlus', 'aaaUserEp', 'certificateManagement', 'cloudMgmtSvc', 'commSvcEp', 'computeRackUnit', 'equipmentRackEnclosure', 'huuController', 'iodController', 'kmipManagement', 'mctpCertificateManagement', 'mgmtBackup', 'mgmtImporter', 'mgmtInventory', 'osiController', 'storageSasExpander', 'systemBoardUnit', 'vicBackupAll', 'vicImporterAll'], ["Get", "Set"]),
        "modular": MoMeta("TopSystem", "topSystem", "sys", VersionMeta.Version2013e, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['topRoot'], ['aaaLdap', 'aaaTacacsPlus', 'aaaUserEp', 'certificateManagement', 'cloudMgmtSvc', 'commSvcEp', 'equipmentChassis', 'sysdebugTechSupportExport'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "cc_enable": MoPropertyMeta("cc_enable", "ccEnable", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "fips_enable": MoPropertyMeta("fips_enable", "fipsEnable", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "time_zone": MoPropertyMeta("time_zone", "timeZone", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, ["Africa/Abidjan", "Africa/Accra", "Africa/Addis Ababa", "Africa/Algiers", "Africa/Asmara", "Africa/Bamako", "Africa/Bangui", "Africa/Banjul", "Africa/Bissau", "Africa/Blantyre", "Africa/Brazzaville", "Africa/Bujumbura", "Africa/Cairo", "Africa/Casablanca", "Africa/Ceuta", "Africa/Conakry", "Africa/Dakar", "Africa/Dar es Salaam", "Africa/Djibouti", "Africa/Douala", "Africa/El Aaiun", "Africa/Freetown", "Africa/Gaborone", "Africa/Harare", "Africa/Johannesburg", "Africa/Juba", "Africa/Kampala", "Africa/Khartoum", "Africa/Kigali", "Africa/Kinshasa", "Africa/Lagos", "Africa/Libreville", "Africa/Lome", "Africa/Luanda", "Africa/Lubumbashi", "Africa/Lusaka", "Africa/Malabo", "Africa/Maputo", "Africa/Maseru", "Africa/Mbabane", "Africa/Mogadishu", "Africa/Monrovia", "Africa/Nairobi", "Africa/Ndjamena", "Africa/Niamey", "Africa/Nouakchott", "Africa/Ouagadougou", "Africa/Porto-Novo", "Africa/Sao Tome", "Africa/Tripoli", "Africa/Tunis", "Africa/Windhoek", "America/Adak", "America/Anchorage", "America/Anguilla", "America/Antigua", "America/Araguaina", "America/Argentina/Buenos Aires", "America/Argentina/Catamarca", "America/Argentina/Cordoba", "America/Argentina/Jujuy", "America/Argentina/La Rioja", "America/Argentina/Mendoza", "America/Argentina/Rio Gallegos", "America/Argentina/Salta", "America/Argentina/San Juan", "America/Argentina/San Luis", "America/Argentina/Tucuman", "America/Argentina/Ushuaia", "America/Aruba", "America/Asuncion", "America/Atikokan", "America/Bahia", "America/Bahia Banderas", "America/Barbados", "America/Belem", "America/Belize", "America/Blanc-Sablon", "America/Boa Vista", "America/Bogota", "America/Boise", "America/Cambridge Bay", "America/Campo Grande", "America/Cancun", "America/Caracas", "America/Cayenne", "America/Cayman", "America/Chicago", "America/Chihuahua", "America/Costa Rica", "America/Creston", "America/Cuiaba", "America/Curacao", "America/Danmarkshavn", "America/Dawson", "America/Dawson Creek", "America/Denver", "America/Detroit", "America/Dominica", "America/Edmonton", "America/Eirunepe", "America/El Salvador", "America/Fortaleza", "America/Glace Bay", "America/Godthab", "America/Goose Bay", "America/Grand Turk", "America/Grenada", "America/Guadeloupe", "America/Guatemala", "America/Guayaquil", "America/Guyana", "America/Halifax", "America/Havana", "America/Hermosillo", "America/Indiana/Indianapolis", "America/Indiana/Knox", "America/Indiana/Marengo", "America/Indiana/Petersburg", "America/Indiana/Tell City", "America/Indiana/Vevay", "America/Indiana/Vincennes", "America/Indiana/Winamac", "America/Inuvik", "America/Iqaluit", "America/Jamaica", "America/Juneau", "America/Kentucky/Louisville", "America/Kentucky/Monticello", "America/Kralendijk", "America/La Paz", "America/Lima", "America/Los Angeles", "America/Lower Princes", "America/Maceio", "America/Managua", "America/Manaus", "America/Marigot", "America/Martinique", "America/Matamoros", "America/Mazatlan", "America/Menominee", "America/Merida", "America/Metlakatla", "America/Mexico City", "America/Miquelon", "America/Moncton", "America/Monterrey", "America/Montevideo", "America/Montreal", "America/Montserrat", "America/Nassau", "America/New York", "America/Nipigon", "America/Nome", "America/Noronha", "America/North Dakota/Beulah", "America/North Dakota/Center", "America/North Dakota/New Salem", "America/Ojinaga", "America/Panama", "America/Pangnirtung", "America/Paramaribo", "America/Phoenix", "America/Port of Spain", "America/Port-au-Prince", "America/Porto Velho", "America/Puerto Rico", "America/Rainy River", "America/Rankin Inlet", "America/Recife", "America/Regina", "America/Resolute", "America/Rio Branco", "America/Santa Isabel", "America/Santarem", "America/Santiago", "America/Santo Domingo", "America/Sao Paulo", "America/Scoresbysund", "America/Shiprock", "America/Sitka", "America/St Barthelemy", "America/St Johns", "America/St Kitts", "America/St Lucia", "America/St Thomas", "America/St Vincent", "America/Swift Current", "America/Tegucigalpa", "America/Thule", "America/Thunder Bay", "America/Tijuana", "America/Toronto", "America/Tortola", "America/Vancouver", "America/Whitehorse", "America/Winnipeg", "America/Yakutat", "America/Yellowknife", "Antarctica/Casey", "Antarctica/Davis", "Antarctica/DumontDUrville", "Antarctica/Macquarie", "Antarctica/Mawson", "Antarctica/McMurdo", "Antarctica/Palmer", "Antarctica/Rothera", "Antarctica/South Pole", "Antarctica/Syowa", "Antarctica/Troll", "Antarctica/Vostok", "Arctic/Longyearbyen", "Asia/Aden", "Asia/Almaty", "Asia/Amman", "Asia/Anadyr", "Asia/Aqtau", "Asia/Aqtobe", "Asia/Ashgabat", "Asia/Baghdad", "Asia/Bahrain", "Asia/Baku", "Asia/Bangkok", "Asia/Beirut", "Asia/Bishkek", "Asia/Brunei", "Asia/Choibalsan", "Asia/Chongqing", "Asia/Colombo", "Asia/Damascus", "Asia/Dhaka", "Asia/Dili", "Asia/Dubai", "Asia/Dushanbe", "Asia/Gaza", "Asia/Harbin", "Asia/Hebron", "Asia/Ho Chi Minh", "Asia/Hong Kong", "Asia/Hovd", "Asia/Irkutsk", "Asia/Jakarta", "Asia/Jayapura", "Asia/Jerusalem", "Asia/Kabul", "Asia/Kamchatka", "Asia/Karachi", "Asia/Kashgar", "Asia/Kathmandu", "Asia/Khandyga", "Asia/Kolkata", "Asia/Krasnoyarsk", "Asia/Kuala Lumpur", "Asia/Kuching", "Asia/Kuwait", "Asia/Macau", "Asia/Magadan", "Asia/Makassar", "Asia/Manila", "Asia/Muscat", "Asia/Nicosia", "Asia/Novokuznetsk", "Asia/Novosibirsk", "Asia/Omsk", "Asia/Oral", "Asia/Phnom Penh", "Asia/Pontianak", "Asia/Pyongyang", "Asia/Qatar", "Asia/Qyzylorda", "Asia/Rangoon", "Asia/Riyadh", "Asia/Sakhalin", "Asia/Samarkand", "Asia/Seoul", "Asia/Shanghai", "Asia/Singapore", "Asia/Taipei", "Asia/Tashkent", "Asia/Tbilisi", "Asia/Tehran", "Asia/Thimphu", "Asia/Tokyo", "Asia/Ulaanbaatar", "Asia/Urumqi", "Asia/Ust-Nera", "Asia/Vientiane", "Asia/Vladivostok", "Asia/Yakutsk", "Asia/Yekaterinburg", "Asia/Yerevan", "Atlantic/Azores", "Atlantic/Bermuda", "Atlantic/Canary", "Atlantic/Cape Verde", "Atlantic/Faroe", "Atlantic/Madeira", "Atlantic/Reykjavik", "Atlantic/South Georgia", "Atlantic/St Helena", "Atlantic/Stanley", "Australia/Adelaide", "Australia/Brisbane", "Australia/Broken Hill", "Australia/Currie", "Australia/Darwin", "Australia/Eucla", "Australia/Hobart", "Australia/Lindeman", "Australia/Lord Howe", "Australia/Melbourne", "Australia/Perth", "Australia/Sydney", "Europe/Amsterdam", "Europe/Andorra", "Europe/Athens", "Europe/Belgrade", "Europe/Berlin", "Europe/Bratislava", "Europe/Brussels", "Europe/Bucharest", "Europe/Budapest", "Europe/Busingen", "Europe/Chisinau", "Europe/Copenhagen", "Europe/Dublin", "Europe/Gibraltar", "Europe/Guernsey", "Europe/Helsinki", "Europe/Isle of Man", "Europe/Istanbul", "Europe/Jersey", "Europe/Kaliningrad", "Europe/Kiev", "Europe/Lisbon", "Europe/Ljubljana", "Europe/London", "Europe/Luxembourg", "Europe/Madrid", "Europe/Malta", "Europe/Mariehamn", "Europe/Minsk", "Europe/Monaco", "Europe/Moscow", "Europe/Oslo", "Europe/Paris", "Europe/Podgorica", "Europe/Prague", "Europe/Riga", "Europe/Rome", "Europe/Samara", "Europe/San Marino", "Europe/Sarajevo", "Europe/Simferopol", "Europe/Skopje", "Europe/Sofia", "Europe/Stockholm", "Europe/Tallinn", "Europe/Tirane", "Europe/Uzhgorod", "Europe/Vaduz", "Europe/Vatican", "Europe/Vienna", "Europe/Vilnius", "Europe/Volgograd", "Europe/Warsaw", "Europe/Zagreb", "Europe/Zaporozhye", "Europe/Zurich", "Indian/Antananarivo", "Indian/Chagos", "Indian/Christmas", "Indian/Cocos", "Indian/Comoro", "Indian/Kerguelen", "Indian/Mahe", "Indian/Maldives", "Indian/Mauritius", "Indian/Mayotte", "Indian/Reunion", "Pacific/Apia", "Pacific/Auckland", "Pacific/Chatham", "Pacific/Chuuk", "Pacific/Easter", "Pacific/Efate", "Pacific/Enderbury", "Pacific/Fakaofo", "Pacific/Fiji", "Pacific/Funafuti", "Pacific/Galapagos", "Pacific/Gambier", "Pacific/Guadalcanal", "Pacific/Guam", "Pacific/Honolulu", "Pacific/Johnston", "Pacific/Kiritimati", "Pacific/Kosrae", "Pacific/Kwajalein", "Pacific/Majuro", "Pacific/Marquesas", "Pacific/Midway", "Pacific/Nauru", "Pacific/Niue", "Pacific/Norfolk", "Pacific/Noumea", "Pacific/Pago Pago", "Pacific/Palau", "Pacific/Pitcairn", "Pacific/Pohnpei", "Pacific/Port Moresby", "Pacific/Rarotonga", "Pacific/Saipan", "Pacific/Tahiti", "Pacific/Tarawa", "Pacific/Tongatapu", "Pacific/Wake", "Pacific/Wallis", "UTC"], []),
            "address": MoPropertyMeta("address", "address", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_time": MoPropertyMeta("current_time", "currentTime", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "local_time": MoPropertyMeta("local_time", "localTime", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cluster", "stand-alone", "unspecified"], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

        "modular": {
            "cc_enable": MoPropertyMeta("cc_enable", "ccEnable", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "fips_enable": MoPropertyMeta("fips_enable", "fipsEnable", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "time_zone": MoPropertyMeta("time_zone", "timeZone", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, ["Africa/Abidjan", "Africa/Accra", "Africa/Addis Ababa", "Africa/Algiers", "Africa/Asmara", "Africa/Bamako", "Africa/Bangui", "Africa/Banjul", "Africa/Bissau", "Africa/Blantyre", "Africa/Brazzaville", "Africa/Bujumbura", "Africa/Cairo", "Africa/Casablanca", "Africa/Ceuta", "Africa/Conakry", "Africa/Dakar", "Africa/Dar es Salaam", "Africa/Djibouti", "Africa/Douala", "Africa/El Aaiun", "Africa/Freetown", "Africa/Gaborone", "Africa/Harare", "Africa/Johannesburg", "Africa/Juba", "Africa/Kampala", "Africa/Khartoum", "Africa/Kigali", "Africa/Kinshasa", "Africa/Lagos", "Africa/Libreville", "Africa/Lome", "Africa/Luanda", "Africa/Lubumbashi", "Africa/Lusaka", "Africa/Malabo", "Africa/Maputo", "Africa/Maseru", "Africa/Mbabane", "Africa/Mogadishu", "Africa/Monrovia", "Africa/Nairobi", "Africa/Ndjamena", "Africa/Niamey", "Africa/Nouakchott", "Africa/Ouagadougou", "Africa/Porto-Novo", "Africa/Sao Tome", "Africa/Tripoli", "Africa/Tunis", "Africa/Windhoek", "America/Adak", "America/Anchorage", "America/Anguilla", "America/Antigua", "America/Araguaina", "America/Argentina/Buenos Aires", "America/Argentina/Catamarca", "America/Argentina/Cordoba", "America/Argentina/Jujuy", "America/Argentina/La Rioja", "America/Argentina/Mendoza", "America/Argentina/Rio Gallegos", "America/Argentina/Salta", "America/Argentina/San Juan", "America/Argentina/San Luis", "America/Argentina/Tucuman", "America/Argentina/Ushuaia", "America/Aruba", "America/Asuncion", "America/Atikokan", "America/Bahia", "America/Bahia Banderas", "America/Barbados", "America/Belem", "America/Belize", "America/Blanc-Sablon", "America/Boa Vista", "America/Bogota", "America/Boise", "America/Cambridge Bay", "America/Campo Grande", "America/Cancun", "America/Caracas", "America/Cayenne", "America/Cayman", "America/Chicago", "America/Chihuahua", "America/Costa Rica", "America/Creston", "America/Cuiaba", "America/Curacao", "America/Danmarkshavn", "America/Dawson", "America/Dawson Creek", "America/Denver", "America/Detroit", "America/Dominica", "America/Edmonton", "America/Eirunepe", "America/El Salvador", "America/Fortaleza", "America/Glace Bay", "America/Godthab", "America/Goose Bay", "America/Grand Turk", "America/Grenada", "America/Guadeloupe", "America/Guatemala", "America/Guayaquil", "America/Guyana", "America/Halifax", "America/Havana", "America/Hermosillo", "America/Indiana/Indianapolis", "America/Indiana/Knox", "America/Indiana/Marengo", "America/Indiana/Petersburg", "America/Indiana/Tell City", "America/Indiana/Vevay", "America/Indiana/Vincennes", "America/Indiana/Winamac", "America/Inuvik", "America/Iqaluit", "America/Jamaica", "America/Juneau", "America/Kentucky/Louisville", "America/Kentucky/Monticello", "America/Kralendijk", "America/La Paz", "America/Lima", "America/Los Angeles", "America/Lower Princes", "America/Maceio", "America/Managua", "America/Manaus", "America/Marigot", "America/Martinique", "America/Matamoros", "America/Mazatlan", "America/Menominee", "America/Merida", "America/Metlakatla", "America/Mexico City", "America/Miquelon", "America/Moncton", "America/Monterrey", "America/Montevideo", "America/Montreal", "America/Montserrat", "America/Nassau", "America/New York", "America/Nipigon", "America/Nome", "America/Noronha", "America/North Dakota/Beulah", "America/North Dakota/Center", "America/North Dakota/New Salem", "America/Ojinaga", "America/Panama", "America/Pangnirtung", "America/Paramaribo", "America/Phoenix", "America/Port of Spain", "America/Port-au-Prince", "America/Porto Velho", "America/Puerto Rico", "America/Rainy River", "America/Rankin Inlet", "America/Recife", "America/Regina", "America/Resolute", "America/Rio Branco", "America/Santa Isabel", "America/Santarem", "America/Santiago", "America/Santo Domingo", "America/Sao Paulo", "America/Scoresbysund", "America/Shiprock", "America/Sitka", "America/St Barthelemy", "America/St Johns", "America/St Kitts", "America/St Lucia", "America/St Thomas", "America/St Vincent", "America/Swift Current", "America/Tegucigalpa", "America/Thule", "America/Thunder Bay", "America/Tijuana", "America/Toronto", "America/Tortola", "America/Vancouver", "America/Whitehorse", "America/Winnipeg", "America/Yakutat", "America/Yellowknife", "Antarctica/Casey", "Antarctica/Davis", "Antarctica/DumontDUrville", "Antarctica/Macquarie", "Antarctica/Mawson", "Antarctica/McMurdo", "Antarctica/Palmer", "Antarctica/Rothera", "Antarctica/South Pole", "Antarctica/Syowa", "Antarctica/Troll", "Antarctica/Vostok", "Arctic/Longyearbyen", "Asia/Aden", "Asia/Almaty", "Asia/Amman", "Asia/Anadyr", "Asia/Aqtau", "Asia/Aqtobe", "Asia/Ashgabat", "Asia/Baghdad", "Asia/Bahrain", "Asia/Baku", "Asia/Bangkok", "Asia/Beirut", "Asia/Bishkek", "Asia/Brunei", "Asia/Choibalsan", "Asia/Chongqing", "Asia/Colombo", "Asia/Damascus", "Asia/Dhaka", "Asia/Dili", "Asia/Dubai", "Asia/Dushanbe", "Asia/Gaza", "Asia/Harbin", "Asia/Hebron", "Asia/Ho Chi Minh", "Asia/Hong Kong", "Asia/Hovd", "Asia/Irkutsk", "Asia/Jakarta", "Asia/Jayapura", "Asia/Jerusalem", "Asia/Kabul", "Asia/Kamchatka", "Asia/Karachi", "Asia/Kashgar", "Asia/Kathmandu", "Asia/Khandyga", "Asia/Kolkata", "Asia/Krasnoyarsk", "Asia/Kuala Lumpur", "Asia/Kuching", "Asia/Kuwait", "Asia/Macau", "Asia/Magadan", "Asia/Makassar", "Asia/Manila", "Asia/Muscat", "Asia/Nicosia", "Asia/Novokuznetsk", "Asia/Novosibirsk", "Asia/Omsk", "Asia/Oral", "Asia/Phnom Penh", "Asia/Pontianak", "Asia/Pyongyang", "Asia/Qatar", "Asia/Qyzylorda", "Asia/Rangoon", "Asia/Riyadh", "Asia/Sakhalin", "Asia/Samarkand", "Asia/Seoul", "Asia/Shanghai", "Asia/Singapore", "Asia/Taipei", "Asia/Tashkent", "Asia/Tbilisi", "Asia/Tehran", "Asia/Thimphu", "Asia/Tokyo", "Asia/Ulaanbaatar", "Asia/Urumqi", "Asia/Ust-Nera", "Asia/Vientiane", "Asia/Vladivostok", "Asia/Yakutsk", "Asia/Yekaterinburg", "Asia/Yerevan", "Atlantic/Azores", "Atlantic/Bermuda", "Atlantic/Canary", "Atlantic/Cape Verde", "Atlantic/Faroe", "Atlantic/Madeira", "Atlantic/Reykjavik", "Atlantic/South Georgia", "Atlantic/St Helena", "Atlantic/Stanley", "Australia/Adelaide", "Australia/Brisbane", "Australia/Broken Hill", "Australia/Currie", "Australia/Darwin", "Australia/Eucla", "Australia/Hobart", "Australia/Lindeman", "Australia/Lord Howe", "Australia/Melbourne", "Australia/Perth", "Australia/Sydney", "Europe/Amsterdam", "Europe/Andorra", "Europe/Athens", "Europe/Belgrade", "Europe/Berlin", "Europe/Bratislava", "Europe/Brussels", "Europe/Bucharest", "Europe/Budapest", "Europe/Busingen", "Europe/Chisinau", "Europe/Copenhagen", "Europe/Dublin", "Europe/Gibraltar", "Europe/Guernsey", "Europe/Helsinki", "Europe/Isle of Man", "Europe/Istanbul", "Europe/Jersey", "Europe/Kaliningrad", "Europe/Kiev", "Europe/Lisbon", "Europe/Ljubljana", "Europe/London", "Europe/Luxembourg", "Europe/Madrid", "Europe/Malta", "Europe/Mariehamn", "Europe/Minsk", "Europe/Monaco", "Europe/Moscow", "Europe/Oslo", "Europe/Paris", "Europe/Podgorica", "Europe/Prague", "Europe/Riga", "Europe/Rome", "Europe/Samara", "Europe/San Marino", "Europe/Sarajevo", "Europe/Simferopol", "Europe/Skopje", "Europe/Sofia", "Europe/Stockholm", "Europe/Tallinn", "Europe/Tirane", "Europe/Uzhgorod", "Europe/Vaduz", "Europe/Vatican", "Europe/Vienna", "Europe/Vilnius", "Europe/Volgograd", "Europe/Warsaw", "Europe/Zagreb", "Europe/Zaporozhye", "Europe/Zurich", "Indian/Antananarivo", "Indian/Chagos", "Indian/Christmas", "Indian/Cocos", "Indian/Comoro", "Indian/Kerguelen", "Indian/Mahe", "Indian/Maldives", "Indian/Mauritius", "Indian/Mayotte", "Indian/Reunion", "Pacific/Apia", "Pacific/Auckland", "Pacific/Chatham", "Pacific/Chuuk", "Pacific/Easter", "Pacific/Efate", "Pacific/Enderbury", "Pacific/Fakaofo", "Pacific/Fiji", "Pacific/Funafuti", "Pacific/Galapagos", "Pacific/Gambier", "Pacific/Guadalcanal", "Pacific/Guam", "Pacific/Honolulu", "Pacific/Johnston", "Pacific/Kiritimati", "Pacific/Kosrae", "Pacific/Kwajalein", "Pacific/Majuro", "Pacific/Marquesas", "Pacific/Midway", "Pacific/Nauru", "Pacific/Niue", "Pacific/Norfolk", "Pacific/Noumea", "Pacific/Pago Pago", "Pacific/Palau", "Pacific/Pitcairn", "Pacific/Pohnpei", "Pacific/Port Moresby", "Pacific/Rarotonga", "Pacific/Saipan", "Pacific/Tahiti", "Pacific/Tarawa", "Pacific/Tongatapu", "Pacific/Wake", "Pacific/Wallis", "UTC"], []),
            "address": MoPropertyMeta("address", "address", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "addressv6": MoPropertyMeta("addressv6", "addressv6", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "cmc1_is_active": MoPropertyMeta("cmc1_is_active", "cmc1IsActive", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["absent", "active", "standby"], []),
            "cmc2_is_active": MoPropertyMeta("cmc2_is_active", "cmc2IsActive", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["absent", "active", "standby"], []),
            "current_time": MoPropertyMeta("current_time", "currentTime", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "local_time": MoPropertyMeta("local_time", "localTime", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 20, 20, r"""[a-z_0-9 ]*""", [], []),
            "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cluster", "stand-alone", "unspecified"], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "ccEnable": "cc_enable", 
            "dn": "dn", 
            "fipsEnable": "fips_enable", 
            "rn": "rn", 
            "status": "status", 
            "timeZone": "time_zone", 
            "address": "address", 
            "childAction": "child_action", 
            "currentTime": "current_time", 
            "localTime": "local_time", 
            "mode": "mode", 
            "name": "name", 
        },

        "modular": {
            "ccEnable": "cc_enable", 
            "dn": "dn", 
            "fipsEnable": "fips_enable", 
            "rn": "rn", 
            "status": "status", 
            "timeZone": "time_zone", 
            "address": "address", 
            "addressv6": "addressv6", 
            "childAction": "child_action", 
            "cmc1IsActive": "cmc1_is_active", 
            "cmc2IsActive": "cmc2_is_active", 
            "currentTime": "current_time", 
            "localTime": "local_time", 
            "mode": "mode", 
            "name": "name", 
        },

    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.cc_enable = None
        self.fips_enable = None
        self.status = None
        self.time_zone = None
        self.address = None
        self.child_action = None
        self.current_time = None
        self.local_time = None
        self.mode = None
        self.name = None
        self.addressv6 = None
        self.cmc1_is_active = None
        self.cmc2_is_active = None

        ManagedObject.__init__(self, "TopSystem", **kwargs)

