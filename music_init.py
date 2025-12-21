print("🔄 Создаём ПОЛНУЮ БД... 144 легенды! R&B ИСПРАВЛЕН!")

import sqlite3

conn = sqlite3.connect('music.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS artists 
                 (name TEXT, years TEXT, genre TEXT, hits TEXT, facts TEXT)''')

# 🎸 ROCK (12) ✅
rock_data = [
    ('AC/DC', '1973-', 'Hard Rock', 'Back In Black', '1.9B streams - Angus в школьной форме'),
    ('Guns N\' Roses', '1985-', 'Hard Rock', 'Sweet Child O\' Mine', '2.8B streams - Axl Rose скандалист'),
    ('Aerosmith', '1970-', 'Hard Rock', 'Dream On', '1.2B streams - Steven Tyler 70+ лет'),
    ('Queen', '1970-1991', 'Rock', 'Bohemian Rhapsody', '2.9B streams - Фредди Меркьюри'),
    ('Led Zeppelin', '1968-1980', 'Hard Rock', 'Stairway to Heaven', '1.5B streams - Джимми Пейдж'),
    ('Deep Purple', '1968-', 'Hard Rock', 'Smoke on the Water', '800M streams - Классика рока'),
    ('Nirvana', '1987-1994', 'Grunge', 'Smells Like Teen Spirit', '1.9B streams - Курт Кобейн'),
    ('Metallica', '1981-', 'Thrash Metal', 'Enter Sandman', '1.9B streams - James Hetfield'),
    ('Pink Floyd', '1965-', 'Progressive Rock', 'Comfortably Numb', '700M streams - The Wall опера'),
    ('The Beatles', '1960-1970', 'Rock', 'Here Comes the Sun', '2.1B streams - Битломания'),
    ('The Doors', '1965-1973', 'Psychedelic Rock', 'Light My Fire', '600M streams - Джим Моррисон'),
    ('The Rolling Stones', '1962-', 'Rock', 'Paint It Black', '1.1B streams - Мик Джаггер')
]

# 🎤 POP (12) ✅
pop_data = [
    ('Madonna', '1958-', 'Pop', 'Hung Up', '500M streams - Королева поп-музыки'),
    ('Michael Jackson', '1958-2009', 'Pop', 'Billie Jean', '2.1B streams - Король поп-музыки'),
    ('Britney Spears', '1981-', 'Pop', 'Baby One More Time', '900M streams - Принцесса поп'),
    ('Elvis Presley', '1935-1977', 'Rock Pop', 'Suspicious Minds', '700M streams - Король рок-н-ролла'),
    ('ABBA', '1972-1982', 'Pop', 'Dancing Queen', '2.2B streams - Шведский квартет'),
    ('Taylor Swift', '1989-', 'Pop', 'Anti-Hero', '1.8B streams - Эра туров'),
    ('Rihanna', '1988-', 'Pop R&B', 'We Found Love', '1.6B streams - Fenty империя'),
    ('Cher', '1946-', 'Pop', 'Believe', '1.2B streams - Автотюн №1 хит'),
    ('Whitney Houston', '1963-2012', 'Pop Soul', 'I Will Always Love You', '1.4B streams - Голос 7 октав'),
    ('Prince', '1958-2016', 'Pop Funk', 'Purple Rain', '800M streams - Гитарный виртуоз'),
    ('George Michael', '1963-2016', 'Pop', 'Careless Whisper', '1.7B streams - Wham! карьера'),
    ('Lady Gaga', '1986-', 'Pop', 'Bad Romance', '1.5B streams - Маленькие монстры')
]

# 🤘 METAL (12) ✅
metal_data = [
    ('Iron Maiden', '1975-', 'Heavy Metal', 'The Trooper', '400M streams - Эдди маскот'),
    ('Judas Priest', '1969-', 'Heavy Metal', 'Breaking the Law', '300M streams - Роб Хэлфорд'),
    ('Black Sabbath', '1968-', 'Heavy Metal', 'Paranoid', '700M streams - Оззи Осборн'),
    ('Slayer', '1981-', 'Thrash Metal', 'Raining Blood', '200M streams - Трэш пионеры'),
    ('Megadeth', '1983-', 'Thrash Metal', 'Symphony of Destruction', '250M streams - Дэйв Мастейн'),
    ('Slipknot', '1995-', 'Nu Metal', 'Duality', '500M streams - 9 масок'),
    ('Rammstein', '1994-', 'Industrial Metal', 'Du Hast', '600M streams - Немецкий шок-рок'),
    ('Ozzy Osbourne', '1948-', 'Heavy Metal', 'Crazy Train', '900M streams - Принц тьмы'),
    ('Pantera', '1981-2003', 'Groove Metal', 'Walk', '400M streams - Dimebag Darrell'),
    ('System of a Down', '1994-', 'Alternative Metal', 'Chop Suey!', '1.1B streams - Армянский метал'),
    ('Motörhead', '1975-2015', 'Heavy Metal', 'Ace of Spades', '300M streams - Lemmy Килмистер'),
    ('Disturbed', '1994-', 'Nu Metal', 'Down With The Sickness', '800M streams - Oomph! кавер')
]

# 🔥 DISCO (12) ✅
disco_data = [
    ('Bee Gees', '1958-2012', 'Disco', 'Stayin\' Alive', '1.2B streams - Диско короли'),
    ('Donna Summer', '1948-2012', 'Disco', 'I Feel Love', '600M streams - Королева диско'),
    ('Village People', '1977-', 'Disco', 'Y.M.C.A.', '1.5B streams - Костюмы 70-х'),
    ('Boney M', '1976-1986', 'Disco', 'Rasputin', '900M streams - Бобби Фаррелл'),
    ('Earth Wind & Fire', '1969-', 'Disco Funk', 'September', '1.3B streams - Хорн-секция'),
    ('Chic', '1976-', 'Disco Funk', 'Le Freak', '700M streams - Nile Rodgers'),
    ('KC and the Sunshine Band', '1973-', 'Disco', 'Get Down Tonight', '400M streams - Флорида диско'),
    ('Gloria Gaynor', '1949-', 'Disco', 'I Will Survive', '1.1B streams - Диско-гимн'),
    ('Cerrone', '1952-', 'Disco', 'Supernature', '200M streams - Французский диско'),
    ('Sylvester', '1947-1988', 'Disco', 'You Make Me Feel', '300M streams - Фэлсет-король'),
    ('The Jacksons', '1964-', 'Disco Funk', 'Shake Your Body', '400M streams - Братья Джексоны'),
    ('ABBA', '1972-1982', 'Pop Disco', 'Dancing Queen', '2.2B streams - Шведский квартет')
]

# 🎤 HIP-HOP (12) ✅
hiphop_data = [
    ('Eminem', '1972-', 'Hip-Hop', 'Love The Way You Lie', '2.0B streams - 8 Mile рэпер'),
    ('Drake', '1986-', 'Hip-Hop', "God's Plan", '1.7B streams - 6ixside король'),
    ('Kanye West', '1977-', 'Hip-Hop', 'Stronger', '1.2B streams - Yeezy империя'),
    ('Tupac Shakur', '1971-1996', 'Gangsta Rap', 'California Love', '600M streams - West Coast'),
    ('The Notorious B.I.G.', '1972-1997', 'East Coast Rap', 'Hypnotize', '700M streams - Biggie Smalls'),
    ('Snoop Dogg', '1971-', 'G-Funk', 'Gin and Juice', '500M streams - Dre протеже'),
    ('Nas', '1973-', 'Hip-Hop', 'NY State of Mind', '300M streams - Illmatic'),
    ('50 Cent', '1975-', 'Gangsta Rap', 'In Da Club', '1.0B streams - 9 пуль'),
    ('Post Malone', '1995-', 'Hip-Hop Pop', 'Rockstar', '2.2B streams - Тату рэпер'),
    ('Travis Scott', '1991-', 'Trap', 'Sicko Mode', '1.9B streams - Astroworld'),
    ('Lil Wayne', '1982-', 'Hip-Hop', 'Lollipop', '800M streams - Young Money'),
    ('Cardi B', '1992-', 'Hip-Hop', 'WAP', '1.3B streams - Первая рэперша №1')
]

# ⚡️ EDM (12) ✅
edm_data = [
    ('David Guetta', '1967-', 'EDM', 'Titanium', '1.8B streams - Французский хаус'),
    ('Daft Punk', '1993-2021', 'French House', 'Get Lucky', '1.9B streams - Роботы в шлемах'),
    ('Avicii', '1989-2018', 'Progressive House', 'Wake Me Up', '1.7B streams - Levels хит'),
    ('Calvin Harris', '1984-', 'EDM', 'Feel So Close', '800M streams - Шотландский диджей'),
    ('Marshmello', '1992-', 'Future Bass', 'Happier', '1.5B streams - Маршмеллоу шлем'),
    ('Martin Garrix', '1996-', 'Big Room', 'Animals', '1.6B streams - Самый молодой топ'),
    ('Skrillex', '1988-', 'Dubstep', 'Bangarang', '500M streams - Дубстеп король'),
    ('Deadmau5', '1981-', 'Progressive House', "Ghosts 'n' Stuff", '600M streams - Мышь шлем'),
    ('The Chainsmokers', '2008-', 'EDM Pop', 'Closer', '1.9B streams - Selfie диджеи'),
    ('Tiësto', '1969-', 'Trance', 'Adagio For Strings', '400M streams - Trance бог'),
    ('Armin van Buuren', '1976-', 'Trance', 'Blah Blah Blah', '300M streams - A State of Trance'),
    ('Swedish House Mafia', '2008-2023', 'Progressive House', "Don't You Worry Child", '1.2B streams - Mafia трио')
]

# 💎 R&B (12) - ✅ ПОЛНОСТЬЮ ЗАПОЛНЕНО!
rnb_data = [
    ('Beyoncé', '1981-', 'R&B Pop', 'Halo', '1.4B streams - Destiny\'s Child лидер'),
    ('The Weeknd', '1990-', 'R&B', 'Blinding Lights', '4.6B streams - Starboy эра'),
    ('Alicia Keys', '1981-', 'R&B Soul', 'If I Ain\'t Got You', '1.2B streams - Пианистка'),
    ('SZA', '1989-', 'R&B', 'Kill Bill', '1.5B streams - Ctrl альбом'),
    ('Usher', '1978-', 'R&B', 'Yeah!', '1.1B streams - Confessions альбом'),
    ('Chris Brown', '1989-', 'R&B', 'No Guidance', '900M streams - Танцоры король'),
    ('Frank Ocean', '1987-', 'R&B', 'Thinkin Bout You', '600M streams - Blonde альбом'),
    ('H.E.R.', '1997-', 'R&B', 'Best Part', '500M streams - Грамми победитель'),
    ('Kehlani', '1995-', 'R&B', 'CRZY', '300M streams - Bay Area звезда'),
    ('Bryson Tiller', '1993-', 'R&B Trap', "Don't", '1.0B streams - Trap соул'),
    ('Daniel Caesar', '1995-', 'R&B Soul', 'Get You', '400M streams - Freudian хит'),
    ('Ne-Yo', '1979-', 'R&B', 'So Sick', '500M streams - Хитмейкер №1')
]

# 🌀 PSYCHEDELIC (12) ✅
psy_data = [
    ('Pink Floyd', '1965-', 'Psychedelic Rock', 'Wish You Were Here', '1.2B streams - The Wall концепт'),
    ('The Doors', '1965-1973', 'Psychedelic Rock', 'Riders on the Storm', '500M streams - Джим Моррисон'),
    ('Jimi Hendrix', '1942-1970', 'Psychedelic Rock', 'All Along the Watchtower', '600M streams - Гитара зубами'),
    ('Grateful Dead', '1965-1995', 'Psychedelic Rock', 'Touch of Grey', '200M streams - Длинные джемы'),
    ('Jefferson Airplane', '1965-1972', 'Psychedelic Rock', 'White Rabbit', '300M streams - Грейс Слик'),
    ('Cream', '1966-1968', 'Psychedelic Rock', 'Sunshine of Your Love', '700M streams - Эрик Клэптон'),
    ('The Who', '1964-', 'Psychedelic Rock', 'Baba O\'Riley', '800M streams - Синтезаторный рифф'),
    ('The Moody Blues', '1964-', 'Psychedelic Rock', 'Nights in White Satin', '600M streams - Симфонический рок'),
    ('Procol Harum', '1967-', 'Psychedelic Rock', 'A Whiter Shade of Pale', '500M streams - Орган Хаммонд'),
    ('The Zombies', '1961-1967', 'Psychedelic Rock', 'Time of the Season', '400M streams - Британское вторжение'),
    ('The Byrds', '1964-1973', 'Psychedelic Rock', 'Turn! Turn! Turn!', '400M streams - 12-струнная гитара'),
    ('Love', '1965-1971', 'Psychedelic Rock', 'Alone Again Or', '200M streams - Артур Ли')
]

# 🇯🇲 REGGAE (12) ✅
reggae_data = [
    ('Bob Marley', '1945-1981', 'Reggae', 'Three Little Birds', '1.8B streams - Король регги'),
    ('Peter Tosh', '1944-1987', 'Reggae', 'Legalize It', '100M streams - Wailers сооснователь'),
    ('Steel Pulse', '1975-', 'Reggae', 'Your House', '50M streams - Британский регги'),
    ('UB40', '1978-', 'Reggae Pop', 'Red Red Wine', '800M streams - Британский регги-рок'),
    ('Jimmy Cliff', '1944-', 'Reggae', 'The Harder They Come', '100M streams - Регги-фильм'),
    ('Toots and the Maytals', '1963-', 'Ska Reggae', 'Pressure Drop', '200M streams - Funky Kingston'),
    ('Burning Spear', '1945-', 'Roots Reggae', 'Marcus Garvey', '80M streams - Дреды пророк'),
    ('Gregory Isaacs', '1951-2010', 'Lovers Rock', 'Night Nurse', '150M streams - Крул-лару'),
    ('Black Uhuru', '1974-', 'Roots Reggae', "Guess Who's Coming to Dinner", '50M streams - Дуб-трио'),
    ('Third World', '1973-', 'Reggae Pop', 'Now That We Found Love', '100M streams - Стеви Вандер кавер'),
    ('Aswad', '1975-', 'Reggae Funk', "Don't Turn Around", '150M streams - Ace of Base кавер'),
    ('Shaggy', '1968-', 'Reggae Pop', "It Wasn't Me", '1.2B streams - Mr. Boombastic')
]

# ⛓️ PUNK (12) ✅
punk_data = [
    ('Green Day', '1987-', 'Punk Rock', 'Boulevard of Broken Dreams', '1.5B streams - American Idiot'),
    ('The Clash', '1976-1986', 'Punk Rock', 'Should I Stay or Should I Go', '600M streams - Политический панк'),
    ('Sex Pistols', '1975-1978', 'Punk Rock', 'God Save the Queen', '200M streams - Шок-панк'),
    ('The Ramones', '1974-1996', 'Punk Rock', 'Blitzkrieg Bop', '300M streams - Hey ho let\'s go'),
    ('The Offspring', '1984-', 'Punk Rock', 'Self Esteem', '400M streams - Smash альбом'),
    ('Blink-182', '1992-', 'Pop Punk', 'All the Small Things', '1.2B streams - Enema of the State'),
    ('Sum 41', '1996-', 'Pop Punk', 'In Too Deep', '300M streams - All Killer No Filler'),
    ('NOFX', '1983-', 'Punk Rock', 'Linoleum', '100M streams - Fat Mike'),
    ('Rancid', '1991-', 'Punk Rock', 'Time Bomb', '150M streams - Тим Армстронг'),
    ('Bad Religion', '1980-', 'Punk Rock', '21st Century Digital Boy', '80M streams - Грег Графин'),
    ('Dead Kennedys', '1978-1986', 'Hardcore Punk', 'Holiday in Cambodia', '100M streams - Джей Си'),
    ('Black Flag', '1976-1986', 'Hardcore Punk', 'Rise Above', '80M streams - Грег Гинн')
]

# 🌈 INDIE (12) ✅
indie_data = [
    ('Arctic Monkeys', '2002-', 'Indie Rock', 'I Wanna Be Yours', '2.88B streams - AM альбом'),
    ('Tame Impala', '2007-', 'Psychedelic Indie', 'The Less I Know The Better', '1.9B streams - Kevin Parker'),
    ('The Strokes', '1998-', 'Indie Rock', 'Last Nite', '500M streams - Is This It дебют'),
    ('Radiohead', '1985-', 'Alternative Indie', 'Creep', '2.0B streams - OK Computer шедевр'),
    ('The Killers', '2001-', 'Indie Rock', 'Mr. Brightside', '2.1B streams - Hot Fuss'),
    ('Franz Ferdinand', '2002-', 'Indie Rock', 'Take Me Out', '600M streams - Шотландский инди'),
    ('Vampire Weekend', '2006-', 'Indie Pop', 'A-Punk', '200M streams - Колумбийский университет'),
    ('The 1975', '2002-', 'Indie Pop', 'Chocolate', '800M streams - Матти Хили'),
    ('Foster the People', '2009-', 'Indie Pop', 'Pumped Up Kicks', '2.3B streams - Инди хит №1'),
    ('MGMT', '2002-', 'Indie Electronic', 'Electric Feel', '900M streams - Oracular Spectacular'),
    ('Phoenix', '1999-', 'Indie Rock', '1901', '400M streams - Французский инди'),
    ('Two Door Cinema Club', '2007-', 'Indie Rock', 'What You Know', '500M streams - Северная Ирландия')
]

# 👑 LEGENDS (12) ✅
legends_data = [
    ('Queen', '1970-1991', 'Rock', 'Bohemian Rhapsody', '2.9B streams - Вечная классика'),
    ('The Beatles', '1960-1970', 'Rock', 'Here Comes the Sun', '2.1B streams - Битломания'),
    ('Michael Jackson', '1958-2009', 'Pop', 'Billie Jean', '2.1B streams - Король поп-музыки'),
    ('Metallica', '1981-', 'Thrash Metal', 'Enter Sandman', '1.9B streams - Метал-легенды'),
    ('Eminem', '1972-', 'Hip-Hop', 'Love The Way You Lie', '2.0B streams - Рэп №1'),
    ('Madonna', '1958-', 'Pop', 'Hung Up', '500M streams - Королева поп'),
    ('Led Zeppelin', '1968-1980', 'Hard Rock', 'Stairway to Heaven', '1.5B streams - Рок-легенды'),
    ('Pink Floyd', '1965-', 'Progressive Rock', 'Wish You Were Here', '1.2B streams - Психоделия'),
    ('Bob Marley', '1945-1981', 'Reggae', 'Three Little Birds', '1.8B streams - Регги король'),
    ('Nirvana', '1987-1994', 'Grunge', 'Smells Like Teen Spirit', '1.9B streams - Гранж революция'),
    ('AC/DC', '1973-', 'Hard Rock', 'Back In Black', '1.9B streams - Хард-рок короли'),
    ('Elvis Presley', '1935-1977', 'Rock Pop', 'Suspicious Minds', '700M streams - Король рок-н-ролла')
]

# ========================================
# ВСЕ 144 АРТИСТА!
# ========================================
all_data = (rock_data + pop_data + metal_data + disco_data + hiphop_data + 
            edm_data + rnb_data + psy_data + reggae_data + punk_data + 
            indie_data + legends_data)

# ОЧИСТИМ и ЗАПОЛНИМ
cursor.execute("DELETE FROM artists")
cursor.executemany("INSERT INTO artists VALUES (?,?,?,?,?)", all_data)
conn.commit()
conn.close()

print(f"✅ ПОЛНАЯ БАЗА! {len(all_data)} легенд!")
print("🎵 R&B: Beyoncé, The Weeknd, SZA ✅ ВСЕ РАБОТАЕТ!")
print("🚀 py bot.py")
