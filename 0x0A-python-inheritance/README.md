# 0x0A. Python - Inheritance

## GENERAL :open_book::open_book::open_book::

 <ol>
	<li>Why Python programming is awesome </li>
	<li>What is a superclass, baseclass or parentclass</li>
	<li>What is a subclass</li>
	<li>How to list all attributes and methods of a class or instance</li>
	<li>When can an instance have new attributes</li>
	<li>How to inherit class from another</li>
	<li>How to define a class with multiple base classes </li>
	<li>What is the default class every class inherit from</li>
	<li>How to override a method or attribute inherited from the base class</li>
	<li>Which attributes or methods are available by heritage to subclasses</li>
	<li>What is the purpose of inheritance</li>
	<li>What are, when and how to use <code>isinstance</code>, <code>issubclass</code>, <code>type</code> and <code>super</code> built-in functions</li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/E2Bs3bxX8GuSEKuWqswU7g" title="Inheritance" target="_blank">Inheritance</a> </li>
	<li><a href="/rltoken/auwnZOKkBZ97JaLtrMryuA" title="Multiple inheritance" target="_blank">Multiple inheritance</a> </li>
	<li><a href="/rltoken/ycewwwPmDpXqRp2R1FW51w" title="Inheritance in Python" target="_blank">Inheritance in Python</a> </li>
	<li><a href="/rltoken/F8LUzmvPI4yur1Z37ZM1fQ" title="Learn to Program 10 : Inheritance Magic Methods" target="_blank">Learn to Program 10 : Inheritance Magic Methods</a> </li>
</ol>

## INTRODUCTION TO FILES :closed_book::closed_book::closed_book::

0.	[**0-lookup.py**:](#0-lookuppy) Function that returns the list of available attributes and methods of an object
1.	[**1-my_list.py, tests/1-my_list.txt**:](#1-my_listpy-tests1-my_listtxt) Class <code>MyList</code> that inherits from <code>list</code>
2.	[**2-is_same_class.py**:](#2-is_same_classpy) Function that returns <code>True</code> if the object is <em>exactly</em> an instance of the specified class ; otherwise <code>False</code>.
3.	[**3-is_kind_of_class.py**:](#3-is_kind_of_classpy) Function that returns <code>True</code> if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise <code>False</code>.
4.	[**4-inherits_from.py**:](#4-inherits_frompy) Function that returns <code>True</code> if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise <code>False</code>.
5.	[**5-base_geometry.py**:](#5-base_geometrypy) An empty class <code>BaseGeometry</code>.
6.	[**6-base_geometry.py**:](#6-base_geometrypy) Class <code>BaseGeometry</code> (based on <code>5-base_geometry.py</code>).
7.	[**7-base_geometry.py, tests/7-base_geometry.txt**:](#7-base_geometrypy-tests7-base_geometrytxt) Class <code>BaseGeometry</code> (based on <code>6-base_geometry.py</code>).
8.	[**8-rectangle.py**:](#8-rectanglepy) Class <code>Rectangle</code> that inherits from <code>BaseGeometry</code> (<code>7-base_geometry.py</code>).
9.	[**9-rectangle.py**:](#9-rectanglepy) Class <code>Rectangle</code> that inherits from <code>BaseGeometry</code> (<code>7-base_geometry.py</code>).
(task based on <code>8-rectangle.py</code>)
10.	[**10-square.py**:](#10-squarepy) Class <code>Square</code> that inherits from <code>Rectangle</code> (<code>9-rectangle.py</code>)
11.	[**11-square.py**:](#11-squarepy) Class <code>Square</code> that inherits from <code>Rectangle</code> (<code>9-rectangle.py</code>).
(task based on <code>10-square.py</code>).
12.	[**100-my_int.py**:](#100-my_intpy) Class <code>MyInt</code> that inherits from <code>int</code>

## FILES :bookmark_tabs::bookmark_tabs::bookmark_tabs::

### 0-lookup.py

**<p>Function that returns the list of available attributes and methods of an object</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x0A$ cat 0-main.py
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

guillaume@ubuntu:~/0x0A$ ./0-main.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
guillaume@ubuntu:~/0x0A$ 
</code></pre>

### 1-my_list.py, tests/1-my_list.txt

**<p>Class <code>MyList</code> that inherits from <code>list</code></p>**

<pre><code>guillaume@ubuntu:~/0x0A$ cat 1-main.py
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

guillaume@ubuntu:~/0x0A$ ./1-main.py
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
guillaume@ubuntu:~/0x0A$ 
</code></pre>

### 2-is_same_class.py

**<p>Function that returns <code>True</code> if the object is <em>exactly</em> an instance of the specified class ; otherwise <code>False</code>.</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x0A$ cat 2-main.py
#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

guillaume@ubuntu:~/0x0A$ ./2-main.py
1 is an instance of the class int
guillaume@ubuntu:~/0x0A$ 
</code></pre>

### 3-is_kind_of_class.py

**<p>Function that returns <code>True</code> if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise <code>False</code>.</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x0A$ cat 3-main.py
#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

guillaume@ubuntu:~/0x0A$ ./3-main.py
1 comes from int
1 comes from object
guillaume@ubuntu:~/0x0A$ 
</code></pre>

### 4-inherits_from.py

**<p>Function that returns <code>True</code> if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise <code>False</code>.</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x0A$ cat 4-main.py
#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

guillaume@ubuntu:~/0x0A$ ./4-main.py
True inherited from class int
True inherited from class object
guillaume@ubuntu:~/0x0A$ 
</code></pre>

### 5-base_geometry.py

**<p>An empty class <code>BaseGeometry</code>.</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x0A$ cat 5-main.py
#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))

guillaume@ubuntu:~/0x0A$ ./5-main.py
&lt;5-base_geometry.BaseGeometry object at 0x7f2050c69208&gt;
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
guillaume@ubuntu:~/0x0A$ 
</code></pre>

### 6-base_geometry.py

**<p>Class <code>BaseGeometry</code> (based on <code>5-base_geometry.py</code>).</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x0A$ cat 6-main.py
#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0A$ ./6-main.py
[Exception] area() is not implemented
guillaume@ubuntu:~/0x0A$ 
</code></pre>

### 7-base_geometry.py, tests/7-base_geometry.txt

**<p>Class <code>BaseGeometry</code> (based on <code>6-base_geometry.py</code>).</p>**

<pre><code>guillaume@ubuntu:~/0x0A$ cat 7-main.py
#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0A$ ./7-main.py
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
guillaume@ubuntu:~/0x0A$ 
</code></pre>

### 8-rectangle.py

**<p>Class <code>Rectangle</code> that inherits from <code>BaseGeometry</code> (<code>7-base_geometry.py</code>).</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x0A$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0A$ ./8-main.py
&lt;8-rectangle.Rectangle object at 0x7f6f488f7eb8&gt;
['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
[AttributeError] 'Rectangle' object has no attribute 'width'
[TypeError] height must be an integer
guillaume@ubuntu:~/0x0A$ 
</code></pre>

### 9-rectangle.py

**<p>Class <code>Rectangle</code> that inherits from <code>BaseGeometry</code> (<code>7-base_geometry.py</code>).
(task based on <code>8-rectangle.py</code>)</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x0A$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())

guillaume@ubuntu:~/0x0A$ ./9-main.py
[Rectangle] 3/5
15
guillaume@ubuntu:~/0x0A$ 
</code></pre>

### 10-square.py

**<p>Class <code>Square</code> that inherits from <code>Rectangle</code> (<code>9-rectangle.py</code>)</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x0A$ cat 10-main.py
#!/usr/bin/python3
Square = __import__('10-square').Square

s = Square(13)

print(s)
print(s.area())

guillaume@ubuntu:~/0x0A$ ./10-main.py
[Rectangle] 13/13
169
guillaume@ubuntu:~/0x0A$ 
</code></pre>

### 11-square.py

**<p>Class <code>Square</code> that inherits from <code>Rectangle</code> (<code>9-rectangle.py</code>).
(task based on <code>10-square.py</code>).</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x0A$ cat 11-main.py
#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())

guillaume@ubuntu:~/0x0A$ ./11-main.py
[Square] 13/13
169
guillaume@ubuntu:~/0x0A$ 
</code></pre>

### 100-my_int.py

**<p>Class <code>MyInt</code> that inherits from <code>int</code></p><p></p>**

<pre><code>guillaume@ubuntu:~/0x0A$ cat 100-main.py
#!/usr/bin/python3
MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)

guillaume@ubuntu:~/0x0A$ ./100-main.py
3
False
True
guillaume@ubuntu:~/0x0A$ 
</code></pre>

