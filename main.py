# main.py

from api_handler import APIHandler
from data_displayer import DataDisplayer


def main():
    url = "https://671be4272c842d92c381a5ab.mockapi.io/test"
    api_handler = APIHandler(url)
    data = api_handler.fetch_data()

    if data:
        displayer = DataDisplayer(data)
        displayer.display_data()
    else:
        print("No se pudieron obtener datos para mostrar.")


if __name__ == "__main__":
    main()
