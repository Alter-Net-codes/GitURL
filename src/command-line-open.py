import webbrowser
while True:
  print("welcome this is a application that helps you open github repo's straight from the command line.")
  print("just enter the url and we will bring you there!")
  url = input("URL:")
  if "github.com" in url:
    webbrowser.open(url)
  else:
    print("url has to be to github.com! try something like github.com/alter-net-codes")
