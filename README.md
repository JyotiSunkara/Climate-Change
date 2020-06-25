# Climate-Change
Data visualization to find climate change buried in millions of data points obtained from verified source: GHCN(Global Historical Climatology Network)

## Getting Started

Enter the `Data Visards` directory containing the code and proceed to run the following command:

```
    http-server --cors
```

Navigate to:

```
    http://127.0.0.1:8080
```

And click on the folder named `Main`, this will open a main page with a side navigation bar containing beautiful and informative visualizations! The visualizations have not been added to a single page because the data is heavy and does not allow for a fast render.

## Directory Structure 

Inside `Data Visards`:
<br><br>.
<br>├── CSV
<br>│   ├── final-data.csv
<br>│   ├── months.csv
<br>│   ├── tester.csv
<br>│   ├── totals.csv
<br>│   ├── weeks.csv
<br>│   └── years.csv
<br>├── HTML
<br>│   ├── Chart-bars.html
<br>│   ├── Chart-donuts.html
<br>│   ├── Chart-monthly.html
<br>│   ├── Chart-spatial.html
<br>│   ├── Chart-totals.html
<br>│   ├── Chart-weekly.html
<br>│   └── Chart-yearly.html
<br>├── JSON
<br>│   └── world.geojson
<br>├── Main
<br>│   ├── images
<br>│   │   ├── image1.png
<br>│   │   └── image2.png
<br>│   ├── index.html
<br>│   ├── script.js
<br>│   └── style.css
<br>└── README.md



### CSV And JSON
Contains all the parsed CSV and JSON files used for the visualizations.

### HTML
Contains all the HTML files and scripts for the visualizations.

### Main 
Contains the main web page with navigation links to the visualizations!





