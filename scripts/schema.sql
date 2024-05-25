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

CREATE TABLE IF NOT EXISTS scrape.Facebook (
   "Facebook_Username" VARCHAR(255),
    "Post_Title" VARCHAR(255),
    "Post_Content" VARCHAR,
    "Date_Posted" VARCHAR(50)
);