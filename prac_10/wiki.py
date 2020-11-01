import wikipedia

search_result = input("Search: ")
while search_result != "":
    print(wikipedia.search(search_result))
    page_title = input("Page Title: ")
    try:
        page_detail = wikipedia.page(page_title)
        print(page_detail.title)
        print(wikipedia.summary(page_title))
        print(page_detail.url)
    except wikipedia.exceptions.DisambiguationError:
        print("Search term needs to be refined, too many search result")


    search_result = input("Search: ")
print("exit search")