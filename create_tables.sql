CREATE TABLE course_data(
  class_num INTEGER,
  section_num INTEGER,
  lec_type VARCHAR(10),
  campus VARCHAR(30),
  open_status VARCHAR(30),
  begin_date DATE,
  end_date DATE,
  course_name VARCHAR(30),
  start_time TIME,
  end_time TIME,
  meet_days VARCHAR(15),
  instructor VARCHAR(30),
  PRIMARY KEY (class_num)
  );

