# What is this?

Quinki is an ATSP instances solver that uses an evolutive computing approach.

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
