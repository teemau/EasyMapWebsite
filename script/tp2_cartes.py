
### 2. Cartes intéractives sous Python


#Librairies
import folium
from folium import plugins
from folium.plugins import BeautifyIcon
import pandas as pd
import webbrowser
import numpy as np
from folium.plugins import FloatImage
from folium.features import DivIcon


#Chargement des données géographiques
F_in_StationLocations = "E:/BUT3/SAE/SAE5.EMS.01/data_tp/StationsLocation.xlsx"
F_out = "E:/BUT3/SAE/SAE5.EMS.01/ManausMap.html"

df_StationsLocation = pd.read_excel(F_in_StationLocations)
df_StationsLocation.columns = ['Label', 'Lat', 'Lon']
df_airport=pd.DataFrame(data=np.array([[-3.15,-59.9833]]),columns=['latitude','longitude'])

study_zone_map = folium.Map(location=[-3.1190, -60.0217],
    tiles = 'Esri.WorldTopoMap',
    width="100%",height="100%",)

study_zone_map.save(F_out)
webbrowser.open(F_out)

#  Nous sommes au brésil

# a quoi servent les 4 options dans la fonction folium.map()
# Location : sert à choisir ou l'on regarde
# Tiles : met le style de carte que l'on voit
# Witdh :  largeur de carte
# Height :  hauteur de carte

#  selon l'aide il y aurai 3 fonds de carte




# 2. Ajouts d'éléments (marqueur, label, boucle, mini map zoom, photos, legende, echelle et fleche du nord)

# ajout de marqueur
F_in_StationLocations = "E:/BUT3/SAE/SAE5.EMS.01/data_tp/StationsLocation.xlsx"
F_out = "E:/BUT3/SAE/SAE5.EMS.01/ManausMap3.html"

icon_star = BeautifyIcon(icon='star', inner_icon_style='color:black;font-size:15px;',
background_color='transparent', border_color='transparent',)

# add the icon to the map

df_StationsLocation = pd.read_excel(F_in_StationLocations)
df_StationsLocation.columns = ['Label', 'Lat', 'Lon']
df_airport=pd.DataFrame(data=np.array([[-3.15,-59.9833]]),columns=['latitude','longitude'])

study_zone_map = folium.Map(location=[-3.1190, -60.0217],
    tiles = 'Esri.WorldTopoMap',
    width="100%",height="100%",)

folium.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
tooltip="Click me!",
popup='Airport in the Popup', icon=icon_star,).add_to(study_zone_map)

study_zone_map.save(F_out)

# j'ai ajouté un icon etoile sur l'aeroport de la ville



# 3. Ajout de marqueurs de type cercle


F_in_StationLocations = "E:/BUT3/SAE/SAE5.EMS.01/data_tp/StationsLocation.xlsx"
F_out = "E:/BUT3/SAE/SAE5.EMS.01/ManausMap4.html"

icon_star = BeautifyIcon(icon='star', inner_icon_style='color:black;font-size:15px;',
background_color='transparent', border_color='transparent',)

df_StationsLocation = pd.read_excel(F_in_StationLocations)
df_StationsLocation.columns = ['Label', 'Lat', 'Lon']
df_airport=pd.DataFrame(data=np.array([[-3.15,-59.9833]]),columns=['latitude','longitude'])

study_zone_map = folium.Map(location=[-3.1190, -60.0217],
    tiles = 'Esri.WorldTopoMap',
    width="100%",height="100%",)

folium.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
tooltip="Click me!",
popup='Airport in the Popup', icon=icon_star,).add_to(study_zone_map)

# ajout du marqueur cercle
folium.Circle(location=[df_StationsLocation['Lat'][0],df_StationsLocation['Lon'][1]],
 tooltip="Click me!",
 popup=df_StationsLocation['Label'][0],
 color='crimson',fill=True,radius=15).add_to(study_zone_map)

study_zone_map.save(F_out)

# j'ai ajouté un icon cercle rouge a une location différente dans la ville




# 4. Ajout de labels sur la carte.

F_in_StationLocations = "E:/BUT3/SAE/SAE5.EMS.01/data_tp/StationsLocation.xlsx"
F_out = "E:/BUT3/SAE/SAE5.EMS.01/ManausMap5.html"

icon_star = BeautifyIcon(icon='star', inner_icon_style='color:black;font-size:15px;',
background_color='transparent', border_color='transparent',)

df_StationsLocation = pd.read_excel(F_in_StationLocations)
df_StationsLocation.columns = ['Label', 'Lat', 'Lon']
df_airport=pd.DataFrame(data=np.array([[-3.15,-59.9833]]),columns=['latitude','longitude'])

study_zone_map = folium.Map(location=[-3.1190, -60.0217],
    tiles = 'Esri.WorldTopoMap',
    width="100%",height="100%",)

folium.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
tooltip="Click me!",
popup='Airport in the Popup', icon=icon_star,).add_to(study_zone_map)

folium.Circle(location=[df_StationsLocation['Lat'][0],df_StationsLocation['Lon'][1]],
 tooltip="Click me!",
 popup=df_StationsLocation['Label'][0],
 color='crimson',fill=True,radius=15).add_to(study_zone_map)

# ajout des labels
folium.map.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
icon=DivIcon(icon_size=(150,36),
icon_anchor=(0,0),
html='Airport is here',)).add_to(study_zone_map)


study_zone_map.save(F_out)

# j'ai ajouté un icon label aeroport is here a icon star




# 5. Ajout dune boucle pour avoir les 6 points de collecte marquées rouge et leur nom en label a coté

F_in_StationLocations = "E:/BUT3/SAE/SAE5.EMS.01/data_tp/StationsLocation.xlsx"
F_out = "E:/BUT3/SAE/SAE5.EMS.01/ManausMap6.html"

icon_star = BeautifyIcon(icon='star', inner_icon_style='color:black;font-size:15px;',
    background_color='transparent', border_color='transparent',)

df_StationsLocation = pd.read_excel(F_in_StationLocations)
df_StationsLocation.columns = ['Label', 'Lat', 'Lon']
df_airport=pd.DataFrame(data=np.array([[-3.15,-59.9833]]),columns=['latitude','longitude'])

study_zone_map = folium.Map(location=[-3.1190, -60.0217],
    tiles = 'Esri.WorldTopoMap',
    width="100%",height="100%",)

folium.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
    tooltip="Click me!",
    popup='Airport in the Popup', icon=icon_star,).add_to(study_zone_map)

folium.Circle(location=[df_StationsLocation['Lat'][0],df_StationsLocation['Lon'][1]],
    tooltip="Click me!",
    popup=df_StationsLocation['Label'][0],
    color='crimson',fill=True,radius=15).add_to(study_zone_map)

folium.map.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
    icon=DivIcon(icon_size=(150,36),
    icon_anchor=(0,0),
    html='Airport is here',)).add_to(study_zone_map)

# Boucle pour ajouter les 6 points de collecte (Cercles rouges + Labels à côté)
for idx, row in df_StationsLocation.iterrows():
    # Ajout du cercle rouge pour chaque station
    folium.Circle(
        location=[row['Lat'], row['Lon']],
        tooltip="Click me!",
        popup=str(row['Label']),
        color='crimson',
        fill=True,
        radius=15
    ).add_to(study_zone_map)

    # Ajout du label textuel (nom de la station) à côté du point
    folium.map.Marker(
        location=[row['Lat'], row['Lon']],
        icon=DivIcon(
            icon_size=(150, 36),
            icon_anchor=(-10, 10),  # Décalage pour ne pas superposer exactement sur le cercle
            html=f'<div style="font-size: 10pt; color: black; font-weight: bold;">{row["Label"]}</div>',
        )
    ).add_to(study_zone_map)

study_zone_map.save(F_out)




# 6. Ajout de mini-carte zoom


F_in_StationLocations = "E:/BUT3/SAE/SAE5.EMS.01/data_tp/StationsLocation.xlsx"
F_out = "E:/BUT3/SAE/SAE5.EMS.01/ManausMap7.html"

icon_star = BeautifyIcon(icon='star', inner_icon_style='color:black;font-size:15px;',
    background_color='transparent', border_color='transparent',)

df_StationsLocation = pd.read_excel(F_in_StationLocations)
df_StationsLocation.columns = ['Label', 'Lat', 'Lon']
df_airport=pd.DataFrame(data=np.array([[-3.15,-59.9833]]),columns=['latitude','longitude'])

study_zone_map = folium.Map(location=[-3.1190, -60.0217],
    tiles = 'Esri.WorldTopoMap',
    width="100%",height="100%",)

folium.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
    tooltip="Click me!",
    popup='Airport in the Popup', icon=icon_star,).add_to(study_zone_map)

folium.Circle(location=[df_StationsLocation['Lat'][0],df_StationsLocation['Lon'][1]],
    tooltip="Click me!",
    popup=df_StationsLocation['Label'][0],
    color='crimson',fill=True,radius=15).add_to(study_zone_map)

folium.map.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
    icon=DivIcon(icon_size=(150,36),
    icon_anchor=(0,0),
    html='Airport is here',)).add_to(study_zone_map)

for idx, row in df_StationsLocation.iterrows():
    folium.Circle(
        location=[row['Lat'], row['Lon']],
        tooltip="Click me!",
        popup=str(row['Label']),
        color='crimson',
        fill=True,
        radius=15
    ).add_to(study_zone_map)

    folium.map.Marker(
        location=[row['Lat'], row['Lon']],
        icon=DivIcon(
            icon_size=(150, 36),
            icon_anchor=(-10, 10),
            html=f'<div style="font-size: 10pt; color: black; font-weight: bold;">{row["Label"]}</div>',
        )
    ).add_to(study_zone_map)

# Minimap
minimap = plugins.MiniMap(zoom_level_offset=-7,
    tile_layer = 'Esri.WorldTopoMap')

study_zone_map.add_child(minimap)

study_zone_map.save(F_out)




# 7. Ajout de photos dans les pop ups


F_in_StationLocations = "E:/BUT3/SAE/SAE5.EMS.01/data_tp/StationsLocation.xlsx"
F_out = "E:/BUT3/SAE/SAE5.EMS.01/ManausMap8.html"

icon_star = BeautifyIcon(icon='star', inner_icon_style='color:black;font-size:15px;',
    background_color='transparent', border_color='transparent',)

df_StationsLocation = pd.read_excel(F_in_StationLocations)
df_StationsLocation.columns = ['Label', 'Lat', 'Lon']
df_airport=pd.DataFrame(data=np.array([[-3.15,-59.9833]]),columns=['latitude','longitude'])

study_zone_map = folium.Map(location=[-3.1190, -60.0217],
    tiles = 'Esri.WorldTopoMap',
    width="100%",height="100%",)

folium.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
    tooltip="Click me!",
    popup='Airport in the Popup', icon=icon_star,).add_to(study_zone_map)

folium.Circle(location=[df_StationsLocation['Lat'][0],df_StationsLocation['Lon'][1]],
    tooltip="Click me!",
    popup=df_StationsLocation['Label'][0],
    color='crimson',fill=True,radius=15).add_to(study_zone_map)

folium.map.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
    icon=DivIcon(icon_size=(150,36),
    icon_anchor=(0,0),
    html='Airport is here',)).add_to(study_zone_map)

for idx, row in df_StationsLocation.iterrows():
    folium.Circle(
        location=[row['Lat'], row['Lon']],
        tooltip="Click me!",
        popup=str(row['Label']),
        color='crimson',
        fill=True,
        radius=15
    ).add_to(study_zone_map)

    folium.map.Marker(
        location=[row['Lat'], row['Lon']],
        icon=DivIcon(
            icon_size=(150, 36),
            icon_anchor=(-10, 10),
            html=f'<div style="font-size: 10pt; color: black; font-weight: bold;">{row["Label"]}</div>',
        )
    ).add_to(study_zone_map)

minimap = plugins.MiniMap(zoom_level_offset=-7,
    tile_layer = 'Esri.WorldTopoMap')
study_zone_map.add_child(minimap)

locations = [
    {"name": "Manaus teater", "coords": [-3.1301766836937137, -60.02340049029022],
    "color": "blue", "icon": "church",
    "image": "https://lh5.googleusercontent.com/p/AF1QipM_wIwvAy2YHYT1aHdFiV5eTv14EyU51OSdRIO7=w408-h271-k-no"},
    {"name": "Moon Beach", "coords": [-3.0327694203954794, -60.132860744341016],
    "color": "green", "icon": "umbrella",
    "image": "https://lh5.googleusercontent.com/p/AF1QipOJHfhvspTgy56sr1pInhBAJHfplRPqMfM3c3p=w426-h240-k-no"},
]

# Python Folium icon list
# https://fontawesome.com/icons?d=gallery
for loc in locations:
 # Create the HTML for the popup
    popup_content = f'<strong>{loc["name"]}</strong><br><img src="{loc["image"]}" alt="{loc["name"]}" width="150">'
    folium.Marker(
        loc["coords"],
        tooltip=loc["name"],
        popup=folium.Popup(popup_content, max_width=200),
        icon=folium.Icon(color=loc["color"], prefix='fa', icon=loc["icon"])
        ).add_to(study_zone_map)


study_zone_map.save(F_out)

# Ici on a rajouté 2 icones en plus sur deux locations déterminés plus tôt. Puis on a fait en sorte que lorsque la souris passe sur les 2 icones, on a les photos des lieux de ces icones qui s'affichent



# 8. Ajout de légende

F_in_StationLocations = "E:/BUT3/SAE/SAE5.EMS.01/data_tp/StationsLocation.xlsx"
F_out = "E:/BUT3/SAE/SAE5.EMS.01/ManausMap9.html"

icon_star = BeautifyIcon(icon='star', inner_icon_style='color:black;font-size:15px;',
    background_color='transparent', border_color='transparent',)

df_StationsLocation = pd.read_excel(F_in_StationLocations)
df_StationsLocation.columns = ['Label', 'Lat', 'Lon']
df_airport=pd.DataFrame(data=np.array([[-3.15,-59.9833]]),columns=['latitude','longitude'])

study_zone_map = folium.Map(location=[-3.1190, -60.0217],
    tiles = 'Esri.WorldTopoMap',
    width="100%",height="100%",)

folium.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
    tooltip="Click me!",
    popup='Airport in the Popup', icon=icon_star,).add_to(study_zone_map)

folium.Circle(location=[df_StationsLocation['Lat'][0],df_StationsLocation['Lon'][1]],
    tooltip="Click me!",
    popup=df_StationsLocation['Label'][0],
    color='crimson',fill=True,radius=15).add_to(study_zone_map)

folium.map.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
    icon=DivIcon(icon_size=(150,36),
    icon_anchor=(0,0),
    html='Airport is here',)).add_to(study_zone_map)

for idx, row in df_StationsLocation.iterrows():
    folium.Circle(
        location=[row['Lat'], row['Lon']],
        tooltip="Click me!",
        popup=str(row['Label']),
        color='crimson',
        fill=True,
        radius=15
    ).add_to(study_zone_map)

    folium.map.Marker(
        location=[row['Lat'], row['Lon']],
        icon=DivIcon(
            icon_size=(150, 36),
            icon_anchor=(-10, 10),
            html=f'<div style="font-size: 10pt; color: black; font-weight: bold;">{row["Label"]}</div>',
        )
    ).add_to(study_zone_map)

minimap = plugins.MiniMap(zoom_level_offset=-7,
    tile_layer = 'Esri.WorldTopoMap')
study_zone_map.add_child(minimap)

locations = [
    {"name": "Manaus teater", "coords": [-3.1301766836937137, -60.02340049029022],
    "color": "blue", "icon": "church",
    "image": "https://lh5.googleusercontent.com/p/AF1QipM_wIwvAy2YHYT1aHdFiV5eTv14EyU51OSdRIO7=w408-h271-k-no"},
    {"name": "Moon Beach", "coords": [-3.0327694203954794, -60.132860744341016],
    "color": "green", "icon": "umbrella",
    "image": "https://lh5.googleusercontent.com/p/AF1QipOJHfhvspTgy56sr1pInhBAJHfplRPqMfM3c3p=w426-h240-k-no"},
]

for loc in locations:
    popup_content = f'<strong>{loc["name"]}</strong><br><img src="{loc["image"]}" alt="{loc["name"]}" width="150">'
    folium.Marker(
        loc["coords"],
        tooltip=loc["name"],
        popup=folium.Popup(popup_content, max_width=200),
        icon=folium.Icon(color=loc["color"], prefix='fa', icon=loc["icon"])
        ).add_to(study_zone_map)

# legend
legend_html = '''
<div style="position: fixed; top: 50px; left: 50px; z-index: 9999;
background-color: white; border:2px solid grey; border-radius:3px; padding: 10px;">
 &nbsp;<i class="fa-solid fa-church" style="color:blue"></i><span> &nbsp; Places to
see </span><br>
 &nbsp;<i class="fa-solid fa-umbrella-beach" style="color:green"></i><span> &nbsp;
Beach</span><br>
 &nbsp;<i class="fa fa-star" style="color:black"></i><span> &nbsp; Meteorological
station</span><br>
 &nbsp;<i class="fa-solid fa-circle" style="color:red"></i><span> &nbsp; River
sample</span><br>
</div>
'''
study_zone_map.get_root().html.add_child(folium.Element(legend_html))

study_zone_map.save(F_out)

#  on a ajouter une légende écrite en HTML



# 9. Ajout d’échelle et de flèche du nord


F_in_StationLocations = "E:/BUT3/SAE/SAE5.EMS.01/data_tp/StationsLocation.xlsx"
F_out = "E:/BUT3/SAE/SAE5.EMS.01/ManausMap10.html"

icon_star = BeautifyIcon(icon='star', inner_icon_style='color:black;font-size:15px;',
    background_color='transparent', border_color='transparent',)

df_StationsLocation = pd.read_excel(F_in_StationLocations)
df_StationsLocation.columns = ['Label', 'Lat', 'Lon']
df_airport=pd.DataFrame(data=np.array([[-3.15,-59.9833]]),columns=['latitude','longitude'])

study_zone_map = folium.Map(location=[-3.1190, -60.0217],
    tiles = 'Esri.WorldTopoMap',
    width="100%",height="100%",)

folium.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
    tooltip="Click me!",
    popup='Airport in the Popup', icon=icon_star,).add_to(study_zone_map)

folium.Circle(location=[df_StationsLocation['Lat'][0],df_StationsLocation['Lon'][1]],
    tooltip="Click me!",
    popup=df_StationsLocation['Label'][0],
    color='crimson',fill=True,radius=15).add_to(study_zone_map)

folium.map.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
    icon=DivIcon(icon_size=(150,36),
    icon_anchor=(0,0),
    html='Airport is here',)).add_to(study_zone_map)

for idx, row in df_StationsLocation.iterrows():
    folium.Circle(
        location=[row['Lat'], row['Lon']],
        tooltip="Click me!",
        popup=str(row['Label']),
        color='crimson',
        fill=True,
        radius=15
    ).add_to(study_zone_map)

    folium.map.Marker(
        location=[row['Lat'], row['Lon']],
        icon=DivIcon(
            icon_size=(150, 36),
            icon_anchor=(-10, 10),
            html=f'<div style="font-size: 10pt; color: black; font-weight: bold;">{row["Label"]}</div>',
        )
    ).add_to(study_zone_map)

minimap = plugins.MiniMap(zoom_level_offset=-7,
    tile_layer = 'Esri.WorldTopoMap')
study_zone_map.add_child(minimap)

locations = [
    {"name": "Manaus teater", "coords": [-3.1301766836937137, -60.02340049029022],
    "color": "blue", "icon": "church",
    "image": "https://lh5.googleusercontent.com/p/AF1QipM_wIwvAy2YHYT1aHdFiV5eTv14EyU51OSdRIO7=w408-h271-k-no"},
    {"name": "Moon Beach", "coords": [-3.0327694203954794, -60.132860744341016],
    "color": "green", "icon": "umbrella",
    "image": "https://lh5.googleusercontent.com/p/AF1QipOJHfhvspTgy56sr1pInhBAJHfplRPqMfM3c3p=w426-h240-k-no"},
]

for loc in locations:
    popup_content = f'<strong>{loc["name"]}</strong><br><img src="{loc["image"]}" alt="{loc["name"]}" width="150">'
    folium.Marker(
        loc["coords"],
        tooltip=loc["name"],
        popup=folium.Popup(popup_content, max_width=200),
        icon=folium.Icon(color=loc["color"], prefix='fa', icon=loc["icon"])
        ).add_to(study_zone_map)


legend_html = '''
<div style="position: fixed; top: 50px; left: 50px; z-index: 9999;
background-color: white; border:2px solid grey; border-radius:3px; padding: 10px;">
 &nbsp;<i class="fa-solid fa-church" style="color:blue"></i><span> &nbsp; Places to
see </span><br>
 &nbsp;<i class="fa-solid fa-umbrella-beach" style="color:green"></i><span> &nbsp;
Beach</span><br>
 &nbsp;<i class="fa fa-star" style="color:black"></i><span> &nbsp; Meteorological
station</span><br>
 &nbsp;<i class="fa-solid fa-circle" style="color:red"></i><span> &nbsp; River
sample</span><br>
</div>
'''
study_zone_map.get_root().html.add_child(folium.Element(legend_html))

#fleche du nord
study_zone_map.control_scale = True

north_arrow_url = 'https://upload.wikimedia.org/wikipedia/commons/8/84/North_Pointer.svg'

# Add the north arrow image to the map
FloatImage(north_arrow_url,
    bottom=75, left=85,scale=0.2).add_to(study_zone_map)


study_zone_map.save(F_out)

