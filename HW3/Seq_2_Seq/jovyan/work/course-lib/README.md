
# `course-lib` - Public course-wide library and data files (visible, read-only)

This directory is for data files or scripts that might be common to multiple assignments you generate. This directory will be part of the Python path for all users.

Please don't confuse this directory with the `[release|source]/[hwid]-lib` directories that may contain data specific to each individual homework separately.

## Placement

In the lab container, the contents of this directory will be placed in:

```
/home/jovyan/work/course-lib/
```

These files will be read-only. These will be available for all users, including students. However, it's better not to refer to these files using absolute paths; see best practices below.

## Best practices

Python files in this directory will be on the Python system path, so it's best to write a Python loader for data you need and refer to the data with relative paths *under the library directory* (never using ".." to refer to a directory above).

Staff members should refer to additional notes in the staff library directories.
