text/StringTemplate
===================

.. module:: text/StringTemplate

.. cover:: String
    
    :from: ``Char*``
    .. memberfunction:: formatTemplate (values: :class:`~structs/HashMap HashMap<T>` ) -> :cover:`~text/StringTemplate String` 
        
        Replace all template tokens in *this* with the matching value of *values*.
        
        Example::
        
            import text/StringTemplate
            values := HashMap<String> new()
            values put("what", "world") .put("suffix", "... yay")
            "Hello {{ what }}! {{   suffix}}" formatTermplate(values) println()
            // -> Hello world! ... yay
        
        
        
