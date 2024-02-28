In order to use this simple case, from [tutorial](https://www.rabbitmq.com/tutorials/tutorial-four-python)

dependency:
```commandline
 python -m pip install pika --upgrade
 ```

for only save warning and error:
```commandline
python receive_logs_direct.py warning error > logs_from_rabbit.log
```

have log in terminal:
```commandline
python receive_logs_direct.py info warning error
```

emit an error:
```commandline
python emit_log_direct.py error "Run. Run. Or it will explode."
```
