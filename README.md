## Pyspark training


#### Setup

```
> source venv/bin/activate
> pip install -r requirements.txt
```


#### Run

* Locally:
```
python3 spark_app/spark_main.py
```

* Using `spark-submit`:
```
spark-submit spark_app/spark_main.py
```


#### Packaging

* Using `--py-files` option 

    (from https://spark.apache.org/docs/latest/api/python/user_guide/python_packaging.html#using-pyspark-native-features)

    Specify `--py-files` option in `spark-submit` command. This is a straightforward method to ship additional custom Python code to the cluster. 
    
    ⚠️ However, it does not allow to add packages built as Wheels and therefore does not allow to include dependencies with native code.


* Using `venv`

    (from https://spark.apache.org/docs/latest/api/python/user_guide/python_packaging.html#using-virtualenv)

    A virtual environment to use on both driver and executor can be created as demonstrated below. It packs the current virtual environment to an archive file:

    ```
    python -m venv pyspark_venv
    source pyspark_venv/bin/activate
    pip install pyarrow pandas venv-pack
    venv-pack -o pyspark_venv.tar.gz
    ```
