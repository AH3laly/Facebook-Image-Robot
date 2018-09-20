DROP DATABASE IF EXISTS imagerobot;
CREATE DATABASE imagerobot;

USE imagerobot;

DROP TABLE IF EXISTS image;
CREATE TABLE image (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    url varchar(255) NOT NULL,
    catchDate DATETIME NOT NULL,
    isPublished TINYINT NOT NULL DEFAULT 0,
    publishDate DATETIME NULL,
    categoryId INT NOT NULL,
    urlId VARCHAR(255) NOT NULL,
    type VARCHAR(20) NOT NULL,
    publishError TINYINT NOT NULL DEFAULT 0,
    facebookId VARCHAR(255) NULL,
    INDEX urlId(urlId),
    INDEX categoryId(categoryId),
    INDEX isPublished(isPublished)
) CHARSET UTF8;

DROP TABLE IF EXISTS category;

CREATE TABLE category (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(255) NOT NULL,
    searchString VARCHAR(255) NULL,
    title VARCHAR(255) NULL,
    description VARCHAR(255) NULL,
    keywords VARCHAR(255) NULL,
    isEnabled TINYINT NOT NULL DEFAULT 1,
    UNIQUE INDEX name(name)
) CHARSET UTF8;

INSERT INTO category (name,description) VALUES ('nature','Wonderful Nature');

INSERT INTO category (name,description) VALUES ('space','Wonderful Space');

INSERT INTO category (name,description) VALUES ('universe','Wonderful Universe');

INSERT INTO category (name,description) VALUES ('sweet babies','Wonderful Babies');

INSERT INTO category (name,description) VALUES ('weapons','Wonderful Weapons');

INSERT INTO category (name,description) VALUES ('planes','Wonderful Planes');

INSERT INTO category (name,description) VALUES ('babies','Wonderful Babies');

INSERT INTO category (name,description) VALUES ('baby','Wonderful Babies');

INSERT INTO category (name,description) VALUES ('mountains','Wonderful Mountains');

INSERT INTO category (name,description) VALUES ('green lands','Wonderful Lands');

INSERT INTO category (name,description) VALUES ('backgrounds','Wonderful Backgrounds');

INSERT INTO category (name,description) VALUES ('cute cats','Wonderful Cats');

INSERT INTO category (name,description) VALUES ('cute birds','Wonderful Birds');

INSERT INTO category (name,description) VALUES ('cute dogs','Wonderful Dogs');

INSERT INTO category (name,description) VALUES ('cars','Wonderful Cars');

INSERT INTO category (name,description) VALUES ('villas','Wonderful Villas');

INSERT INTO category (name,description) VALUES ('nice homes','Wonderful Homes');

INSERT INTO category (name,description) VALUES ('desert','Wonderful Desert');

INSERT INTO category (name,description) VALUES ('pyramids','Wonderful Pyramids');

INSERT INTO category (name,description) VALUES ('towers','Wonderful Towers');

INSERT INTO category (name,description) VALUES ('fish','Wonderful Fish');

INSERT INTO category (name,description) VALUES ('space rocket','Wonderful Space Rockets');

INSERT INTO category (name,description) VALUES ('bmw cars','Wonderful BMW Cars');

INSERT INTO category (name,description) VALUES ('harley davidson bikes','Wonderful Bikes');

INSERT INTO category (name,description) VALUES ('jaguar cat','Wonderful Cats');

INSERT INTO category (name,description) VALUES ('creative background','Wonderful Backgrounds');

INSERT INTO category (name,description) VALUES ('nuclear explosion','Wonderful Nuclear Power');

INSERT INTO category (name,description) VALUES ('jewellery','Wonderful Jewellery');

INSERT INTO category (name,description) VALUES ('diamond','Wonderful Diamond');

INSERT INTO category (name,description) VALUES ('emerald','Wonderful Emerald');

INSERT INTO category (name,description) VALUES ('snakes','Wonderful Snakes');

INSERT INTO category (name,description) VALUES ('wind turbine','Wonderful Wind Turbines');

INSERT INTO category (name,description) VALUES ('flying balloon','Wonderful Balloon');

INSERT INTO category (name,description) VALUES ('honey bee','Wonderful Bee');

INSERT INTO category (name,description) VALUES ('roses images','Wonderful Roses');

INSERT INTO category (name,description) VALUES ('happy birthday wishes','Happy Birthday Wishes');

INSERT INTO category (name,description) VALUES ('happy birthday cake','Happy Birthday Cakes');

INSERT INTO category (name,description) VALUES ('sunrise','Wonderful Sunrise');

INSERT INTO category (name,description) VALUES ('ocean sunrise','Wonderful Ocean Sunrise');

INSERT INTO category (name,description) VALUES ('ocean waves','Wonderful Ocean Waves');

INSERT INTO category (name,description) VALUES ('wallpaper hd','Wonderful Wallpapers');

INSERT INTO category (name,description) VALUES ('background hd','Wondeful Backgrounds');

INSERT INTO category (name,description) VALUES ('robots images hd','Wonderful Robots');

INSERT INTO category (name,description) VALUES ('tom and jerry comics','Tom & Jerry <3');

INSERT INTO category (name,description) VALUES ('light bulbs wallpaper','Wonderful Light Bulbs');

INSERT INTO category (name,description) VALUES ('guns images hd','Wonderful Weapons');

INSERT INTO category (name,description) VALUES ('knife images hd','Wonderful Weapons');

INSERT INTO category (name,description) VALUES ('glass wallpaper hd','Wonderful Glass Wallpapers');

INSERT INTO category (name,description) VALUES ('falls wallpaper hd','Wonderful Falls Wallpaper');

INSERT INTO category (name,description) VALUES ('ship wallpaper hd','Wonderful Ships');

INSERT INTO category (name,description) VALUES ('cartoon wallpaper hd','Wonderful Cartoon <3 ');

INSERT INTO category (name,description) VALUES ('dinosaur wallpaper hd','Wonderful Dinosaur');

INSERT INTO category (name,description) VALUES ('galaxy wallpaper','Wonderful Galaxy');

INSERT INTO category (name,description) VALUES ('panda hd wallpaper','Wonderful Panda');

INSERT INTO category (name,description) VALUES ('business wallpaper','Wonderful Business Wallpaper');


UPDATE category SET searchString = name;

DROP TABLE IF EXISTS setting;

CREATE TABLE setting (
    optionName VARCHAR(255) NOT NULL KEY,
    optionValue VARCHAR(255) NOT NULL
) CHARSET UTF8;

INSERT INTO setting VALUES ('lastParsedCategory','0');
INSERT INTO setting VALUES ('lastPublishedCategory','0');
INSERT INTO setting VALUES ('lastPublishedImage','0');

