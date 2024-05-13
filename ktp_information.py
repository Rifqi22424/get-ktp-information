import calendar
ktp_2004 = 3272070408040001
ktp_cewe = 3202415201050002

def zodiak(day:int, month:str):
    
    astro_sign = ""
    if month == "december":
        if day < 22: 
            astro_sign = "Sagittarius" 
        else:
            astro_sign ="capricorn" 
    elif month == "january":
        if day < 20: 
            astro_sign = "Capricorn" 
        else:
            astro_sign = "aquarius"  
    elif month == "february":
        if day < 19: 
            astro_sign = "Aquarius" 
        else:
            astro_sign = "pisces"  
    elif month == "march":
        if day < 21:  
            astro_sign = "Pisces" 
        else:
            astro_sign = "aries"  
    elif month == "april":
        if day < 20: 
            astro_sign = "Aries" 
        else:
            astro_sign = "taurus"  
    elif month == "may":
        if day < 21: 
            astro_sign = "Taurus" 
        else:
            astro_sign = "gemini"  
    elif month == "june":
        if day < 21: 
            astro_sign = "Gemini" 
        else:
            astro_sign = "cancer"  
    elif month == "july":
        if day < 23: 
            astro_sign = "Cancer" 
        else:
            astro_sign = "leo"  
    elif month == "august":
        if day < 23:  
            astro_sign = "Leo" 
        else:
            astro_sign = "virgo"
    elif month == "september":
        if day < 23: 
            astro_sign = "Virgo" 
        else:
            astro_sign = "libra"  
    elif month == "october":
        if day < 23: 
            astro_sign = "Libra" 
        else:
            astro_sign = "scorpio"  
    elif month == "november":
        if day < 22: 
            astro_sign = "scorpio" 
        else:
            astro_sign = "sagittarius"  
    return astro_sign

def infoKtp(ktp:int, isPerempuan:bool):
    ktp = str(ktp)
    
    tgl = ktp[6:8]
    bln = ktp[8:10]
    thn = ktp[10:12]
    
    tgl = int(tgl)
    
    if isPerempuan:
        tgl = int(tgl) - 40
    
    bln = int(bln)
    string_bln = calendar.month_name[bln]
    
    tahun_lhr = 0
    if 2000 + int(thn) >= 2024:
        tahun_lhr = "19" + thn 
    else:
        tahun_lhr = "20" + thn
    
    print(f"tanggal lahir: {tgl}, {string_bln}, {tahun_lhr}")
    
    tahun_ksr = 2024 - int(tahun_lhr)
    
    if bln > 5 or (bln == 5 and tgl > 13):
        tahun_ksr -= 1
    
    print(f"umur: {tahun_ksr}")
    print(f"zodiak {zodiak(int(tgl), string_bln.lower())}")

infoKtp(ktp_2004, False)
infoKtp(ktp_cewe, True)