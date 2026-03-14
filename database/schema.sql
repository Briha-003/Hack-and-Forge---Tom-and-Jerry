CREATE TABLE users(
id UUID PRIMARY KEY,
email TEXT,
organization TEXT
);

CREATE TABLE conversations(
id UUID PRIMARY KEY,
user_id UUID
);

CREATE TABLE vocabulary(
id UUID PRIMARY KEY,
term TEXT,
enterprise_meaning TEXT,
department TEXT
);
