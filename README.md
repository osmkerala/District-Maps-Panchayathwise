# Kerala-Panchayath-Maps
Python project to generate Kerala's distrcit level panchayath map.


As of now, geojson files of Kollam and Kozhikode are added to the folder `geojson_files`. So other districts won't work.

### Usage 

1. Install requirements using 

    ```pip install -r requirements.txt ```

2. Run the below command:

    ```python map_generator.py -d Kollam -f png -c True```
    
    Here `-f` and `-c` are optional arguements. 
    
    For details on arguements, run:
    
    ```python map_generator.py -h```
    
    output:
    
	>    		optional arguments:
	>            		-h, --help            show this help message and exit
	>  
	>            -d DISTRICT, --district DISTRICT
	>                        District name
	>                        
	>            -f FORMAT, --format FORMAT
	>                        Output image format (default: png)
	>                        
	>            -c CMAP, --cmap CMAP  
	>                    If coloured map is required, use True. else use False.(default : True)
	>  
	    
    
4. Map file is generated in `maps` folder.

### Sample Map

#### Coloured Map

![kollam-cmap](maps/Kollam.png)

#### Black and White Map

![kollam-no-cmap](maps/Kollam_no_cmap.png)

### Generate GeoJson from OpenstreetMap

goto [Overpass](http://overpass-turbo.eu/) and use the code below:

	[out:xml][timeout:500];
	{{geocodeArea:Kozhikode district}}->.searchArea;
	(
	   nwr["boundary"="local_authority"]["admin_level"="8"](area.searchArea);
	);
	// print results
	out meta;
	>;
	out meta qt;

change district name to desired one.

### References

1. [https://wiki.openstreetmap.org/wiki/Local_Bodies_in_Kerala](https://wiki.openstreetmap.org/wiki/Local_Bodies_in_Kerala) https://wiki.openstreetmap.org/wiki/Local_Bodies_in_Kerala
2. [http://overpass-turbo.eu/](http://overpass-turbo.eu/) http://overpass-turbo.eu/
3. [https://opendatakerala.org/](https://opendatakerala.org/) https://opendatakerala.org/
4. Various solved answers from [Stack Overflow](https://stackoverflow.com/)
