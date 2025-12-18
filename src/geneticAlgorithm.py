from geneticAlgorithmCore import *
# import argparse
# import random

def genetic_algorithm(
    problem: KnapsackProblem,
    population_size=50,
    generations=50,
    tournament_size=3,
    mutation_rate=0.05,
    elitism_size=2,
    crossover_op='single_point',        # choose: 'single_point', 'two_point', 'uniform'
    mutation_op='bit_flip'              # choose: 'bit_flip', 'swap', 'scramble'
):
    population = [Individual(problem) for _ in range(population_size)]

    crossover_ops = {
        'single_point': single_point_crossover,
        'two_point': two_point_crossover,
        'uniform': uniform_crossover,
        'arithmetic': arithmetic_crossover
    }

    mutation_ops = {
        'bit_flip': lambda ind: bit_flip_mutation(ind, mutation_rate),
        'swap': swap_mutation,
        'scramble': scramble_mutation
    }

    crossover_func = crossover_ops[crossover_op]
    mutation_func = mutation_ops[mutation_op]

    # # track progress
    # best_per_gen = []

    for _ in range(generations):
        population.sort(key=lambda ind: ind.fitness, reverse=True)
        # best_per_gen.append(population[0].fitness)

        new_population = population[:elitism_size]

        while len(new_population) < population_size:
            parent1 = selection(population, tournament_size)
            parent2 = selection(population, tournament_size)
            child1, child2 = crossover_func(parent1, parent2)

            mutation_func(child1)
            mutation_func(child2)

            child1.fitness = child1.evaluate_fitness()
            child2.fitness = child2.evaluate_fitness()

            new_population.extend([child1, child2])

        population = new_population[:population_size]

    return max(population, key=lambda ind: ind.fitness)


# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--instance', type=str, required=True)
#     parser.add_argument('--seed', type=int, required=True)
#     parser.add_argument('--population_size', type=int, default=50)
#     parser.add_argument('--generations', type=int, default=50)
#     parser.add_argument('--mutation_rate', type=float, default=0.05)
#     parser.add_argument('--crossover_op', type=str, default='single_point')
#     parser.add_argument('--mutation_op', type=str, default='bit_flip')
#     parser.add_argument('--elitism_size', type=int, default=2)
#     parser.add_argument('--tournament_size', type=int, default=3)
#     args = parser.parse_args()

#     random.seed(args.seed)
#     weights, values, capacity = load_kplib_instance(args.instance)
#     problem = KnapsackProblem(weights, values, capacity)
#     best = genetic_algorithm(
#         problem=problem,
#         population_size=args.population_size,
#         generations=args.generations,
#         mutation_rate=args.mutation_rate,
#         crossover_op=args.crossover_op,
#         mutation_op=args.mutation_op,
#         elitism_size=args.elitism_size,
#         tournament_size=args.tournament_size
#     )
    
#     print(best.fitness)

# if __name__ == "__main__":
#     main()