CREATE DATABASE personal_library;

use rsonal_library;


book_dictionary["Publisher"] = publisher
book_dictionary["Subjects"] = subjects
book_dictionary["Pagination"] = pagination
book_dictionary["Info URL"] = info_url
book_dictionary['Location'] = "A1"    

--Table for the books. 
CREATE TABLE books
(
  book_id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(240) NOT NULL,
  firstName VARCHAR(240) NOT NULL,
  lastName VARCHAR(240) NOT NULL,
  LC_Classifications VARCHAR(240) NOT NULL,
  Publish_Date DATE NOT NULL, 
  Publisher VARCHAR(240) NOT NULL, 
  Subjects VARCHAR(240) NOT NULL, 
  PRIMARY KEY(user_id)
);