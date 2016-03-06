CREATE EXTERNAL TABLE base_profiles_active 
(person_id string,name string,first_name string,last_name string,username string,country_code string,age string,email string,gender string,birthday string,location_independent string)  ROW FORMAT
              DELIMITED FIELDS TERMINATED BY '\t'
              LINES TERMINATED BY '\n' 
              STORED AS TEXTFILE
              LOCATION '/user/data/extracted/base_data';


CREATE EXTERNAL TABLE cv 
(person_id string,cv string)  ROW FORMAT
              DELIMITED FIELDS TERMINATED BY '\t'
              LINES TERMINATED BY '\n' 
              STORED AS TEXTFILE
              LOCATION '/user/data/extracted/cv';


CREATE EXTERNAL TABLE educations
(person_id string,school_id string,school string,school_type string,school_year string)  ROW FORMAT
              DELIMITED FIELDS TERMINATED BY '\t'
              LINES TERMINATED BY '\n' 
              STORED AS TEXTFILE
              LOCATION '/user/data/extracted/educations';


CREATE EXTERNAL TABLE workplaces
(person_id string,employer_id string,employer string,location string,position string)  ROW FORMAT
              DELIMITED FIELDS TERMINATED BY '\t'
              LINES TERMINATED BY '\n' 
              STORED AS TEXTFILE
              LOCATION '/user/data/extracted/workplaces';


CREATE EXTERNAL TABLE haves
(person_id string,haves string)  ROW FORMAT
              DELIMITED FIELDS TERMINATED BY '\t'
              LINES TERMINATED BY '\n' 
              STORED AS TEXTFILE
              LOCATION '/user/data/extracted/haves';

CREATE EXTERNAL TABLE emails
(person_id string,email string)  ROW FORMAT
              DELIMITED FIELDS TERMINATED BY '\t'
              LINES TERMINATED BY '\n' 
              STORED AS TEXTFILE
              LOCATION '/user/data/extracted/emails';

CREATE EXTERNAL TABLE infos
(person_id string,info string)  ROW FORMAT
              DELIMITED FIELDS TERMINATED BY '\t'
              LINES TERMINATED BY '\n' 
              STORED AS TEXTFILE
              LOCATION '/user/data/extracted/infos';

CREATE EXTERNAL TABLE languages
(person_id string,language string)  ROW FORMAT
              DELIMITED FIELDS TERMINATED BY '\t'
              LINES TERMINATED BY '\n' 
              STORED AS TEXTFILE
              LOCATION '/user/data/extracted/languages';

CREATE EXTERNAL TABLE locations
(person_id string,lid string,geocoded_name string,source string,location_type string)  ROW FORMAT
              DELIMITED FIELDS TERMINATED BY '\t'
              LINES TERMINATED BY '\n' 
              STORED AS TEXTFILE
              LOCATION '/user/data/extracted/locations';

CREATE EXTERNAL TABLE logins
(person_id string,login string)  ROW FORMAT
              DELIMITED FIELDS TERMINATED BY '\t'
              LINES TERMINATED BY '\n' 
              STORED AS TEXTFILE
              LOCATION '/user/data/extracted/logins';

CREATE EXTERNAL TABLE mails_sent
(person_id string,mail_sent string)  ROW FORMAT
              DELIMITED FIELDS TERMINATED BY '\t'
              LINES TERMINATED BY '\n' 
              STORED AS TEXTFILE
              LOCATION '/user/data/extracted/mails_sent';

CREATE EXTERNAL TABLE friends_ids
(person_id string,friend_id string)  ROW FORMAT
              DELIMITED FIELDS TERMINATED BY '\t'
              LINES TERMINATED BY '\n' 
              STORED AS TEXTFILE
              LOCATION '/user/data/extracted/friends_ids';



