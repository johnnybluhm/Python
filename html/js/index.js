$(document).ready(function() {    


/*`{'Class Nbr:': '29448', 'Section #:': '001', 'Type:': 'LEC',\
 'Campus:': 'Main', 'Meets:': 'MW', 'Instructor:': '', 'Status:': 'Open',\
  'Dates:': '01-13 to 04-30', 'name': 'CSCI 3010', 'start_time': '4:30p',\
   'end_time': '5:45p'},`*/

   var time = 12;

   for(var i = 0; i< course_list.length;i++){

    for(var j = 0; j< course_list[i].length;j++){
        
        course_list[i][j]['class_num'] = course_list[i][j]['Class Nbr:'];
        course_list[i][j]['section_num'] = course_list[i][j]['Section #:'];
        course_list[i][j]['type'] = course_list[i][j]['Type:'];
        course_list[i][j]['campus'] = course_list[i][j]['Campus:'];
        course_list[i][j]['days'] = course_list[i][j]['Meets:'];
        course_list[i][j]['status'] = course_list[i][j]['Status:'];
        course_list[i][j]['campus'] = course_list[i][j]['Campus:'];
        course_list[i][j]['dates'] = course_list[i][j]['Dates:'];
        course_list[i][j].instructor = course_list[i][j]['Instructor:'];
        delete course_list[i][j]['Type:'];
        delete course_list[i][j]['Class Nbr:'];
        delete course_list[i][j]['Section #:'];
        delete course_list[i][j]['Campus:'];
        delete course_list[i][j]['Meets:'];
        delete course_list[i][j]['Status:'];
        delete course_list[i][j]['Campus:'];
        delete course_list[i][j]['Dates:'];
        delete course_list[i][j]['Instructor:'];

        parseTime(course_list[i][j]);
        
    }//inner for

   }//outer for

   console.log(course_list)

   


});

//parse time from a class object
//time is in from 12:12a or 03:20p
function parseTime(course_obj){

    //get dates in form [1-12, to, 2-23]
    var parse_date= course_obj.dates.split(" ");
   
    var start_date=parse_date[0].split("-");
    var end_date = parse_date[2].split("-");

    var start_month = parseInt(start_date[0],10);
    var start_day = parseInt(start_date[1],10);

    var end_month = parseInt(end_date[0],10);
    var end_day = parseInt(end_date[1],10);

    var start=course_obj.start_time;
    var end = course_obj.end_time;


//remove colon and am/pm and turn into into
  var start_split = start.split(":");
  var end_split = end.split(":");
  var start_hour = parseInt(start_split[0],10);
  var start_min = parseInt(start_split[1],10);
  var start_ampm = start_split[2];

  var end_hour = parseInt(end_split[0],10);
  var end_min = parseInt(end_split[1],10);
  var end_ampm = end_split[2];



 if(start_ampm == 'PM' && start_hour!= 12){
   start_hour = start_hour+12
 }
  
 if(end_ampm == 'PM' && end_hour != 12){
  end_hour = end_hour+12
 }

  var class_start = new Date(2019, start_month-1, start_day, start_hour, start_min);
  var class_end = new Date(2019, end_month-1, end_day, end_hour, end_min);


course_obj['start_time'] = class_start;
course_obj['end_time'] = class_end;

    
}