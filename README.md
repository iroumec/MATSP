# What is this?

Quinki is an ATSP instances solver that uses an evolutive computing approach.

It has an educational purpose, so it's not expected to be used in real environments nor be extremely efficient. All operators habe been programmed by students.

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

## Credits

- González, Joaquín Tesoro.
- Roumec, Iñaki.
