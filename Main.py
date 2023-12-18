def PrefixPhonetics(prefix, text, standard_word):
    prefix = prefix
    text = text
    standar_word = standard_word

    # Mengambil huruf terakhir dari prefix
    last_perfix = prefix[-1]
    first_standard_word = standard_word[0]

    # Membandingkan huruf terakhir prefix dan huruf pertama kata baku
    if last_perfix == first_standard_word:
        phonem = word[0:2]
    else:
        # membandingkan apakah katabaku ada didalam text
        if standard_word in word:
            phonem = word[0:3]
        else:
            phonem = word[0:2]

    # Mengembalikan bentuk fonem pertama
    return phonem
