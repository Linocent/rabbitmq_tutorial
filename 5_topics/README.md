In order to use this simple case, from [tutorial](https://www.rabbitmq.com/tutorials/tutorial-five-python)

dependency:
```commandline
 python -m pip install pika --upgrade
 ```

Receive all logs:
```commandline
python receive_logs_topic.py "#"
```

Receive logs from the facility " ```kern```":
```commandline
python receive_logs_topic.py "kern.*"
```

Receive "```critical```":
```commandline
python receive_logs_topic.py "*.critical"
```

Receive multiple bind:
```commandline
python receive_logs_topic.py "kern.*" "*.critical"
```

Emit a log with a routing key:
```commandline
python emit_log_topic.py "kern.critical" "A critical kernel error"
```
