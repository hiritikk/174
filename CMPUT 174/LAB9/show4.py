import requests
# import requests_cache
# requests_cache.install_cache('cmput174_cache')
BASE_URL = "https://api.tvmaze.com/"

def get_shows(query: str) -> list[dict]:
    """
    Search for TV shows using the TV Maze API.
    If the show is not found, return None
    """
    url = BASE_URL + 'search/shows?q=:' + query
    response = requests.get(url)  # use .get() to read the url and get output into variable response
    data = response.json()
    return data  # returns a JSON object

def format_show_name(show: dict) -> str:
    """
    Format the show name.
    """
    data = show["show"]
    genres = data["genres"]
    name = data["name"]
    premiered = data["premiered"]
    ended = data["ended"]
    # different scenarios where out of the variable is Noneobject so we replace that with a "?"
    if type(premiered) != str and type(ended) != str and type(genres) != list:
        output = f'{name} (? - ?, ?)'

    elif type(premiered) != str and type(ended) == str and type(genres) == list:
        output = f'{name} (? - {ended[0:4]}, {", ".join(genres)})'
        
    elif type(premiered) == str and type(ended) != str and type(genres) == list:
        output = f'{name} ({premiered[0:4]} - ?, {", ".join(genres)})'
        
    elif type(premiered) == str and type(ended) == str and len(genres) == 0:
        output = f'{name} ({premiered[0:4]} - {ended[0:4]}, ? )'
        
    elif type(premiered) == str and type(ended) != str and type(genres) != list:
        output = f'{name} ({premiered[0:4]} - ?, ? )'
        
    elif type(premiered) != str and type(ended) != str and type(genres) == list:
        output = f'{name} (? - ?, {", ".join(genres)} )'

    else:
        output = f'{name} ({premiered[0:4]} - {ended[0:4]}, {", ".join(genres)})'

    return output


def get_seasons(show_id: int) -> list[dict]:
    """
    Get the seasons for a given show_id
    """
    # TODO: Implement the function
    response = requests.get(f"https://api.tvmaze.com/shows/{show_id}/seasons")
    data = response.json()
    return data


def format_season_name(season: dict) -> str:
    """
    Format the season name
    """
    # TODO: Implement the function
    number = season["number"]
    name = season["name"]
    premiered = season["premiereDate"]
    ended = season["endDate"]
    episodes = season['episodeOrder']
    # different scenarios where out of the variable is Noneobject so we replace that with a "?"
    if type(premiered) != str and type(ended) != str:
        output = f'Season {number} (? - ?), {episodes} episodes'

    elif type(premiered) != str and type(ended) == str:
        output = f'Season {number} (? - {ended[0:4]}), {episodes} episodes'
        
    elif type(premiered) == str and type(ended) != str:
        output = f'Season {number} ({premiered[0:4]} - ?), {episodes} episodes'
        
    elif type(premiered) == str and type(ended) == str:
        output = f'Season {number} ({premiered[0:4]} - {ended[0:4]}), {episodes} episodes'
        
    elif type(premiered) == str and type(ended) != str:
        output = f'Season {number} ({premiered[0:4]} - ?), {episodes} episodes'
        
    elif type(premiered) != str and type(ended) != str:
        output = f'Season {number} ( ? - ? ), {episodes} episodes'
    else:
        output = f'Season {number} ({premiered[0:4]} - {ended[0:4]}), {episodes} episodes'

    return output



def get_episodes_of_season(season_id: int) -> list[dict]:
    """
    Get the episodes of a given season of a show
    season_id is the id (not the number!) of the season
    """
    # TODO: Implement the function
    
    url = BASE_URL + 'seasons/' + str(season_id) + '/episodes'  # adds the endpoint from the website with show id
    response = requests.get(url)  # searches for desired result
    data = response.json()  # converts the result into dict format
    return data


def format_episode_name(episode: dict) -> str:
    """
    Format the episode name
    """
    # TODO: Implement the function
    season = episode['season']
    number = episode['number']
    name = episode['name']
    rating = episode['rating']
    for i in rating.values():
        rating = i    
        # different scenarios where out of the variable is Noneobject so we replace that with a "?"
    if type(season) != int and type(number) != int and type(rating) != float:
        output = f'S?E? (Rating : ? )'

    elif type(season) == int and type(number) != int and type(rating) != float:
        output = f'S{season}E? (Rating : ?)'
        
    elif type(season) == int and type(number) == int and type(rating) != float:
        output = f'S{season}E{number} {name} (Rating : ?)'
        
    elif type(season) != int and type(number) == int and type(rating) != float:
        output = f'S?E{number} {name} (Rating : ?)'
        
    elif type(season) == int and type(number) != int and type(rating) == float:
        output = f'S{season}E? (Rating : {rating})'
        
    elif type(season) != int and type(number) == int and type(rating) == float:
        output = f'S?E{number} {name} (Rating : {rating})'
    else:
        output = f'S{season}E{number} {name} (Rating : {rating})'

    return output    

def main():
    # TODO: Update main():
    # 1. Ask the user to select a season of the selected show
    # 2. Display all episodes of the selected season

    query = input("Search for a show: ")
    results = get_shows(query)

        
    if not results:
        print("No results found")
    else:
        n = 1
        print("Here are the results:")
        for result in results:
            show = result["show"]
            print(f"{n}. {format_show_name(result)}")
            n += 1
        select = int(input(" Select a show: "))
        selected_show = results[select - 1]
        info_show = selected_show['show']
        show_id = info_show['id']
        data = get_seasons(show_id)
        for s in data:
            print(format_season_name(s))
            # for the episodes data according to the season
    select_S = int(input(" Select a season: "))
    selected_season = data[select_S - 1]
    season_id = selected_season['id']
    ep_info = get_episodes_of_season(season_id)
    for ep in ep_info:
        print(format_episode_name(ep))
    




if __name__ == '__main__':
    main()
