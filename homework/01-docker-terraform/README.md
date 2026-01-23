# Module 1 Homework: Docker & SQL

This repository contains my solution for **Module 1 - Docker & SQL**.

---

## Question 1: Understanding Docker images

**Task:**  
Run Docker with the `python:3.13` image, use `bash` as the entrypoint, and check the version of `pip`.

### Commands used

```bash
docker run -it --entrypoint bash python:3.13
pip --version
pip 25.3
```

[Screenshot for question 1](screenshots/no_1.png)

---

## Question 2: Docker networking and docker-compose

PgAdmin and Postgres are on the same Docker Compose network.

Containers communicate using the **service name** and the **container port**.

**Answer:** `db:5432`
