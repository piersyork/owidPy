# owidPy

A package for importing data from Our World in Data into Python. Currently in the early stages of development.

## Install
```
pip install owidPy
```

## How to use
To search for data you can use `owid_search()`. This function takes a key word as an argument and then returns the chart_ids of datasets that match the keyword. `Owid()` then takes a chart_id and returns an instance of the Owid class.

```python
owid_search('rights')
owid = Owid('human-rights-scores')
```

To see the raw data, you can do:

```python
owid.data
```

## Plotting
This functionality is not fully developed yet. To very quickly visualise the data you can use:
```python
owid.plot()
```






