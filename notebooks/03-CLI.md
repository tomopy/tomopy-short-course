# Command Line Interfaces
Your computer has a command line interface (CLI) which you will need to use in order to run Python code, install TomoPy, and update TomoPy.

### Where is your command prompt?
On Unix, search for a program called `terminal`.
On Windows, search for a program called `cmd`.

## CLI Basics
The command line is a text interface to your computer. To run programs from a command line, we use the following syntax:

```bash
$ [program] [arguments] [options]
```

The [program] that we want to run must be named first. Then we list positional [arguments] for that program and [options]. For example:

```bash
$ cowpy "Hi, I'm a cow."
________________
< Hi, I'm a cow. >
----------------
    \   ^__^
     \  (oo)\_______
        (__)\       )\/\
          ||----w |
          ||     ||

```

In this case, the program is called `cowpy`, and it has a positional argument which is the message that the cow will say.

Options are provided to programs using a single minus `-` with a letter(s) or a double minus `--` with a word(s). For example, many programs will provide a short summary of how to use them by passing the `--help` option.

```bash
$ cowpy --help
usage: cowpy [-h] [-l] [-L] [-t] [-u] [-e EYES] [-c COWACTER] [-E] [-r] [-x]
             [-C]
             [msg [msg ...]]

Cowsay for Python. Directly executable and importable.

positional arguments:
  msg                   Message for the cow to say

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            Output all available cowacters
  -L, --list-variations
                        Output all available cowacters and their variations.
  -t, --thoughts        Use a thought bubble instead of a dialog bubble.
  -u, --tongue          Add a tounge to the selected cowacter, if appropriate.
  -e EYES, --eyes EYES  Use a specifice type of eyes on the cowacter
  -c COWACTER, --cowacter COWACTER
                        Specify which cowacter to use. (case insensitive)
  -E, --list-eyes       Print a listing of the available eye types.
  -r, --random          Choose a cowacter at random (consider --nsfw).
  -x, --nsfw            Enable 'not safe for work' cowacters and eyes.
  -C, --copy            Create a local copy of cow.py for you to include in
                        your own python program.
```

<!--- INSTRUCTOR ACTIVITY

Demonstrate using the cowsay help to make a cow with different eyes.

--->

<!--- SOLO ACTIVITY

Use cowsay to make a cat say something your favorite teacher told you once.

--->
