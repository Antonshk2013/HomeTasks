import requests
from local_settings import API_KEY

def get_list_movies(key, movie_name):
    url = " https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': key,
        'query': movie_name
    }
    resp = requests.get(url, params=params)
    return resp.json().get("results")

def print_data(datay):
    for i in datay:
        print(i.get("original_title"))
        print(i.get("overview"))
        print(i.get("release_date"))

if __name__ == '__main__':
    resp = get_list_movies(API_KEY, 'Matrix')
    print_data(resp)

