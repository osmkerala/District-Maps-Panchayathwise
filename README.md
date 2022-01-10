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
