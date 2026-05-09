# What is this?

MATSP is an ATSP instances solver that uses a memetic algorithm (MA) approach.

## TO DO

- Terminar el informe.
  - Redactar las secciones.
  - Hacer las pruebas y comparaciones.
- Completar todos los docstrings.

## Ideas

- Remplazar los .txt por .md (para poder incrustar imágenes y mejorar el formato).

## Usage Examples

### One Configuration

```sh
make run CONFIG="resources/configuration.example.yml"
```

Parses and executes the indicated configuration YAML file.

The output consists on a configuration markdown summary and a covergence graph.

### Multiple Configurations

```sh
make run CONFIG="resources/configurations/"
```

Parses and executes all configuration YAML files in the indicated folder.

The output consisten on a configuration markdown summary and an individual convergence graph for each configuration, and a combined convergence graphs, costs and average execution times comparison plot.

#### Configuration Naming

If you want the files to be executed and mapped in the same order you write them, do not name them like this:

config_1, config_2, ..., config_10, config_11

Becuase:

- C1 -> config_1
- C2 -> config_10

This is cause due to the string comparison, which is done character by character.

Instead, use the zero-padding convention, which is the standard convention in scientific computing, datasets, logs, simulations, rendering pipelines, backups, and so on.

Examples: config_01, config_02, config_03, ..., config_10, config_11, config_12.

## AI Usage

Artificial Intelligence (AI) was used in this project with the following objectives:

- During the project development:
  - to evaluate different solutions;
  - to solve bugs whose solution was unknown;
  - to build the matrix extraction script algorithm; and
  - to learn about some standard solutions for faced problems, like Protocol (PEP 544);

- Once finished the project:
  - to check for inconsistences and typos; and
  - to apply minor optimizations to the algorithms.

## Disclaimer

Quinki has an educational purpose: it's not expected to be used in real environments nor be extremely efficient for real-scale problems.

## Credits

- González, Joaquín Tesoro.
- Roumec, Iñaki.
