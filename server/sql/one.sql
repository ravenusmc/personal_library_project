CREATE DATABASE personal_library;

use rsonal_library;


book_dictionary["Authors"] = authors
book_dictionary["LC Classifications"] = lc_classifications
book_dictionary["Publish Date"] = publish_date
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
  lastName VARCHAR(240) NOT NULL,
username VARCHAR(240) NOT NULL,
  email VARCHAR(240) NOT NULL,
  password VARCHAR(240) NOT NUll,
  PRIMARY KEY(user_id)
);