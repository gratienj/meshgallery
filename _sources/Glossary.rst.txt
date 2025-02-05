.. image:: images/IFPENVF_quadri.jpg
   :scale: 8 %
   :align: right

.. _Glossary:

###############################
Glossary
###############################

.. glossary::

   module
      A module is a set of entry points and variables within the Arcane time loop. It can include configuration 
      options that allow the user to customize the module via the simulation's data set. 
      Serving as a software component, a module models a specific physical phenomenon and shares 
      variables within the Arcane framework.
      
   service
      A service is a feature or functionality of the application. Similar to a :term:`module`, it can have variables 
      and configuration options accessible through the XML input data file. From a software design perspective, 
      a service implements an interface, and multiple implementations may be available for a given 
      functionality in Fraxim. 
      
      .. Seealso::
      
         To learn more about services and modules :  `Arcane core types <https://arcaneframework.github.io/arcane/userdoc/html/d4/dc9/arcanedoc_core_types.html>`_.
  

      