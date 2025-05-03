import random

class Chromosome:    
    def __init__(self, genes, knapsack, weight_limit):
        self.genes = list(genes)
        self.knapsack = knapsack
        self.weight_limit = weight_limit
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        # Evaluate how good a chromosome (solution) is.
        fitness = 0
        total_weight = 0

        for i in range(len(self.genes)):
            if self.genes[i] == 1:
                value, weight = self.knapsack[i]
                fitness += value
                total_weight += weight

        # If weight exceeds limit, set fitness to 0 (invalid solution)
        return fitness if total_weight <= self.weight_limit else 0  

    def __str__(self):
        return f"Genes: {self.genes}, Fitness: {self.fitness}"


class GeneticAlgorithm:
    def __init__(self, weight_limit, knapsack, population_size, mutation_rate):
        self.weight_limit = weight_limit
        self.knapsack = knapsack
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population()

    def initialize_population(self):
        # Initialize a population with random gene sequences
        population = []
        for _ in range(self.population_size):
            genes = [random.randint(0, 1) for _ in range(len(self.knapsack))]
            chromosome = Chromosome(genes, self.knapsack, self.weight_limit)
            population.append(chromosome)
        return population

    def selection(self):
        # Choose the best chromosomes for reproduction using elitism.
        self.population.sort(key=lambda x: x.fitness, reverse=True)
        return self.population[:self.population_size // 2]

    def crossover(self, parent1, parent2):
        # Perform single-point crossover to create new offspring
        crossover_point = random.randint(1, len(parent1.genes) - 1)

        # Create two children by swapping genes at the crossover point.
        child1_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
        child2_genes = parent2.genes[:crossover_point] + parent1.genes[crossover_point:]

        return Chromosome(child1_genes, self.knapsack, self.weight_limit), \
               Chromosome(child2_genes, self.knapsack, self.weight_limit)

    def mutation(self, chromosome):
        # Introduce small random changes to prevent premature convergence.
        for i in range(len(chromosome.genes)):
            if random.random() < self.mutation_rate:
                chromosome.genes[i] = 1 - chromosome.genes[i]  # Flip the bit

        # Recalculate fitness after mutation.
        chromosome.fitness = chromosome.calculate_fitness()
        return chromosome

    def evolve(self):
        # Evolve and generate a new population.
        new_population = []
        selected = self.selection()

        while len(new_population) < self.population_size:
            parent1, parent2 = random.sample(selected, 2)  # Pick two parents
            child1, child2 = self.crossover(parent1, parent2)
            new_population.append(self.mutation(child1))
            if len(new_population) < self.population_size:
                new_population.append(self.mutation(child2))

        self.population = new_population

    def get_solution(self):
        # Fetch the best solution based on fitness
        return max(self.population, key=lambda c: c.fitness)


def build_knapsack(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract weight limit from first line
    first_line = list(map(int, lines[0].split()))
    weight_limit = first_line[1]

    # Read items (value, weight) into dictionary
    knapsack = {i: tuple(map(int, line.split())) for i, line in enumerate(lines[1:])}

    return weight_limit, knapsack


def main():
    weight_limit, knapsack = build_knapsack("test.txt")
    ga = GeneticAlgorithm(weight_limit, knapsack, population_size=10, mutation_rate=0.2)

    for _ in range(50):  # Evolve over 50 generations
        ga.evolve()

    best_solution = ga.get_solution()
    print("Best solution found:", best_solution)
    print("Fitness of best solution:", best_solution.fitness)
main()