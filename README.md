
# This repo refers to the below udemy project 
- https://www.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/33653704#overview


# Types of executors

- Sequential Executor
- Local executor
- Celery executor

# Points to remember

Airflow uses a database (Postgres SQL) to store metadata about the DAGs, tasks, and their state. The metadata database is used to keep track of the state of all tasks in the DAG, such as their status (running, success, failure), start and end times, dependencies, and more. hen using the Celery executor, Airflow uses a message broker such as RabbitMQ or Apache Kafka to send messages between the Airflow scheduler and the Celery worker processes. These messages contain information about the tasks that need to be executed, including their dependencies and parameters.
