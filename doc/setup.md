# Project setup

## Development environment

 - Use Conda + direnv? I've not really tried that before.
 - Make a Conda environment (called "`blocks`").
 - Put the following into `~/.direnvrc`:
 
```
use_conda() {
  . /opt/anaconda/etc/profile.d/conda.sh
  conda activate "$1"
}
```

 - Put the following into the `.envrc` in the project directory: `use
   conda blocks`.

Then use Conda to install packages, or `pip` for Python things (Conda
keeps track of packages installed with `pip`).

Export Conda environment to a file for reproducibility:

```
conda env export > conda-env.yaml
```

You can then get the Python dependency information out of this to put
in requirements files for deployment — Heroku uses a
`requirements.txt` file in the project root to install dependencies,
so that has to be there.


## Project template

 - I looked at `cookiecutter-django`, but I don't like it too much.
   There's too much stuff in there, and I have the feeling I'll spend
   a lot of time chasing down things that don't work. Might be good to
   keep around for reference, but I don't want to use it.
 - To avoid any more messing around, just start from `django-admin
   startproject`!
   

## Hosting

Heroku free dynos support Postgres and Redis, so let's use one of
those. (Also covered in the Django Cookiecutter template, I think.)


## CSS styling

Use Bootstrap with `django_bootstrap5`.
