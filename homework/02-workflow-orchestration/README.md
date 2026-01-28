# Module 1 Homework: Workflow Orchestration

This repository contains my solution for **Module 1 - Workflow Orchestration**.

---

## Question 1

Within the execution for `Yellow` Taxi data for the year `2020` and month `12`: what is the uncompressed file size (i.e. the output file `yellow_tripdata_2020-12.csv` of the `extract` task)?

**Answer**: `134.5 MiB`

![Screenshot for question 1](screenshots/no_1.png)

---

## Question 2

What is the rendered value of the variable file when the inputs taxi is set to green, year is set to 2020, and month is set to 04 during execution?

**Answer:** `db:5432`

## Question 3: Counting short trips

For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile?

**Answer**: `8,007`

![Screenshot for question 3](screenshots/no_3.png)

## Question 4. Longest trip for each day

Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles (to exclude data errors).

Use the pick up time for your calculations.

**Answer**: `2025-11-14`

![Screenshot for question 4](screenshots/no_4.png)

## Question 5. Biggest pickup zone

Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?

**Answer**: `East Harlem North`

![Screenshot for question 5](screenshots/no_5.png)

## Question 6. Largest tip

For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?

Note: it's `tip` , not `trip`. We need the name of the zone, not the ID.

**Answer**: `Yorkville West`

![Screenshot for question 6](screenshots/no_6.png)

## Terraform Exercise

[`main.tf`](https://github.com/mjoshua97241/data-engineering-zoomcamp/blob/main/homework/01-docker-terraform/terraform/main.tf)
[`variable.tf`](https://github.com/mjoshua97241/data-engineering-zoomcamp/blob/main/homework/01-docker-terraform/terraform/variable.tf)

## Question 7. Terraform Workflow

Which of the following sequences, respectively, describes the workflow for:

    1. Downloading the provider plugins and setting up backend,
    2. Generating proposed changes and auto-executing the plan
    3. Remove all resources managed by terraform`

**Answer**: `terraform init, terraform apply -auto-approve, terraform destroy`
