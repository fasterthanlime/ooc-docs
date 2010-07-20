text/StringTemplate
===================

.. module:: text/StringTemplate

.. cover:: String
    
    :from: ``Char*``
    .. method:: formatTemplate (values: :class:`~structs/HashMap HashMap<K, V>` ) -> :cover:`~text/StringTemplate String` 
        
        Replace all template tokens in *this* with the matching value of *values*.
        
        Example::
        
            import text/StringTemplate
            values := HashMap<String, String> new()
            values put("what", "world") .put("suffix", "... yay")
            "Hello {{ what }}! {{   suffix}}" formatTermplate(values) println()
            // -> Hello world! ... yay
        
        
        
