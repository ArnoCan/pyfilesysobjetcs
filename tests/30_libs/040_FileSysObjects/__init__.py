"""Filesystem as Object Oriented Storage.

The filesystem is used as a object storage including the class hierarchy.
 
The common test structure is as depicted in the following figure,
where each file 'data' contains the relative path including 'a'
for 'assert' verification.
The tests include in particular structural and navigation tests::

   a
   |-- b
   |   |-- c
   |   |   |-- b0
   |   |   |   `-- data
   |   |   |-- b1
   |   |   |   `-- data
   |   |   |-- b2
   |   |   |   `-- data
   |   |   |-- d
   |   |   |   |-- data
   |   |   |   `-- e
   |   |   |       |-- b0
   |   |   |       |   `-- data
   |   |   |       |-- b1
   |   |   |       |   `-- data
   |   |   |       |-- b2
   |   |   |       |   `-- data
   |   |   |       |-- data
   |   |   |       `-- f
   |   |   |           |-- data
   |   |   |           `-- g
   |   |   |               |-- b0
   |   |   |               |   `-- data
   |   |   |               |-- b1
   |   |   |               |   `-- data
   |   |   |               |-- b2
   |   |   |               |   `-- data
   |   |   |               |-- data
   |   |   |               `-- h
   |   |   |                   |-- a
   |   |   |                   |   |-- b
   |   |   |                   |   |   |-- c
   |   |   |                   |   |   |   |-- d
   |   |   |                   |   |   |   |   |-- data
   |   |   |                   |   |   |   |   `-- e
   |   |   |                   |   |   |   |       |-- data
   |   |   |                   |   |   |   |       `-- f
   |   |   |                   |   |   |   |           |-- data
   |   |   |                   |   |   |   |           `-- g
   |   |   |                   |   |   |   |               |-- data
   |   |   |                   |   |   |   |               `-- h
   |   |   |                   |   |   |   |                   |-- a
   |   |   |                   |   |   |   |                   |   |-- b
   |   |   |                   |   |   |   |                   |   |   |-- c
   |   |   |                   |   |   |   |                   |   |   |   |-- d
   |   |   |                   |   |   |   |                   |   |   |   |   |-- data
   |   |   |                   |   |   |   |                   |   |   |   |   `-- e
   |   |   |                   |   |   |   |                   |   |   |   |       |-- data
   |   |   |                   |   |   |   |                   |   |   |   |       `-- f
   |   |   |                   |   |   |   |                   |   |   |   |           |-- data
   |   |   |                   |   |   |   |                   |   |   |   |           `-- g
   |   |   |                   |   |   |   |                   |   |   |   |               |-- data
   |   |   |                   |   |   |   |                   |   |   |   |               `-- h
   |   |   |                   |   |   |   |                   |   |   |   |                   `-- data
   |   |   |                   |   |   |   |                   |   |   |   `-- data
   |   |   |                   |   |   |   |                   |   |   `-- data
   |   |   |                   |   |   |   |                   |   `-- data
   |   |   |                   |   |   |   |                   `-- data
   |   |   |                   |   |   |   `-- data
   |   |   |                   |   |   `-- data
   |   |   |                   |   `-- data
   |   |   |                   `-- data
   |   |   `-- data
   |   `-- data
   |-- b0
   |   `-- data
   |-- b1
   |   `-- data
   |-- b2
   |   `-- data
   `-- data


The data is generated by the following calls::

   mkdir -p a/b/c/d/e/f/g/h/a/b/c/d/e/f/g/h/a/b/c/d/e/f/g/h
   mkdir -p a/b/c/d/e/f/g/{b0,b1,b2}
   mkdir -p a/b/c/d/e/{b0,b1,b2}
   mkdir -p a/b/c/{b0,b1,b2}
   mkdir -p a/{b0,b1,b2}
        
   export x=0;for i in `find a -type d `;do echo "${i#./}" > "$i/data" ;done


"""
