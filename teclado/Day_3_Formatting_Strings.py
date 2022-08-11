# 1 String interpolation with the f-string

greeting = "Hello, world"
exclamation = "!"

print(f"{greeting}{exclamation}")

# 1 String interpolation with the format method

print("{}{}".format("Hello, world", "!"))

# 1 String concatenation

print(greeting + exclamation)

# 2 Name input and greeting

name = input("What is your name? ").title().strip()
print(f"Hello, {name}!")

# 3 String and integer concatenation

age = str(29)
print("I am " + age)

# 4 String interpolation

title = "Joker"
director = "Todd Phillips"
release_year = 2019
print(f"{title} ({release_year}), directed by {director}")
