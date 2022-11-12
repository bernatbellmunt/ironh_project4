use rickandmorty;

set global local_infile =1;

DROP TABLE IF EXISTS all_info;
CREATE TABLE all_info(
	season_no int, episode_no int, episode_name varchar(50),character_name varchar(50), line longtext

);

LOAD data local INFILE '/Users/bernat/github_repo/ironh_project4/data/RickandMorty_2.csv'
	INTO TABLE all_info
		FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;
-- Error Code: 1290. The MySQL server is running with the --secure-file-priv option so it cannot execute this statement
-- Error Code: 2068. LOAD DATA LOCAL INFILE file request rejected due to restrictions on access.
-- Error Code: 2. File '/Users/bernat/github_repo/ironh_project4/data/RickandMorty_2' not found (OS errno 2 - No such file or directory)

select * from all_info limit 2000;