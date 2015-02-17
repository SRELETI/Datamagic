%if defined('incidents'):
<div id="map" style='height:100%'></div>
%end
<div class='jumbotron' style='width:500px;margin:auto'>
<form action='/query-interval' method='post'>
<div class='form-group'><label>Select Start Date:</label><input type='text' name='startDate' class='form-control'></br></div><div class='form-group'><label>Select End Date:</label><input type='text' name='endDate' class='form-control'></br></div><div class='form-group'><label>Start At</label><input type='text' name='startTime' class='form-control'></br></div><div class='form-group'><label>End At:</label><input type='text' name='endTime' class='form-control'></br></div><button type='submit'>Submit</button></form>

% if defined('incidents'):  
	<script type="text/javascript"
            src="http://maps.google.com/maps/api/js?sensor=false"></script>
        <script type="text/javascript">
	
	var locations=[];
	%for index in incidents:
	   var lat_lon_arr=  {{ index['Incident_map'] }} ;
	   var description= {{index['Incident_type']}};
	   description += '<br/>';
           description += {{index['Incident_date']}};
           description += '<br/>';
           description += {{index['Incident_location']}};
	   
	   var one_location=[];
	   one_location.push(description);
	   one_location.push(lat_lon_arr[0]);
	   one_location.push(lat_lon_arr[1]);
        locations.push(one_location);
        %end 
	 var map = new google.maps.Map(document.getElementById('map'), {
       zoom: 11,
       center: new google.maps.LatLng(43.468365, -80.517933),
       mapTypeId: google.maps.MapTypeId.ROADMAP
     });

     var infowindow = new google.maps.InfoWindow();

     var marker,i;

     for (i = 0; i < locations.length; i++) {
       marker = new google.maps.Marker({
         position: new google.maps.LatLng(locations[i][1], locations[i][2]),
         map: map
       });

       google.maps.event.addListener(marker, 'click', (function(marker, i) {
         return function() {
           infowindow.setContent(locations[i][0]);
           infowindow.open(map, marker);
         }
       })(marker, i));
     }
    </script>
 
 %end 
</div>
	
