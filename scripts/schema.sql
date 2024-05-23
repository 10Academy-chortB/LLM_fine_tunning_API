CREATE TABLE IF NOT EXISTS scrape.News (
   "Headline" TEXT,
   "Content" TEXT,
    "Source" TEXT,
    "date" TEXT
);


CREATE TABLE IF NOT EXISTS scrape.Lyrics (
   "artist" VARCHAR(255),
    "song_name" VARCHAR(255),
    "lyrics" TEXT,
    "duration" VARCHAR(50)
);