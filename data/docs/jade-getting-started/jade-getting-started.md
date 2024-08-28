Learn how to use the JADE software to have a first look at JADE events and use analysis tools:

1. ["How do I start JADE software?"](#start)
2. ["Installing the JADE software with Docker"](#docker)
3. ["Testing the installed software and running simple data analysis"](#test)

## <a name="start">"How do I start JADE software?"</a>

JADE software needs to be run inside a container, e.g. with Docker or Podman. The corresponding GitHub repository can be found [here](https://github.com/andriish/JADE).

## <a name="docker">"Installing the JADE software with Docker"</a>

It is required to have Docker installed and the repository cloned, e.g. with `git clone https://github.com/rdebrand/JADE --branch software-only --depth 1` (will take up to 730 MB disk space, for additional documentation check out the gihub repository).

1. Pull the image with `docker pull ghcr.io/andriish/fedora39x86_64i686_gnu:latest`
2. Run the container `docker run -it --platform linux/amd64 --name jade_soft -v $PWD:/home ghcr.io/andriish/fedora39x86_64i686_gnu` <br>
   The `-v` option will mount the current directory (where it might be necessary to use `$(pwd)` instead of `$PWD` if an error occurs) to the home directory inside the container. It is thus useful to set the working directory beforehand to the cloned repository to conveniently run the software scripts and programs. <br>
   Note that not specifying a platform will result in the container software trying to run the image on the hosts platform type, while the image requires to be run on the linux/amd64 platform. The `-it` (interactive, tty) option is also necessary to keep the container running and be interactive, else it might close immediately.
3. Inside the container navigate to the JADE directory with `cd /home/JADE` and run `sh ./jadeinstall.sh --bits=32` <br>
   Note that everything inside the container has to be run with 32 bits, as most of the packages (especially Cernlib) only support this architecture.
4. The container can be exited by invoking `exit` and one can attach again with `docker start jade_soft` followed by `docker attach jade_soft`

## <a name="test">"Testing the installed software and running simple data analysis"</a>

While still attached to the container, the software can simply be tested with `sh ./jadetest.sh --bits=32`
