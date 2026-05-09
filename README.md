# What is this?

MATSP is an ATSP instances solver that uses a memetic algorithm (MA) approach.

## Usage Examples

One file:

```sh
make run CONFIG="resources/configuration.example.yml"
```

A directory:

```sh
make run CONFIG="resources/configurations/"
```

Parses and executes all configurations in the YAML files. A file can contain more than one configuration.

The output consists on a configuration markdown summary and an individual convergence graph for each configuration, and a combined convergence graphs, costs and average execution times comparison plot, in case the number of configuration is greater than one.

### Configuration Naming

In case of running a directory of multuple files, if you want the files to be executed and mapped in the same order you write them, do not name them like this:

```text
config_1, config_2, ..., config_10, config_11
```

They will be mapped in this order:

```text
config_1, config_10, config_11, config_2, ...
```

This is cause due to the string comparison, which is done character by character.

Instead, use the zero-padding convention, which is the standard convention in scientific computing, datasets, logs, simulations, rendering pipelines, backups, and so on.

```text
config_01, config_02, config_03, ..., config_10, config_11, config_12.
```

## Transparency Commitment

Artificial Intelligence (AI) was used in this project with the following objectives:

- During the project development:
  - to evaluate different solutions;
  - to solve bugs whose solution was unknown;
  - to build the matrix extraction algorithm;
  - to learn about some standard solutions for faced problems, like Protocol (PEP 544); and
  - to build the YAML expansion algorithm for building different configuration from a single file.

- Once finished the project:
  - to check for inconsistences and typos; and
  - to apply minor optimizations to the algorithms.

## Disclaimer

Quinki has an educational purpose: it's not expected to be used in real environments nor be extremely efficient for real-scale problems.

## Credits

- González, Joaquín Tesoro.
- Roumec, Iñaki.
