import webbrowser

while True:
    print("Welcome! This application helps you open GitHub repos straight from the command line.")
    print("Just enter the URL, and we will bring you there!")
    
    url = input("URL: ").strip()

    # Check if the input contains exactly 'github.com'
    if url.startswith("https://github.com") or url.startswith("http://github.com"):
        webbrowser.open(url)
    else:
        print("The URL has to be a GitHub link! Try something like https://github.com/alter-net-codes")
