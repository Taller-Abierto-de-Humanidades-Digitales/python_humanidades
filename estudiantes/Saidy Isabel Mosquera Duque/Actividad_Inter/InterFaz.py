from busqueda import searchByTitle, searchByAuthorName, searchByKeyWord, printElements
from biblioteca import biblioteca

biblioteca = biblioteca()

answer = True
while answer == True:
  # print("Search by title")
  # title = input()
  # searchByTitle(title)

  # print("Search by author")
  # authorName = input()
  # searchByAuthorName(authorName)

  # print("Search by YEAR")
  # year = input()
  # searchByYear(year)

  # Example: Try with keyword etal2013companion and title companion
  print("Search by keyword")
  keyWordToSearch = str(input())
  print("Search by title")
  titleToSearch = str(input())
  print('-----------------')
  foundElements = searchByKeyWord(keyWordToSearch, 'partial', biblioteca)
  # example of 2nd search with another criteria chained to the 1st one 
  foundElements = searchByTitle(titleToSearch, 'partial', foundElements)
  # notice above I pass biblioteca for the first search
  # but pass foundElement for the second to do the search on the
  # result of the 1st search result
  printElements(foundElements)


  # final question
  print("Do you want to continue searching?")
  inputData = input("S/N: ") # las instrucciones nunca están de más :p
  answer = inputData.lower() == "s" # para que coincida con la instrucción previa