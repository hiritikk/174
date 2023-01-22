BASE_URL = "https://api.tvmaze.com/"
"""
This program we search for shows and get possible outputs with a possible and not more than 2 typos 
"""
def get_shows(query: str) -> list[dict]:
    """
    Search for TV shows using the TV Maze API.
    If the show is not found, return None
    """
    response = requests.get(f"https://api.tvmaze.com/search/shows?q={query}")  # use .get() to read the url and get output into variable response
    return response.json()  # returns a JSON object

def format_show_name(show: dict) -> str:
    """
    Format the show name.
    """
    # TODO: Implement the function


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
            print(f"{n}. {show['name']}")
            n += 1

if __name__ == '__main__':
    main()