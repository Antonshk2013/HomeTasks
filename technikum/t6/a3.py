import requests
api_key = '699e4b5fad9a4db7541c9c7ddcaae4ac' # In andere Datei, sensitive credentials
url_start = 'https://api.themoviedb.org/'
url_start = 'https://api.themoviedb.org/'
# ?api_key={api_key}&query=' # Aufteilen




def get_movie_info(movie_name):
    url = url_start + '3/search/movie'
    params = {
        'api_key': api_key,
        'query': movie_name,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
      return response.json()


if __name__ == '__main__':
    my_movie = input('Geben Sie einen Film ein: ')
    outer_dict = get_movie_info(my_movie) # Dictionary 1
# Dictionary1 [‘results’] -> Liste[0] -> Dictionary[‘title’], Dictionary[‘overview’]
    try:
        inner_list = outer_dict.get('results')[0]
        print(f"Title {inner_list.get('title')}  Overview {inner_list.get('overview')}")
    except:
        print("Es gibt keine movie in resdults")
