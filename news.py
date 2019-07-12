import requests
from colorama import init, Fore, Back, Style

print("")
print("**************************************************************************")
print("")
print(Fore.YELLOW + Style.BRIGHT + "\t\t\t\t N E W S  B O T")
print("")
print(Fore.WHITE + "**************************************************************************")
print("")
print("")
print("\t\t\tHello there, welcome to newsbot! ")
print("")
print("\t\t  Please select your preferred option number!")
print("\t\t--------------------------------------------")
print("")
print("")
print("1." + Fore.CYAN + " See top headlines from around the world! " + Fore.WHITE)
print("")
print("2." + Fore.CYAN + " Get latest entertainment, technology and business news!" + Fore.WHITE)
print("")
print("3." + Fore.CYAN + " Search for news to a specific keyword. (It could be a product or a celebrity)" + Fore.WHITE)
print("-------------------------------------------------------------------- ")

user_input = input()
print("")
def get_results(option_1):
    open_bbc_page = requests.get(option_1).json() 
    article = open_bbc_page["articles"] 
    title = [] 
    details = []
    url = []
    for ar in article: 
        title.append(ar["title"]) 
        details.append(ar["description"])
        url.append(ar["url"])


    for i in range(len(details)):  
        print("")  
        print(str(i+1) + ". " + Fore.GREEN + title[i] + Fore.RESET) 
        print("--------------------------------------------------------------------------------")
        print("")
        print(details[i])
        print("")
        print(" Visit this link for more details! " + "=> " + Fore.BLUE + url[i] + Fore.RESET)
        print("")
        if details[i] == None:
            continue
        

def top_headlines(user_input):
    print("Please select from this list of countries")
    print("-----------------------------------------")
    print("")
    print("1."+ Fore.GREEN + " America" + Fore.RESET)
    print("")
    print("2." + Fore.GREEN + "Uk" + Fore.RESET)
    print("")
    print("3." + Fore.GREEN + "Nigeria" + Fore.RESET)
    print("")
    country = input()
    if country == "1":
        main_url = " https://newsapi.org/v2/top-headlines?country=us&apiKey=2cf7726ebd2f4cbeb683413f1b9b371a"
        get_results(main_url)
    elif country == "2":
        main_url = " https://newsapi.org/v2/top-headlines?country=gb&apiKey=2cf7726ebd2f4cbeb683413f1b9b371a"
        get_results(main_url)
    elif country == "3":
        main_url = " https://newsapi.org/v2/top-headlines?country=ng&apiKey=2cf7726ebd2f4cbeb683413f1b9b371a"
        get_results(main_url)
       
    else:
        print(Fore.RED + "Invalid option type! " + Fore.RESET)     


def options(user_input):
    print("To view Please select from this list of categories")
    print("------------------------------------------------------------")
    print("")
    print("1."+ Fore.GREEN + "Entertainment news" + Fore.RESET)
    print("")
    print("2." + Fore.GREEN + "Technology news" + Fore.RESET)
    print("")
    print("3." + Fore.GREEN + "Business news" + Fore.RESET)
    print("")
    print("4." + Fore.GREEN + "Sport news" + Fore.RESET)
    category = input()
    if category == "1":
        main_url = " https://newsapi.org/v2/top-headlines?category=entertainment&language=en&apiKey=2cf7726ebd2f4cbeb683413f1b9b371a"
        get_results(main_url)
    elif category == "2":
        main_url = " https://newsapi.org/v2/top-headlines?category=entertainment&language=en&apiKey=2cf7726ebd2f4cbeb683413f1b9b371a"
        return main_url
    elif category == "3":
        main_url = " https://newsapi.org/v2/top-headlines?category=business&language=en&apiKey=2cf7726ebd2f4cbeb683413f1b9b371a"
        get_results(main_url)
    elif category == "4":
        main_url = " https://newsapi.org/v2/top-headlines?category=sports&apiKey=2cf7726ebd2f4cbeb683413f1b9b371a"
        get_results(main_url)
    else:
        print(Fore.RED + "Invalid option type! " + Fore.RESET) 

def keyword(user_input):
    print("\t\t  Please select from this list of categories ")
    query_string = input()
    main_url = " https://newsapi.org/v2/everything?q="+query_string+"&apiKey=2cf7726ebd2f4cbeb683413f1b9b371a"
    get_results(main_url)

if user_input == "1":
    option_1 = top_headlines(user_input)
elif user_input == "2":
    option_1 = options(user_input)
elif user_input == "3":
    option_1 = keyword(user_input)
else:
    print(Fore.RED + "Invalid option type! " + Fore.RESET)

