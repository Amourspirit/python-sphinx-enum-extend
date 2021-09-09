#!coding: utf-8
from enum_extend import AutoEnum

class FruitEnum(AutoEnum):
    """
    Fruit is a healthy snack for most all...
    """
    APPLE = """
    The **apple tree** (`Malus <https://simple.wikipedia.org/wiki/Malus>`_ domestica) is a tree that grows **apples**.
    It is best known for this juicy, tasty fruit. The tree is grown worldwide.
    Its fruit is low-cost, and is harvested all over the world.
    """
    ORANGE = 'Orange Fruit'
    PEACH = 'Peach Fruit'
    GRAPE = 'Grape Fruit'
    MANGO = """
    Mango Fruit
    """
    BLUEBERRY = """
    ``Blueberry Fruit``
    
    A blueberry is a berry, a very small fruit.
    It grows in a type of woody plant called a `shrub <https://simple.wikipedia.org/wiki/Shrub>`_.
    Many types of blueberries grow in North America and eastern Asia.
    Blueberries are more common between May and October.
    
    Blueberries have a sweet taste, with a little acidic hint.
    Wild blueberries have a stronger taste.
    Blueberries are good for making jelly, jam, pie, muffins, and many other foods.
    The most widely cultivated species of blueberry is Vaccinium corymbosum.
    Some similar kinds of berries are called blueberry or huckleberry in different places.
    
    .. image:: https://upload.wikimedia.org/wikipedia/commons/1/15/Blueberries.jpg
       :width: 320px
       :height: 209px
    """
