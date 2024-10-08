﻿# Amplytics

 ## Inspiration
We were inspired by the growing challenge of managing rising utility costs in homes all around the world. As utility expenses like electricity, water, and gas continue to increase, understanding these trends becomes crucial for effective budgeting and energy management. Our goal is to help individuals navigate these changes by providing clear, data-driven insights into future electricity prices, ultimately fostering more informed and proactive decisions.

## What it does
It uses a linear regression model using past data of electricity costs in big metropolitan cities, and from the user input of city and future year, it takes that in and outputs the predicted electricity cost per kilowatt hour for that location and year.

## How we built it
We used Python for the backend of our project, using the BeautifulSoup4 library to parse data and create our own csv file, then pandas, numpy and scikit-learn to create a linear regression model based off our data. Then, for handling requests in the backend, we used the Flask framework for Python. On the front end, we used JavaScript and React to design and create the web page, and the Axios Library to handle GET and POST requests.

## Challenges we ran into
One challenge we had was figuring out how exactly to sort our data, and make it easily able to feed into our linear regression model. Another challenge we ran into was just with making Flask and React work together, as it was our first time ever using a Python backend framework with a JavaScript frontend.

## Accomplishments that we're proud of
We are proud of how we were able to solve our errors and debug our code. We were often faced with many problems we had never seen before, and our logical thinking skills were put to the test. But we were able to problem solve and come out strong, completing this project which made our whole group feel proud of ourselves.

## What we learned
We learned how to parse data into any format we want, so that it can be used for any sort of purpose. We also got experience working with and testing machine learning models, and how to implement them into a web app. 

## What's next for Amplytics
The next goals for Amplytics is to be able to have a search bar mechanism, where users can input any city in the United States and the entire country, and have it find the predicted electricity cost, as well as convert the currency for other countries. Additionally, we want to be able to predict utility costs as well, as we had the dataset for it but not enough time to integrate it into the application.

