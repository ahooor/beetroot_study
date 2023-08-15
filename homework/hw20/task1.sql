CREATE TABLE animals (
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(255),
PRIMARY KEY (id)
);

ALTER TABLE animals
RENAME TO mammals;

ALTER TABLE mammals 
ADD COLUMN cuteness ENUM("yes", "no");

INSERT INTO mammals(name, cuteness) VALUES
("cat", "yes"),
("dog", "yes"),
("rat", "no"),
("human", "no"),
("cow", "yes");


UPDATE mammals SET cuteness = "no" WHERE name = "cow";

DELETE FROM mammals WHERE id = 5;