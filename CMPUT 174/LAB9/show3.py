import requests

BASE_URL = "https://api.tvmaze.com/"

def get_shows(query: str) -> list[dict]:
    """
    Search for TV shows using the TV Maze API.
    If the show is not found, return None
    """
    response = requests.get(f"https://api.tvmaze.com/search/shows?q={query}")  # use .get() to read the url and get output into variable response
    data = response.json()
    return data  # returns a JSON object

def format_show_name(show: dict) -> str:
    """
    Format the show name.
    """
    """
    variables to assign the data from the API
    """    
    data = show["show"]
    genres = data["genres"]
    name = data["name"]
    premiered = data["premiered"]
    ended = data["ended"]

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
    """
    variables to assign the data from the API
    """
    # TODO: Implement the function
    season_number = season["number"]
    name = season["name"]
    premiered = season["premiereDate"]
    ended = season["endDate"]
    episodes = season['episodeOrder']

    if type(premiered) != str and type(ended) != str:
        output = f'Season {season_number} (? - ?), {episodes} episodes'

    elif type(premiered) != str and type(ended) == str:
        output = f'Season {season_number} (? - {ended[0:4]}), {episodes} episodes'
        
    elif type(premiered) == str and type(ended) != str:
        output = f'Season {season_number} ({premiered[0:4]} - ?), {episodes} episodes'
        
    elif type(premiered) == str and type(ended) == str:
        output = f'Season {season_number} ({premiered[0:4]} - {ended[0:4]}), {episodes} episodes'
        
    elif type(premiered) == str and type(ended) != str:
        output = f'Season {season_number} ({premiered[0:4]} - ?), {episodes} episodes'
        
    elif type(premiered) != str and type(ended) != str:
        output = f'Season {season_number} ( ? - ? ), {episodes} episodes'
    else:
        output = f'Season {season_number} ({premiered[0:4]} - {ended[0:4]}), {episodes} episodes'

    return output


def main():
    """
    Main function 
    """
    # TODO: Update main():
    # 1. Ask the user to select a show
    # 2. Display all seasons of the selected show
    
    
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
        a = selected_show['show']
        showid = a['id']
        data = get_seasons(showid)
        for i in data:
            print(format_season_name(i))



if __name__ == '__main__':
    main()
