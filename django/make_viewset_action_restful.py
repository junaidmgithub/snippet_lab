make viewset action restful

Decorator *@action* can be  used to create extra actions that corresponds to the same url(viewset) 
There is Also *@action.mapping* decorator, using that multiple viewset methods can handle different http methods of an action
	
        # Example usage:

        class MyViewSet(ViewSet):
            
            ...

            @action(detail=False)
            def example(self, request, **kwargs):
                ...

            @example.mapping.post
            def create_example(self, request, **kwargs):
                ...
            
            @example.mapping.delete
            def remove_example(self, request, **kwargs):
                ...


