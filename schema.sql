

CREATE TABLE athletes (
    id        	      serial PRIMARY KEY,
    name              varchar(64),

    age      	        int,
    hieght            varchar(5),
    wieght            int,

    clean_and_jerk    varchar(32),
    snatch            varchar(32),
    deadlift          varchar(32),
    back_squat        varchar(32),
    max_pullups       int,
    run_5k            varchar(32),
    created_at        timestamp default current_timestamp
);