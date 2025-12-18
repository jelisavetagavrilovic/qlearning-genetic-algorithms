import re
import csv

def extract_elite_configs(log_file, output_file, keys):
    elite_configs = []
    seen = set()
    post_selection_started = False
    elite_start = False

    with open(log_file, "r") as f:
        for line in f:
            line = line.strip()
            
            if "Starting post-selection:" in line:
                post_selection_started = True
                continue

            if post_selection_started and "Elite configurations" in line:
                elite_start = True
                next(f)  # preskoči header liniju
                continue

            if elite_start:
                if line == "" or line.startswith("#") or line.startswith("Total CPU") or line.startswith("NULL"):
                    elite_start = False
                    post_selection_started = False
                    continue
                
                parts = re.split(r"\s+", line)
                if len(parts) < len(keys) + 1:  # +1 za ID
                    continue
                cfg_values = parts[1:1+len(keys)]  # preskoči ID
                cfg_tuple = tuple(cfg_values)
                if cfg_tuple not in seen:
                    seen.add(cfg_tuple)
                    elite_configs.append(cfg_values)


    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f, delimiter="=")
        for cfg in elite_configs:
            for k, v in zip(keys, cfg):
                writer.writerow([k, v])
            writer.writerow([])

    print(f"✅ Final elite configurations saved in {output_file}")


# Q-learning GA
extract_elite_configs(
    log_file="R_console-qLearning.txt",
    output_file="configurations-qLearning.txt",
    keys=["population_size", "generations", "mutation_rate", "elitism_size",
          "tournament_size", "alpha", "gamma", "epsilon_start", "epsilon_end"]
)

# standard GA
extract_elite_configs(
    log_file="hyperparameters.txt",
    output_file="R_console.txt",
    keys=["population_size", "generations", "mutation_rate",
          "crossover_op", "mutation_op", "elitism_size", "tournament_size"]
)
