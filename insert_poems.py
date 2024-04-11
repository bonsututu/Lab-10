def insert_poems(poems):
    conn = sqlite3.connect('poems.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO poems VALUES (?, ?, ?)', poems)
    conn.commit()
    conn.close()

# List of poems
poems = [
    ('The Road Not Taken', 'Robert Frost', 'Two roads diverged in a yellow wood, And sorry I could not travel both...'),
    ('Ozymandias', 'Percy Bysshe Shelley', 'I met a traveller from an antique land Who said: Two vast and trunkless legs of stone...'),
    ('Daffodils', 'William Wordsworth', 'I wandered lonely as a cloud That floats on high o''er vales and hills...'),
    ('Sonnet 18', 'William Shakespeare', 'Shall I compare thee to a summer''s day? Thou art more lovely and more temperate...'),
    ('The Raven', 'Edgar Allan Poe', 'Once upon a midnight dreary, while I pondered, weak and weary...')
]

# Insert poems into the database
insert_poems(poems)
