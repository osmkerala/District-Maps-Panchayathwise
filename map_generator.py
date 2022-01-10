import geopandas as gpd
from pathlib import Path
 
 
class MapGenerator(object):
    
    """
    Generates map of given district of kerala with localbody boundaries.
    
    ...
    
    Attributes
    ----------
    
    district : str
    
        Name of district of which map is needed.
        
    out_format : str
        
        Format of image output. Normal formats supported by matplotlib `savefig()`.
        
    Methods
    -------
    plot_map(cmap = True)
    
        Function to save the plotin given image format.
    
    """
    
    def __init__(self, district: str, out_format: str):
        self.district = district.lower()
        self.out_format = out_format.lower()
        
    def __clean_map(self) -> gpd.geodataframe.GeoDataFrame:
        df = gpd.read_file(f"geojson_files/{self.district}.geojson")
        remove_words = ['panchayath', 'Grama', 'grama', 'Panchayath', 'panchayat',
                        'Panchayat','Gramapanchayat', 'Gramapanchayath','Grampanchayat']
        rem = r'\b(?:{})\b'.format('|'.join(remove_words))
        df["NAME"] = df['name'].str.replace(rem, '',regex=True)
        df.dropna(subset=['NAME'], inplace=True)
        v_df = df[df['local_authority:IN'].isin(['municipal_corporation','gram_panchayat','municipality'])].copy()
        v_df["NAME"] = v_df["NAME"].str.rstrip()
        v_df['coords'] = v_df['geometry'].apply(lambda x: x.representative_point().coords[:])
        v_df['coords'] = [coords[0] for coords in v_df['coords']]
        return v_df
        
    def plot_map(self,cmap: bool  = True):
        """
        Saves image of map of given district with option for colour or balck and white map with given format.
        
        Parameters
        ----------
        
        cmap : bool, default : True
        
            If coloured map is needed, use `cmap = True`. Else for black and white map diagram, use `cmap = False`.      
        
        """
        
        v_df = self.__clean_map()
        if cmap == True:
            ax = v_df.plot(figsize=(25,25),scheme="quantiles", edgecolor='gray',linewidth=2,cmap= 'Set3')
        else:
            ax = v_df.plot(figsize=(25,25),scheme="quantiles", edgecolor='black',linewidth=2,color='white')
        ax.tick_params(left = False, bottom = False, labelbottom = False, labelleft = False)
        ax.axis('off')
        for idx, row in v_df.iterrows():
            ax.annotate(text=row['NAME'], xy=row['coords'],color='black',
                         horizontalalignment='center')
        fig = ax.get_figure()
        fig.tight_layout()
        
        Path('maps').mkdir(parents=True, exist_ok=True)
        fig.savefig(f"maps/{self.district.capitalize()}.{self.out_format}",dpi=300, 
                    bbox_inches='tight',pad_inches = 0)
        print(f"Map of {self.district.capitalize()} created in maps folder.")
        
        
if __name__=='__main__':
    maps = MapGenerator('Kollam','png')
    maps.plot_map(cmap= True)
