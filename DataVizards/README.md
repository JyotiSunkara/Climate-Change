# Climate-Change
Data visualization to find climate change buried in millions of data points obtained from verified source: GHCN(Global Historical Climatology Network)

## Getting Started

Enter the directory containing the code and proceed to run the following command:

```
    http-server --cors
```

Navigate to:

```
    http://127.0.0.1:8080
```

And click on the folder named `Main`, this will open a main page with a side navigation bar containing beautiful and informative visualizations! The visualizations have not been added to a single page because the data is heavy and does not allow for a fast render.

## Directory Structure 

.
├── CSV
│   ├── final-data.csv
│   ├── months.csv
│   ├── tester.csv
│   ├── totals.csv
│   ├── weeks.csv
│   └── years.csv
├── HTML
│   ├── Chart-bars.html
│   ├── Chart-donuts.html
│   ├── Chart-monthly.html
│   ├── Chart-spatial.html
│   ├── Chart-totals.html
│   ├── Chart-weekly.html
│   └── Chart-yearly.html
├── JSON
│   └── world.geojson
├── Main
│   ├── images
│   │   ├── image1.png
│   │   └── image2.png
│   ├── index.html
│   ├── script.js
│   └── style.css
└── README.md



### CSV 
### JSON
Contains all the parsed CSV and JSON files used for the visualizations.

### HTML
Contains all the HTML files and scripts for the visualizations.

### Main 
Contains the main web page with navigation links to the visualizations!





