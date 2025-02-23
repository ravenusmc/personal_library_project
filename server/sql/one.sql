mysql -u root -p 

CREATE DATABASE personal_library;

use personal_library;

--Table for the books. 
CREATE TABLE books
(
  book_id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(240) NOT NULL,
  firstName VARCHAR(240) NOT NULL,
  lastName VARCHAR(240) NOT NULL,
  LC_Classifications VARCHAR(240) NOT NULL,
  Publish_Date DATE NULL, 
  Publisher VARCHAR(240) NOT NULL, 
  Subjects VARCHAR(240) NOT NULL, 
  Pagination VARCHAR(240) NOT NULL, 
  Info_URL VARCHAR(240) NOT NULL, 
  location VARCHAR(10) NOT NULL,
  PRIMARY KEY(book_id)
);

CREATE TABLE users
(
  user_id INT NOT NULL AUTO_INCREMENT,
	username VARCHAR(240) NOT NULL,
  email VARCHAR(240) NOT NULL,
  password VARCHAR(240) NOT NUll,
  PRIMARY KEY(user_id)
);