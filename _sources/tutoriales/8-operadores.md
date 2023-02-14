---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Operadores

Los operadores son símbolos especiales que le indican al intérprete de Python qué debe realizar una tarea matemática, relacional o lógica y qué debe mostrar en pantalla como resultado.

## Operadores aritméticos

Los operadores aritméticos son los que se utilizan para realizar operaciones matemáticas básicas.

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
| `+`      | Suma        | `2 + 2` |
| `-`      | Resta       | `2 - 2` |
| `*`      | Multiplicación | `2 * 2` |
| `/`      | División    | `2 / 2` |
| `**`     | Potencia    | `2 ** 2` |
| `%`      | Módulo      | `2 % 2` |
| `//`     | División entera | `2 // 2` |

## Operadores de asignación

Los operadores de asignación se utilizan para asignar valores a variables.

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
| `=`      | Asignación simple | `x = 5` |
| `+=`     | Asignación aditiva | `x += 5` |
| `-=`     | Asignación sustractiva | `x -= 5` |
| `*=`     | Asignación multiplicativa | `x *= 5` |
| `/=`     | Asignación divisiva | `x /= 5` |
| `**=`    | Asignación potenciación | `x **= 5` |
| `%=`     | Asignación módulo | `x %= 5` |
| `//=`    | Asignación división entera | `x //= 5` |

## Operadores de comparación

Los operadores de comparación se utilizan para comparar valores.

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
| `==`     | Igual a     | `2 == 2` |
| `!=`     | Diferente de | `2 != 2` |
| `>`      | Mayor que   | `2 > 2` |
| `<`      | Menor que   | `2 < 2` |
| `>=`     | Mayor o igual que | `2 >= 2` |
| `<=`     | Menor o igual que | `2 <= 2` |

## Operadores lógicos

Los operadores lógicos se utilizan para combinar declaraciones condicionales.

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
| `and`    | Y lógico    | `x < 5 and  x < 10` |
| `or`     | O lógico    | `x < 5 or x < 4` |
| `not`    | Negación    | `not(x < 5 and x < 10)` |

## Operadores de identidad

Los operadores de identidad se utilizan para comparar los objetos, no si son iguales, sino si son realmente el mismo objeto, con la misma ubicación de memoria.

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
| `is`     | Si es el mismo objeto | `x is y` |
| `is not` | Si no es el mismo objeto | `x is not y` |

## Operadores de membresía

Los operadores de membresía se utilizan para probar si una secuencia está presente en un objeto.

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
| `in`     | Si está presente en el objeto | `x in y` |
| `not in` | Si no está presente en el objeto | `x not in y` |

## Ejemplos

### Ejemplo 1

```{code-cell}
# Operadores aritméticos
print(2 + 2) # Suma
print(2 - 2) # Resta
print(2 * 2) # Multiplicación
print(2 / 2) # División
print(2 ** 2) # Potencia
print(2 % 2) # Módulo
print(2 // 2) # División entera

# Operadores de asignación
x = 5
x += 5
print(x)
x -= 5
print(x)

# Operadores de comparación
print(2 == 2) # Igual a
print(2 != 2) # Diferente de
print(2 > 2) # Mayor que
print(2 < 2) # Menor que
print(2 >= 2) # Mayor o igual que
print(2 <= 2) # Menor o igual que

# Operadores lógicos
x = 5
print(x < 5 and  x < 10)
print(x < 5 or x < 4)
print(not(x < 5 and x < 10))

# Operadores de identidad
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

# Operadores de membresía
x = ["apple", "banana"]
print("banana" in x)
print("pineapple" not in x)
```

### Ejemplo 2. Operadores con cadenas

```{code-cell}
# Operadores aritméticos
print("Hola " + "mundo") # Suma
print("Hola " * 3) # Multiplicación

# Operadores de asignación
x = "Hola "
x += "mundo"
print(x)

# Operadores de comparación
print("Hola" == "Hola") # Igual a
print("Hola" != "Hola") # Diferente de

# Operadores lógicos
x = "Hola"
print(x == "Hola" and x == "Mundo")
print(x == "Hola" or x == "Mundo")
print(not(x == "Hola" and x == "Mundo"))

# Operadores de identidad
x = "Hola"
y = "Hola"
z = x
print(x is z)
print(x is y)
print(x == y)

# Operadores de membresía
x = "Hola mundo"
print("Hola" in x)
print("Adiós" not in x)
```
