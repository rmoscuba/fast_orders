# fast_orders
FastAPI orders processing

## Description
Implements a FastAPI project with an endpoint solution that receives a list of orders and a 
filter criterion. The endpoint filters the orders based on the criterion and return 
the total revenue for the filtered orders.

## Validation
The endpoint validates that the input price of items is not negative, and has a valid status and criterium input.

## Deployment
Deployed to Render.com using Docker support