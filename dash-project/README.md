# Dash Examples

In the `singlepage` folder, you'll find single-page apps, from simple to complex:

- `minimal.py`
- `twocols.py`
- `app.py`: a working app with a dropdown menu

- `withamap.py`: an example that adds a map

In the `multipage` folder, there's an example that combines existing pages into a basic multipage app.

In the `nextlevel` folder, there's a version of the same app enhanced using Bootstrap and Layout. This goes well beyond the level we expect, but you can play around with it if you have web experience.

## Setup

You will need to download the `emissions.csv` file:

1. Go to the folder containing the page you want to run.
2. Run the following command in the terminal:

```bash
curl -s https://raw.githubusercontent.com/owid/co2-data/refs/heads/master/owid-co2-data.csv > emissions.csv
```

If you want to run another page, copy or move the `emissions.csv` file to the relevant folder.
