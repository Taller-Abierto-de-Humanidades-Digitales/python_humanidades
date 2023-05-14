#####################################################
# Busqueda
#####################################################
from biblioteca import biblioteca

biblioteca = biblioteca()


# Funcion de formateado
#__________________________

def printWithFormat(libro):
  for clave in libro:
    if clave == 'accessed' or clave == 'issued':
      print(clave + ": " + libro[clave]['date-parts'][0][0])
    elif clave == 'author':
      for author in libro[clave]:
        authorsString = ''
        if 'family' in author and 'given' in author:
          authorsString += ' ' + author['family'] + ' ' + author['given']
        else:
          authorsString += ' ' + author['literal']
        print(clave + ": " + authorsString)
    elif not isinstance(libro[clave], list):
      print(clave + ": " + libro[clave])
  print('-----------------')

def printElements(libreria):
  for libro in libreria:
    printWithFormat(libro)



# Funcion de busqueda 
#__________________________

def busqueda(clave, textTosearch, method = 'exact', libreria = biblioteca):
  foundElements = []
  for libro in libreria:
    if method == 'exact':
      if textTosearch.lower() == libro[clave].lower():
        foundElements.append(libro)
    else:
      # metodo parcial
      if textTosearch.lower() in libro[clave].lower():
        foundElements.append(libro)
  return foundElements

def searchByTitle(titleTosearch, method = 'exact', libreria = biblioteca):
  return busqueda('title', titleTosearch, method, libreria)

def searchByType(typeTosearch, method = 'exact', libreria = biblioteca):
  return busqueda('type', typeTosearch, method, libreria)


# busqueda especifica
##__________________________

def searchByAuthorName(authorTosearch, method = 'exact', libreria = biblioteca):
  foundElements = []
  for libro in libreria:
    if "author" in libro:
      authors = libro['author']
      for author in authors:
        for item in author:
          authorPartialName = author[item].lower()
          if method == 'exact':
            if authorTosearch.lower() == authorPartialName:
              foundElements.append(libro)
          else:
            # metodo parcial
            if authorTosearch.lower() in authorPartialName:
              foundElements.append(libro)
  return foundElements


# acceso y emisión
##__________________________

def searchDate(dateTosearch, clave, method = 'exact', libreria = biblioteca):
  foundElements = []
  for libro in libreria:
    if (clave in libro):
      dates = libro[clave]['date-parts'][0]
      for date in dates:
        if method == 'exact':
          if date == dateTosearch:
            foundElements.append(libro)
        else:
          # metodo parcial
          if dateTosearch in str(date):
            foundElements.append(libro)
  return foundElements

def searchByKeyWord(keyWordTosearch, method = 'exact', libreria = biblioteca):
  foundElements = []
  for libro in libreria:
    for prop in libro:
      value = libro[prop]
      if isinstance(value, list) or isinstance(value, dict):
        continue
      if method == 'exact':
        if keyWordTosearch.lower() == value.lower():
          foundElements.append(libro)
      else:
      # metodo parcial
        if keyWordTosearch.lower() in value.lower():
          foundElements.append(libro)
  foundElements.extend(searchDate(keyWordTosearch, 'accessed', method))
  foundElements.extend(searchDate(keyWordTosearch, 'issued', method))
  return foundElements
