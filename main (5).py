import random
problem_list = ["Living Giant Tree", "Alien Flying Saucer", "Monster Spirit from the Parallel Universe", "Evil Artificial Intelligence", "Parasites that capture the brain", "Mad Godzilla", "Black dragon", "Titanium", "Mutant Centipede", "Terrorblade", "Shadow Fiend", "Queen of Pain"]
problem_index = random.randint(0, len(problem_list) -1)
problem = problem_list[problem_index]
print(f"The thread we faced - {problem}")
hero_list = [input("Choose first hero:"), input("Choose second hero:"), input("Choose third hero:")]
print(f"This Superheroes {hero_list} went  on a mission!")