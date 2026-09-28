"""Points d'appui (GCP) relevés par Claude le 28/09/2026 sur la carte West Point n° 31 (WWIIEurope31.jpg, 5100×3300 px).
Format : (lieu, longitude, latitude, x_pixel, y_pixel). Repère = le petit cercle de la ville sur la carte."""
import numpy as np, pyproj
G=[('Helsinki',24.94,60.17,2089,306),('Hanko',22.95,59.82,1942,346.5),('Riga',24.11,56.95,2005,797.5),('Danzig',18.65,54.35,1444,1154),
('Berlin',13.40,52.52,905,1344.5),('Warsaw',21.01,52.23,1638,1510),('Budapest',19.04,47.50,1346,2238),('Belgrade',20.46,44.82,1454,2677),
('Pitesti',24.87,44.86,1920,2710),('Moscow',37.62,55.76,3141.5,986),('Kiev',30.52,50.45,2525,1850),('Fastiv',29.92,50.08,2475,1908),
('Leningrad',30.32,59.94,2503.5,356.5),('Viipuri',28.74,60.71,2382,259),('Stalingrad',44.52,48.71,3926,1991),('Kotelnikovo',43.14,47.63,3832,2180.5)]
G+=[('Memel',21.13,55.71,1726,971.5),('Vilnius',25.28,54.69,2067,1166),('Bialystok',23.16,53.13,1856.5,1392.5),('Brest',23.70,52.10,1894,1561.5),
('Krakow',19.94,50.06,1492,1833),('Lviv',24.03,49.84,1890,1923.5),('Szeged',20.15,46.25,1432,2461)]
