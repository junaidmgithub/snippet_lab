    import sqlparse

    def pprint_sql(queryset, **options):
        print(sqlparse.format(str(queryset.query), reindent=True, indent_width=4, **options))

    from django.db.models import Exists, OuterRef, Count, Subquery, IntegerField, Q
    from django.db.models.functions import Coalesce
    
    # Check parent rows has child rows
    
    exist_q = Exists(Department.objects.filter(branch=OuterRef('pk'), is_deleted=False))
    b = Branch.objects.annotate(
        has_children=exist_q
    )
    pprint_sql(b)
    
    # Get Count of child on parent rows, (2 ways)

    b = Branch.objects.filter(is_deleted=False).annotate(
        child_count=Count('department', filter=Q(is_deleted=False)))
    pprint_sql(b) 
    
    # OR

    subquery = Subquery(Department.objects.filter(branch=OuterRef('id'), is_deleted=False)
                        .values('branch')
                        .annotate(count=Count('*'))
                        .values('count'), output_field=IntegerField())

    b = Branch.objects.filter(is_deleted=False).annotate(child_count=Coalesce(subquery, 0))
    pprint_sql(b)

