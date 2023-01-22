"""
This program we search for shows and get possible outputs with a possible and not more than 2 typos 
"""
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




def main():
    """
    Main function 
    """

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
        


if __name__ == '__main__':
    main()