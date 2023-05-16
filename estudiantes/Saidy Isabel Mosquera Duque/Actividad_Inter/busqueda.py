#####################################################
# Busqueda
#####################################################
from biblioteca import biblioteca

biblioteca = biblioteca()

# Formatting functions

def printWithFormat(book):
  for key in book:
    if key == 'accessed' or key == 'issued':
      print(key + ": " + book[key]['date-parts'][0][0])
    elif key == 'author':
      for author in book[key]:
        authorsString = ''
        if 'family' in author and 'given' in author:
          authorsString += ' ' + author['family'] + ' ' + author['given']
        else:
          authorsString += ' ' + author['literal']
        print(key + ": " + authorsString)
    elif not isinstance(book[key], list):
      print(key + ": " + book[key])
  print('-----------------')

def printElements(library):
  for book in library:
    printWithFormat(book)

# Search functions
def search(key, textToSearch, method = 'exact', library = biblioteca):
  foundElements = []
  for book in library:
    if method == 'exact':
      if textToSearch.lower() == book[key].lower():
        foundElements.append(book)
    else:
      # means method is partial
      if textToSearch.lower() in book[key].lower():
        foundElements.append(book)
  return foundElements

def searchByTitle(titleToSearch, method = 'exact', library = biblioteca):
  return search('title', titleToSearch, method, library)

def searchByType(typeToSearch, method = 'exact', library = biblioteca):
  return search('type', typeToSearch, method, library)


# Specific search functions
def searchByAuthorName(authorToSearch, method = 'exact', library = biblioteca):
  foundElements = []
  for book in library:
    if "author" in book:
      authors = book['author']
      for author in authors:
        for item in author:
          authorPartialName = author[item].lower()
          if method == 'exact':
            if authorToSearch.lower() == authorPartialName:
              foundElements.append(book)
          else:
            # means method is partial
            if authorToSearch.lower() in authorPartialName:
              foundElements.append(book)
  return foundElements

# accessed and issued
def searchDate(dateToSearch, key, method = 'exact', library = biblioteca):
  foundElements = []
  for book in library:
    if (key in book):
      dates = book[key]['date-parts'][0]
      for date in dates:
        if method == 'exact':
          if date == dateToSearch:
            foundElements.append(book)
        else:
          # means method is partial
          if dateToSearch in str(date):
            foundElements.append(book)
  return foundElements

def searchByKeyWord(keyWordToSearch, method = 'exact', library = biblioteca):
  foundElements = []
  for book in library:
    for prop in book:
      value = book[prop]
      if isinstance(value, list) or isinstance(value, dict):
        continue
      if method == 'exact':
        if keyWordToSearch.lower() == value.lower():
          foundElements.append(book)
      else:
      # means method is partial
        # print(keyWord, value)
        if keyWordToSearch.lower() in value.lower():
          foundElements.append(book)
  foundElements.extend(searchDate(keyWordToSearch, 'accessed', method))
  foundElements.extend(searchDate(keyWordToSearch, 'issued', method))
  return foundElements
