import socket
import requests
from pyfiglet import Figlet
# import folium


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)
        
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        
        for k, v in data.items():
            print(f'{k} : {v}')
        
        # area = folium.Map(location=[response.get('lat'), response.get('lon')])
        # area.save(f'{response.get("query")}_{response.get("city")}.html')
        
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


# def get_ip():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.settimeout(0)
#     try:
#         # doesn't even have to be reachable
#         s.connect(('10.254.254.254', 1))
#         IP = s.getsockname()[0]
#     except Exception:
#         IP = '127.0.0.1'
#     finally:
#         s.close()
#     return IP


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    ip = input('Please enter a target IP: ')
    
    get_info_by_ip(ip=ip)
    
    
if __name__ == '__main__':
    main()


# ______________________________________________
# import geocoder

# def get_current_gps_coordinates():
#     g = geocoder.ip('me')#this function is used to find the current information using our IP Add
#     if g.latlng is not None: #g.latlng tells if the coordiates are found or not
#         return g.latlng
#     else:
#         return None

# if __name__ == "__main__":
#     coordinates = get_current_gps_coordinates()
#     if coordinates is not None:
#         latitude, longitude = coordinates
#         print(f"Your current GPS coordinates are:")
#         print(f"Latitude: {latitude}")
#         print(f"Longitude: {longitude}")
#     else:
#         print("Unable to retrieve your GPS coordinates.")