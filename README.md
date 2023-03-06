<h1 align="center">
    UrbE Auction
</h1>

<br/>

<p align="center">
<img src="./assets/GitHubImages/Admin-Homepage.png" width="80%" alt="UrbE Auction Homepage">
</a>
</p>

<br/>

This project is a web application for a charity auction organized by UrbE, a micromobility company.

The repo in question is the part of the project that uses Django to handle the backend of the web application. It includes various components such as models, views, and serializers that interact with the database and handle the logic of the application. The Django app also includes APIs to allow communication between the frontend and the backend. Overall, this part of the project plays a crucial role in managing the backend and ensuring that the web application runs smoothly.

<hr/>
  
## 🛠️&nbsp; How to run
- Install Redis if you want to keep track of the various auction bids and write the env variable in the .env file, like in the .env.example.

### Hardhat

#### Git clone the hardhat project repo

-   Clone the repo:
    ```
    git clone https://github.com/Meno96/urbe-auction-hardhat.git
    ```
-   Enter the directory:
    ```
    cd urbe-auction-hardhat
    ```
-   Install packages:
    ```
    yarn
    ```
    
#### Deploy to goerli

After installing dependencies, deploy your contracts to goerli:

```
yarn hardhat deploy --network goerli
```

### TheGraph

#### Deploy your subgraph

```
cd ..
```

Follow the instructions of the [README](https://github.com/Meno96/urbe-auction-thegraph/blob/master/README.md) of that repo.

### NextJS

Make sure that:

-   In your `networkMapping.json` you have an entry for `UrbEAuction` on the goerli network.
-   Make a `.env` file and place your temporary query URL into it as `NEXT_PUBLIC_SUBGRAPH_URL`.

-   Clone the repo:
    ```
    cd ..
    ```
    ```
    git clone https://github.com/Meno96/urbe-auction-nextjs.git
    ```
-   Enter the directory:
    ```
    cd urbe-auction-nextjs
    ```
-   Install packages:
    ```
    yarn
    ```
-   Run UI:
    ```
    yarn dev
    ```
    
### Django

On other terminal:

- Clone the repo:
    ```
    git clone https://github.com/Meno96/urbe-auction-django.git
    ```
- Create and activate virtual enviroment
- Install requirements: --> 
    ```
    pip install -r requirements.txt
    ```
- Make database migrations: --> 
    ```
    python manage.py makemigrations
    ``` 
    ```
    python manage.py migrate
    ```
- Run server: --> 
    ```
    python manage.py runserver
    ```
- Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser

## 🗎&nbsp; Requirements

* The platform must have an endpoint to manage user registration and access.

* Automatically assign 1 to 10 bitcoins to each user.
* Each user can post one or more sales or purchase orders of a certain amount.
* At the time of publication, if the purchase price of the order is equal to or greater than the selling price of any other user, match the transaction and mark both orders as filled.
* Provide an endpoint to get all active buy and sell orders.
* Provide an endpoint to calculate the total profit or loss from each user's trades.
* Assume that the platform in question is totally free for users and does not retain any type of commission on operations.


## 🚀&nbsp; How it's suppose to work?

<p align="center">
    <img width="80%" src="./assets/GitHubImage/Homepage1.png" alt="Homepage">
</p>

<p align="center">
    <img width="80%" src="./assets/GitHubImage/Homepage2.png" alt="Homepage">
</p>


