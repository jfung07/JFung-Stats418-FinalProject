# Machine Learning Personal Color Analysis

Course: Stats418
Name: Julia Fung
Term: Spring 2026

The Streamlit application predicts a person's color analysis based on their features.  The app predicts one of 12 seasons in two ways.  The first page, manual, predicts the person's color analysis based on their manual input, contrast, eye color, hair color, and skin tone.  The second page, picture, predicts the person's season on an image of themselves.

Access URL: https://streamlit-app-980738607455.us-central1.run.app

## API Infrastructure
The web app implements an API via Google Cloud Run with the full implementation on GitHub.  

## Repository Folders
The project includes three folders containing runnable scripts, api, models, and streamlit_app and five data scripts, data_cleaner.py, data_scraper.py, data_split.py, exploration.py, and scrape_image.py.

## Reproducing
![Figure 1](visualizations/Stats418Final_MermaidDiagram.png)
Figure 1 shows the project flow.  The project starts with data_scraper.py which scrapes data from the site https://colormineai.com/celebrity/.  Then, the data_cleaner.py script cleans the missing values and the noisy categorical features.  Next, scrape_images.py scrapes images based on the pic_url column in the cleaned data file, processed.csv.  After gathering the data, data_split.py splits the data into training, vlaidation, and testing sets.  Using the splits, the random_forest.py and cnn.py scripts train random forest and cnn models respectively and save the models to .pkl and .pth files respectively.  Rf_api and cnn_api deploy the models to a FastAPI application on Google Coud Run which streamlit_app uses to deploy the interactive application to Google Cloud Run.


 First, clone the repository with "git clone https://github.com/jfung07/JFung-Stats418-FinalProject".  Switch nto the project directory then install the project's requirements with "pip install -r requirements.txt".

To run the streamlit app locally, run "streamlit run app/main.py".

To explore the api using the Dockerfile, run "docker build -t rf-api -f api/rf_api/Dockerfile.rf .". Then run the container locally with "docker run -p 8000:8000 rf-api".  The random forest model uses FastAPI, while the CNN implementation uses Flask.  However, the project does not implement the CNN API because the deployment was too large and expensive.  The line below builds, pushes, and deploys the API.  gcloud builds submit --tag us-central1-docker.pkg.dev/jfung-color-fastapi/fastapi-repo/cnn-api . && gcloud run deploy cnn-api --image us-central1-docker.pkg.dev/jfung-color-fastapi/fastapi-repo/cnn-api --platform managed --region us-central1 --allow-unauthenticated --port 8000









